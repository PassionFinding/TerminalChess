from Piece import Piece
class Rook(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
    
  def get_column(self, board):
    column = []
    for item in board:
      if  int(self.position[-1]) - 1 == Piece.layout.index(item):
        for i in item:
          if item.index(i) == Piece.a_h.index(self.position[-2]): 
            column.append(str(Piece.a_h[Piece.a_h.index(item.index(i))]) + str(Piece.layout.index(item)))
  
  def get_row(self, board):
    row = []
    for item in board:
      if  int(self.position[-1]) - 1 == Piece.layout.index(item):
        for i in item:
          row.append(str(Piece.a_h[Piece.a_h.index(item.index(i))]) + str(Piece.layout.index(item)))

  def legal(self, board, move):
    if self.llegal(self.get_column(), board, move) == True or self.llegal(self.get_row(), board, move) == True:
      return True
    else:
      return False
  
  def rlegal(self, board, move):
    if self.llegal(self.get_column(), board, move) == True or self.llegal(self.get_row(), board, move) == True:
      self.piece_move(move)
    else:
      print("Bro you can't do that")