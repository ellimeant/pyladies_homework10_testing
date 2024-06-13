import pytest
from homework10_testing import move, evaluate

def test_move_1():
    #tests if the board is returned properly
    boardie = "------xxo-----------"
    result = move(boardie, "x", 1)
    assert result =="-x----xxo-----------" 

def test_move_2():
    #tests if function only accepts integers up to and including 20 as position - so that the string doesn't get any longer!
    posit =21
    boardstringie = "------xxo-----------"
    with pytest.raises(ValueError):
        move(boardstringie, "o", posit)