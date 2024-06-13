from homework10_testing import move, evaluate

def test_evaluate_1():
    boardstring = "-------------xxx--"
    result = evaluate(boardstring)
    assert result == "X won"
    #assert len(20) == True

def test_evaluate_2():
    board = "HelloWord HelloWorld"
    res = evaluate(board)
    assert res == "game not over yet"

def test_evaluate_3():
    boardie = "ooxxooxxooxxoxooxxoo"
    res = evaluate(boardie)
    assert res == "draw"


#this test does not test the function but just if the variable boardstring is contains "xxx".
def test_evaluate_variablecontent():
    boardstring = "-------------xxx--"
    result = evaluate(boardstring)
    assert "xxx" in boardstring
    # assert len(20) == True