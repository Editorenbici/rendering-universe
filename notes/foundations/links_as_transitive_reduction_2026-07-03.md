# Links as Transitive Reduction / Hasse Diagram

**Date:** 2026-07-03  
**Sources (verified):**  
- Wikipedia "Covering relation" and "Transitive reduction" (standard order theory definitions).  
- Glaser & Surya, "Towards a Definition of Locality in a Manifoldlike Causal Set", arXiv:1309.3403 (2013) — explicit statement that links are the irreducible (covering) relations.  
- Surya, "The causal set approach to quantum gravity", Living Rev. Relativ. 22, 5 (2019) — discussion of links, valency, and non-locality in sprinklings.  
- Standard references on posets and DAGs (transitive reduction uniqueness for acyclic graphs).

**Purpose:** Formalize the statement that a link is the irreducible direct causal step, using precise mathematical language. Keep everything at the level of poset/graph definitions and CST translation. No physical claims.

## Formal Definition

In a partially ordered set (poset) (P, ≼):

- An element y **covers** x (written x ⋖ y) if and only if x ≺ y (i.e., x ≼ y and x ≠ y) **and** there is no z ∈ P such that x ≺ z ≺ y.

Equivalently: the order interval [x, y] = {z | x ≼ z ≼ y} contains exactly two elements {x, y}.

The set of all such covering pairs is called the **covering relation** of the poset.

For a directed acyclic graph (DAG) representing a poset (where an edge u → v means u ≺ v):

- The **transitive reduction** is the unique smallest subgraph that has exactly the same reachability relation as the original graph.  
- In a DAG, this transitive reduction consists precisely of the covering relations and is called the **Hasse diagram** of the poset.

For finite DAGs / posets the transitive reduction is unique.

## Translation to Causal Sets (CST)

In a causal set C (a locally finite poset):

- The **links** are exactly the covering relations: y is a link to the future of x (or x ≺ y is a link) if x ≺ y and there exists no z with x ≺ z ≺ y.
- The Hasse diagram of the causal set is the graph whose edges are precisely these links (the irreducible causal relations).
- Counting "raw causal past" of an element counts **all** y ≺ x (the full transitive closure).  
- Counting **links** counts only the direct (covering) predecessors/successors.

Thus: the link count is the result of taking the transitive reduction of the causal graph.

## Visual Analogy

Imagine the full causal graph as a dense web of arrows (all transitive relations).  
The Hasse diagram / link graph is the "skeleton" obtained by erasing every arrow that can be reconstructed as a chain of two or more shorter arrows. What remains are the immediate "steps" — the edges that cannot be shortcut.

In a sprinkling, most potential future elements are "blocked" by intermediates; only the unblocked nearest ones survive as links in the Hasse diagram.

## Risks

- In manifold-like sprinklings into Minkowski space (d > 1+1), the number of links per element (valency) is typically **infinite** because the relevant region (hyperboloid near the light cone) has infinite volume. This is a direct consequence of Lorentz invariance + discreteness (Surya 2019 review).
- Conflating "number of causal past elements" with "number of links" changes the scaling dramatically: the former can be volume-like, the latter is governed by the thin shell near the light cone.
- The transitive reduction assumes the structure is a strict partial order (acyclic, transitive, etc.). Adding noise or approximate relations can make the reduction non-unique or unstable.

## 2–3 Verified References

1. Glaser & Surya (2013), arXiv:1309.3403: "In a causal set, the nearest neighbours of an element are the links or irreducible relations."
2. Surya (2019), Living Rev. Relativ. 22, 5: discussion of links as covering relations and the resulting infinite valency in continuum-like sprinklings.
3. Standard order theory: Covering relation definition (e.g., Wikipedia "Covering relation"); Transitive reduction is unique for DAGs and yields the Hasse diagram.

**Strictly formal note.** All statements are definitions or direct translations from the cited mathematical and CST literature. No extrapolation to physics or new claims.

## Appendix: Language guardrails

**Bad wording:** “Los links son la realidad fundamental.”  
**Safer wording:** “En la representación como poset, los links son las relaciones de cubrimiento (covering relations) del orden causal.”  
**Why:** Convierte una definición matemática del orden parcial en una afirmación ontológica.

**Bad wording:** “El universo está hecho de links.”  
**Safer wording:** “Este experimento cuenta los links del poset, es decir, los pares irreducibles según la definición de transitive reduction.”  
**Why:** Usa el lenguaje del poset como si describiera la constitución última del mundo.

**Bad wording:** “Los links son los verdaderos portadores de la causalidad.”  
**Safer wording:** “Los links son los elementos del diagrama de Hasse: las únicas relaciones que no pueden ser reconstruidas a partir de cadenas más largas en el poset.”  
**Why:** Atribuye un rol físico privilegiado en lugar de una propiedad formal del grafo reducido.

**Bad wording:** “Contar links captura toda la información causal real.”  
**Safer wording:** “Contar links equivale a usar la transitive reduction del grafo causal; contar el pasado causal completo usa la clausura transitiva.”  
**Why:** Borra la distinción precisa entre el grafo reducido y el grafo con todas las relaciones transitivas.

**Bad wording:** “A diferencia de otras teorías, aquí la estructura básica son los links.”  
**Safer wording:** “En el formalismo de posets usado aquí, la reducción transitiva (Hasse diagram) retiene exactamente las mismas relaciones de alcanzabilidad que el poset original, pero solo con los bordes irreducibles.”  
**Why:** Presenta los links como una ventaja ontológica en lugar de una elección de representación matemática del orden.
