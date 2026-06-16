# RIGOR — Claude 4.8 tuning

Use `protocols/base.md` as the system prompt, plus these notes.

**Where to put it:** Claude apps → Settings → Profile → "user preferences" /
custom instructions, or the `system` field via API. For Claude Code / Cowork,
drop `base.md` into a project skill or `CLAUDE.md`.

**Tuning notes**
- Claude already leans honest and will say "I don't know" — RIGOR mostly *amplifies*
  this and adds the cognitive protocols. The biggest lift is rule 3 (anti-sycophancy)
  and rule 2 (verify) which benefit from explicit instruction.
- Claude follows structured, principle-based instructions well. Keep the protocol
  as-is; you don't need to over-specify.
- For long technical work, Claude responds well to the Compression protocol — it
  will proactively offer state summaries if told to.
- If you want minimal hedging, add: "State known facts without disclaimers."
- Pair with Claude's code execution so rule 2 (verify) actually runs the check.

**One-line add-on for research/engineering:**
> "When a claim is computationally testable, write and run the code; show raw
> results, not a description of what the code would show."
