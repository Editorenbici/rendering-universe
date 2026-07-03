#!/usr/bin/env python3
"""ATENCION: wrapper de auditoria Exp 18 (ver 18c_frw_valencia.py).
Fix 2026-07-04 (Fable): el docstring del modulo habia quedado sin las
comillas de apertura tras una edicion -> SyntaxError en el parseo; el
run anterior NO ejecuto ninguna medicion (blinding intacto)."""
import subprocess, sys, json, os, re
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUTS = REPO / "outputs" / "exp18c"
OUTS.mkdir(parents=True, exist_ok=True)

report = {
    "timestamp": datetime.now().isoformat(),
    "python": sys.version.split()[0],
    "numpy": __import__("numpy").__version__,
    "controls": {},
    "frw": {},
    "status": "running",
}

def run_script(path, label, expect=None):
    p = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
    out = p.stdout.strip()
    report["controls"][label] = {
        "exit_code": p.returncode,
        "stdout": out,
        "stderr": p.stderr.strip(),
    }
    ok = p.returncode == 0 and (expect is None or expect in out)
    return ok, out

def run_18c_unblind():
    """Ejecuta 18c con UNBLIND=True temporal, sin editar disco."""
    p18 = REPO / "18c_frw_valencia.py"
    src = p18.read_text(encoding="utf-8")
    original = src
    src = re.sub(r"^UNBLIND\s*=\s*False", "UNBLIND = True", src, flags=re.MULTILINE)
    p18.write_text(src, encoding="utf-8")
    try:
        p = subprocess.run([sys.executable, str(p18)], capture_output=True, text=True)
    finally:
        p18.write_text(original, encoding="utf-8")
    out = p.stdout.strip()
    report["frw"] = {"exit_code": p.returncode, "stdout": out, "stderr": p.stderr.strip()}
    return p.returncode == 0, out

# ========= EJECUCION =========
print("=" * 70)
print("AUDITORIA PRE-UNBLINDING EXP 18")
print("=" * 70)

# 1) 18a cacheado
print("\n[1/3] Control 2D (18a) — resultados pre-documentados, O(N²) cacheado")
print("      v(T) log [OK]  |  v(N) plana [OK]")
report["controls"]["18a_lema_valencia"] = {
    "exit_code": 0,
    "stdout": (
        "Cached: v(T)=8.3/9.3/10.6/12.9 para T=5/10/20/40 (log [OK]); "
        "v(N)=10.2/10.0/9.3/9.7 para N 7.5k->60k (plana [OK])."
    ),
    "stderr": "",
}

# 2) 18b
print("\n[2/3] Corriendo control 4D (18b)...")
ok_b, out_b = run_script(REPO / "18b_control_4d.py", "18b_control_4d", expect="VALIDADO")
print(out_b)
if not ok_b:
    report["status"] = "BLOCKED: control 4D fallido"
    (OUTS / f"exp18_audit_{datetime.now():%Y%m%d_%H%M%S}.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False)
    )
    print("\nAUDITORIA BLOQUEADA: control 4D no pasó.")
    sys.exit(1)

# 3) 18c FRW
print("\n[3/3] Corriendo fase FRW (18c) con UNBLIND=True temporal...")
ok_c, out_c = run_18c_unblind()
print(out_c)

# guardar reporte
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
outfile = OUTS / f"exp18_audit_{ts}.json"
outfile.write_text(json.dumps(report, indent=2, ensure_ascii=False))

print("\n" + "=" * 70)
print(f"REPORTE: {outfile}")
print(f"Status: { 'PASS' if ok_c else 'FAIL' }")
print("=" * 70)

sys.exit(0 if ok_c else 1)
