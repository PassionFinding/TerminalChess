from Chess import layout
from Chess import a_h
from Chess import white_notation
from Chess import black_notation
from Chess import black_pieces
from Chess import white_pieces
from Pawn import Pawn
from Queen import Queen
from King import King
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
white_queen = Queen(True, "🆀", "d1", False)
white_king = King(True, "🅺", "e1", False)
white_left_rook = Rook(True, "🆁", "a1", False)
white_right_rook = Rook(True, "🆁", "h1", False)
white_left_knight = Knight(True, "🅽", "b1", False)
white_right_knight = Knight(True, "🅽", "g1", False)
white_left_bishop = Bishop(True, "🅱", "c1", False)
white_right_bishop = Bishop(True, "🅱", "f1", False)

def move(p_move):
    square = p_move[-2]
    notation = p_move[0]
    clarification = p_move[1]
    if move == True:
        if notation in a_h or notation == "P" or notation == "p":
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
        elif notation == "Q" or notation == "q":
            white_queen.qlegal(p_move)
        elif notation == "K" or notation == "k":
            white_king.klegal(p_move)
        elif notation == "N" or notation == "n":
            if white_left_knight.legal(p_move) == True and white_right_knight.legal(p_move) == True:
                if clarification in white_left_knight.position:
                    white_left_knight.piece_move(p_move)
                elif clarification in white_right_knight.position:
                    white_right_knight.piece_move(p_move)
            elif white_left_knight.legal(p_move) == True:
                white_left_knight.piece_move(p_move)
            elif white_right_knight == True:
                white_right_knight.piece_move(p_move)
            else:
                print("not legal")
        elif notation == "B":
            if white_left_bishop.legal(p_move) == True and white_right_bishop.legal(p_move) == True:
                if clarification in white_left_bishop.position:
                    white_left_bishop.piece_move(p_move)
                elif clarification in white_right_bishop.position:
                    white_right_bishop.piece_move(p_move)
            elif white_left_bishop.legal(p_move) == True:
                white_left_bishop.piece_move(p_move)
            elif white_right_bishop == True:
                white_right_bishop.piece_move(p_move)
            else:
                print("not legal")
#Make sure to do a castling thing for the rooks