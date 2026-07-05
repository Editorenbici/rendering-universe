# Tabla de Símbolos Canónica — Nuevas Convenciones

**Fecha:** 2026-07-03  
**Propósito:** Unificar notación entre código, notas y paper. Evitar ambigüedades dimensionales y de precedencia.  
**Fuente base:** `variables_R_and_epsilon_link_draft.md`, `variables_literature_review_2026-07-03.md`, `link_abundance_poisson_sprinkling.md`, búsquedas CST/CDT.  
**Convención sticky:** \([\mathcal{R}] = 1\) (adimensional). Usar \(L_R\) o \(E_R\) explícitamente cuando se compare con escalas físicas.

**Convención ℛ cerrada 2026-07-03:** \([\mathcal{R}]=1\). Usar \(L_R/E_R\) para dimensionales.

---

## 1. Tabla de Símbolos Nuevos

| Símbolo | Definición | Dimensión | Estado | Valor benchmark | Alias código / papel | Equivalencias literarias |
|---------|------------|-----------|--------|------------------|----------------------|--------------------------|
| \( v_R \) | \( v_R = \frac{d\mathcal{R}}{dt} = \beta_t \frac{\mathcal{R}}{t} \) (tasa de cambio de resolución; \(\beta_t = d\ln\mathcal{R}/d\ln t\)) | \( T^{-1} \) | Propuesto (nuevo en esta combinación) | N/A | código: `v_R`, `dR_dt`<br>paper: \( v_R \), \( \dot{\mathcal{R}} \) | "rate of change of discreteness scale" / "resolution refinement rate" (sin precedente exacto en CST/CDT; análogo a da/dt en simulaciones de lattice pero con \(\mathcal{R}\) adim.) |
| \( \epsilon_{\rm link} \) | \( \epsilon_{\rm link} = \frac{\langle N_{\rm links}\rangle}{\langle N_{\rm past}\rangle} \) (eficiencia fraccional de links / linking efficiency; normalizada para \(\ll 1\)) | 1 (adimensional) | CONFIRMADO | 0.0735 | código: `epsilon_link`, `eps_link`, `epsilon_frac`<br>paper: \( \eta_{\rm link} \) (recomendado) | "linking fraction" \( p = N_0 / (n^2/2) \) (Carlip arXiv:2405.14059); "valency fraction" o covering density (Glaser & Surya usan \(N_0\) sin normalizar como fracción principal) |
| \( v_{\rm link} \) | \( v_{\rm link} \equiv \langle N_{\rm links}\rangle \) (valencia media / número promedio de links por elemento; sigue ley de área en cutoff) | 1 (conteo adimensional) | CONFIRMADO | 769.53 (0% error vs π√6 √ρ L_R²) | código: `v_link`, `valencia`, `valencia_frw`<br>paper: \( v_{\rm link} \), \( N_{\rm links} \) | "valency" (número de nearest neighbours / covering relations por elemento) — Glaser & Surya 2013 (arXiv:1309.3403), Surya 2019 Living Rev. Relativ. (infinita en límite continuo sin cutoff) |
| \( \eta_E \) | \( \eta_E \equiv \pi\sqrt{6} \frac{\sqrt{\rho}\, E_R^2}{M_{\rm Pl}^4} \) (abundancia adimensional de escala de energía; NO es fracción) | 1 (adimensional) | PROHIBIDO_COMO_FRACCIÓN | 769.53 (>>1) | código: `eta_E`, `eta_energy`<br>paper: \( \eta_E \) | Factores de interval abundances \(\langle N_m^d \rangle\) (Glaser & Surya usan \(\Gamma\) functions y \(\chi_k\); \(\pi\sqrt{6}\) es específico de banda de links en 4D cutoff, no reportado verbatim para links) |
| \( \psi \) | \( \psi = \nabla \ln \mathcal{R} \) (campo escalar del gradiente de resolución; genera métrica disforme \( ds^2 = -e^{-2\psi} c^2 dt^2 + e^{2\psi} dx^2 \)) | \( L^{-1} \) | Propuesto (motivación específica) | N/A | código: `psi`<br>paper: \( \psi \) | Disformal scalar en general (Bekenstein 1993; Sakstein 2014 arXiv:1409.1734; Bettoni-Liberati 2013). Ninguna fuente usa exactamente \(\psi = \nabla \ln R(t)\) con canvas fijo + resolución variable. Precedente para acoplamientos y límites newtonianos (Sakstein), pero no esta derivación. |

**Notas sobre la tabla:**
- Todas las definiciones respetan \([\mathcal{R}]=1\).
- \( v_{\rm link} \) es conteo (puede ser grande); \( \epsilon_{\rm link} \) es fracción \(\ll 1\); \( \eta_E \) es abundancia adim. para comparaciones de escala (PROHIBIDO_COMO_FRACCIÓN).
- \( G_{\rm eff} = G \epsilon_{\rm link} f(\psi) \) con \( f(\psi) = 1 + \mathcal{O}(\psi^2) \).
- Columna "Valor benchmark" reporta números del script exp24 (o equivalente).

---

## 2. Tabla Anti-Símbolos (Prohibidos por Ambigüedad)

Estos usos están prohibidos en paper, notas y código nuevo para evitar confusiones dimensionales, de fracción vs. abundancia, o claims excesivos.

| Símbolo / Frase Prohibida | Razón | Alternativa Canónica |
|---------------------------|-------|----------------------|
| \(\beta\) sin subíndice | Conflicto entre \(\beta_t = d\ln\mathcal{R}/d\ln t\) (proyecto/Exp 15) y \(\beta_a = d\ln\mathcal{R}/d\ln a\). La forma \(v_R = \beta H \mathcal{R}\) solo vale para \(\beta_a\). | \(\beta_t\) o \(\beta_a\) siempre etiquetado; documentar \( \beta_a = \beta_t / (H t) \) |
| \(\mathcal{R}\) como escala de energía sin aclarar | \([\mathcal{R}]=1\) (adim.). Insertar en fórmulas con \(M_{\rm Pl}\) produce errores dimensionales o valores absurdos (ej. \(10^{60}\)). | Usar explícitamente \(L_R\) (longitud/cutoff) o \(E_R\) (energía). Ej.: \(\eta_E\) usa \(E_R\). |
| "fracción de enlaces" sin especificar si es \(\epsilon_{\rm link}\) o \(\eta_E\) | \(\epsilon_{\rm link}\) es fracción normalizada \(\ll 1\); \(\eta_E\) es abundancia de escala (puede ser >>1 o ~10^60). Mezclar destruye significado en \(G_{\rm eff}\). | Siempre: \(\epsilon_{\rm link}\) (o \(\eta_{\rm link}\) en paper) para la fracción; \(\eta_E\) para la abundancia de energía. |
| Cualquier claim de "teoría demostrada", "reemplazo de GR", "gravedad explicada", "nueva teoría de gravedad" etc. | Exceso de claim. Los experimentos validan mecanismos parciales (links → Newton en 12-13) pero falsifican otros (ISW, etc.). Precedentes literarios existen para partes. | Lenguaje preciso: "mecanismo de links reproduce kernel newtoniano en tests estáticos"; "postulado X sobrevive tests Y"; "no se encontró precedente para Z". Citar baselines (Glaser-Surya, Carlip, Sakstein). |

---

## 3. Tabla de Equivalencias

### Código → Paper (notación unificada)

| Código (analysis/, scripts) | Paper (notación recomendada) | Notas |
|-----------------------------|------------------------------|-------|
| `epsilon_link`, `eps_link`, `epsilon_frac` | \(\eta_{\rm link}\) o \(\epsilon_{\rm link}\) (con footnote) | En paper preferir griego \(\eta\) para fracciones (evita confusión con epsilon de otros contextos). Definir explícitamente como \(\langle N_{\rm links}\rangle / \langle N_{\rm past}\rangle\). |
| `v_link`, `valencia`, `valencia_frw` | \(v_{\rm link}\) o \(N_{\rm links}\) (por elemento) | Clarificar que es valencia media (conteo), no fracción. |
| `eta_E`, `eta_energy` (o expresión \(\pi\sqrt{6} \sqrt{\rho} E_R^2 / M_{\rm Pl}^4\)) | \(\eta_E\) | Solo para scaling/abundancia adim.; **nunca** llamar "fracción" o usar como \(\epsilon_{\rm link}\). |
| `v_R`, `dR_dt` | \(v_R = d\mathcal{R}/dt\) | Mantener. Acompañar siempre de \(\beta_t\) o equivalente. |
| `psi` (campo) | \(\psi\) | Definir como \(\psi = \nabla \ln \mathcal{R}\). En métrica: \(e^{\pm 2\psi}\). |

### Proyecto → Literatura (precedentes y mapeos)

| Concepto del Proyecto | Equivalente / Precedente en Literatura | Referencia | Notas de Diferencia |
|-----------------------|---------------------------------------|------------|---------------------|
| \(v_{\rm link}\) (valencia media de links en sprinkling con cutoff) | "valency" (número de nearest neighbours / covering relations) | Glaser & Surya, Phys. Rev. D 88, 124026 (2013) arXiv:1309.3403; Surya, Living Rev. Relativ. 22, 5 (2019) | Literatura nota que es "infinite" en límite continuo sin cutoff (región hyperboloid volumen infinito). Proyecto usa cutoff finito \(L_R\) o \(T\) → finita y sigue ~área. |
| \(\epsilon_{\rm link}\) (fracción normalizada) | "linking fraction" \( p = N_0 / (n^2 / 2) \) | Carlip, "Causal Sets and an Emerging Continuum", arXiv:2405.14059 (2024) | Carlip usa \(p\) global combinatorio sobre todos los pares posibles. Proyecto normaliza localmente por \(N_{\rm past}\) (candidatos causales). Ambos <<1 en N grande. |
| \(\eta_E\) (abundancia adim. con escala energía) | Factores en interval abundances \(\langle N_m^d \rangle\), \(\chi_k\) (Myrheim-Meyer etc.) | Glaser & Surya 2013; Roy et al. para d'Alembertian | \(\pi\sqrt{6}\) surge de integral de banda de links en 4D (volumen ~\(\tau^4\)); no aparece verbatim como coeficiente de abundancia de links en las refs principales (aparece en kernels de acción BD). |
| \(\psi = \nabla \ln \mathcal{R}(t)\) + métrica disforme | Disformal transformations / acoplamientos con factores \(A(\phi)\), \(B(\phi)\) generando \(e^{\pm 2\psi}\)-like | Bekenstein (1993); Sakstein arXiv:1409.1734; Bettoni & Liberati arXiv:1306.6724 | Fuentes dan transformaciones generales o acoplamientos a materia. Ninguna usa motivación "canvas Minkowski fijo + \(\mathcal{R}(t)\) variable" ni deriva la forma exacta desde conteo de links / resolución. Pueden citarse para límites newtonianos y screening. |
| \(G_{\rm eff} = G \epsilon_{\rm link} f(\psi)\) | \(G_{\rm eff}( \phi, X )\) modificada por factores disformales | Sakstein 2014; Zumalacárregui et al.; Koivisto screening papers | Factorización con \(\epsilon_{\rm link}\) (fracción de links) no reportada. \(f(\psi)\) con \(\psi\) de links es nuevo en esta motivación. |

---

## 4. Quién Audita Cuándo

| Auditor | Responsabilidad | Momento |
|---------|-----------------|---------|
| **Fable** | Audita paper/ (claims, lenguaje, precedentes, honestidad de alcance, falsificaciones reportadas). | Después del domingo (post pre-reg / runs). No antes de que código y notas estén estables. |
| **Codex** | Valida consistencia dimensional y notación (convenciones [ℛ]=1, subíndices en β, L_R vs E_R, fracciones vs abundancias). | En cada draft de notas o antes de push a papel. Revisa que no se usen anti-símbolos. |
| **Grok** | Valida precedentes literarios y equivalencias (búsquedas arXiv/CST/CDT, citas correctas a Glaser-Surya, Carlip, Sakstein, etc.; "NO ENCONTRADO" cuando corresponde). | En revisiones de notas (ej. variables_literature_review, symbol_table). Actualiza cuando hay búsquedas nuevas. |

**Reglas operativas:**
- Cualquier cambio en definiciones de v_R, ε_link, etc. debe actualizar esta tabla primero.
- Antes de escribir en paper/: cruzar contra esta tabla + anti-símbolos.
- Claims de prioridad solo después de validación Grok (precedentes) + Codex (dims) + Fable (alcance honesto).
- Esta tabla vive en `notes/` y es la fuente de verdad para convenciones nuevas.

**Convención ℛ cerrada 2026-07-03:** \([\mathcal{R}]=1\). Usar \(L_R/E_R\) para dimensionales.

---

**Fin del documento.** Mantener actualizado. No copiar claims sin pasar por las auditorías listadas.