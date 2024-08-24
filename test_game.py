# from Terminal > pip install pytest
# from Terminal > pytest .
import pytest
import game



def test_validity_rock_num():
    x: str = "rock"
    expected: int = 2
    actual: int = game.check_validity(x)

    assert expected == actual

def test_validity_scissors_num():
    x: str = "scissors"
    expected: int = 1
    actual: int = game.check_validity(x)

    assert  expected == actual


def test_validity_paper_num():
    x: str = "paper"
    expected: int = 0
    actual : int = game.check_validity(x)

    assert expected == actual

def test_validity_caprock_num():
    x: str = "ROCK"
    expected: int = 2
    actual: int = game.check_validity(x)

    assert expected == actual


def test_validity_capscissors_num():
    x: str = "SCISSORS"
    expected: int = 1
    actual: int = game.check_validity(x)

    assert  expected == actual


def test_validity_cappaper_num():
    x: str = "PAPER"
    expected: int = 0
    actual : int = game.check_validity(x)

    assert expected == actual


def test_validity_value_error():
    x: str = "abc"
    with pytest.raises(ValueError) as e:
        actual: int = game.check_validity(x)

    assert str (e.value) == "Illegal Game Option"

def test_winner_draw_rock():
    x: int = 2
    y: int = 2
    expected: int = 0
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_player2():
    x: int = 2
    y: int = 0
    expected: int = 2
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_player1():
    x: int = 2
    y: int = 1
    expected: int = 1
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_player1():
    x: int = 0
    y: int = 2
    expected: int = 1
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_draw_paper():
    x: int = 0
    y: int = 0
    expected: int = 0
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_player2():
    x: int = 0
    y: int = 1
    expected: int = 2
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_player2():
    x: int = 1
    y: int = 2
    expected: int = 2
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_player1():
    x: int = 1
    y: int = 0
    expected: int = 1
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_draw_scissors():
    x: int = 1
    y: int = 1
    expected: int = 0
    actual: int = game.check_winner(x,y)

    assert expected == actual

def test_winner_error():
    x: int = 3
    y: int = 40
    with pytest.raises(ValueError) as e:
        actual: int = game.check_winner(x,y)
    assert str(e.value) == "Illegal Game Option"

