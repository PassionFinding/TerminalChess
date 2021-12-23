from string import ascii_uppercase as wordbabies


#Dictionary does not work due to complications with printing out the board.

layout = [["X" for i in range(8)] for i in range(8)]



a_h = list(wordbabies[:8])

class Piece:
    def __init__(self, notation, color, position, oldposition, movedyet):
        self.notation = notation
        self.color = color
        self.position = position
        self.oldposition = oldposition
        self.movedyet = movedyet

#For pawn moves, when removing the old position, maybe check
#One or two spaces back to see if a pawn is back there
#Or just make a new class with new parameters

white_apawn = Piece("p", True, layout[1][0], layout[1][0], False)
layout[1][0] = white_apawn.notation

white_bpawn = Piece("p", True, layout[1][1], layout[1][1], False)
layout[1][1] = white_apawn.notation

white_cpawn = Piece("p", True, layout[1][2], layout[1][2], False)
layout[1][2] = white_cpawn.notation

white_dpawn = Piece("p", True, layout[1][3], layout[1][3], False)
layout[1][3] = white_dpawn.notation

white_epawn = Piece("p", True, layout[1][4], layout[1][4], False)
layout[1][4] = white_epawn.notation

white_fpawn = Piece("p", True, layout[1][5], layout[1][5], False)
layout[1][5] = white_fpawn.notation

white_gpawn = Piece("p", True, layout[1][6], layout[1][6], False)
layout[1][6] = white_gpawn.notation

white_hpawn = Piece("p", True, layout[1][7], layout[1][7], False)
layout[1][7] = white_hpawn.notation

black_apawn = Piece("p", False, layout[6][0], layout[6][0], False)
layout[6][0] = black_apawn.notation

black_bpawn = Piece("p", False, layout[6][1], layout[6][1], False)
layout[6][1] = black_bpawn.notation

black_cpawn = Piece("p", False, layout[6][2], layout[6][2], False)
layout[6][2] = black_cpawn.notation

black_dpawn = Piece("p", False, layout[6][3], layout[6][3], False)
layout[6][3] = black_dpawn.notation

black_epawn = Piece("p", False, layout[6][4], layout[6][4], False)
layout[6][4] = black_epawn.notation

black_fpawn = Piece("p", False, layout[6][5], layout[6][5], False)
layout[6][5] = black_fpawn.notation

black_gpawn = Piece("p", False, layout[6][6], layout[6][6], False)
layout[6][6] = black_gpawn.notation

black_hpawn = Piece("p", False, layout[6][7], layout[6][7], False)
layout[6][7] = black_hpawn.notation

FirstWhiteRook = Piece("R", True, layout[0][0], layout[0][0], False)
layout[0][0] = FirstWhiteRook.notation

SecondWhiteRook = Piece("R", True, layout[0][7], layout[0][7], False)
layout[0][7] = SecondWhiteRook.notation

FirstBlackRook = Piece("R", False, layout[7][0], layout[7][0], False)
layout[7][0] = FirstBlackRook.notation

SecondBlackRook = Piece("R", False, layout[7][7], layout[7][7], False)
layout[7][7] = SecondBlackRook.notation

FirstWhiteKnight = Piece("N", True, layout[0][1], layout[0][1], False)
layout[0][1] = FirstWhiteKnight.notation

SecondWhiteKnight = Piece("N", True, layout[0][6], layout[0][6], False)
layout[0][6] = SecondWhiteKnight.notation

FirstBlackKnight = Piece("N", False, layout[7][1], layout[0][6], False)
layout[7][1] = FirstBlackKnight.notation

SecondBlackKnight = Piece("N", False, layout[7][6], layout[0][6], False)
layout[7][6] = SecondBlackKnight.notation

FirstWhiteBishop = Piece("B", True, layout[0][2], layout[0][2], False)
layout[0][2] = FirstWhiteBishop.notation

SecondWhiteBishop = Piece("B", True, layout[0][5], layout[0][5], False)
layout[0][5] = SecondWhiteBishop.notation

FirstBlackBishop = Piece("B", False, layout[7][2], layout[7][2], False)
layout[7][2] = FirstBlackBishop.notation

SecondBlackBishop = Piece("B", False, layout[7][5], layout[7][5], False)
layout[7][5] = SecondBlackBishop.notation

WhiteKing = Piece("K", True, layout[0][4], layout[0][4], False)
layout[0][4] = WhiteKing.notation

BlackKing = Piece("K", False, layout[7][4], layout[7][4], False)
layout[7][4] = BlackKing.notation

WhiteQueen = Piece("Q", True, layout[0][3], layout[0][3], False)
layout[0][3] = WhiteQueen.notation

BlackQueen = Piece("Q", False, layout[7][3], layout[7][3], False)
layout[7][3] = BlackQueen.notation

def printboard():
    for thing in layout:
        print(" ".join(thing))

def move():
    player_move = input("Enter move. ")

printboard()


# while True:
#     player_move = input("Enter move. ")

#     player_move = list(player_move)

#     layout[int(player_move[1])-1][a_h.index(player_move[0])] = "p"

#     printboard()