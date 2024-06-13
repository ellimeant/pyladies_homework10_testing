def evaluate(boardstring):
    #boardstring = "------xxx-----------"
    xxx = "xxx"
    ooo = "ooo"
    empty_space = " "

    if xxx in boardstring and ooo in boardstring:
        raise ValueError("This is impossible!")
    elif xxx in boardstring: 
        # this value is boardstring too because it is the input that will change everytime
        return("X won")
    elif ooo in boardstring:
        # this value is boardstring too because it is the input that will change everytime
        return("O won")
    elif empty_space in boardstring: # note to self: default check mode is that an utterance is True.
        return("game not over yet")

    else:
        return("draw")

def move(board, mark, position):
    if position not in range(0,21):
        raise ValueError("Only numbers from 0 to 20!")
    else:
        return board[:position] + mark + board[position+1:] 

teststring = "------xxo-----------"

#print(move(teststring, "x", 24))
