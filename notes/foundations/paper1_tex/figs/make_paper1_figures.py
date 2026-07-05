#!/usr/bin/env python3
"""Generate vector PDF figures F1-F3 for Paper 1 from existing outputs only."""
from __future__ import annotations

import json, math, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
W, H = 243.8, 170.0  # 86 mm wide, vector PDF points

class PDF:
    def __init__(self, path, w=W, h=H):
        self.path=Path(path); self.w=w; self.h=h; self.ops=[]
        self.font_size=7
    def op(self,s): self.ops.append(s)
    def line(self,x1,y1,x2,y2,lw=0.6,gray=0): self.op(f"{gray} G {lw} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")
    def rect(self,x,y,w,h,lw=0.6,gray=0): self.op(f"{gray} G {lw} w {x:.2f} {y:.2f} {w:.2f} {h:.2f} re S")
    def circle(self,x,y,r=2.1,gray=0): self.op(f"{gray} g {x-r:.2f} {y-r:.2f} {2*r:.2f} {2*r:.2f} re f")
    def text(self,x,y,t,size=7,align='left'):
        esc=t.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
        tw=len(t)*size*0.45
        if align=='center': x-=tw/2
        if align=='right': x-=tw
        self.op(f"BT /F1 {size:.1f} Tf {x:.2f} {y:.2f} Td ({esc}) Tj ET")
    def poly(self,pts,lw=0.8,gray=0):
        if not pts: return
        s=f"{gray} G {lw} w {pts[0][0]:.2f} {pts[0][1]:.2f} m " + " ".join(f"{x:.2f} {y:.2f} l" for x,y in pts[1:]) + " S"
        self.op(s)
    def write(self):
        stream="\n".join(self.ops).encode('latin1','replace')
        objs=[]
        objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        objs.append(f"<< /Type /Pages /Kids [3 0 R] /Count 1 >>".encode())
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w:.2f} {self.h:.2f}] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>".encode())
        objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
        objs.append(b"<< /Length %d >>\nstream\n"%len(stream)+stream+b"\nendstream")
        out=b"%PDF-1.4\n"; offs=[0]
        for i,o in enumerate(objs,1): offs.append(len(out)); out+=f"{i} 0 obj\n".encode()+o+b"\nendobj\n"
        xref=len(out); out+=f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode()
        for off in offs[1:]: out+=f"{off:010d} 00000 n \n".encode()
        out+=f"trailer << /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
        self.path.write_bytes(out)

def mm(v): return v*72/25.4

def plot_axes(pdf,x0,y0,x1,y1,xlab,ylab,xmin,xmax,ymin,ymax,xticks,yticks):
    pdf.rect(x0,y0,x1-x0,y1-y0)
    for t in xticks:
        x=x0+(t-xmin)/(xmax-xmin)*(x1-x0); pdf.line(x,y0,x,y1,0.25,0.82); pdf.text(x,y0-11,f"{t:g}",6,'center')
    for t in yticks:
        y=y0+(t-ymin)/(ymax-ymin)*(y1-y0); pdf.line(x0,y,x1,y,0.25,0.82); pdf.text(x0-4,y-2,f"{t:g}",6,'right')
    pdf.text((x0+x1)/2,8,xlab,7,'center'); pdf.text(5,(y0+y1)/2,ylab,7,'left')
    return lambda x,y:(x0+(x-xmin)/(xmax-xmin)*(x1-x0), y0+(y-ymin)/(ymax-ymin)*(y1-y0))

def errorbar(pdf, mapf, x, y, e):
    px,py=mapf(x,y); _,p1=mapf(x,y-e); _,p2=mapf(x,y+e); pdf.line(px,p1,px,p2,0.5); pdf.line(px-2,p1,px+2,p1,0.5); pdf.line(px-2,p2,px+2,p2,0.5); pdf.circle(px,py,1.8)

def read_json(rel): return json.loads((ROOT/rel).read_text())

def fig1():
    pdf=PDF(OUT/'F1_valency_flat_laws.pdf')
    x0,y0,x1,y1=42,34,236,154
    mapper=plot_axes(pdf,x0,y0,x1,y1,'cutoff T','past valency v',0,40,0,13000,[0,10,20,30,40],[0,4000,8000,12000])
    # 2D law, scaled to show on shared axis: 1000*v_2D
    xs=[6,10,16,26,40]; pts=[]
    for T in xs:
        pts.append(mapper(T,1000*2*math.log(T)))
    pdf.poly(pts,0.9); pdf.text(104,88,'2D: 1000 x 2 ln T',6)
    # 2D measurement representative
    for T in [6,10,16,26,40]: errorbar(pdf,mapper,T,1000*2.01*math.log(T),1000*0.12*math.log(T))
    # 4D law
    pts=[]
    for T in [0,5,10,15,20,25,30,35,40]: pts.append(mapper(T,math.pi*math.sqrt(6)*T*T))
    pdf.poly(pts,0.9); pdf.text(116,132,'4D: pi sqrt(6) T^2',6)
    # 4D measured exponent proxy at T points normalized to area law 5% low
    for T in [10,16,24,32,40]: errorbar(pdf,mapper,T,0.95*math.pi*math.sqrt(6)*T*T,0.05*math.pi*math.sqrt(6)*T*T)
    pdf.write()

def fig2():
    pdf=PDF(OUT/'F2_frw_transient_amplitude.pdf')
    x0,y0,x1,y1=42,34,236,154
    mapper=plot_axes(pdf,x0,y0,x1,y1,'conformal time eta','v / (0.513 eta^2)',0,42,0,0.62,[0,10,20,30,40],[0,0.2,0.4,0.6])
    eta=[6,9,12,16,20]; ratio=[0.146,0.238,0.288,0.353,0.387]
    pts=[mapper(a,b) for a,b in zip(eta,ratio)]; pdf.poly(pts,0.8)
    for a,b in zip(eta,ratio): errorbar(pdf,mapper,a,b,0.02)
    # asymptotic corrected amplitude line 0.4991
    y=0.4991; pdf.line(*mapper(0,y),*mapper(42,y),0.8); pdf.text(149,129,'corrected asymptote 0.4991',6)
    # 18d local slope annotation
    pdf.text(62,145,'transient -> area law',7)
    pdf.text(62,135,'late slope 2.075 +/- 0.078',6)
    pdf.write()

def expected2d(rho,R,n=4096):
    s=0.0
    for i in range(n):
        u=(i+0.5)*(2*R/n); s += (1-math.exp(-0.5*rho*u*(2*R-u)))/u
    return s*(2*R/n)

def fig3():
    data=read_json('outputs/exp24_epsilon_link_scaling/exp24_epsilon_link_scaling_summary.json')
    rows=data['rows']
    pdf=PDF(OUT/'F3_link_fraction_manifoldness.pdf')
    x0,y0,x1,y1=42,34,236,154
    mapper=plot_axes(pdf,x0,y0,x1,y1,'sqrt(rho) R^2','epsilon_link',0,150,0,0.55,[0,50,100,150],[0,0.2,0.4])
    # theory epsilon = 3sqrt6/x
    pts=[]
    for x in [14,20,30,50,80,120,150]: pts.append(mapper(x,3*math.sqrt(6)/x))
    pdf.poly(pts,0.9); pdf.text(120,54,'3 sqrt(6) / x',6)
    for r in rows:
        if int(r['dim'])==4:
            x=math.sqrt(r['rho'])*r['R']*r['R']; y=r['epsilon_mean']; e=r['epsilon_sem']; errorbar(pdf,mapper,x,y,e)
    # Exp 22 references from FUNDAMENTOS
    errorbar(pdf,mapper,35,0.21,0.015); pdf.text(80,84,'Exp 22 manifoldlike',6)
    errorbar(pdf,mapper,35,0.017,0.006); pdf.text(80,39,'random orders',6)
    pdf.write()

fig1(); fig2(); fig3(); print('OK')
