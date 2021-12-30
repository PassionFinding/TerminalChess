from Piece import Piece
class Rook(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
    
  def get_column(self):
    column = []
    for item in Piece.layout:
      if  int(self.position[-1]) - 1 == Piece.layout.index(item):
        for i in item:
          if item.index(i) == Piece.a_h.index(self.position[-2]): 
            column.append(str(Piece.a_h[Piece.a_h.index(item.index(i))]) + str(Piece.layout.index(item)))
  
  def get_row(self):
    row = []
    for item in Piece.layout:
      if  int(self.position[-1]) - 1 == Piece.layout.index(item):
        for i in item:
          row.append(str(Piece.a_h[Piece.a_h.index(item.index(i))]) + str(Piece.layout.index(item)))

  def legal(self, move):
    if self.llegal(self.get_column(), move) == True or self.llegal(self.get_row(), move) == True:
      return True
    else:
      return False
  
  def rlegal(self, move):
    if self.llegal(self.get_column(), move) == True or self.llegal(self.get_row(), move) == True:
      self.piece_move(move)
    else:
      print("Bro you can't do that")