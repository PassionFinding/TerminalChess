from Piece import Piece
from Piece import a_h
class Pawn(Piece):
    def __init__(self, color, notation, position, moved, passantable, current_column):
        super().__init__(color, notation, position, moved)
        self.passantable = passantable
        self.current_column = self.position[0]
    def legal(self, move):
        square = move[-2] + str(int(move[-1]) - 1)
        black_front = [int(self.position[-1])-2, a_h.index(self.position[-2])]
        black_double_front = [int(self.position[-1])-3, a_h.index(self.position[-2])]
        black_right = [int(self.position[-1])-2, a_h.index(self.position[-2]) - 1]
        black_left = [int(self.position[-1])-2, a_h.index(self.position[-2]) + 1]

        white_front = [int(self.position[-1]), a_h.index(self.position[-2])]
        white_double_front = [int(self.position[-1])+1, a_h.index(self.position[-2])]
        white_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 1]
        white_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 1]

        moves = [white_front, white_double_front, white_right, white_left, black_front, black_double_front, black_right, black_left]
        def possible_moves():
            
        


        if self.color == True:
            if square == a_h[white_double_front[-1]] + str(white_double_front[-2]) and white_double_front[-2] in range(8):
                 if layout[white_double_front[-2]][white_double_front[-1]] == "⬚" and layout[white_front[-2]][white_front[-1]] == "⬚" and self.moved == False:
                    self.passantable = True
                    return True
                 else:
                    return False
            elif square == a_h[white_front[-1]] + str(white_front[-2]) and white_front[-2] in range(8):
                if layout[white_front[-2]][white_front[-1]] == "⬚":
                    self.passantable = False
                    return True
                else:
                    return False
            elif square == a_h[white_right[-1]] + str(white_right[-2]) and white_right[-2] in range(8) and white_right[-1] in range(8):
                if layout[white_right[-2]][white_right[-1]] in Piece.black_notation:
                    self.passantable = False
                    return True
                else:
                    return False
            elif square == a_h[white_left[-1]] + str(white_left[-2]) and white_left[-2] in range(8) and white_right[-1] in range(8):
                if layout[white_left[-2]][white_left[-1]] in Piece.black_notation:
                    self.passantable = False
                    return True
                else:
                    return False
            else:
                return False
        else:
            if square == a_h[black_double_front[-1]] + str(black_double_front[-2]) and black_double_front[-2] in range(8):
                if layout[black_double_front[-2]][black_double_front[-1]] == "⬚" and layout[black_front[-2]][black_front[-1]] == "⬚" and self.moved == False:
                    self.passantable = True
                    return True
                else:
                    return False
            elif square == a_h[black_front[-1]] + str(black_front[-2]) and black_front[-2] in range(8):
                if layout[black_front[-2]][black_front[-1]] == "⬚":
                    self.passantable == False
                    return True
                else:
                    return False
            elif square == a_h[black_right[-1]] + str(black_right[-2]) and black_right[-1] in range(8) and black_right[-2] in range(8):
                if layout[black_right[-2]][black_right[-1]] in Piece.white_notation:
                    self.passantable = False
                    return True
                else:
                    return False
            elif square == a_h[black_left[-1]] + str(black_left[-2]) and black_left[-2] in range(8) and black_left[-1] in range(8):
                if layout[black_left[-2]][black_left[-1]] in Piece.white_notation:
                    self.passantable = False
                    return True
                else:
                    return False
    def plegal(self, move):
        if self.legal(move) == True:
            self.piece_move(move)
        else:
            print("Bro you can't do that")