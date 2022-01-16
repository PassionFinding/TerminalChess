from string import ascii_lowercase as wordbabies
from Piece import Pawn
from Piece import King
from Piece import Knight
from Piece import Bishop
from Piece import Rook
from Piece import Queen
from Piece import printboard
from Piece import reverseboard
from Piece import move
layout = [["⬚" for i in range(8)] for i in range(8)]
a_h = list(wordbabies[:8])
white_notation = ["🆁", "🅱", "🅽", "🆀", "🅺", "🅿"]
black_notation = ["🅁", "🄱", "🄽", "🅀", "🄺", "🄿"]

white_a_pawn = Pawn(True, "🅿", "a2", False, False, "a")
white_b_pawn = Pawn(True, "🅿", "b2", False, False, "b")
white_c_pawn = Pawn(True, "🅿", "c2", False, False, "c")
white_d_pawn = Pawn(True, "🅿", "d2", False, False, "d")
white_e_pawn = Pawn(True, "🅿", "e2", False, False, "e")
white_f_pawn = Pawn(True, "🅿", "f2", False, False, "f")
white_g_pawn = Pawn(True, "🅿", "g2", False, False, "g")
white_h_pawn = Pawn(True, "🅿", "h2", False, False, "h")
white_left_rook = Rook(True, "🆁", "a1", False)
white_right_rook = Rook(True, "🆁", "h1", False)
white_left_knight = Knight(True, "🅽", "b1", False)
white_right_knight = Knight(True, "🅽", "g1", False)
white_left_bishop = Bishop(True, "🅱", "c1", False)
white_right_bishop = Bishop(True, "🅱", "f1", False)
white_queen = Queen(True, "🆀", "d1", False)
white_king = King(True, "🅺", "e1", False)
white_pieces = [white_a_pawn, white_b_pawn, white_c_pawn, white_d_pawn, white_e_pawn, white_f_pawn, white_g_pawn, white_h_pawn, white_left_rook,
white_right_rook, white_left_knight, white_right_knight, white_left_bishop, white_right_bishop, white_queen, white_king]
white_pawns = [white_a_pawn, white_b_pawn, white_c_pawn, white_d_pawn, white_e_pawn, white_f_pawn, white_g_pawn, white_h_pawn]

black_a_pawn = Pawn(False, "🄿", "a7", False, False, "a")
black_b_pawn = Pawn(False, "🄿", "b7", False, False, "b")
black_c_pawn = Pawn(False, "🄿", "c7", False, False, "c")
black_d_pawn = Pawn(False, "🄿", "d7", False, False, "d")
black_e_pawn = Pawn(False, "🄿", "e7", False, False, "e")
black_f_pawn = Pawn(False, "🄿", "f7", False, False, "f")
black_g_pawn = Pawn(False, "🄿", "g7", False, False, "g")
black_h_pawn = Pawn(False, "🄿", "h7", False, False, "h")
black_left_rook = Rook(False, "🅁", "h8", False)
black_right_rook = Rook(False, "🅁", "a8", False)
black_left_knight = Knight(False, "🄽", "g8", False)
black_right_knight = Knight(False, "🄽", "b8", False)
black_left_bishop = Bishop(False, "🄱", "f8", False)
black_right_bishop = Bishop(False, "🄱", "c8", False)
black_queen = Queen(False, "🅀", "d8", False)
black_king = King(False, "🄺", "e8", False)
black_pieces = [black_a_pawn, black_b_pawn, black_c_pawn, black_d_pawn, black_e_pawn, black_f_pawn, black_g_pawn, black_h_pawn, black_right_rook, black_left_rook,
black_right_knight, black_left_knight, black_right_bishop, black_left_bishop, black_queen, black_king]
black_pawns = [black_a_pawn, black_b_pawn, black_c_pawn, black_d_pawn, black_e_pawn, black_f_pawn, black_g_pawn, black_h_pawn]

def starting_board():
  for item in black_pieces:
    layout[int(item.position[-1]) - 1][a_h.index(item.position[-2])] = item.notation
  for item in white_pieces:
    layout[int(item.position[-1]) - 1][a_h.index(item.position[-2])] = item.notation

def move(p_move):
  square = p_move[-2]
  notation = p_move[0]
  clarification = p_move[1]
  if move == True:
    if notation in a_h:
      candidates = []
      for item in white_pawns:
        if item.legal(layout, move, black_pawns, white_pawns, black_pieces, white_pieces) == True and item.checker(layout, move, black_pieces, white_king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          candidates.append(item)
        else:
          continue
      if len(candidates) == 0:
        print("Invalid move.")
      elif len(candidates) == 1:
        candidates[0].plegal(layout, p_move, black_pieces, white_king, black_pawns, white_pawns, black_pieces, white_pieces)
        candidates[0].promotion(white_pieces, black_pieces, white_pawns, black_pawns, layout)
      else:
        for candidate in candidates:
          if candidate.current_column == notation:
            candidate.plegal(layout, p_move, black_pieces, white_king, black_pawns, white_pawns, black_pieces, white_pieces)
            candidate.promotion(white_pieces, black_pieces, white_pawns, black_pawns, layout)
            break
    elif notation:
      pass
      



                


# while True:
#     starting_board()
#     printboard()
#     p_move = input("Enter move: ")
