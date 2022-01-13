from string import ascii_lowercase as wordbabies
from Chess import layout
import copy
a_h = list(wordbabies[:8])
from Piece import Piece
from Piece import Pawn
from Piece import King
from Piece import Knight
from Piece import Bishop
from Piece import Rook
from Piece import Queen
from Piece import printboard
wking = King(True, "🅺", "e1", False)
rwrook = Rook(True, "🆁", "h1", False)
lwrook = Rook(True, "🆁", "a1", False)
bking = King(False, "🄺", "e8", False)
# rbrook = Rook(False, "🅁", "a8", True)
# lbrook = Rook(False, "🅁", "e7", False)
layout[int(wking.position[-1])-1][a_h.index(wking.position[-2])] = wking.notation
layout[int(rwrook.position[-1])-1][a_h.index(rwrook.position[-2])] = rwrook.notation
layout[int(lwrook.position[-1])-1][a_h.index(lwrook.position[-2])] = lwrook.notation
layout[int(bking.position[-1])-1][a_h.index(bking.position[-2])] = bking.notation
# layout[int(lbrook.position[-1])-1][a_h.index(lbrook.position[-2])] = lbrook.notation
# layout[int(rbrook.position[-1])-1][a_h.index(rbrook.position[-2])] = rbrook.notation
pawn1 = Pawn(True, "🅿", "c1", True, True, "c")
layout[int(pawn1.position[-1])-1][a_h.index(pawn1.position[0])] = pawn1.notation
black_pieces = [bking]
white_pieces = [wking, rwrook, lwrook, pawn1]
# print(rbrook.legal(layout, wking.position))
turn = True
# wking.castle(layout, wking, rwrook, lwrook, bking, None, None, white_pieces, black_pieces, "O-O-O", turn, [], [])

# pawn1 = Pawn(True, "🅿", "c1", True, True, "c")
# pawn2 = Pawn(False, "🄿", "h4", True, True, "d")
# layout[int(pawn1.position[-1])-1][a_h.index(pawn1.position[0])] = pawn1.notation
# layout[int(pawn2.position[-1])-1][a_h.index(pawn2.position[0])] = pawn2.notation
# queen = Queen(False, "🅀", "h5", True)
# queen2 = Queen(False, "🅀", "a5", True)
# layout[int(queen.position[-1])-1][a_h.index(queen.position[0])] = queen.notation
# layout[int(queen2.position[-1])-1][a_h.index(queen2.position[0])] = queen2.notation
# rook = Rook(True, "🆁", "f5", True)
# layout[int(rook.position[-1])-1][a_h.index(rook.position[0])] = rook.notation
# black_pieces = [pawn2, queen, queen2]
# black_pawns = [pawn2]
# white_pawns = [pawn1]
# white_pieces = [pawn1, wking, rook]
# print(wking.checker(layout, "f6", black_pieces, wking, black_pawns, white_pawns, black_pieces, white_pieces))
# printboard()

class Nothing:
    def __init__(self, name):
        self.name = name
class MoreNothing:
    pass
# class Something:
#     def change(self, list):
#         list.remove(self)
#         self = Nothing()
#         list.append(self)
# thing = Something()
# stuff = [thing]
# print(type(thing))
# # thing.change(stuff)
# print(type(stuff[0]))
# print(stuff)

counter = 1
suh = Nothing('bob')
list = []
name = suh.name + str(counter)
def f(counter):
    counter += 1

name = MoreNothing()
list.append(name)
f(counter)
name = MoreNothing()
list.append(name)
print(list)
print(name.name)
#THIS WORKS
