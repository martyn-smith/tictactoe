"""
Plays tic-tac-toe.  This file runs the main loop, and also contains
console UI commands (default)
"""
from time import sleep
from board import Board
from player import Player
from messages import *

#NUM_PLAYERS=2

def play_tictactoe(ui="console"):
    board = Board((3,3), dtype=int)
    #okay, so this is a hack.
    #numpy.ndarray is completely weird and normal __init__ methods don't work.
    #so initialise with random crap, then fill with zeros
    board.fill(0)
    player1 = Player(1, "human")
    player2 = Player(2,"cpu")
    players = [player1, player2]
    i=1
    while True:
        #print(board.__class__)
        board.draw()
        i += 1
        i = i % 2
        while True:
            if (players[i].move(board, player1)):
                break
        if (board.victory(players[i].number)):
            board.draw()
            print(victory_message.format(players[i].number))
            break
        if board.tie():
            board.draw()
            print(tie_message)
            break

if __name__ == "__main__":
    play_tictactoe()
