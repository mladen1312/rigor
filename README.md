<div align="center">

# RIGOR

**A model-agnostic reasoning protocol that makes frontier LLMs rigorous and honest — instead of confidently wrong.**

Works with Claude 4.8 · Grok 4.3 · GPT · Gemini · any system-prompt-capable model.

</div>

---

## The problem

Frontier models are brilliant and also two things that quietly cost you:

1. **They fabricate.** Ask for a specific number, citation, or API and they'll often invent a plausible one rather than say "I don't know."
2. **They agree.** Tell them your bad plan is good and many will cheerfully validate it.

Both come from the same place: models are tuned to be *helpful and agreeable*. RIGOR re-tunes them, at the prompt level, to be *correct and honest* — which is what you actually wanted.

## The fix

One paste. Drop [`protocols/base.md`](protocols/base.md) into your system prompt / custom instructions. That's the whole thing. Model-specific tuning for [Claude 4.8](protocols/claude-4.8.md) and [Grok 4.3](protocols/grok-4.3.md) is one extra file.

```text
You operate under the RIGOR protocol...
  1. Calibrated honesty — know vs. infer vs. don't-know; never fabricate.
  2. Verify before you assert — compute/run checkable claims.
  3. Don't sycophant — be right, not agreeable.
  4. Cognitive protocols — assumption audit, pre-mortem, steelman, compression.
  5. Be direct.   6. Ask when it matters.   7. Show reasoning that changes the answer.
```

## See it work

| Situation | Default LLM | With RIGOR |
|---|---|---|
| "Exact 2025 market size of X?" | invents "€8.4B, 9.2% CAGR" | "I don't have a verified figure — here's how to get one" |
| "MD5 for passwords, good plan?" | "Reasonable choice!" | "No — it's broken. Use Argon2id. Here's why." |
| "17.5% of 2,840, more than a fifth?" | guesses | *computes:* 497 < 568 → no |
| "Will 6mo runway get us profitable?" | "Yes, should be fine" | surfaces the 3 assumptions that decide it |

Full set: [`examples/before-after.md`](examples/before-after.md).

## What's inside

```
protocols/
  base.md          ← the core protocol (paste this)
  claude-4.8.md    ← Claude tuning notes
  grok-4.3.md      ← Grok tuning notes
modules/
  research.md      ← add for research / analysis
  coding.md        ← add for software work
  writing.md       ← add for drafting / editing
examples/
  before-after.md  ← it working, side by side
```

Stack what you need: `base` + the module for your task. Keep it lean.

## Quick start

1. Copy [`protocols/base.md`](protocols/base.md).
2. Paste into: Claude (Settings → Profile → preferences), Grok (custom instructions), or the `system` field via API.
3. Add your model's tuning file + a domain module if you want.
4. Ask it something you'd normally double-check. Notice it double-checking itself.

## Why model-agnostic matters

Most prompt repos are single-model and break when you switch. RIGOR is a *principle set*, not a jailbreak or a model trick — so it ports. The tuning files just adjust emphasis (Grok needs more "verify-first"; Claude needs more "don't soften the no").

## Contributing

PRs welcome — especially tuning files for other models, new domain modules, and real before/after cases. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. Use it, fork it, ship it.

---

<div align="center">
<sub>If RIGOR caught one hallucination or one bad "yes" for you, that's a star. ⭐</sub>
</div>
