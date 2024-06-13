import pytest
from homework10_testing import move, evaluate

def test_evaluate_x_wins():
    boardstring = "-------------xxx--"
    result = evaluate(boardstring)
    assert result == "X won"
    #assert len(20) == True

def test_evaluate_continue_game():
    board = "HelloWord HelloWorld"
    res = evaluate(board)
    assert res == "game not over yet"

def test_evaluate_draw():
    boardie = "ooxxooxxooxxoxooxxoo"
    res = evaluate(boardie)
    assert res == "draw"

def test_valueerror():
    a = "oooxoxxxooxxoxooxxoo"
    with pytest.raises(ValueError):
        evaluate(a)



#this test does not test the function but just if the variable boardstring is contains "xxx".
def test_evaluate_variablecontent():
    boardstring = "-------------xxx--"
    result = evaluate(boardstring)
    assert "xxx" in boardstring
    # assert len(20) == True