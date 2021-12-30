from Piece import Piece
class Bishop(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
  
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
    if self.llegal(self.get_positive(), move) == True or self.llegal(self.get_negative(), move) == True:
      return True
    else:
      return False
  
  def blegal(self, move):
    if self.llegal(self.get_positive(), move) == True or self.llegal(self.get_negative(), move) == True:
      self.piece_move(move)
    else:
      print("Bro you can't do that")