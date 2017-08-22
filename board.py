"""
class to handle the board.
"""
import numpy as np
from messages import board_image, player_symbols
SIZE=3

class Board(np.ndarray):

    def victory(self, player_num):
        #check for rows, columns or diagonals
        if any(all(cell == player_num for cell in row) for row in self):
            return True
        elif any(all(cell == player_num for cell in col) for col in self.transpose()):
            return True
        elif (all(cell == player_num for cell in self.diagonal()) or
                all(cell == player_num for cell in self[::-1].diagonal())):
            return True
        else:
            return False

    def tie(self):
        if all(all(cell for cell in row) for row in self):
            return True
        else:
            return False

    def do_move(self, pos, player):
        #print("trying to place {}".format(pos))
        if not(self[pos]):
            self[pos]=player.number
            return True
        else:
            return False

    def draw(self, ui="console"):
        if (ui=="console"):
            print(board_image.format(*[player_symbols[i] for i in self.flatten()]))

    @property
    def center_value(self):
        return self[(len(self)//2, len(self)//2)]

    @property
    def center_pos(self):
        return (len(self)//2, len(self)//2)

    @property
    def corners(self):
        return (self[(0,0)], self[(len(self)-1,0)],
                self[(0,len(self)-1)], self[(len(self)-1, len(self)-1)])

    def opposite_corner_locations(self, x):
        return {
        3:(len(self)-1, len(self)-1),
        2:(len(self-1),0),
        1:(0,len(self)-1),
        0:(len(self)-1, len(self)-1)
        }[x]

    def corner_locations(self, x):
        return {
            0:(0,0),
            1:(len(self-1),0),
            2:(0,len(self)-1),
            3:(len(self)-1, len(self)-1)
        }[x]
