from Piece import Piece
class King(Piece):
    def __init__(self, color, notation, position, moved):
        super().__init__(color, notation, position, moved)
    
    def legal(self, move):
        alo = move[-2] + str(int(move[-1]) - 1)
        front = [int(self.position[-1]), Piece.a_h.index(self.position[-2])]
        back = [int(self.position[-1]) - 2, Piece.a_h.index(self.position[-2])]
        left = [int(self.position[-1]) - 1, Piece.a_h.index(self.position[-2]) - 1]
        right = [int(self.position[-1]) - 1, Piece.a_h.index(self.position[-2]) + 1]
        front_left = [int(self.position[-1]), Piece.a_h.index(self.position[-2]) - 1]
        front_right = [int(self.position[-1]), Piece.a_h.index(self.position[-2]) + 1]
        back_left = [int(self.position[-1]) - 2, Piece.a_h.index(self.position[-2]) - 1]
        back_right = [int(self.position[-1]) - 2, Piece.a_h.index(self.position[-2]) + 1]
        possible_moves = [front, back, left, right, front_left, front_right, back_left, back_right]

        for possible in possible_moves:
            if alo == Piece.a_h[possible[1]] + str(possible[0]) and (Piece.layout[possible[0]][possible[1]] == "☐" or (Piece.layout[possible[0]][possible[1]] in 
            Piece.black_notation and self.color == True) or (Piece.layout[possible[0]][possible[1]] in Piece.white_notation and self.color == False)):
                return True
                break
            else:
                continue
    
    def klegal (self, move):
        if self.legal(move) == True:
            self.piece_move(move)
        else:
            print("nah")