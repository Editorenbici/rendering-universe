# Logística Zenodo + Email a la comunidad CST (preparación preprint)

**Fecha:** 2026-07-03  
**Objetivo:** Subir preprint (Paper A + material) a Zenodo + contactos para feedback.

## Zenodo para preprints de física

### Prácticas recomendadas (de docs oficiales + guías)
- **DOI**: Zenodo asigna DOI automáticamente (o reserva uno). Usa "Get a DOI now" antes de publicar. Cada versión nueva tiene su propio DOI + "concept DOI" para todo el trabajo.
- **Versionado**: Excelente. Sube v1 → más tarde "New version" para correcciones. No sobrescribes.
- **Metadatos mínimos (llena todo lo posible)**:
  - Title, authors (con ORCID si tienes), abstract (copia del paper).
  - Keywords: "causal set theory", "quantum gravity", "causal sets", "sprinkling", "interval abundance", "FRW", etc.
  - Related identifiers: si subes a arXiv después, enlaza.
  - Resource type: "Publication" o "Preprint".
  - Publication date: la fecha del preprint.
- **Archivos**: 
  - PDF del preprint (principal).
  - Opcional: zip del repo (o link a GitHub release).
  - Tablas/figures extras si quieres.
- **Licencias** (importante):
  - Zenodo **default** para records/preprints: **CC-BY 4.0**.
  - Para **código**: MIT está perfectamente recomendado.
  - **Mixed licenses soportadas**: Declara por separado.
    Ejemplo: PDF bajo CC-BY 4.0 ; código bajo MIT.
  - **No** uses MIT para el PDF del paper (usa CC-BY o CC0 para documentos). El repo ya es MIT → perfecto para el código.
  - En metadatos puedes especificar "This upload contains: preprint PDF (CC-BY 4.0) and source code (MIT)".
- GitHub integration: Si el repo está en GitHub, puedes archivar releases directamente en Zenodo (genera DOI para el software).
- Buena práctica física: Subir el PDF limpio + metadata rica. Zenodo es aceptado para preprints y citable.

**Pasos sugeridos**:
1. Prepara PDF final (o draft listo).
2. Ve a zenodo.org → New upload.
3. Sube PDF + (opcional) código.
4. Llena metadata completo.
5. Elige licencia(s) correctamente.
6. Publica → obtienes DOI inmediato.
7. Opcional: sube también a arXiv (mejor visibilidad en física).

## Contactos clave en la comunidad CST (2026)

### Emails (públicos / de perfiles institucionales)
- **Sumati Surya** (Raman Research Institute, Bengaluru) — líder del campo  
  ssurya@rri.res.in  
  (También aparece rrimail.rri.res.in en algunos perfiles)

- **Fay Dowker** (Imperial College London + Perimeter)  
  f.dowker@imperial.ac.uk

- **Stav Zalel** (anteriormente Imperial; ahora Cambridge / DAMTP en algunos registros recientes)  
  stav.zalel11@imperial.ac.uk (verificar actual si rebota)

- **Petros Wallden** (University of Edinburgh)  
  petros.wallden@ed.ac.uk

### Seminarios / listas / canales
- **"Causal Set Seminar" virtual**:  
  Búsquedas exhaustivas (2024-2026) no muestran evidencia clara de un seminario virtual regular y activo actualmente. Existen talks aislados en PIRSA, FQXi, etc.
- Hay actividad: 
  - Talleres y reuniones (ej. Monsoon Meet, conferencias).
  - **Importante**: "The path to quantum gravity with causal sets" — Royal Society Theo Murphy meeting, Manchester, **7-8 September 2026**. Participantes esperados incluyen Surya, Dowker, Wallden, etc. Buen lugar futuro para presentar.
- Estrategia recomendada:
  1. Subir primero a Zenodo (y/o arXiv).
  2. Enviar emails cortos, educados + link al preprint/DOI.
  3. Mencionar disponibilidad para presentar en seminarios o el meeting de 2026.
  4. Evitar "cold email" puro: referencia trabajos de ellos + qué feedback específico buscas (ej. sobre abundances en curved o embeddings).

## Template sugerido para email (corto)

Asunto: Preprint sobre link abundances en sprinklings FRW transitorio (causal sets)

Hola [Nombre],

Adjunto / link al preprint [DOI or Zenodo link] donde derivamos y medimos numéricamente una ley de abundancia de links en sprinklings Poisson con cutoff FRW transitorio (usando la resolución variable).

Citamos fuertemente vuestro trabajo [Glaser-Surya 2013 / tu paper relevante] como baseline para abundances en curved.

¿Tendrías 5 minutos para comentarios o correcciones? Especialmente en la sección de prioridad / abundances en cosmologías en expansión.

Saludos,  
[Tu nombre]

---

**Estado actual**: Notas listas. Zenodo + contactos documentados. Próximo paso: preparar PDF y subir.

Esta nota puede crecer con más contactos o experiencias reales de upload.

---

## AUDITORIA (Fable, 2026-07-03)
- **EVENTO VERIFICADO (el hallazgo estrategico):** Royal Society Theo
  Murphy meeting "The path to quantum gravity with causal sets",
  Manchester, 7-8 septiembre 2026. Organizan **Yasaman Yazdi (DIAS)**
  y **Stav Zalel (University of CAMBRIDGE)**. Fuente: pagina oficial
  royalsociety.org + Hyperspace. Registro anticipado obligatorio,
  plazas limitadas.
- **CORRECCIONES a los contactos de Grok:**
  1. Zalel esta en CAMBRIDGE segun la Royal Society — el email de
     Imperial (stav.zalel11@imperial.ac.uk) probablemente rebota.
     Buscar direccion actual en DAMTP/Cambridge antes de enviar.
  2. AGREGAR a Yasaman Yazdi a la lista (co-organizadora del meeting
     Y coautora de Surya-X-Yazdi 2019 sobre el vacio SJ, que este
     repo ya cita): contacto via DIAS.
  3. TODOS los emails quedan en estado NO VERIFICADO — confirmar cada
     direccion en la pagina institucional antes de enviar. Un email
     rebotado o mal dirigido es la peor primera impresion posible.
- Zenodo/licencias: recomendaciones razonables y consistentes con las
  practicas conocidas (PDF CC-BY 4.0, codigo MIT, DOI por version +
  concept DOI). Sin objeciones.
- **Estrategia sugerida por Fable:** el meeting de septiembre cambia
  el plan optimo — preprint en Zenodo con margen (julio-agosto),
  email breve a Yazdi/Zalel COMO ORGANIZADORAS mencionando el meeting
  (contexto natural, no cold email), con el resultado tecnico
  (Glaser-Surya 0.07 sigma -> ley slab -> FRW a 4 cifras) y el DOI.

