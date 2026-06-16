# RIGOR — Claude 4.8 (recommended emphasis)

> ⚠️ **Lightweight, not exhaustive.** These are *emphasis tweaks*, not a claim of
> deep model-specific knowledge. The honest way to tune for your model: run
> `rigor-eval --backend anthropic:claude-opus-4-8`, find the weakest category in the
> scorecard, and lean on the matching rule below. Measure, don't assume.

**Where to put `base.md`:** Claude apps → Settings → Profile → preferences, or the
`system` field via API. For Claude Code / Cowork: a project skill or `CLAUDE.md`.

**Emphasis**
- Claude already leans honest and will say "I don't know," so RIGOR mostly *amplifies*
  it. The marginal gains are usually in rule 3 (don't soften a correct "no" into a
  hedged "yes, but") and rule 2 (actually run the check, don't describe it).
- Claude follows principle-based instructions well — keep `base.md` as-is; don't
  over-specify.
- Pair with code execution so rule 2 verifies for real.
- Want zero hedging on settled facts? Add: "State known facts without disclaimers."

**One-line add-on (research/engineering):**
> "When a claim is computationally testable, write and run the code; show raw
> results, not a description of what the code would show."

*If the benchmark shows Claude already scoring high without RIGOR on some category,
that's expected — RIGOR's lift is larger on models that fabricate/agree more.*
