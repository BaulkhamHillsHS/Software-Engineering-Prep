# Lab 02 — Calculator (Variables & I/O)

Write `calc.py` with two functions and a simple CLI:

## Part A — Functions
- `add(a: float, b: float) -> float`
- `divide(a: float, b: float) -> float` (raise `ValueError` if `b == 0`)

## Part B — CLI

If the user runs `python calc.py` prompt for two numbers, then print:
```
sum: <value>
quotient: <value or 'undefined'>
```

### Run tests

```bash
pytest -q labs/lab02_calc/tests/test_calc.py
```
