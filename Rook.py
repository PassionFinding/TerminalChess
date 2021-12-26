import Piece
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
  
  def rlegal(self, move):
    if Rook.legal(Rook.get_column(), move) == True or Rook.legal(Rook.get_row(), move) == True:
      Rook.piece_move(move)