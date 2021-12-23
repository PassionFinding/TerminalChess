import Piece
class Pawn(Piece):

    def __init__(self, color, notation, position, moved):
    
        super().__init__(color, notation, position, moved)
    
    def legal(self, move):
    #input will be set to move
        if self.color == False:
        
            if self.moved == False:
            
                #Checks if the space two in front of it is available
                
                if Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2])] == "X" and Piece.layout[int(self.position[-1])-3][Piece.a_h.index(self.position[-2])] == "X" and Piece.layout[int(self.position[-1])-3][Piece.Piece.a_h.index(self.position[-2])] == Piece.Piece.layout[int(list(move)[-1]) - 1][Piece.Piece.a_h.index(list(move)[-2])]:
                    
                    
                    return True
                    
                #Checks if the space in front of it is available
                
                elif Piece.layout[int(self.position[-1])-2][self.position(move[-2])] == "X" and Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2])] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(list(move)[-2])]:
                
                    
                    return True
                    
                #Checks if the space one square diagonal right from it is occupied by a piece
                
                elif Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) - 1] != "X" and Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) - 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                
                    if Piece.a_h.index(self.position[-2]) - 1 >= 0:
                    
                        return True
                
                #Checks if the space one square diagonal left from it is occupied by a piece
                
                elif Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) + 1] != "X" and Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) + 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                    
                    if Piece.a_h.index(self.position[-2]) + 1 <=7:
                    
                        return True
                
                else:
                
                    return False
                    
            if self.moved == True:
            
                if Piece.layout[int(self.position[-1])-2][self.position(move[-2])] == "X" and Piece.layout[int(self.position[-1])-2][Piece.Piece.a_h.index(self.position[-2])] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(list(move)[-2])]:
                
                    
                    return True
                    
                #Checks if the space one square diagonal right from it is occupied by a piece
                
                elif Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) - 1] != "X" and Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) - 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                
                    if Piece.a_h.index(self.position[-2]) - 1 >= 0:
                    
                        return True
                
                #Checks if the space one square diagonal left from it is occupied by a piece
                
                elif Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) + 1] != "X" and Piece.layout[int(self.position[-1])-2][Piece.a_h.index(self.position[-2]) + 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                
                    if Piece.a_h.index(self.position[-2]) + 1 <=7:
                    
                        return True
                
                else:
                
                    return False
                    
        if self.color == True:
            
            if self.moved == False:
                
                if Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])] == "X" and Piece.layout[int(self.position[-1])+1][Piece.a_h.index(self.position[-2])] == "X" and Piece.layout[int(self.position[-1])+1][Piece.a_h.index(self.position[-2])] == Piece.layout[int(move[-1]) - 1][Piece.a_h.index(move[-2])]:
                
                    return True
                
                elif Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])] == "X" and Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])] == Piece.layout[int(move[-1]) - 1][Piece.a_h.index(move[-2])]:
                
                    return True
                
                elif Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) + 1] != "X" and Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) + 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                    
                    if Piece.a_h.index(self.position[-2]) + 1 <= 7:
                        
                        return True
                 
                elif Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) - 1] != "X" and Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) - 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                    
                    if Piece.a_h.index(self.position[-2]) - 1 >= 0:
                        
                        return True
                else:
                    
                    return False

            elif self.moved == True:
            
                if Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])] == "X" and Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2])] == Piece.layout[int(move[-1]) - 1][Piece.a_h.index(move[-2])]:
                
                    return True
                
                elif Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) + 1] != "X" and Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) + 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.a_h.index(move[-2])]:
                    
                    if Piece.a_h.index(self.position[-2]) + 1 <= 7:
                        
                        return True
                 
                elif Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) - 1] != "X" and Piece.layout[int(self.position[-1])][Piece.a_h.index(self.position[-2]) - 1] == Piece.layout[int(list(move)[-1]) - 1][Piece.Piece.a_h.index(move[-2])]:
                    
                    if Piece.Piece.a_h.index(self.position[-2]) - 1 >= 0:
                        
                        return True
                else:
                    
                    return False
                    
    
        