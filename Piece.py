#What does a piece in Chess have?
#1. A color
#2. A set of moves
#3. A notation symbol
#4. A position
#5. A starting position
#6. A legal move checker
#   a. To see if the King will be in check
#   b. To see if the piece is even allowed on that square
layout = [["X" for i in range(8)] for i in range(8)]
from string import ascii_uppercase as wordbabies
a_h = list(wordbabies[:8])

class Piece:
    white_notation = ["R", "B", "N", "Q", "K", "P"]
    black_notation = ["r", "b", "n", "q", "k", "p"]
    def __init__(self, color, notation, position, moved):
        self.color = color
        self.notation = notation
        self.position = position
        self.moved = moved

    def piece_move(self, p_move):
    #player input will be set to p_move
        layout[int(self.position[-1]) - 1][a_h.index(self.position[-2])] = "X"
        layout[int(p_move[-1]) - 1][a_h.index(p_move[-2])] = self.notation
        self.position = str(p_move[-2]) + str(p_move[-1])




            
                
            
                
                    