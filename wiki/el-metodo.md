# El Método

Cada regla del protocolo existe porque su violación ya nos costó algo concreto. Fuente: `PROTOCOLO.md`.

## Las reglas con sus cicatrices

### 1. Pre-registro ANTES de correr
Los criterios de éxito/fracaso se congelan antes de ver el resultado. `git` prueba el orden temporal.
*Cicatriz:* todo el proyecto empezó sin esto. Los primeros 11 experimentos fueron exploratorios sin baranda.

### 2. Candados que se EJECUTAN
El bloqueo se lanza como script y se exige el mensaje de bloqueo. Nunca buscar strings.
*Cicatriz:* 17b corrió porque un match en un docstring no activó el candado. Costó una semana de remedición.

### 3. Validación astrométrica E2E
Los marcos y unidades se leen del HEADER (`assert COORDSYS`), no se asumen. Los tests nulos son ciegos a errores de marco.
*Cicatriz:* el bug ecuatorial/galáctico del Exp 17. ~2° de desviación sistemática. Tuvo que venir Fable a encontrarlo. Ahora es protocolo.

### 4. El ensamble es el modelo
Modelos estocásticos se juzgan por evidencia/fracción, jamás por máximo.
*Cicatriz:* discrepancia 2.70 vs 2.95 por confundir "mejor seed" con "resultado del modelo".

### 5. Publicar salga como salga
Incluidos negativos y bugs propios. Un rescate exige predicción nueva pre-registrada, no reinterpretación (Lakatos).
*Cicatriz:* 17, 18, 19.

### 6. Reproducibilidad determinista
Seeds fijos declarados. Toda medición debe poder reproducirse bit-exacta.
*Cicatriz:* 17b, 24.

### 7. Cuarentena de datos de chat
Ningún número entra a código sin verificación contra el release oficial (URL/SHA en docstring).
*Cicatriz:* corrupción de los BAO del script 02 por copy-paste desde un chat.

### 8. Citas verificadas
Toda cita se verifica contra arXiv/journal antes de entrar al repo; lo no verificado se marca NO VERIFICADO.
*Cicatriz:* citas de Grok mal asignadas a papers que no decían lo que se citaba.

### 9. git add por archivo explícito, nunca por directorio.
*Cicatriz:* dos barridos de archivos sin auditar que metieron basura al repo.

### 10. Paper y README son del autor
Herramientas escriben en code/analysis/, notes/, outputs/. Los wrappers/pipelines se congelan en la auditoría.
*Cicatriz:* +83 líneas huérfanas en el .tex y crashes del wrapper 18.

### 11. Concesiones irreversibles
Lo que entra al Cementerio no resucita sin argumento nuevo CON cálculo.
*Cicatriz:* bases 3, 6 y 7 resucitando tres veces.

### 12. Mirror→master con auditoría
Trabajo en espejos se integra con commit propio de provenance del autor, revisado antes de citar.
*Cicatriz:* Exp 20 barrido; Exp 24 corrido en freeze.

### 13. No inflar símbolos
Inventario cerrado en FUNDAMENTOS §II. Símbolo nuevo requiere que DERIVE algo.
*Cicatriz:* numerología y exponentes ajustados que había que archivar.

### 14. Claims con estados de FUNDAMENTOS
Toda tabla usa MEDIDO / DERIVADO / TEOREMA / REFUTADO / HIPÓTESIS / ABIERTO.
*Cicatriz:* claims table errada del diff del paper que usaba "VIVO" y "LIVE".
