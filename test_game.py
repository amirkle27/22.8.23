# from Terminal > pip install pytest
# from Terminal > pytest .
import pytest
import game



def test_validity_str_num():
    x: str = "rock"
    expected: int = 2
    actual: int = game.check_validity(x)

    assert expected == actual
"""This test has to be performed from the Terminal, using 'pytest -s'.
 It would not work in here because pytest is trying to capture standard input/output
  (stdin/stdout) while executing the tests"""
