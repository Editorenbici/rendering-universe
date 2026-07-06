# rendernum

`rendernum` is a small Python package for finite-resolution arithmetic over
dyadic intervals, the arithmetic object used in the Render Universe notes as
`N_R`.

It is intentionally minimal:

- finite measurements are intervals of width `2^-R`;
- exact rationals live in the vector layer with zero width;
- addition follows the law of the minimum through interval propagation;
- multiplication and division use exact interval arithmetic;
- division by an unresolved zero returns `TOP_R`;
- `+INF_R` and `-INF_R` are relative to the resolution grade.

Install locally:

```bash
python -m pip install -e packages/rendernum
```

Quick use:

```python
from rendernum import from_float, from_fraction, exact, top, pos_inf

x = from_float(1.0, R=3)
y = from_fraction(1, 3)      # exact rational
z = x + y
```

The package is a formal artifact, not a physics claim.

