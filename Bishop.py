import Piece
class Bishop(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
  

#So every square on a bishop's diagonal adds or subtracts the same number from the bishop's coordinates
#It goes four directions, with 1 and -1, -1 and 1, 1 and 1, and -1 and -1. 
#you can perform those operations on the index numbers of the piece's positions and stop once a value is at zero, at 7, or the pair of number coordinates on the layout don't equal an empty space
  def legal(self, move):
    legal_list = []
    positive_diagonal = []
    negative_diagonal = []
    #So im planning to check for each diagonal that the bishop is on, the positive slope diagonal and the negative slope diagonal
    #The positive slope diagonal, in reference to the bishop's position, goes +1 +1 and -1 -1
    #The negative slop diagonal, in reference to the bishop's position, goes +1 -1 and -1 +1
    column_pos = Piece.a_h.index(self.position[-2])
    row_pos = int(self.position[-1]-1)
    while column_pos < 8 and row_pos < 8:
      column_pos += 1
      row_pos+= 1
      positive_diagonal.append(str(Piece.a_h[column_pos]) + str(row_pos))
    while column_pos >= 0 and row_pos >= 0:
      column_pos -= 1
      row_pos -= 1
      positive_diagonal.append(str(Piece.a_h[column_pos]) + str(row_pos))
    while column_pos >= 0 and row_pos < 8:
      column_pos -= 1
      row_pos += 1
      negative_diagonal.append(str(Piece.a_h[column_pos]) + str(row_pos))
    while column_pos < 8 and row_pos >= 0:
      column_pos += 1
      row_pos -= 1
      negative_diagonal.append(str(Piece.a_h[column_pos]) + str(row_pos))
    
    legal_pos = []
    test_pos = []
    for square in positive_diagonal:
      if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] == "X":
        legal_pos.append(square)
        test_pos.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
      else:
        if square[-2] + str(int(square[-1]) + 1) == self.position:
          test_pos.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
        else:
          if self.notation in test_pos:
            if self.color == True:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.white_notation:
                for item in legal_pos:
                  legal_list.append(item)
                break
              else:
                legal_pos.append(square)
                for item in legal_pos:
                  legal_list.append(item)
                break
            elif self.color == False:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.black_notation:
                for item in legal_pos:
                  legal_list.append(item)
                break
              else:
                legal_pos.append(square)
                for item in legal_pos:
                  legal_list.append(item)
                break
          else:
            legal_pos.clear()
            test_pos.clear()
            if self.color == True:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.white_notation:
                pass
              else:
                legal_list.append(square)
            else:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.black_notation:
                pass
              else:
                legal_list.append(square)
    legal_neg = []
    test_neg = []
    for square in negative_diagonal:
      if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] == "X":
        legal_neg.append(square)
        test_neg.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
      else:
        if square[-2] + str(int(square[-1]) + 1) == self.position:
          test_neg.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
        else:
          if self.notation in test_neg:
            if self.color == True:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.white_notation:
                for item in legal_neg:
                  legal_list.append(item)
                break
              else:
                legal_neg.append(square)
                for item in legal_neg:
                  legal_list.append(item)
                break
            elif self.color == False:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.black_notation:
                for item in legal_neg:
                  legal_list.append(item)
                break
              else:
                legal_neg.append(square)
                for item in legal_neg:
                  legal_list.append(item)
                break
          else:
            legal_neg.clear()
            test_neg.clear()
            if self.color == True:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.white_notation:
                pass
              else:
                legal_list.append(square)
            else:
              if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] in Piece.Piece.black_notation:
                pass
              else:
                legal_list.append(square)
                
    test_move = move[0] + str(int(move[-1]) - 1)
    if test_move in legal_list:
      return True
    else:
     return False
