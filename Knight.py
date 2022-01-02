from Piece import Piece
from Piece import a_h
class Knight(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
  
  def legal(self, move):
      #will be done from the perspective of white
      square = move[-2:]
      upper_upper_left = [int(self.position[-1]) + 1, Piece.a_h.index(self.position[-2]) - 1]
      upper_upper_right = [int(self.position[-1]) + 1, Piece.a_h.index(self.position[-2]) + 1]
      upper_left = [int(self.position[-1]), Piece.a_h.index(self.position[-2]) - 2]
      upper_right = [int(self.position[-1]), Piece.a_h.index(self.position[-2]) + 2]
      lower_left = [int(self.position[-1]) - 2, Piece.a_h.index(self.position[-2]) - 2]
      lower_right = [int(self.position[-1]) - 2, Piece.a_h.index(self.position[-2]) + 2]
      lower_lower_left = [int(self.position[-1]) - 3, Piece.a_h.index(self.position[-2]) - 1]
      lower_lower_right = [int(self.position[-1]) - 3, Piece.a_h.index(self.position[-2]) + 1]

      if self.color == True:
        if (square == uul and (upper_upper_left ==  "⬚" or upper_upper_left in Piece.black_notation) and double_up < 8 and left >= 0) or (
        square == uur and (upper_upper_right == "⬚" or upper_upper_right in Piece.black_notation) and double_up < 8 and right < 8) or (
        square == ul and (upper_left == "⬚" or upper_left in Piece.black_notation) and double_left >= 0) or (
        square == ur and (upper_right == "⬚" or upper_right in Piece.black_notation) and double_right < 8) or (
        square == ll and (lower_left == "⬚" or lower_left in Piece.black_notation) and down >= 0 and double_left >= 0) or (
        square == lr and (lower_right == "⬚" or lower_right in Piece.black_notation) and down >= 0 and double_right > 8) or (
        square == lll and (lower_lower_left == "⬚" or lower_lower_left in Piece.black_notation) and double_down >= 0 and left >= 0) or (
        square == llr and (lower_lower_right == "⬚" or lower_lower_right in Piece.black_notation) and double_down >= 0 and right < 8):
            return True
        else:
            return False
      else:
        if (square == uul and (upper_upper_left ==  "⬚" or upper_upper_left in Piece.white_notation) and double_up < 8 and left >= 0) or (
        square == uur and (upper_upper_right == "⬚" or upper_upper_right in Piece.white_notation) and double_up < 8 and right < 8) or (
        square == ul and (upper_left == "⬚" or upper_left in Piece.white_notation) and double_left >= 0) or (
        square == ur and (upper_right == "⬚" or upper_right in Piece.white_notation) and double_right < 8) or (
        square == ll and (lower_left == "⬚" or lower_left in Piece.white_notation) and down >= 0 and double_left >= 0) or (
        square == lr and (lower_right == "⬚" or lower_right in Piece.white_notation) and down >= 0 and double_right > 8) or (
        square == lll and (lower_lower_left == "⬚" or lower_lower_left in Piece.white_notation) and double_down >= 0 and left >= 0) or (
        square == llr and (lower_lower_right == "⬚" or lower_lower_right in Piece.white_notation) and double_down >= 0 and right < 8):
            return True
        else:
            return False
  def nlegal(self, move):
    if self.legal(move) == True:
        self.piece_move(move)
    else:
        print("Bro you can't do that")


            

      