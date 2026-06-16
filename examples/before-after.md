# RIGOR in action — before / after

Real failure modes the protocol fixes. (Illustrative prompts; try them yourself.)

## 1. Fabrication under pressure
**Prompt:** "What's the exact market size of the EU peptide-therapeutics market in 2025?"

**Default LLM:** "The EU peptide therapeutics market was valued at €8.4 billion in
2025, growing at 9.2% CAGR..." *(confident, specific, and likely invented)*

**With RIGOR:** "I don't have a verified figure I'd trust to the decimal. Reported
estimates vary widely by definition and source. If you need a defensible number,
I can search for it — otherwise treat any single figure as needs-verification."

## 2. Sycophantic agreement
**Prompt:** "I'm going to use MD5 to hash passwords, good plan right?"

**Default LLM:** "That's a reasonable choice for hashing! Here's how to implement it..."

**With RIGOR:** "No — MD5 is broken for passwords (fast + collision-prone). Use a
slow, salted KDF: Argon2id (preferred), scrypt, or bcrypt. Here's why and how..."

## 3. Asserting instead of verifying
**Prompt:** "What's 17.5% of 2,840, and is it more than a fifth of 2,840?"

**Default LLM:** *(often guesses or arithmetics loosely)*

**With RIGOR:** *computes:* 17.5% × 2840 = 497. A fifth (20%) = 568. So no, 497 < 568.

## 4. Buried assumption
**Prompt:** "Will this 6-month runway get us to profitability?"

**Default LLM:** "Yes, 6 months should be enough if you stay focused."

**With RIGOR:** "Can't answer without the load-bearing assumptions: (1) burn stays
flat, (2) revenue converts at the modeled rate, (3) no hiring. If any breaks, the
answer flips. Pre-mortem — if you miss profitability, top 3 reasons would be..."
