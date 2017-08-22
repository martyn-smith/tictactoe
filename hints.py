def near_victory(board, player):
    """
    Returns a square that will result in a full row, column, or diagonal,
    for player.
    """

    """
    One rejected approach earlier on was to create subgrids (board, resized
    by -1) and check for a victory condition in these.  If found, extending
    by one would result in victory.

    I don't believe this approach will detect X-X situations, and may be
    excessively object-complex, so was abandoned.  The one commented-out line
    of code remains.

    One final remaining concern with the below approach (and all aspects of
    the AI, really) is the determinism.  E.g. given two near_victory conditions,
    one being horizontal and the other vertical, it will always go for the
    vertical.  Given the determinism of tic-tac-toe I do not belive this is a
    problem, but it is worth keeping a watchful eye.
    """
    #subgrids = (board[:-1][:-1], board[1:][1:], board[1:][:-1], board[:-1][1:])
    #find rows
    for i, row in enumerate(board):
        #I keep forgetting why, if the conditional here is not(cell) instead of
        #cell != player.number it ignores valid moves.
        possibles = [j for j, cell in enumerate(row) if cell != player.number]
        if len(possibles) == 1 and not(board[(i, possibles[0])]):
            #print("possible index, row is {} and {}".format(i, possibles[0]))
            return (i, possibles[0])
    #find cols
    for j, col in enumerate(board.transpose()):
        possibles = [i for i, cell in enumerate(col) if cell != player.number]
        if len(possibles) == 1 and not(board[(possibles[0], j)]):
            #print("possible col, index {}, {}".format(possibles[0], j))
            #print("column looks like: {}".format(col))
            #print("possibles: {}".format(possibles))
            return (possibles[0], j)
    #diagonals
    possibles = [x for x, cell in enumerate(board.diagonal()) if cell != player.number]
    if len(possibles) == 1:# and not (possibles[0], possibles[0]):
        print("possible left diagonal is {}".format(possibles))
        return (possibles[0], possibles[0])
    possibles = [x for x, cell in enumerate(board[::-1].diagonal()) if cell != player.number]
    if len(possibles) == 1:# and not ((len(board)-(possibles[0]+1)), possibles[0]):
        print("possible diagonal is {}".format(possibles))
        return ((len(board)-(possibles[0]+1)), possibles[0])

def fork(board, player):
    """
    Returns a square that will create a fork (row of two + column of two,
    or (row or column of two) + diagonal of two).  The two do not need to be
    continous (!).
    """
    #for i, row in enumerate(board):
    #    occupied = [j for j, cell in enumerate(row) if (
    #                    cell != player.number and cell != 0)]
    #    if not occupied:
