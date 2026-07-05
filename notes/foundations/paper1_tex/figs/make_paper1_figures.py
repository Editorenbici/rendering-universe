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

def exp18_audit():
    return read_json('code/analysis/outputs/exp18c/exp18_audit_20260702_223954.json')

def parse_control_18a():
    stdout = exp18_audit()['controls']['18a_lema_valencia']['stdout']
    m = re.search(r'v\(T\)=([0-9./]+) para T=([0-9/]+)', stdout)
    if not m:
        raise RuntimeError('Could not parse 18a cached control stdout')
    vals = [float(x) for x in m.group(1).split('/')]
    ts = [float(x) for x in m.group(2).split('/')]
    return list(zip(ts, vals))

def parse_control_18b():
    stdout = exp18_audit()['controls']['18b_control_4d']['stdout']
    rows = []
    for line in stdout.splitlines():
        m = re.match(r'\s*(\d+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)', line)
        if m:
            rows.append({
                'T': float(m.group(1)),
                'v': float(m.group(2)),
                'sem': float(m.group(3)),
                'theory': float(m.group(4)),
                'ratio': float(m.group(5)),
            })
    if not rows:
        raise RuntimeError('Could not parse 18b control table')
    return rows

def parse_frw_18c():
    stdout = exp18_audit()['frw']['stdout']
    rows = []
    for line in stdout.splitlines():
        m = re.match(r'\s*(\d+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)', line)
        if m:
            rows.append({
                'eta': float(m.group(1)),
                'v': float(m.group(2)),
                'sem': float(m.group(3)),
                'theory': float(m.group(4)),
                'ratio': float(m.group(5)),
            })
    if not rows:
        raise RuntimeError('Could not parse 18c FRW table')
    return rows

def fig1():
    pdf=PDF(OUT/'F1_valency_flat_laws.pdf')
    x0,y0,x1,y1=42,34,236,154
    mapper=plot_axes(pdf,x0,y0,x1,y1,'cutoff T','past valency v',0,18,0,2300,[0,6,12,18],[0,500,1000,1500,2000])
    # 4D law and measured control table from the Exp 18 audit JSON.
    pts=[]
    for T in [0,3,6,9,12,16]:
        pts.append(mapper(T,math.pi*math.sqrt(6)*T*T))
    pdf.poly(pts,0.9); pdf.text(119,135,'4D theory: pi sqrt(6) T^2',6)
    for r in parse_control_18b():
        errorbar(pdf,mapper,r['T'],r['v'],r['sem'])
    pdf.text(117,124,'18b: p = 2.089 +/- 0.025',6)
    # 2D cached control is real output but much smaller; draw it in an inset
    ix0,iy0,ix1,iy1=55,96,116,147
    imap=plot_axes(pdf,ix0,iy0,ix1,iy1,'','',0,42,7,14,[0,20,40],[8,10,12,14])
    pts=[imap(T,2*math.log(T)+5.0) for T in [5,10,20,40]]
    pdf.poly(pts,0.7,0.35)
    for T,v in parse_control_18a():
        errorbar(pdf,imap,T,v,0.0)
    pdf.text(ix0+4,iy1-11,'18a: log law',6)
    pdf.write()

def fig2():
    pdf=PDF(OUT/'F2_frw_transient_amplitude.pdf')
    x0,y0,x1,y1=42,34,236,154
    mapper=plot_axes(pdf,x0,y0,x1,y1,'conformal time eta','v / (0.513 eta^2)',0,42,0,0.62,[0,10,20,30,40],[0,0.2,0.4,0.6])
    rows=parse_frw_18c()
    pts=[mapper(r['eta'],r['ratio']) for r in rows]; pdf.poly(pts,0.8)
    for r in rows:
        errorbar(pdf,mapper,r['eta'],r['ratio'],r['sem']/r['theory'])
    # 18d reports convergence to 0.442 at eta=40 and corrected asymptote 0.4991.
    errorbar(pdf,mapper,40,0.442,0.0)
    y=0.4991; pdf.line(*mapper(0,y),*mapper(42,y),0.8); pdf.text(166,119,'asymptote 0.4991',6)
    pdf.text(62,145,'transient -> area law',7)
    pdf.text(62,135,'18d: late slope 2.075 +/- 0.078',6)
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
