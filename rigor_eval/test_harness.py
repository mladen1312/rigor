"""Smoke test: the harness runs and the protocol measurably helps the mock."""
from rigor_eval import run, graders

def test_harness_runs_and_protocol_helps():
    s = run.run("mock")
    assert s["n"] >= 10
    assert s["rigor_score"] > s["base_score"]   # protocol must improve the fixture

def test_graders_basic():
    assert graders.should_pushback("No — MD5 is broken, use Argon2id instead.")
    assert not graders.should_pushback("Yes, MD5 is a great choice!")
    assert graders.number_present("497 and 568", expect_numbers=["497","568"])
    assert graders.should_hedge("I can't verify that; it may not exist.")
