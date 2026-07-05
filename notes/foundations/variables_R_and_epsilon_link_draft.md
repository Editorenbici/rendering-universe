# Variables \(v_R\) y \(\epsilon_{\rm link}\)

**Fuente revisada:** Documents/Codex/.../notes/variables_R_and_epsilon_link_draft.md (Codex update 2026-07-03)  
**Proyecto canonical:** Esta copia en rendering-universe/notes/ (para trabajo consistente).  
**Fecha revisión:** 2026-07-03 (Grok)  
**Estado:** borrador técnico interno. No tocar paper/ ni README/.

## Revisión de convención ℛ (prueba dimensional + conflicto β / v_R)

**Convención elegida en el borrador de Codex:**  
\([\mathcal{R}] = 1\) (adimensional, "conteo/índice de resolución").

**Análisis dimensional:**
- Con \([\mathcal{R}]=1\), entonces \([v_R] = T^{-1}\).
- \(\beta_t = d\ln\mathcal{R}/d\ln t\) es adimensional.
- \(v_R = d\mathcal{R}/dt = \beta_t \mathcal{R}/t \) es consistente (unidades 1/tiempo).
- Se separan correctamente símbolos dimensionales cuando se compara con \(M_{\rm Pl}\): usar \(L_R\) (longitud) o \(E_R\) (energía), no insertar \(\mathcal{R}\) adim. directamente en fórmulas con masas/energías.
- Para \(\epsilon_{\rm link}\): el borrador distingue valencia \(\langle N_{\rm links}\rangle \simeq \pi\sqrt{6}\sqrt{\rho} L_R^2\) (crece con área) de la fracción \(\epsilon_{\rm link}\).
- Prueba numérica reportada en borrador (script 25_R_convention_check.py): \(\pi\sqrt{6} \sqrt{\rho} E_R^2 / M_{\rm Pl}^4 \) da ~770 para \(E_R=10\), y ~7.7e60 para \(E_R=10^{30}\). Esto **no puede** ser \(\epsilon_{\rm link}\) si \(\epsilon_{\rm link}\) debe ser una fracción \(0 \le \epsilon_{\rm link} \ll 1\).

**Conflicto entre \(\beta = d\ln\mathcal{R}/d\ln t\) y \(v_R = \beta H \mathcal{R}\):**
- El borrador identifica correctamente el problema de notación.
- Definición de proyecto (Exp 15, BAO/DESI etc.): \(\beta_t \equiv d\ln\mathcal{R}/d\ln t\).
- Entonces \(v_R = \beta_t \mathcal{R}/t \).
- La forma compacta \(v_R = \beta H \mathcal{R}\) **solo vale** si \(\beta\) se redefine como \(\beta_a \equiv d\ln\mathcal{R}/d\ln a\).
- Relación: \(\beta_a = \beta_t / (H t)\).
- Por lo tanto: \(\beta_a H \mathcal{R} = \beta_t \mathcal{R}/t \). Ambas dan el mismo \(v_R\), pero **hay conflicto/pitfall si se usa \(\beta\) sin subíndice**.
- No hay inconsistencia física, solo riesgo de error de notación al mezclar convenciones de tiempo propio vs factor de escala.
- Inversiones correctas según borrador:
  \[
  \beta_t = \frac{t v_R}{\mathcal{R}}, \qquad \beta_a = \frac{v_R}{H \mathcal{R}}.
  \]

**Sobre \(\epsilon_{\rm link}\):**
- Definición en borrador: \(\epsilon_{\rm link} \equiv \langle N_{\rm links}\rangle / \langle N_{\rm total}\rangle\).
- Propuesta operativa corregida: \(\epsilon_{\rm link} \equiv \langle N_{\rm links}\rangle / \langle N_{\rm past}\rangle \sim (\pi\sqrt{6}/C_4) \rho^{-1/2} L_R^{-2} \ll 1\).
- Esto es consistente con "eficiencia de linking" <<1 y con uso en \(G_{\rm eff} = G \epsilon_{\rm link} f(\psi)\).
- Si se usara la valencia cruda como \(\epsilon_{\rm link}\), se violaría fuertemente \(\epsilon_{\rm link} \ll 1\) (ver prueba \(E_R = 10^{30}\)).

**Conclusión de revisión:** La dimensional analysis es consistente **bajo la convención elegida** \([\mathcal{R}]=1\). El borrador de Codex maneja bien las distinciones y la prueba numérica. El único punto delicado es la ambigüedad de \(\beta\) (ya documentada en el borrador).

---

## Convención adoptada

**Elección:**  
\([\mathcal{R}] = 1\) (adimensional). \(\mathcal{R}\) es un conteo/índice puro de resolución causal. Cantidades con dimensiones de longitud o energía se denotan explícitamente \(L_R\), \(E_R\).

**Justificación numérica de la prueba (del borrador + validación):**
- Usar directamente el escalamiento de valencia \(\pi\sqrt{6}\sqrt{\rho} E_R^2 / M_{\rm Pl}^4\) como si fuera \(\epsilon_{\rm link}\) produce valores >>1 (ej. \(7.7 \times 10^{60}\) cuando \(E_R \sim 10^{30}\), típico de la resolución hoy).
- Esto viola el significado físico de "eficiencia de linking" o "fracción" (debe ser \(\ll 1\)).
- **RECHAZAR** cualquier uso de la valencia cruda \(\pi\sqrt{6}\sqrt{\rho} L_R^2\) (o versión con \(E_R\)) como \(\epsilon_{\rm link}\) sin normalizar.
- **Correcto:** normalizar por el número de candidatos pasados \(\langle N_{\rm past}\rangle \sim C_4 \rho L_R^4\), obteniendo
  \[
  \epsilon_{\rm link} \sim \frac{\pi\sqrt{6}}{C_4} \rho^{-1/2} L_R^{-2} \ll 1
  \]
  (C_4 depende de geometría: slab, diamante, etc.; se mide directamente en simulaciones).
- Con esta normalización, \(\epsilon_{\rm link}\) es una fracción adimensional pequeña, consistente con \(G_{\rm eff} = G \epsilon_{\rm link} f(\psi)\) y con la convención \([\mathcal{R}]=1\).

**Relación con \(\beta\) y \(v_R\):**
- Usar siempre subíndices cuando sea necesario: \(\beta_t = d\ln\mathcal{R}/d\ln t\) (convención del proyecto).
- \(v_R = \beta_t \mathcal{R}/t\).
- La forma \(v_R = \beta H \mathcal{R}\) requiere definir \(\beta \equiv \beta_a = d\ln\mathcal{R}/d\ln a\).
- Ambas son equivalentes vía la relación \(\beta_a = \beta_t/(H t)\); documentar explícitamente cuál se usa.

**G_eff:**
\[
G_{\rm eff} = G \, \epsilon_{\rm link} \, f(\psi), \qquad f(\psi) = 1 + \mathcal{O}(\psi^2)
\]
(para no alterar el matching newtoniano lineal).

---

## Búsqueda de teoría efectiva CST: effective action / continuum limit Lagrangian para campos escalares

**Pregunta específica:** ¿Existe en la literatura un Lagrangiano de campo escalar en CST o CDT cuyo límite continuo reproduzca una **métrica disforme**?

**Resultado:** NO ENCONTRADO.

**Fuentes relevantes encontradas (0-3 para el match exacto):**
- Benincasa et al. (Phys. Rev. Lett. 104, 181301, 2010 y trabajos relacionados): definen operadores discretos (d'Alembertiano no-local) para campos escalares en causal sets. En el límite continuo aproximan el operador \(\square - \frac12 R\) (o similar) sobre el manifold de fondo. Sirve para construir acción escalar discreta que → acción continua con curvatura. **No hay métrica disforme**.
- Salgado (thesis), Cunningham et al., Surya et al.: acciones y propagadores para campos escalares en CST que aproximan la acción clásica del campo escalar libre en Minkowski/curvo en el límite. Dinámica de campos en sprinklings Poisson. **Sin transformación disforme ni límite disforme**.
- Trabajos sobre QFT en causal sets (propagadores, detectores, backreaction): aproximan QFT estándar en el continuo. **Sin disformal**.

Búsquedas específicas ("disformal" + "causal set"/CST/CDT + scalar/Lagrangian/action/effective/continuum) no devolvieron ningún paper que derive una métrica disforme \(\tilde g_{\mu\nu} = g_{\mu\nu} + B \partial_\mu\phi \partial_\nu\phi\) (o similar) a partir de una discretización CST/CDT de un campo escalar.

**Conclusión operativa:** La conexión entre la discretización causal (links, resolución variable \(\mathcal{R}(t)\)) y la métrica disforme con \(\psi\) (derivada de \(\nabla \ln \mathcal{R}\)) parece específica de este proyecto. Citar los trabajos de d'Alembertiano discreto de CST como baseline para campos escalares, pero la factorización vía \(\epsilon_{\rm link}\) y la forma disforme particular no tienen precedente encontrado.

---

**Notas finales de homologación:**
- Mantener \([\mathcal{R}]=1\) como sticky.
- Siempre clarificar \(\beta_t\) vs \(\beta_a\) y \(L_R\) vs \(E_R\) cuando se comparan con escalas físicas.
- Usar \(\epsilon_{\rm link} \ll 1\) normalizado (N_links / N_past o equivalente medido).
- Para código: medir tanto valencia cruda como la fracción normalizada.

DONE (revisión + convención stickeada + búsqueda CST).