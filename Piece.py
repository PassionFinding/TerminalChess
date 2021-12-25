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
    

  def legal(self, list_of_moves, move): 
    legal_list = [] 
    test_list = [] 
    for square in list_of_moves: 
      if layout[int(square[-1])][a_h.index(square[-2])] == "X": 
        legal_list.append(square) 
        test_list.append(layout[int(square[-1])][a_h.index(square[-2])]) 
      else:
        if square[-2] + str(int(square[-1]) + 1) == self.position:
          test_list.append(layout[int(square[-1])][a_h.index(square[-2])])
        else:
          if self.notation in test_list:
            if self.color == True:
              if layout[int(square[-1])][a_h.index(square[-2])] in Piece.white_notation:
                break
              else:
                legal_list.append(square)
                break
            elif self.color == False:
              if layout[int(square[-1])][a_h.index(square[-2])] in Piece.black_notation:
                break
              else:
                legal_list.append(square)
                break
          else:
            legal_list.clear()
            test_list.clear()
            if self.color == True:
              if layout[int(square[-1])][a_h.index(square[-2])] in Piece.white_notation:
                pass
              else:
                legal_list.append(square)
            else:
              if layout[int(square[-1])][a_h.index(square[-2])] in Piece.black_notation:
                pass
              else:
                legal_list.append(square)

    test_move = move[0] + str(int(move[-1]) - 1)
    if test_move in legal_list:
      return True
    else:
      return False

  def piece_move(self, p_move):
  #player input will be set to p_move
    layout[int(self.position[-1]) - 1][a_h.index(self.position[-2])] = "X"
    layout[int(p_move[-1]) - 1][a_h.index(p_move[-2])] = self.notation
    self.position = str(p_move[-2]) + str(p_move[-1])




            
                
            
                
                    