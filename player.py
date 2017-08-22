"""
class to hold the player and A.I.
"""
from time import sleep
from random import randint
import hints

#@validate_pos
def win(player, board, opponent):
    pos=hints.near_victory(board, player.number)
    if pos: #will return winning co-ords
        print("I can win from here!")
        return board.do_move(pos, player)

def block(player, board, opponent):
    pos = hints.near_victory(board, opponent.number)
    if pos:
        print("I've got to stop you winning.")
        return board.do_move(pos, player)

def fork(player, board, opponent):
    pass

def block_fork(player, board, opponent):
    pass

def center(player, board, opponent):
    if not(board.center_value):
        print("the centre is free")
        pos=board.center_pos
        return board.do_move(pos, player)

def oppose_corner(player, board, opponent):
    print("I'm playing in an opposite corner")
    for x, corner in enumerate(board.corners):
        if corner==opponent.number:
            pos=board.opposite_corner_locations(x)
            return board.do_move(pos, player)

def random_corner(player, board, opponent):
    print("I'm playing in an random corner")
    for x, corner in enumerate(board.corners):
        if not(corner):
            pos=board.opposite_corner_locations(x)
            return board.do_move(pos, player)

def random_pos(player, board, opponent):
    print("eh, I'm just gonna choose at random.")
    while True:
        pos=(randint(3), randint(3))
        if not board[pos]:
            return board.do_move(pos, player)

class Player:
    def __init__(self, number, player_type):
        self.number = number
        self.is_cpu = (True if player_type == "cpu" else False)
        #self.name = ""
        #self.options = []

    def move(self, board, opponent):
        pos=None
        if not self.is_cpu:
            pos=tuple(map(int,input("your move...\n").split(','))) #expecting a vector (y,x)
            if not(board[pos]):
                try:
                    board[pos]=self.number
                    return True
                except IndexError:
                    print("play in the board, ejit.")
            else:
                print("oops, that one is taken.  Try again.")
        #    except OccupiedError:
        #        pos=tuple(map(int,input("seat's taken.  Try again...\n").split(',')))
        else:
            """
            rules for moving:
                1. WIN! if you have two in a row, column or diag, place the third.
                2. BLOCK! if the opponent is about to win, block.
                3. FORK! create two non-blocked lines of two.
                4. BLOCK FORK! block one
                5. CENTER! place a piece in the centre.
                6. OPPOSITE CORNER! find a corner the opponent is in, play opposite.
                7. EMPTY CORNER! pick a random corner and occupy i.t
                7. EMPTY SIDE! pick a random side and occupy it.
            """
            print("hmmm... let me think.")
            sleep(1.0)
            for option in [win, block, fork, block_fork, center, oppose_corner,
                            random_corner, random_pos]:
                if (option(self, board, opponent)):
                    return True
