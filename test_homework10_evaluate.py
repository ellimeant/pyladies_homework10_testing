def test_evaluate_1():
    boardstring = "---------------x--"
    assert "xxx" in boardstring
    raise AssertionError("The string doesn't contain 'xxx'!")
    #assert len(20) == True

def test_evaluate_2():
    boardstring = "-------------xxx--"
    assert "xxx" in boardstring == True
    # assert len(20) == True