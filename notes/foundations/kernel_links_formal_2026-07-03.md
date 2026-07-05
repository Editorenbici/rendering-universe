# Kernel de links: precedentes en literatura

**K(x,y)** = 1 si y cubre a x (relación de cubrimiento / link directo, sin elementos intermedios), 0 en otro caso. Equivale a la matriz de adyacencia del diagrama de Hasse (reducción transitiva del grafo causal).

**Precedentes encontrados:**
- En CST: la "link matrix" L (o matriz de covering relations) se usa explícitamente en la construcción del propagador de Johnston para d=4: el kernel de Green retardado se construye a partir de L (ver Johnston PRL 103, 180401 (2009) y Surya review; en 2D se usa la matriz causal C completa). Trabajos recientes exploran propagadores basados en links (Hinrichsen et al., "Link-based causal set propagators").
- En teoría de grafos / posets: la adjacency de la "transitive reduction" o "Hasse diagram" es exactamente la matriz de covering relations (estándar en orden parcial; ver Wikipedia "Transitive reduction", Bollobás et al.).
- En QFT: el análogo continuo es el propagador causal retardado / función de Pauli-Jordan iΔ(x,y) (soporte en el cono de luz); las construcciones CST (Johnston, Sorkin) buscan reproducirlo discretamente. No se encontró el uso exacto de la matriz irreducible de links como kernel de potencial gravitatorio newtoniano fuera de este proyecto.

**NO ENCONTRADO** con la forma irreducible exacta K(x,y) como kernel de potencial gravitatorio (links → 1/r newtoniano) en la literatura revisada; aparece principalmente como kernel para campos escalares libres en CST.

(3 líneas de precedentes: link matrix en CST para propagadores; Hasse/transitive reduction en grafos; causal propagator en QFT. El uso específico para gravedad vía conteo de links parece propio del proyecto.)

## Revisión de kernel_paper_section_draft_2026-07-03.md (apareció en Codex notes/)
Revisado: la definición de K(x,y) usa χ_link = 1[y≺x] 1[N(I(y,x))=0] (exactamente la matriz de covering relations / link matrix).
Consistente con Johnston 2008/2009 (usa link matrix A_R / L para propagadores en CST, especialmente d=4; en 2D usa C).
No conflicto: Johnston construye propagadores QFT desde datos causales; el draft usa el mismo objeto matemático para kernel de potencial newtoniano (proyección estática).
Nota de 3 líneas: "Draft distingue uso (potencial newtoniano vs propagador QFT). Alineado con link matrix de Johnston. Precedente citado; aplicación específica del proyecto. OK sin diff."