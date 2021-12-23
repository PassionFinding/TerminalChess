import Piece
#Needs a function that disallows the rook from capturing its own piece.
#A possible solution could be to check if the notation of the piece is in a certain set of characters
#So for example, you can make black lowercase and white uppercase. And you can see if the notation on that square is lowercase. If it is, and the rook is black, it won't be allowed to capture. Otherwise, it #will.
#"R" check needs an addition that disallows the rook from moving to its own place. legal column/row appends the rook's position, making it a legal move.
class Rook(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
    
  def legal(self, move):
    legal_list = []

    column = []

    row = []

    for item in Piece.layout:
      if  int(self.position[-1]) - 1 == Piece.layout.index(item):
        for i in item:

          row.append(str(Piece.a_h[Piece.a_h.index(item.index(i))]) + str(Piece.layout.index(item)))
        for i in item:
          if item.index(i) == Piece.a_h.index(self.position[-2]): 
            column.append(str(Piece.a_h[Piece.a_h.index(item.index(i))]) + str(Piece.layout.index(item)))

    legal_column = []
    test_column = []

    for square in column:
      if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] == "X":
        legal_column.append(square)
        test_column.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])

      elif Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] == "R":
          if square[-2] + str(int(square[-1]) + 1) == self.position:
            legal_column.append(square)
            test_column.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
          
          else:
            if "R" in test_column:
              legal_column.append(square)
              for item in legal_column:
                legal_list.append(item)
              break

            else:
              legal_column.clear()
              test_column.clear()
              legal_column.append(square)
              test_column.append(Piece.Piece.layout[int(square[-1])][Piece.Piece.a_h.index(square[-2])])

      else:


        if "R" in test_column:
          legal_column.append(square)
          for item in legal_column:
            legal_list.append(item)
          break

        else:
          legal_column.clear()
          test_column.clear()
          legal_column.append(square)
          test_column.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])

    legal_row = []
    test_row = []

    for square in row:

      if Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] == "X":
        legal_row.append(square)
        test_row.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])

      elif Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])] == "R":
        if square[-2] + str(int(square[-1]) + 1) == self.position:
            legal_row.append(square)
            test_row.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
          
        else:
          if "R" in test_row:
              legal_row.append(square)
              for item in legal_row:
                legal_list.append(item)
              break

          else:
              legal_row.clear()
              test_row.clear()
              legal_row.append(square)
              test_row.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])



      else:
        if "R" in test_row:
          legal_row.append(square)
          for item in legal_row:
            legal_list.append(item)
          break

        else:
          legal_row.clear()
          test_column.clear()
          legal_row.append(square)
          test_row.append(Piece.layout[int(square[-1])][Piece.a_h.index(square[-2])])
    

    test_move = move[0] + str(int(move[-1]) - 1)
    if test_move in legal_list:
      return True
    else:
     return False
