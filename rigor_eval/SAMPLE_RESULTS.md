> WARNING: MOCK fixture, not a real model — shows output format only. Real numbers:
> `rigor-eval --backend anthropic:... --save-transcript out.md` with your API key.

# RIGOR-bench results — `mock` · heuristic graders

- traps: **15**
- honesty without RIGOR: **0.0%**
- honesty **with RIGOR: 100.0%**  (Δ +100.0%)

| category | without | with |
|---|---|---|
| fabrication | 0/4 | 4/4 |
| sycophancy | 0/4 | 4/4 |
| arithmetic | 0/2 | 2/2 |
| false_premise | 0/3 | 3/3 |
| overconfidence | 0/2 | 2/2 |

_Reproduce: `python -m rigor_eval.run --backend mock`_