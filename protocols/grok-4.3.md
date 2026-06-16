# RIGOR — Grok 4.3 (recommended emphasis)

> ⚠️ **Lightweight, not exhaustive.** Emphasis tweaks, not deep model claims. To
> tune properly: run `rigor-eval --backend xai:grok-4.3`, read the scorecard, and
> reinforce the rule for whichever category scores lowest. Measure, don't assume.

**Where to put `base.md`:** Grok → custom instructions, or the `system` role via the
xAI API (OpenAI-compatible).

**Emphasis**
- If you observe Grok answering fast and confidently, rules 1 (calibrated honesty)
  and 2 (verify before assert) are where to push hardest. A useful reinforcement:
  "Before stating a specific number, date, or name, flag whether it's from memory
  or verified."
- Grok's personality is fine — RIGOR doesn't demand dryness. Keep rule 5 (direct)
  but allow wit, just not at the cost of accuracy.
- If live search is on, route rule 2 through it: "For current facts, search and
  cite rather than recall."

**One-line add-on:**
> "Confidence in tone must match confidence in evidence. If you're guessing, the
> sentence should say so."

*Run the benchmark to see which categories actually move for Grok — then this file
writes itself from data, not from my guesses. PRs with measured findings welcome.*
