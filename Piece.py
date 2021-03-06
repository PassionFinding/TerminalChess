from re import T
from string import ascii_lowercase as wordbabies
import copy
from tokenize import Number
a_h = list(wordbabies[:8])
class Piece: 
  white_notation = ["🆁", "🅱", "🅽", "🆀", "🅺", "🅿"]
  black_notation = ["🅁", "🄱", "🄽", "🅀", "🄺", "🄿"]
  def __init__(self, color, notation, position, moved):
    self.color = color
    self.notation = notation
    self.position = position
    self.moved = moved

#Pawn has its own version of checker because it needs extra parameters for piece.legal
  def checker(self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
      test_board = copy.deepcopy(board)
      test_board[int(self.position[-1]) - 1][a_h.index(self.position[-2])] = "⬚"
      test_board[int(move[-1])-1][a_h.index(move[-2])] = self.notation
      if type(self) == King:
        orig_pos = []
        orig_pos.append(self.position)
        self.position = move
      for piece in list_of_pieces:
        if type(piece) == Pawn:
          if piece.legal(test_board, king.position, black_pawns, white_pawns, black_pieces, white_pieces) == True:
            if move == piece.position and ((type(self) == Pawn and self.legal(board, move, black_pawns, white_pawns, black_pieces, white_pieces) == True) or (type(self) != Pawn and self.legal(board, move) == True)):
              continue
            else: 
              if type(self) == King:
                self.position = orig_pos
              return True
          else:
            continue
        else:
          if piece.legal(test_board, king.position) == True:
            if move == piece.position and ((type(self) == Pawn and self.legal(board, move, black_pawns, white_pawns, black_pieces, white_pieces) == True) or (type(self) != Pawn and self.legal(board, move) == True)): 
              continue
            else:
              if type(self) == King:
                self.position = orig_pos
              return True
          else:
            continue
      if type(self) == King:
        self.position = orig_pos
      return False

  def llegal(self, list_of_moves, board, move): 
    legal_list = [] 
    test_list = [] 
    for square in list_of_moves:
      if board[int(square[-1]) - 1][a_h.index(square[-2])] == "⬚": 
        legal_list.append(square) 
        test_list.append(board[int(square[-1]) - 1][a_h.index(square[-2])]) 
      else:
        if square == self.position:
          test_list.append(board[int(square[-1]) - 1][a_h.index(square[-2])])
        else:
          if self.notation in test_list:
            if self.color == True:
              if board[int(square[-1])-1][a_h.index(square[-2])] in Piece.white_notation:
                break
              else:
                legal_list.append(square)
                break
            elif self.color == False:
              if board[int(square[-1])-1][a_h.index(square[-2])] in Piece.black_notation:
                break
              else:
                legal_list.append(square)
                break
          else:
            legal_list.clear()
            test_list.clear()
            if self.color == True:
              if board[int(square[-1])-1][a_h.index(square[-2])] in Piece.white_notation:
                continue
              else:
                legal_list.append(square)
            else:
              if board[int(square[-1])-1][a_h.index(square[-2])] in Piece.black_notation:
                continue
              else:
                legal_list.append(square)
    test_move = move[-2] + str(int(move[-1]))
    if test_move in legal_list:
      return True
    else:
      return False

  def piece_move(self, board, p_move, white_pawns, black_pawns):
  #player input will be set to p_move
    board[int(self.position[-1]) - 1][a_h.index(self.position[-2])] = "⬚"
    board[int(p_move[-1]) - 1][a_h.index(p_move[-2])] = self.notation
    self.position = str(p_move[-2]) + str(p_move[-1])    
    self.moved = True
    if self.color == True:
      move = False
      for pawn in black_pawns:
        pawn.passantable == False
    else:
      move = True
      for pawn in white_pawns:
        pawn.passantable == False

class Pawn(Piece):
    def __init__(self, color, notation, position, moved, passantable, current_column):
        super().__init__(color, notation, position, moved)
        self.passantable = passantable
        self.current_column = self.position[0]
        
    def return_moves(self):
      black_front = [int(self.position[-1])-2, a_h.index(self.position[-2])]
      black_double_front = [int(self.position[-1])-3, a_h.index(self.position[-2])]
      black_right = [int(self.position[-1])-2, a_h.index(self.position[-2]) - 1]
      black_left = [int(self.position[-1])-2, a_h.index(self.position[-2]) + 1]

      white_front = [int(self.position[-1]), a_h.index(self.position[-2])]
      white_double_front = [int(self.position[-1])+1, a_h.index(self.position[-2])]
      white_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 1]
      white_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 1]

      white_moves = [white_front, white_double_front, white_right, white_left]
      black_moves = [black_front, black_double_front, black_right, black_left]
      white_possibilities = []
      black_possibilities = []
      if self.color == True:
        for move in white_moves:
          if move[-2] in range(8) and move[-1] in range(8):
            official_notation = a_h[move[1]] + str(move[0] + 1)
            white_possibilities.append(official_notation)
          else:
            continue
        return white_possibilities
      else:
        for move in black_moves:
          if move[-2] in range(8) and move[-1] in range(8):
            official_notation = a_h[move[1]] + str(move[0] + 1)
            black_possibilities.append(official_notation)
          else:
            continue
        return black_possibilities
      


    def legal(self, board, move, black_pawns, white_pawns, black_pieces, white_pieces):
        square = [int(move[-1]) - 1, a_h.index(move[-2])]
        black_front = [int(self.position[-1])-2, a_h.index(self.position[-2])]
        black_double_front = [int(self.position[-1])-3, a_h.index(self.position[-2])]
        black_right = [int(self.position[-1])-2, a_h.index(self.position[-2]) - 1]
        black_left = [int(self.position[-1])-2, a_h.index(self.position[-2]) + 1]

        white_front = [int(self.position[-1]), a_h.index(self.position[-2])]
        white_double_front = [int(self.position[-1])+1, a_h.index(self.position[-2])]
        white_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 1]
        white_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 1]

        moves = [white_front, white_double_front, white_right, white_left, black_front, black_double_front, black_right, black_left]
        possibilities = []
        for move in moves:
          if move[-2] in range(8) and move[-1] in range(8):
            possibilities.append(move)
          else:
            continue
        if square in possibilities:
            if (self.color == True and square == white_double_front and self.moved == False and board[square[-2]][square[-1]] == "⬚" and board[white_front[-2]][white_front[-1]] == "⬚") or (
                self.color == False and square == black_double_front and self.moved == False and board[square[-2]][square[-2]] == "⬚" and board[black_front[-2]][black_front[-1]] == "⬚"
            ):
                self.passantable = True
                return True
            elif (self.color == True and square == white_front and board[square[-2]][square[-1]] == "⬚") or (self.color == False and square == black_front and board[square[-2]][square[-1]] == "⬚"):
                self.passantable = False
                return True
            elif (self.color == True and (square == white_right or square == white_left) and board[square[-2]][square[-1]] in self.black_notation)  or (
                self.color == False and (square == black_left or square == black_right) and board[square[-2]][square[-1]] in self.white_notation
            ):
                self.passantable = False
                return True
            elif ((square == white_right or square == white_left) or (square == black_right or square == black_left) and board[square[-2]][square[-1]] == "⬚"):
              if self.color == True:
                  if board[square[0]-1][square[1]] == "🄿": 
                        for pawn in black_pawns:
                              if pawn.position == a_h[square[1]] + str(square[0]) and pawn.passantable == True:
                                black_pieces.remove(pawn)
                                board[square[-1]-1][square[-2]] = "⬚"
                                return True
              else:
                if board[square[0]+1][square[1]] == "🅿":
                        for pawn in white_pawns:
                              if pawn.position == a_h[(square[1])] + str(square[0] + 2) and pawn.passantable == True:
                                    white_pieces.remove(pawn)
                                    board[square[-1]+1][square[-2]] = "⬚"
                                    return True
            else:
                return False
        else:
            return False
    def promotion(self, list_white, list_black, list_white_pawns, list_black_pawns, board):
      if self.position[-1] == "8":
        promote = input("Pawn promotion to? ")
        if promote == "Q" or promote == "q":
          if self.color == True:
            list_white.remove(self)
            list_white_pawns.remove(self)
            queen = Queen(True, "🆀", self.position, False)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🆀"
            list_white.append(queen)
          else:
            list_black.remove(self)
            list_black_pawns.remove(self)
            queen = Queen(False, "🅀", self.position, False)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🅀"
            list_black.append(queen)
        elif promote == "R" or promote == "r":
          if self.color == True:
            list_white.remove(self)
            list_white_pawns.remove(self)
            rook = Rook(True, "🆁", self.position, True)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🆁"
            list_white.append(rook)
          else:
            list_black.remove(self)
            list_black_pawns.remove(self)
            rook = Rook(False, "🅁", self.position, True)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🅁"
            list_black.append(rook)
        elif promote == "B" or promote == "b":
          if self.color == True:
            list_white.remove(self)
            list_white_pawns.remove(self)
            bishop = Bishop(True, "🅱", self.position, True)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🅱"
            list_white.append(bishop)
          else:
            list_black.remove(self)
            list_black_pawns.remove(self)
            bishop = Bishop(False, "🄱", self.position, True)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🄱"
            list_black.append(bishop)
        elif promote == "N" or promote == "n":
          if self.color == True:
            list_white.remove(self)
            list_white_pawns.remove(self)
            knight = Knight(True, "🅽", self.position, True)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🅽"
            list_white.append(knight)
          else:
            list_black.remove(self)
            list_black_pawns.remove(self)
            knight = Knight(False, "🄽", self.position, True)
            board[int(self.position[1])-1][a_h.index(self.position[0])] = "🄽"
            list_black.append(knight)
        else:
          print("Invalid")


    def plegal(self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
        if self.legal(board, move, black_pawns, white_pawns, black_pieces, white_pieces) == True and self.checker(board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          if board[int(move[-1]) - 1][a_h.index(move[-2])] != "⬚":
            for piece in list_of_pieces:
              if piece.position == move:
                list_of_pieces.remove(piece)
            self.piece_move(board, move, white_pawns, black_pawns)
            self.current_column = self.position[-2]
            self.promotion(white_pieces, black_pieces, white_pawns, black_pawns, board)
          else:
            self.piece_move(board, move, white_pawns, black_pawns)
            self.current_column = self.position[-2]
            self.promotion(white_pieces, black_pieces, white_pawns, black_pawns, board)

class King(Piece):
    def __init__(self, color, notation, position, moved):
        super().__init__(color, notation, position, moved)
    
    def return_moves(self):
        front = [int(self.position[-1]), a_h.index(self.position[-2])]
        back = [int(self.position[-1]) - 2, a_h.index(self.position[-2])]
        left = [int(self.position[-1]) - 1, a_h.index(self.position[-2]) - 1]
        right = [int(self.position[-1]) - 1, a_h.index(self.position[-2]) + 1]
        front_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 1]
        front_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 1]
        back_left = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) - 1]
        back_right = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) + 1]
        possible_moves = [front, back, left, right, front_left, front_right, back_left, back_right]
        only_moves = []
        for possible in possible_moves:
          if possible[-1] in range(8) and possible[-2] in range(8):
            official_notation = a_h[possible[1]] + str(possible[0] + 1)
            only_moves.append(official_notation)
          else:
            continue
        return only_moves

    def legal(self, board, move):
        alo = move[-2] + str(int(move[-1]) - 1)
        front = [int(self.position[-1]), a_h.index(self.position[-2])]
        back = [int(self.position[-1]) - 2, a_h.index(self.position[-2])]
        left = [int(self.position[-1]) - 1, a_h.index(self.position[-2]) - 1]
        right = [int(self.position[-1]) - 1, a_h.index(self.position[-2]) + 1]
        front_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 1]
        front_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 1]
        back_left = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) - 1]
        back_right = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) + 1]
        possible_moves = [front, back, left, right, front_left, front_right, back_left, back_right]

        for possible in possible_moves:
            if possible[-1] in range(8) and possible[-2] in range(8) and alo == a_h[possible[1]] + str(possible[0]):
                if (board[possible[0]][possible[1]] == "⬚" or (board[possible[0]][possible[1]] in 
            self.black_notation and self.color == True) or (board[possible[0]][possible[1]] in self.white_notation and self.color == False)):
                    return True
                    break
                else:
                    continue
            else:
                continue
        return False
    #stalemate function needed, checkmate function needs to be modified
    def in_check(self, board, black_pawns, white_pawns, black_pieces, white_pieces, opponent_pieces):
      for piece in opponent_pieces:
        if type(piece) == Pawn:
          if piece.legal(board, self.position, black_pawns, white_pawns, black_pieces, white_pieces) == True:
            return True
          else:
            continue
        else:
          if piece.legal(board, self.position):
            return True
          else:
            continue
      return False

    def stalemate(self, board, opponent_pieces, your_pieces, black_pawns, white_pawns, black_pieces, white_pieces):
      for piece in your_pieces:
        if type(piece) == Pawn:
          for move in piece.return_moves():
            if piece.legal(board, move, black_pawns, white_pawns, black_pieces, white_pieces) == True and piece.checker(board, move, opponent_pieces, self, black_pawns, white_pawns, black_pieces, white_pieces):
              return False
            else:
              continue
          continue
        elif type(piece) == King:
          for move in piece.return_moves():
            if piece.legal(board, move) and piece.checker(board, move, opponent_pieces, piece, black_pawns, white_pawns, black_pieces, white_pieces):
              return False
            else:
              continue
          continue
        elif type(piece) == Queen:
          for move in piece.get_everything():
            if piece.legal(board, move) and piece.checker(board, move, opponent_pieces, piece, black_pawns, white_pawns, black_pieces, white_pieces):
              return False
            else:
              continue
          continue
        elif type(piece) == Rook:
          for move in piece.get_everything():
            if piece.legal(board, move) and piece.checker(board, move, opponent_pieces, piece, black_pawns, white_pawns, black_pieces, white_pieces):
              return False
            else:
              continue
          continue
        elif type(piece) == Bishop:
          for move in piece.get_everything():
            if piece.legal(board, move) and piece.checker(board, move, opponent_pieces, piece, black_pawns, white_pawns, black_pieces, white_pieces):
              return False
            else:
              continue
          continue
        elif type(piece) == Knight:
          for move in piece.get_everything():
            if piece.legal(board, move) and piece.checker(board, move, opponent_pieces, piece, black_pawns, white_pawns, black_pieces, white_pieces):
              return False
            else:
              continue
          continue
        return True

    def game(self, board, opponent, king, black_pawns, white_pawns, black_pieces, white_pieces):
      front = [int(self.position[-1]), a_h.index(self.position[-2])]
      back = [int(self.position[-1]) - 2, a_h.index(self.position[-2])]
      left = [int(self.position[-1]) - 1, a_h.index(self.position[-2]) - 1]
      right = [int(self.position[-1]) - 1, a_h.index(self.position[-2]) + 1]
      front_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 1]
      front_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 1]
      back_left = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) - 1]
      back_right = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) + 1]
      possible_moves = [front, back, left, right, front_left, front_right, back_left, back_right]
      only_moves = []
      for move in possible_moves:
        if move[-1] in range(8) and move[-2] in range(8):
          move_nt = a_h[move[1]] + str(move[0] + 1)
          only_moves.append(move_nt)
        else:
          continue
      for move in only_moves: 
        if self.legal(board, move) == True and self.checker(board, move, opponent, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          return False
        else:
          continue
      if self.in_check(board, black_pawns, white_pawns, black_pieces, white_pieces, opponent) == True:
        return True
      else:
        return False

        
    def castle(self, board, white_king, white_right_rook, white_left_rook, black_king, black_right_rook, black_left_rook, list_of_white_pieces, list_of_black_pieces, move, turn, black_pawns, white_pawns):
      if (move == "O-O" or move == "o-o") and turn == True:
        if board[0][5] != "⬚" or board[0][6] != "⬚" or white_king.moved == True or white_right_rook.moved == True:
          return print("Can't castle!")
        else:
          for piece in list_of_black_pieces:
            if type(piece) == Pawn:
              if piece.legal(board, "e1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "f1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "g1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "h1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True:
                return print("Can't castle!")
              else:
                continue
            else:
              if piece.legal(board, "e1") == True or piece.legal(board, "f1") == True or piece.legal(board, "g1") == True or piece.legal(board, "h1") == True:
                return print("Can't castle!")
              else:
                continue
          white_king.piece_move(board, "g1")
          white_right_rook.piece_move(board, "f1")
      elif (move == "O-O" or move == "o-o") and turn == False:
        if board[7][5] != "⬚" or board[7][6] != "⬚" or black_king.moved == True or black_left_rook.moved == True:
          return print("Can't castle!")
        else:
          for piece in list_of_white_pieces:
            if type(piece) == Pawn:
              if piece.legal(board, "e8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "f8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "g8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "h8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True:
                return print("Can't castle!")
              else:
                continue
            else:

              if piece.legal(board, "e8") == True or piece.legal(board, "f8") == True or piece.legal(board, "g8") == True or piece.legal(board, "h8") == True:
                return print("Can't castle!")
              else:
                continue
          black_king.piece_move(board, "g8")
          black_left_rook.piece_move(board, "f8")
      elif (move == "O-O-O" or move == "o-o-o") and turn == True:
        if board[0][1] != "⬚" or board[0][2] != "⬚" or board[0][3] != "⬚" or white_king.moved == True or white_left_rook.moved == True:
          return print("Can't castle!")
        else:
          for piece in list_of_black_pieces:
            if type(piece) == Pawn:
              if piece.legal(board, "e1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "d1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "c1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "b1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "a1", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True:
                return print("Can't castle!")
              else:
                continue
            else:
              if piece.legal("e1") == True or piece.legal("d1") == True or piece.legal("c1") == True or piece.legal("b1") == True or piece.legal("a1") == True:
                return print("Can't castle!")
              else:
                continue
          white_king.piece_move(board, "c1")
          white_right_rook.piece_move(board, "d1")
      elif (move == "O-O-O" or move == "o-o-o") and turn == False:
        if board[7][1] != "⬚" or board[7][2] != "⬚" or board[7][3] != "⬚" or black_king.moved == True or black_left_rook.moved == True:
          return print("Can't castle!")
        else:
          for piece in list_of_white_pieces:
            if type(piece) == Pawn:
              if piece.legal(board, "e8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "d8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "c8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "b8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True or piece.legal(board, "a8", black_pawns, white_pawns, list_of_black_pieces, list_of_white_pieces) == True:
                return print("Can't castle!")
              else:
                continue
            else:
              if piece.legal("e8") == True or piece.legal("d8") == True or piece.legal("c8") == True or piece.legal("b8") == True or piece.legal("a8") == True:
                return print("Can't castle!")
              else:
                continue
          black_king.piece_move(board, "c8")
          black_right_rook.piece_move(board, "d8")
      else:
        print("Either you made a typo that began with an O, an invalid castling request format (only all uppercase or all lowercase), or you're trying to break the game.")
    
    def klegal (self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
        if self.legal(board, move) == True and self.checker(board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          if board[int(move[-1]) - 1][a_h.index(move[-2])] != "⬚":
            for piece in list_of_pieces:
              if piece.position == move:
                list_of_pieces.remove(piece)
            self.piece_move(board, move, white_pawns, black_pawns)
          else:
            self.piece_move(board, move, white_pawns, black_pawns)
        else:
            return False

class Knight(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)

  def get_everything(self):
      upper_upper_left = [int(self.position[-1]) + 1, a_h.index(self.position[-2]) - 1]
      upper_upper_right = [int(self.position[-1]) + 1, a_h.index(self.position[-2]) + 1]
      upper_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 2]
      upper_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 2]
      lower_left = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) - 2]
      lower_right = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) + 2]
      lower_lower_left = [int(self.position[-1]) - 3, a_h.index(self.position[-2]) - 1]
      lower_lower_right = [int(self.position[-1]) - 3, a_h.index(self.position[-2]) + 1]
      possible_moves = [upper_upper_left, upper_upper_right, upper_left, upper_right, lower_left, lower_right, lower_lower_left, lower_lower_right]
      only_moves = []
      for possible in possible_moves:
        if possible[-1] in range(8) and possible[-2] in range(8):
          official_notation = a_h[possible[1]] + str(possible[0] + 1)
          only_moves.append(official_notation)
        else:
          continue
      return only_moves
  
  def legal(self, board, move):
      #will be done from the perspective of white
      alo = move[-2] + str(int(move[-1]) - 1)
      upper_upper_left = [int(self.position[-1]) + 1, a_h.index(self.position[-2]) - 1]
      upper_upper_right = [int(self.position[-1]) + 1, a_h.index(self.position[-2]) + 1]
      upper_left = [int(self.position[-1]), a_h.index(self.position[-2]) - 2]
      upper_right = [int(self.position[-1]), a_h.index(self.position[-2]) + 2]
      lower_left = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) - 2]
      lower_right = [int(self.position[-1]) - 2, a_h.index(self.position[-2]) + 2]
      lower_lower_left = [int(self.position[-1]) - 3, a_h.index(self.position[-2]) - 1]
      lower_lower_right = [int(self.position[-1]) - 3, a_h.index(self.position[-2]) + 1]
      possible_moves = [upper_upper_left, upper_upper_right, upper_left, upper_right, lower_left, lower_right, lower_lower_left, lower_lower_right]

      for possible in possible_moves:
        if possible[-1] in range(8) and possible[-2] in range(8):
          if alo == a_h[possible[1]] + str(possible[0]):
            if (board[possible[0]][possible[1]] == "⬚" or (board[possible[0]][possible[1]] in 
            self.black_notation and self.color == True) or (board[possible[0]][possible[1]] in self.white_notation and self.color == False)):
              return True
              break
            else:
              continue
        else:
          continue


  def nlegal(self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
    if self.legal(board, move) == True and self.checker(board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          if board[int(move[-1]) - 1][a_h.index(move[-2])] != "⬚":
            for piece in list_of_pieces:
              if piece.position == move:
                list_of_pieces.remove(piece)
            self.piece_move(board, move, white_pawns, black_pawns)
          else:
            self.piece_move(board, move, white_pawns, black_pawns)
    else:
        return False

class Queen(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)

  def get_column(self):
    column = []
    for i in range(1, 9):
        square = a_h[a_h.index(self.position[-2])] + str(i)
        column.append(square)
    return column
  
  def get_row(self):
    row = []
    for letter in a_h:
        row.append(letter + self.position[-1])
    return row
  
  def get_positive(self):
    positive_diagonal = []
    column_pos = a_h.index(self.position[-2]) 
    row_pos = int(self.position[-1])
    while column_pos in range(7) and row_pos in range(8):
      column_pos += 1
      row_pos+= 1
    positive_diagonal.append(a_h[column_pos] + str(row_pos))
    while column_pos in range(1, 8) and row_pos in range(2, 9):
      column_pos -= 1
      row_pos -= 1
      positive_diagonal.append(a_h[column_pos] + str(row_pos))
    return positive_diagonal

  def get_negative(self):
    negative_diagonal = []
    column_pos = a_h.index(self.position[-2]) 
    row_pos = int(self.position[-1]) 
    while column_pos in range(7) and row_pos in range(2, 9):
      column_pos += 1
      row_pos -= 1
    negative_diagonal.append(a_h[column_pos] + str(row_pos))
    while column_pos in range(1, 8) and row_pos in range(8):
      column_pos -= 1
      row_pos += 1
      negative_diagonal.append(str(a_h[column_pos]) + str(row_pos))
    return negative_diagonal
  
  def get_everything(self):
    everything = []
    for item in self.get_negative():
      everything.append(item)
    for item in self.get_positive():
      everything.append(item)
    for item in self.get_row():
      everything.append(item)
    for item in self.get_column():
      everything.append(item)
    return everything

  def legal(self, board, move):
    if self.llegal(self.get_column(), board, move) == True or self.llegal(self.get_row(), board, move) == True or self.llegal(self.get_positive(), board, move) == True or self.llegal(self.get_negative(), board, move) == True:
      return True
    else:
      return False

  def qlegal(self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
      if (self.llegal(self.get_column(), board, move) == True or self.llegal(self.get_row(), board, move) == True or self.llegal(self.get_positive(), board, move) == True or self.llegal(self.get_negative(), board, move) == True) and self.checker(board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          if board[int(move[-1]) - 1][a_h.index(move[-2])] != "⬚":
            for piece in list_of_pieces:
              if piece.position == move:
                list_of_pieces.remove(piece)
            self.piece_move(board, move, white_pawns, black_pawns)
          else:
            self.piece_move(board, move, white_pawns, black_pawns)
      else:
          return False

class Bishop(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
  
  def get_positive(self):
    positive_diagonal = []
    column_pos = a_h.index(self.position[-2]) 
    row_pos = int(self.position[-1])
    while column_pos in range(7) and row_pos in range(8):
      column_pos += 1
      row_pos+= 1
    positive_diagonal.append(a_h[column_pos] + str(row_pos))
    while column_pos in range(1, 8) and row_pos in range(2, 9):
      column_pos -= 1
      row_pos -= 1
      positive_diagonal.append(a_h[column_pos] + str(row_pos))
    return positive_diagonal

  def get_negative(self):
    negative_diagonal = []
    column_pos = a_h.index(self.position[-2]) 
    row_pos = int(self.position[-1]) 
    while column_pos in range(7) and row_pos in range(2, 9):
      column_pos += 1
      row_pos -= 1
    negative_diagonal.append(a_h[column_pos] + str(row_pos))
    while column_pos in range(1, 8) and row_pos in range(8):
      column_pos -= 1
      row_pos += 1
      negative_diagonal.append(str(a_h[column_pos]) + str(row_pos))
    return negative_diagonal
  
  def get_everything(self):
    everything = []
    for item in self.get_positive():
      everything.append(item)
    for item in self.get_negative():
      everything.append(item)
    return everything
  
  def legal(self, board, move):
    if self.llegal(self.get_positive(), board, move) == True or self.llegal(self.get_negative(), board, move) == True:
      return True
    else:
      return False

  def blegal(self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
      if (self.llegal(self.get_positive(), board, move) == True or self.llegal(self.get_negative(), board, move) == True) and self.checker(board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          if board[int(move[-1]) - 1][a_h.index(move[-2])] != "⬚":
            for piece in list_of_pieces:
              if piece.position == move:
                list_of_pieces.remove(piece)
            self.piece_move(board, move, white_pawns, black_pawns)
          else:
            self.piece_move(board, move, white_pawns, black_pawns)
      else:
          print("Bro you can't do that")
          board[int(self.position[-1])-1][a_h.index(self.position[-2])] = self.notation

class Rook(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)

  def get_column(self):
    column = []
    for i in range(1, 9):
        square = a_h[a_h.index(self.position[-2])] + str(i)
        column.append(square)
    return column
  
  def get_row(self):
    row = []
    for letter in a_h:
        row.append(letter + self.position[-1])
    return row
  
  def get_everything(self):
    everything = []
    for item in self.get_column():
      everything.append(item)
    for item in self.get_row():
      everything.append(item)
    return everything

  def legal(self, board, move):
    if self.llegal(self.get_column(), board, move) == True or self.llegal(self.get_row(), board, move) == True:
      return True
    else:
      return False
  
  def rlegal(self, board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces):
    if (self.llegal(self.get_column(), board, move) == True or self.llegal(self.get_row(), board, move) == True) and self.checker(board, move, list_of_pieces, king, black_pawns, white_pawns, black_pieces, white_pieces) == False:
          if board[int(move[-1]) - 1][a_h.index(move[-2])] != "⬚":
            for piece in list_of_pieces:
              if piece.position == move:
                list_of_pieces.remove(piece)
            self.piece_move(board, move, white_pawns, black_pawns)
          else:
            self.piece_move(board, move, white_pawns, black_pawns)
    else:
      return False

def printboard(board):
    bord = copy.deepcopy(board)
    bord.reverse()
    numb = list(range(1, 9))
    numb.reverse()
    num = iter(numb)
    print("  A B C D E F G H")
    for thing in bord:
        print(next(num), end = " ")
        print(" ".join(thing))

def reverseboard(board):
    numb = list(range(1, 9))
    num = iter(numb)
    print("  H G F E D C B A")
    for thing in board:
        print(next(num), end = " ")
        print(" ".join(thing))

