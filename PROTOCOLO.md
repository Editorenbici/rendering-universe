# PROTOCOLO — reglas de operación (v1.0, 2026-07-05)

Cada regla existe porque su violación ya nos costó algo concreto.
Cambios al protocolo: solo por commit del autor.

## Mediciones
1. **Pre-registro commiteado ANTES de correr.** Criterios de
   éxito/fracaso congelados; git prueba el orden temporal. (Origen:
   todo el proyecto.)
2. **Los candados se verifican EJECUTANDO el bloqueo** — se lanza el
   script y se exige el mensaje de bloqueo — nunca buscando strings.
   (Origen: 17b corrió por un match en el docstring.)
3. **Validación astrométrica/de marcos de extremo a extremo** para
   todo dato del cielo: los marcos y unidades SE LEEN DEL HEADER
   (assert COORDSYS), no se asumen. Los tests nulos son ciegos a
   errores de marco. (Origen: bug ecuatorial/galáctico del 17.)
4. **El ensamble es el modelo; el mejor seed es una anécdota.**
   Modelos estocásticos se juzgan por evidencia/fracción, jamás por
   máximo. (Origen: discrepancia 2.70 vs 2.95.)
5. **Resultado publicado salga como salga** — incluidos los negativos
   y los bugs propios. Un rescate exige predicción nueva
   pre-registrada, no reinterpretación (Lakatos). (Origen: 17, 18, 19.)
6. **Reproducibilidad determinista:** seeds fijos declarados; toda
   medición debe poder reproducirse bit-exacta. (Origen: 17b, 24.)

## Datos y citas
7. **Cuarentena de datos de chat:** ningún número entra a código sin
   verificación contra el release oficial (URL/SHA en docstring).
   (Origen: corrupción de los BAO del script 02.)
8. **Toda cita se verifica contra arXiv/journal antes de entrar al
   repo**; lo no verificado se marca NO VERIFICADO. (Origen: citas de
   Grok mal asignadas.)

## Repo y roles
9. **git add por archivo explícito, nunca por directorio.** (Origen:
   dos barridos de archivos sin auditar.)
10. **El paper y README son del autor.** Herramientas escriben en
    code/analysis/, notes/, outputs/. Los wrappers/pipelines se
    CONGELAN en la auditoría — ni ediciones cosméticas post-audit.
    (Origen: crashes del wrapper 18; +83 líneas huérfanas en el .tex.)
11. **Concesiones irreversibles:** lo que entra al Cementerio de
    FUNDAMENTOS no resucita sin argumento nuevo CON cálculo. (Origen:
    bases 3/6/7 resucitando tres veces.)
12. **Mirror→master con auditoría:** trabajo en espejos se integra
    con commit propio de provenance del autor del trabajo, revisado
    antes de citar. (Origen: Exp 20 barrido; Exp 24 corrido en freeze.)

## Símbolos y claims
13. **No inflar símbolos:** inventario cerrado en FUNDAMENTOS §II;
    símbolo nuevo requiere que DERIVE algo. La numerología y sus
    primos (exponentes ajustados, factores bonitos sin derivación,
    coincidencias de 2 dígitos) se archivan, no se celebran.
14. **Toda tabla de claims usa los estados de FUNDAMENTOS** (MEDIDO /
    DERIVADO / TEOREMA / REFUTADO / HIPÓTESIS / ABIERTO). Un claim
    LIVE exige evidencia commiteada. (Origen: claims table errada del
    diff del paper.)
