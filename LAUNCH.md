# Launch kit (copy-paste, then fill the real numbers)

> Replace every `__%` with your actual `rigor-eval` output. Posting fake numbers
> would be the exact thing this repo is against — and people will run it and check.

## X / Twitter thread (tight)

**1/**
LLMs are trained to be agreeable, not correct.
So they make things up and tell you your bad ideas are good.
I wrote a prompt that fixes both — and a benchmark that proves it. 🧵

**2/**
One paste into the system prompt. The model starts:
• saying "I don't know" instead of inventing
• pushing back when you're wrong
• checking math instead of guessing
[screenshot: a before/after pair from your transcript]

**3/**
Don't trust me — measure it.
`rigor-eval` fires 15 trap prompts at your model with & without the protocol and scores honesty.
On [Claude 4.8 / Grok 4.3]: __% → __% (Δ +__%).
[screenshot: the scorecard]

**4/**
Works on Claude 4.8, Grok 4.3, GPT, Gemini — it's a principle set, not a model trick.
MIT. Run it on your model in 2 min:
github.com/mladen1312/rigor
⭐ if it caught a hallucination for you.

## Show HN

**Title:** Show HN: RIGOR – a prompt that makes LLMs say "I don't know" (with a benchmark)

**First comment:**
> LLMs fabricate and agree because they're tuned to be helpful. RIGOR is a system
> prompt that re-tunes them toward honest — admit uncertainty, push back, verify.
> The part I care about: it ships a benchmark (`rigor-eval`) so you don't take my
> word for it — it scores your model with/without the protocol on 15 trap prompts.
> Heuristic graders by default, optional LLM-judge. Works on Claude/Grok/GPT.
> Feedback on the traps and graders especially welcome.

## Reddit (r/LocalLLaMA, r/PromptEngineering, r/ClaudeAI, r/grok)
Lead with the problem, show the scorecard, link last. Title e.g.:
"I benchmarked how often LLMs fabricate vs. admit 'I don't know' — and a one-paste prompt that moves the number."

## Timing & cadence
- Tue–Thu, morning US time.
- Reply to every comment in the first 2 hours (early momentum compounds).
- New model drops → add a tuning file + post fresh numbers. Free re-share.

## Honest expectation
Most repos get <50 stars; a few get thousands. Quality + real numbers raise your
odds, distribution raises them more, luck does the rest. Ship, share, iterate.
