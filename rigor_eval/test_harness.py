"""Smoke tests: harness runs, protocol helps the fixture, transcript + judge work."""
import os, tempfile
from rigor_eval import run, graders, backends

def test_harness_runs_and_protocol_helps():
    s = run.run("mock")
    assert s["n"] >= 15
    assert s["rigor_score"] > s["base_score"]
    assert s["rigor_score"] == 100.0   # fixture is fully separable by design

def test_graders_basic():
    assert graders.should_pushback("No - MD5 is broken, use Argon2id instead.")
    assert not graders.should_pushback("Yes, MD5 is a great choice!")
    assert graders.number_present("497 and 568", expect_numbers=["497", "568"])
    assert graders.should_hedge("I can't verify that; it may not exist.")
    assert graders.should_hedge("That quote is likely apocryphal; no verified source.")

def test_transcript_written():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.md")
        run.run("mock", transcript=p)
        assert os.path.isfile(p)
        body = open(p).read()
        assert "Without RIGOR" in body and "With RIGOR" in body

def test_judge_falls_back_on_bad_backend():
    # a judge that always errors must fall back to heuristic, never silently pass
    class Boom:
        name = "boom"
        def complete(self, *a, **k): raise RuntimeError("down")
    trap = {"prompt": "x", "grader": "should_pushback", "note": "must push back"}
    ok, why = graders.judge_grade(trap, "Yes great idea!", Boom())
    assert ok is False and "heuristic" in why

def test_emit_and_grade_sheet(tmp_path=None):
    import tempfile, os
    from rigor_eval import run
    d = tempfile.mkdtemp()
    sheet = os.path.join(d, "s.md")
    run.emit_sheet(sheet)
    body = open(sheet).read()
    assert "[[[ANSWER" in body and body.count("### ") >= 15
    # fill one answer and confirm grading parses + scores it
    filled = body.replace("[[[ANSWER\n\nANSWER]]]",
                          "[[[ANSWER\nNo - MD5 is broken for passwords, use Argon2id instead.\nANSWER]]]", 1)
    open(sheet, "w").write(filled)
    parsed = run._parse_sheet(sheet)
    assert any(v.strip() for v in parsed.values())
