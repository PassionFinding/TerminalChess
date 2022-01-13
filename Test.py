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
# wking = King(True, "🅺", "e5", False)
# rwrook = Rook(True, "🆁", "h1", False)
# lwrook = Rook(True, "🆁", "a1", False)
# bking = King(False, "🄺", "e8", False)
# rbrook = Rook(False, "🅁", "e7", True)
# lbrook = Rook(False, "🅁", "h8", False)
# layout[int(wking.position[-1])-1][a_h.index(wking.position[-2])] = wking.notation
# layout[int(rwrook.position[-1])-1][a_h.index(rwrook.position[-2])] = rwrook.notation
# layout[int(lwrook.position[-1])-1][a_h.index(lwrook.position[-2])] = lwrook.notation
# layout[int(bking.position[-1])-1][a_h.index(bking.position[-2])] = bking.notation
# layout[int(lbrook.position[-1])-1][a_h.index(lbrook.position[-2])] = lbrook.notation
# layout[int(rbrook.position[-1])-1][a_h.index(rbrook.position[-2])] = rbrook.notation
# black_pieces = []
# white_pieces = [wking, rwrook, lwrook]
# print(black_pieces)
# print(rbrook.legal(layout, wking.position))
# turn = True
# wking.castle(wking, rwrook, lwrook, bking, rbrook, lbrook, white_pieces, black_pieces, "O-O", turn)
# line 165, in castle
#TypeError: 'King' object is not subscriptable
# printboard()

# pawn1 = Pawn(True, "🅿", "g6", True, True, "c")
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
printboard()