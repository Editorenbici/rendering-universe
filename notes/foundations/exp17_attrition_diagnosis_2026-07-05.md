# Exp 17 — diagnóstico reproducible de atrición

Fecha: 2026-07-05  
Estado: BACKGROUND técnico. No modifica `RESULTS_17.md`.

Objetivo: cerrar la deuda técnica de la atrición 460/1489 con un script
reproducible, sin tocar el pipeline cerrado ni repetir el stack ISW.

Archivo:

```text
code/analysis/17_isw_attrition_diagnosis.py
```

---

## Qué calcula

Para cada void no-edge del catálogo DESIVAST BGS:

1. Carga RA, DEC, \(R\), \(R_{\rm eff}\), NGC/SGC.
2. Reconstruye \(z\), \(L\) y \(\theta_v=R_{\rm eff}/R\) con la misma lógica
   del pipeline 17.
3. Lee `TMASK` del FITS de Planck SMICA.
4. Calcula las fracciones válidas del disco interno y del anillo compensado.
5. Marca descarte si:

\[
{\rm inner\_valid}<0.7
\quad{\rm or}\quad
{\rm ring\_valid}<0.7.
\]

Ese es exactamente el criterio del pipeline:

```python
if mi.mean() < 0.7 or mr.mean() < 0.7:
    return np.nan
```

---

## Qué no calcula

- No mide \(\Delta T_{\rm stack}\).
- No cambia `UNBLIND`.
- No toca `RESULTS_17.md`.
- No modifica `17_isw_stacking_pipeline.py`.
- No rescata ni reinterpreta la predicción ISW refutada.

---

## Comando esperado

Debe correrse en el mismo entorno WSL/Python donde funcionó Exp 17, con
`healpy`, `astropy` y los datos en `/home/hermes/exp1data`:

```bash
python code/analysis/17_isw_attrition_diagnosis.py \
  --data-dir /home/hermes/exp1data \
  --planck-fits /home/hermes/exp1data/COM_CMB_IQU-smica_2048_R3.00_full.fits \
  --out-json outputs/exp17_attrition_diagnosis.json \
  --out-csv outputs/exp17_attrition_diagnosis.csv
```

El script devuelve código `0` si reproduce el descarte esperado:

```text
discarded = 1029
retained = 460
```

Devuelve código `2` si el número de descartes no coincide.

---

## Estado del intento en este mirror

Intento con Python de Windows:

```text
Missing runtime dependency for Exp 17 attrition diagnosis: No module named 'healpy'.
```

Intento con WSL:

```text
Subsistema de Windows para Linux no tiene distribuciones instaladas.
```

Conclusión operativa: el script está listo, pero el run real debe hacerse en
el entorno donde ya corrió `17_isw_stacking_pipeline.py`, porque requiere
`healpy`, `astropy`, Planck SMICA + TMASK y los FITS de DESIVAST.

---

## Resultado esperado

Si el diagnóstico confirma los números cerrados, la causa operacional queda:

> Los 1,029 descartes vienen del umbral pre-registrado de máscara del parche
> compensado: disco interno o anillo con menos de 70% de píxeles válidos.

La dependencia con latitud galáctica y NGC/SGC queda como resumen secundario
del mismo corte de máscara, no como nuevo resultado físico.
