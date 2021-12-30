from Piece import Piece
class Queen(Piece):
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
  
  def get_positive(self):
    positive_diagonal = []
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
    return positive_diagonal

  def get_negative(self):
    negative_diagonal = []
    column_pos = Piece.a_h.index(self.position[-2])
    row_pos = int(self.position[-1]-1)
    while column_pos >= 0 and row_pos < 8:
      column_pos -= 1
      row_pos += 1
      negative_diagonal.append(str(Piece.a_h[column_pos]) + str(row_pos))
    while column_pos < 8 and row_pos >= 0:
      column_pos += 1
      row_pos -= 1
      negative_diagonal.append(str(Piece.a_h[column_pos]) + str(row_pos))
    return negative_diagonal
  
  def legal(self, move):
    if self.llegal(self.get_column(), move) == True or self.llegal(self.get_row(), move) == True or self.llegal(self.get_positive(), move) == True or self.llegal(self.get_negative(), move) == True:
      return True
    else:
      return False

  def qlegal(self, move):
      if self.llegal(self.get_column(), move) == True or self.llegal(self.get_row(), move) == True or self.llegal(self.get_positive(), move) == True or self.llegal(self.get_negative(), move) == True:
          self.piece_move(move)
      else:
          print("Bro you can't do that")
