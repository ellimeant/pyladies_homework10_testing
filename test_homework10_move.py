from homework10_testing import move, evaluate

def test_move_1():
    boardie = "------xxo-----------"
    result = move(boardie, "x", 1)
    assert result =="-x----xxo-----------" 