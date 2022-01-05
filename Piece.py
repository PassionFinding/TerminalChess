from string import ascii_lowercase as wordbabies
from Chess import layout
a_h = list(wordbabies[:8])
class Piece: #Needs check function
  white_notation = ["🆁", "🅱", "🅽", "🆀", "🅺", "🅿"]
  black_notation = ["🅁", "🄱", "🄽", "🅀", "🄺", "🄿"]
  def __init__(self, color, notation, position, moved):
    self.color = color
    self.notation = notation
    self.position = position
    self.moved = moved

  def checker(self, board, list_of_pieces, king):
    test_board = board
    test_board[int(self.position[-1]) - 1][a_h.index(self.position[-2])] = "⬚"
    for piece in list_of_pieces:
      pass

  def llegal(self, list_of_moves, board, move): 
    legal_list = [] 
    test_list = [] 
    for square in list_of_moves:
      if board[int(square[-1]) - 1][a_h.index(square[-2])] == "⬚": 
        legal_list.append(square) 
        test_list.append(board[int(square[-1]) - 1][a_h.index(square[-2])]) 
      else:
        if square[-2] + str(int(square[-1]) + 1) == self.position:
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

  def piece_move(self, board, p_move):
  #player input will be set to p_move
    board[int(self.position[-1]) - 1][a_h.index(self.position[-2])] = "⬚"
    board[int(p_move[-1]) - 1][a_h.index(p_move[-2])] = self.notation
    self.position = str(p_move[-2]) + str(p_move[-1])    
    self.moved = True

class Pawn(Piece): #needs en passant and promotion
    def __init__(self, color, notation, position, moved, passantable, current_column):
        super().__init__(color, notation, position, moved)
        self.passantable = passantable
        self.current_column = self.position[0]
    #The actual board in Chess.py will be substituted for board
    def legal(self, board, move):
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
        def possible_moves(): 
            possibilities = []
            for move in moves:
                if move[-2] in range(8) and move[-1] in range(8):
                    possibilities.append(move)
                else:
                    continue
            return possibilities
        if square in possible_moves():
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
            else:
                return False
        else:
            return False

    def plegal(self, board, move):
        if self.legal(board, move) == True:
            self.piece_move(board, move)
            self.current_column = self.position[-2]
        else:
            print("Bro you can't do that")

class King(Piece): #Needs castling
    def __init__(self, color, notation, position, moved):
        super().__init__(color, notation, position, moved)
    
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
            if alo == a_h[possible[1]] + str(possible[0]) and possible[-1] in range(8) and possible[-2] in range(8):
                if (board[possible[0]][possible[1]] == "⬚" or (board[possible[0]][possible[1]] in 
            self.black_notation and self.color == True) or (board[possible[0]][possible[1]] in self.white_notation and self.color == False)):
                    return True
                    break
                else:
                    continue
            else:
                continue
    
    def castle(self, board, black_pieces, white_pieces):
          pass
    
    def klegal (self, board, move):
        if self.legal(board, move) == True:
            self.piece_move(board, move)
        else:
            print("nah")

class Knight(Piece):
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
  
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
        if alo == a_h[possible[1]] + str(possible[0]) and possible[-1] in range(8) and possible[-2] in range(8):
            if (board[possible[0]][possible[1]] == "⬚" or (board[possible[0]][possible[1]] in 
            self.black_notation and self.color == True) or (board[possible[0]][possible[1]] in self.white_notation and self.color == False)):
              return True
              break
            else:
              continue
        else:
          continue


  def nlegal(self, board, move):
    if self.legal(board, move) == True:
        self.piece_move(board, move)
    else:
        print("Bro you can't do that")

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
    while column_pos in range(8) and row_pos in range(8):
      column_pos += 1
      row_pos+= 1
      positive_diagonal.append(a_h[column_pos - 1] + str(row_pos - 1))
    column_pos = a_h.index(self.position[-2])
    row_pos = int(self.position[-1])
    while column_pos in range(8) and row_pos in range(8):
      column_pos -= 1
      row_pos -= 1
      positive_diagonal.append(a_h[column_pos] + str(row_pos))
    return positive_diagonal

  def get_negative(self):
    negative_diagonal = []
    column_pos = a_h.index(self.position[-2])
    row_pos = int(self.position[-1])
    while column_pos in range(1, 8) and row_pos in range(1, 8):
      column_pos -= 1
      row_pos += 1
      negative_diagonal.append(str(a_h[column_pos]) + str(row_pos))
    column_pos = a_h.index(self.position[-2])
    row_pos = int(self.position[-1])
    while column_pos in range(1, 8) and row_pos in range(1, 8):
      column_pos += 1
      row_pos -= 1
      negative_diagonal.append(str(a_h[column_pos]) + str(row_pos))
    return negative_diagonal
  
  def legal(self, board, move):
    if self.llegal(self.get_column(board), board, move) == True or self.llegal(self.get_row(board), board, move) == True or self.llegal(self.get_positive(), board, move) == True or self.llegal(self.get_negative(), board, move) == True:
      return True
    else:
      return False

  def qlegal(self, board, move):
      if self.llegal(self.get_column(board), board, move) == True or self.llegal(self.get_row(board), board, move) == True or self.llegal(self.get_positive(), board, move) == True or self.llegal(self.get_negative(), board, move) == True:
          self.piece_move(board, move)
      else:
          print("Bro you can't do that")

def printboard():
    layout.reverse()
    numb = list(range(1, 9))
    numb.reverse()
    num = iter(numb)
    print("  A B C D E F G H")
    for thing in layout:
        print(next(num), end = " ")
        print(" ".join(thing))
queen = Queen(True, "🆀", "a1", True)
pawn1 = Pawn(False, "🄿", "g4", True, False, "g")
pawn2 = Pawn(True, "🅿", "b4", True, True, "b")
pawn3 = Pawn(False, "🄿", "e7", False, False, "e")
pawn4 = Pawn(True, "🅿", "e2", False, False, "e")
layout[int(queen.position[-1]) - 1][a_h.index(queen.position[-2])] = queen.notation
layout[int(pawn1.position[-1]) - 1][a_h.index(pawn1.position[-2])] = pawn1.notation
layout[int(pawn2.position[-1]) - 1][a_h.index(pawn2.position[-2])] = pawn2.notation
layout[int(pawn3.position[-1]) - 1][a_h.index(pawn3.position[-2])] = pawn3.notation
layout[int(pawn4.position[-1]) - 1][a_h.index(pawn4.position[-2])] = pawn4.notation
print(queen.get_positive())
