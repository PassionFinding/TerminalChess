from string import ascii_lowercase as wordbabies
from Piece import Piece
from Pawn import Pawn
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight

#Functions needed: Move functionality, En Passant, Promotion, Checks, game end functionality (win/lose)

layout = [["☐" for i in range(8)] for i in range(8)]
a_h = list(wordbabies[:8])
white_notation = ["🆁", "🅱", "🅽", "🆀", "🅺", "🅿"]
black_notation = ["🅁", "🄱", "🄽", "🅀", "🄺", "🄿"]
upper_notation = ["P", "R", "B", "N", "Q", "K"]

#Make a list of each sides pieces. When taken, list.pop(piece)
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

def printboard():
    layout.reverse()
    numb = list(range(1, 9))
    numb.reverse()
    num = iter(numb)
    print("  A B C D E F G H")
    for thing in layout:
        print(next(num), end = " ")
        print(" ".join(thing))

def reverseboard():
    numb = list(range(1, 9))
    num = iter(numb)
    print("  🄰 🄱 🄲 🄳 🄴 🄵 🄶 🄷")
    for thing in layout:
        print(next(num), end = " ")
        print(" ".join(thing))


move = True
def black_move():
    move = False
    print("Black's move")
def white_move():
    move = True
    print("White's move")

def starting_board():
    for item in black_pieces:
        layout[int(item.position[-1]) - 1][a_h.index(item.position[-2])] = item.notation
    for item in white_pieces:
        layout[int(item.position[-1]) - 1][a_h.index(item.position[-2])] = item.notation

def white_short_castle():
    if layout[0][5] != "☐" or layout[0][6] != "☐" or white_king.moved == True or white_right_rook.moved == True:
        print("Can't castle!")
    else:
        for piece in black_pieces:
            if piece.legal("e1") == True or piece.legal("f1") == True or piece.legal("g1") == True or piece.legal("h1") == True:
                print("Can't castle!")
                break
            else:
                layout[0][4] = "☐"
                layout[0][7] = "☐"
                layout[0][5] = "🆁"
                layout[0][6] = "🅺"
                break
def white_long_castle():
    if layout[0][1] != "☐" or layout[0][2] != "☐" or layout[0][3] != "☐" or white_king.moved == True or white_left_rook.moved == True:
        print("Can't castle!")
    else:
        for piece in black_pieces:
            if piece.legal("e1") == True or piece.legal("d1") == True or piece.legal("c1") == True or piece.legal("b1") == True or piece.legal("a1") == True:
                print("Can't castle!")
                break
            else:
                layout[0][4] = "☐"
                layout[0][0] = "☐"
                layout[0][3] = "🆁"
                layout[0][2] = "🅺"
                break
def black_short_castle():
    if layout[7][5] != "☐" or layout[7][6] != "☐" or black_king.moved == True or black_right_rook.moved == True:
        print("Can't castle!")
    else:
        for piece in white_pieces:
            if piece.legal("e1") == True or piece.legal("f1") == True or piece.legal("g1") == True or piece.legal("h1") == True:
                print("Can't castle!")
                break
            else:  
                layout[7][4] = "☐"
                layout[7][7] = "☐"
                layout[7][5] = "🅁"
                layout[7][6] = "🄺"
                break
def black_long_castle(): 
    if layout[7][1] != "☐" or layout[7][2] != "☐" or layout[7][3] != "☐" or black_king.moved == True or black_left_rook.moved == True:
        print("Can't castle!")
    else:
        for piece in white_pieces:
            if piece.legal("e8") == True or piece.legal("d8") == True or piece.legal("c8") == True or piece.legal("b8") == True or piece.legal("a8") == True:
                print("Can't castle!")
                break
            else:
                layout[7][4] = "☐"
                layout[7][0] = "☐"
                layout[7][3] = "🅁"
                layout[7][2] = "🄺"
                break

p_move = input("Enter move: ")
def move(p_move):
    square = p_move[-2]
    notation = p_move[0]
    clarification = p_move[1]
    if move == True:
        if notation in a_h:
            pawns = []
            for item in white_pieces:
                if type(item) == Pawn:
                    pawns.append(item)
            for item in pawns:
                if len(p_move) == 2:
                    if item.legal(p_move) == True:
                        item.plegal(p_move)
                        break
                    else:
                        print("not legal")
                else:
                    if item.current_column == notation:
                        item.plegal(p_move)
                        break
                    else:
                        print("not legal")


                


while True:
    starting_board()
    printboard()
    p_move = input("Enter move: ")
    square = p_move[-2]
    notation = p_move[0]
    clarification = p_move[1]
    
