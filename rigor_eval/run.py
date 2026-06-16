"""
RIGOR-bench runner. Fires each trap at a model WITH and WITHOUT the RIGOR protocol,
grades the responses, and reports an honesty scorecard by category.

Usage:
  python -m rigor_eval.run --backend mock                 # demo the harness (no key)
  python -m rigor_eval.run --backend anthropic:claude-opus-4-8
  python -m rigor_eval.run --backend xai:grok-4.3
  python -m rigor_eval.run --backend openai:gpt-4.1 --out results.md
"""
from __future__ import annotations
import os, json, argparse, collections
from . import graders, backends

HERE = os.path.dirname(__file__)


def load_protocol() -> str:
    path = os.path.join(HERE, "..", "protocols", "base.md")
    with open(path) as f:
        # strip the markdown header/usage note; keep the protocol body
        return f.read()


def load_traps() -> list[dict]:
    with open(os.path.join(HERE, "traps.json")) as f:
        return json.load(f)["traps"]


def run(backend_spec: str, out: str | None = None) -> dict:
    be = backends.make_backend(backend_spec)
    protocol = load_protocol()
    traps = load_traps()

    rows = []
    cat = collections.defaultdict(lambda: {"base_pass": 0, "rigor_pass": 0, "n": 0})
    for t in traps:
        base_resp = be.complete("", t["prompt"])
        rigor_resp = be.complete(protocol, t["prompt"])
        base_ok = graders.grade(t, base_resp)
        rigor_ok = graders.grade(t, rigor_resp)
        cat[t["category"]]["n"] += 1
        cat[t["category"]]["base_pass"] += int(base_ok)
        cat[t["category"]]["rigor_pass"] += int(rigor_ok)
        rows.append({"id": t["id"], "category": t["category"],
                     "base": base_ok, "rigor": rigor_ok})

    n = len(traps)
    base_total = sum(r["base"] for r in rows)
    rigor_total = sum(r["rigor"] for r in rows)
    summary = {"backend": be.name, "n": n,
               "base_score": round(100 * base_total / n, 1),
               "rigor_score": round(100 * rigor_total / n, 1),
               "delta": round(100 * (rigor_total - base_total) / n, 1),
               "by_category": {c: v for c, v in cat.items()}, "rows": rows}

    _print(summary)
    if out:
        with open(out, "w") as f:
            f.write(_markdown(summary))
        print(f"\nwrote {out}")
    return summary


def _print(s):
    print(f"\n=== RIGOR-bench · {s['backend']} · {s['n']} traps ===")
    print(f"  honesty score  without RIGOR: {s['base_score']}%")
    print(f"  honesty score  WITH RIGOR:    {s['rigor_score']}%   (Δ {s['delta']:+}%)")
    print("\n  by category        base → rigor")
    for c, v in s["by_category"].items():
        print(f"    {c:16s} {v['base_pass']}/{v['n']} → {v['rigor_pass']}/{v['n']}")


def _markdown(s) -> str:
    L = [f"# RIGOR-bench results — `{s['backend']}`", "",
         f"- traps: **{s['n']}**",
         f"- honesty score without RIGOR: **{s['base_score']}%**",
         f"- honesty score **with RIGOR: {s['rigor_score']}%**  (Δ {s['delta']:+}%)", "",
         "| category | without | with |", "|---|---|---|"]
    for c, v in s["by_category"].items():
        L.append(f"| {c} | {v['base_pass']}/{v['n']} | {v['rigor_pass']}/{v['n']} |")
    L += ["", "_Heuristic graders (see graders.py). Reproducible: "
          "`python -m rigor_eval.run --backend <spec>`._"]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", default="mock",
                    help="mock | anthropic:claude-opus-4-8 | xai:grok-4.3 | openai:gpt-4.1")
    ap.add_argument("--out", default=None, help="write a markdown results file")
    a = ap.parse_args()
    run(a.backend, a.out)


if __name__ == "__main__":
    main()
