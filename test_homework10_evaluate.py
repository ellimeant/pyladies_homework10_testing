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

#test move function

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

#theory questions:
# a) What is a Python module and how does it differ from a Python package?
# Modules are a bundle of code that we can use straight away as soon as the module is imported into the environment where you want to use it.
# A package contains a number of modules. When you want to import a submodule, you use "import module.submodule".
# b) What are side effects and give some examples.
# A side effect is something that a module does apart from providing functions that we can use; for example, showing a "print" output that does not have any helpful functionality (for example, it could have been created at first to test out a function and then forgotten in the module)
# variables that do not serve any functionality could also  be a side effect that then disrupts the smooth execution from functions that we import from a module.
# c) What are Exceptions and what to do if third-party code that we use throws them?
# An  exception is an error message. If the code throws then, you could raise the exception and some code to overcome them killing a script.
# d) Using which keywords can you create, throw and catch your new custom Exception?
# raise, try, except
# e) Give examples of some benefits of testing?
# 1) You can catch errors in the script functionality before the throw issues when you apply them to other scripts. 2) a test can help you find out if the functionality actually does what you would expect (i.e. do you test what you expect as outcome?)
# 3) You can anticipate potential issues and find workarounds before they appear when someone else uses your code.
