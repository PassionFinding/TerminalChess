from string import ascii_lowercase as wordbabies
from Piece import Piece
from Pawn import Pawn
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight

layout = [["X" for i in range(8)] for i in range(8)]
a_h = list(wordbabies[:8])
white_notation = ["R", "B", "N", "Q", "K", "P"]
black_notation = ["r", "b", "n", "q", "k", "p"]

#Make a list of each sides pieces. When taken, list.pop(piece)
white_a_pawn = Pawn(True, "P", "a2", False)
white_b_pawn = Pawn(True, "P", "b2", False)
white_c_pawn = Pawn(True, "P", "c2", False)
white_d_pawn = Pawn(True, "P", "d2", False)
white_e_pawn = Pawn(True, "P", "e2", False)
white_f_pawn = Pawn(True, "P", "f2", False)
white_g_pawn = Pawn(True, "P", "g2", False)
white_h_pawn = Pawn(True, "P", "h2", False)
white_left_rook = Rook(True, "R", "a1", False)
white_right_rook = Rook(True, "R", "h1", False)
white_left_knight = Knight(True, "N", "b1", False)
white_right_knight = Knight(True, "N", "g2", False)


def printboard():
    for thing in layout:
        print(" ".join(thing))

def move():
    player_move = input("Enter move. ")


# while True:
#     player_move = input("Enter move. ")

#     player_move = list(player_move)

#     layout[int(player_move[1])-1][a_h.index(player_move[0])] = "p"

#     printboard()