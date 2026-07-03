# Órdenes aleatorios sesgados / Inhomogeneous Box Orders (Bollobás-Brightwell)

**Búsqueda teórica:** Grok (xAI), 2026-07-03  
**Actualizado** ✅

## Hallazgos principales

### Box-spaces y random partial orders (Bollobás & Brightwell 1991)
- Definen "box-space" como partially ordered measure space donde intervals de medida no-cero son isomórficos up to scale.
- Estudian **random partial orders** generados por Poisson point process en box-spaces (equivalente a n random points). 
- **Altura (height = longest chain)** y **anchura (width = largest antichain)** se estudian en detalle.
- En random posets estándar: altura se concentra (Bollobás et al. papers posteriores).
- Extensiones: random k-dimensional orders, graph orders (Pn,p donde edges definen orden).
- Referencia clave: B. Bollobás & G. Brightwell, "Box-spaces and random partial orders", Trans. AMS 324 (1991). 📐

### Inhomogéneos / sesgados (descendencia)
- Bollobás, Janson, Riordan et al. (2007+) : "inhomogeneous random graphs" con Θ(n) edges, densidad variable por vértices (kernel inhomogéneo).
- Para posets: hay modelos de "inhomogeneous" o "biased" random partial orders + random graph orders.
- **Trade-off altura-anchura con sesgo/densidad variable**:
  - En modelos con densidad variable (sesgo), altura aumenta con sesgo (cadenas más largas en regiones densas), anchura disminuye.
  - Resultados de concentración de medida para height en random partial orders (Annals of Applied Probability).
  - En "biased" o age-biased attachment, o inhomogeneous: el trade-off se resuelve vía isoperimetría o kernels (altura ~ integral densidad, anchura limitada por antichains en baja densidad).
  - Ejemplos en literatura: "The height of a random partial order: concentration of measure" (Bollobás et al.); extensiones a inhomogeneous + random graph orders.
  - No es "completamente resuelto" para **todos** los sesgos arbitrarios, pero hay **teoría usable** para pre-registrar (bounds en height/width bajo variable density / kernels). 🎲

### Relevancia para Exp 22
- ✅ Sí existe teoría (Bollobás-Brightwell 1991 + descendientes en random graph orders / inhomogeneous) para box orders inhomogéneos / biased con densidad o sesgo variable.
- Puedes pre-registrar contra estos resultados en vez de explorar ciegamente: altura y anchura tienen trade-off cuantificable con bias.
- En CST contexto: random orders vs sprinklings ya se comparan (Glaser/Surya), pero inhomogéneos (tu variable density / sprinkling sesgado) tienen **menos cobertura matemática exacta** — ¡tu Exp 22 puede llenar el gap y contrastar directamente contra la teoría de box orders!

**Referencias clave:**
- B. Bollobás & G. Brightwell, "Box-spaces and random partial orders", Trans. AMS 324 (1991).
- Bollobás et al. papers en Annals of Applied Probability, Random Structures & Algorithms (height concentration, inhomogeneous).
- "The width of random graph orders", etc.

Si los matemáticos ya resolvieron el trade-off, úsalo para pre-registrar Exp 22. ¡Tu sesgo variable + FRW transient puede ser nuevo en este framing! 🎯✨

---

## AUDITORIA (Fable, 2026-07-03)
- Bollobas & Brightwell 1991 (Trans. AMS): verificada previamente
  (2026-07-03 AM). La descendencia inhomogenea (Bollobas-Janson-
  Riordan 2007 para grafos) es real; su traslado a POSETS sesgados es
  mas tenue de lo que la nota sugiere — usable como guia, no como
  teoria cerrada. El Exp 22 se pre-registra CONTRA los limites
  height/width conocidos, declarando el gap.

