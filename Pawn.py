from Piece import Piece
class Pawn(Piece):
    def __init__(self, color, notation, position, moved):
        super().__init__(color, notation, position, moved)
    
    def legal(self, move):
        square = move[-2] + move[-1]
        black_front = Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2])]
        black_double_front = Piece.layout[int(self.position[-1])-3][Piece.a_h.index(self.position[-2])]
        black_right = Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) - 1]
        b_right = Piece.a_h.index(self.position[-2]) - 1
        black_left = Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) + 1]
        b_left = Piece.a_h.index(self.position[-2]) + 1

        white_front = Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])]
        white_double_front = Piece.layout[int(self.position[-1])+1][Piece.a_h.index(self.position[-2])]
        white_right = Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) + 1]
        w_right = Piece.a_h.index(self.position[-2]) + 1
        white_left = Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) - 1]
        w_left = Piece.a_h.index(self.position[-2]) - 1

        if self.color == True:
            if square == white_double_front and white_double_front == "X" and white_front == "X":
                if self.moved == False:
                    return True
            elif square == white_front and white_front == "X":
                return True
            elif (square == white_right and white_right in Piece.black_notation and w_right < 8) or (square == white_left and white_left in Piece.white_notation and w_left >= 0):
                return True
            