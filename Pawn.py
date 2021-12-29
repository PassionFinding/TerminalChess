from Piece import Piece
class Pawn(Piece):
    def __init__(self, color, notation, position, moved, passantable):
        super().__init__(color, notation, position, moved)
        self.passantable = passantable
    def legal(self, move):
        square = move[-2:]
        black_front = Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2])]
        black_front_coordinates = self.position[-2] + str(int(self.position[-1])-1)
        black_double_front = Piece.layout[int(self.position[-1])-3][Piece.a_h.index(self.position[-2])]
        black_double_front_coordinates = self.position[-2] + str(int(self.position[-1])-2)
        black_right = Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) - 1]
        black_right_coordinates = Piece.a_h[Piece.a_h.index(self.position[-2]) - 1] + str(int(self.position[-1])-1)
        b_right = Piece.a_h.index(self.position[-2]) - 1
        black_left = Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) + 1]
        black_left_coordinates = Piece.a_h[Piece.a_h.index(self.position[-2]) + 1] + str(int(self.position[-1]) - 1)
        b_left = Piece.a_h.index(self.position[-2]) + 1

        white_front = Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])]
        white_front_coordinates = self.position[-2] + str(int(self.position[-1]) + 1)
        white_double_front = Piece.layout[int(self.position[-1])+1][Piece.a_h.index(self.position[-2])]
        white_double_front_coordinates = self.position[-2] + str(int(self.positioinp[-1]) + 2)
        white_right = Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) + 1]
        white_right_coordinates = Piece.a_h[Piece.a_h.index(self.position[-2]) + 1] + str(int(self.position[-1]) + 1)
        w_right = Piece.a_h.index(self.position[-2]) + 1
        white_left = Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) - 1]
        white_left_coordinates = Piece.a_h[Piece.a_h.index(self.position[-2]) - 1] + str(int(self.position[-2]) + 1)
        w_left = Piece.a_h.index(self.position[-2]) - 1

        if self.color == True:
            if square == white_double_front_coordinates and white_double_front == "☐" and white_front == "☐" and self.moved == False:
                self.passantable = True
                return True
            elif (
            square == white_front_coordinates and white_front == "☐") or (
            square == white_right_coordinates and white_right in Piece.black_notation and w_right < 8) or (
            square == white_left_coordinates and white_left in Piece.black_notation and w_left >= 0):
                self.passantable = False
                return True
            else:
                return False
        else:
            if square == black_double_front_coordinates and black_double_front == "☐" and black_front == "☐" and self.moved == False:
                self.passantable = True
                return True
            elif (
            square == black_front_coordinates and black_front == "☐") or (
            square == black_right_coordinates and black_right in Piece.white_notation and b_right < 8) or (
            square == black_left_coordinates and black_left in Piece.white_notation and b_left >= 0):
                self.passantable = False
                return True
            else:
                return False
    
    def plegal(self, move):
        if self.legal(move) == True:
            self.piece_move(move)
        else:
            print("Bro you can't do that")