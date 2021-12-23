class Pawn(Piece):

    def __init__(self, color, notation, position, moved):
    
        super().__init__(color, notation, position, moved)
    
    def legal(self, move):
    #input will be set to move
        if self.color == False:
        
            if moved == False:
            
                #Checks if the space two in front of it is available
                
                if layout[int(self.position[-1])-2][a_h.index(self.position[-2])] == "X" and layout[int(self.position[-1])-3][a_h.index(self.position[-2])] == "X" and layout[int(self.position[-1])-3][a_h.index(self.position[-2])] == layout[int(list(move)[-1]) - 1][a_h.index(list(move)[-2]):
                    
                    
                    return True
                    
                #Checks if the space in front of it is available
                
                elif layout[int(self.position[-1])-2][self.position(move[-2])] == "X" and layout[int(self.position[-1])-2][a_h.index(self.position[-2])] == layout[int(list(move)[-1]) - 1][a_h.index(list(move)[-2])]:
                
                    
                    return True
                    
                #Checks if the space one square diagonal right from it is occupied by a piece
                
                elif layout[int(self.position[-1])-2][a_h.index(self.position[-2]) - 1] != "X" and layout[int(self.position[-1])-2][a_h.index(self.position[-2]) - 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                
                    if a_h.index(self.position[-2]) - 1 >= 0:
                    
                        return True
                
                #Checks if the space one square diagonal left from it is occupied by a piece
                
                elif layout[int(self.position[-1])-2][a_h.index(self.position[-2]) + 1] != "X" and layout[int(self.position[-1])-2][a_h.index(self.position[-2]) + 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                    
                    if a_h.index(self.position[-2]) + 1 <=7:
                    
                        return True
                
                else:
                
                    return False
                    
            if moved == True:
            
                if layout[int(self.position[-1])-2][self.position(move[-2])] == "X" and layout[int(self.position[-1])-2][a_h.index(self.position[-2])] == layout[int(list(move)[-1]) - 1][a_h.index(list(move)[-2])]:
                
                    
                    return True
                    
                #Checks if the space one square diagonal right from it is occupied by a piece
                
                elif layout[int(self.position[-1])-2][a_h.index(self.position[-2]) - 1] != "X" and layout[int(self.position[-1])-2][a_h.index(self.position[-2]) - 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                
                    if a_h.index(self.position[-2]) - 1 >= 0:
                    
                        return True
                
                #Checks if the space one square diagonal left from it is occupied by a piece
                
                elif layout[int(self.position[-1])-2][a_h.index(self.position[-2]) + 1] != "X" and layout[int(self.position[-1])-2][a_h.index(self.position[-2]) + 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]
                
                    if a_h.index(self.position[-2]) + 1 <=7:
                    
                        return True
                
                else:
                
                    return False
                    
        if self.color == True:
            
            if moved == False:
                
                if layout[int(self.position[-1])][a_h.index(self.position[-2])] == "X" and layout[int(self.position[-1])+1][a_h.index(self.position[-2])] == "X" and layout[int(self.position[-1])+1][a_h.index(self.position[-2])] == layout[int(move[-1]) - 1][a_h.index(move[-2]):
                
                    return True
                
                elif layout[int(self.position[-1])][a_h.index(self.position[-2])] == "X" and layout[int(self.position[-1])][a_h.index(self.position[-2])] == layout[int(move[-1]) - 1][a_h.index(move[-2]):
                
                    return True
                
                elif layout[int(self.position[-1])][a_h.index(self.position[-2]) + 1] != "X" and layout[int(self.position[-1])][a_h.index(self.position[-2]) + 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                    
                    if a_h.index(self.position[-2]) + 1 <= 7:
                        
                        return True
                 
                elif layout[int(self.position[-1])][a_h.index(self.position[-2]) - 1] != "X" and layout[int(self.position[-1])][a_h.index(self.position[-2]) - 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                    
                    if a_h.index(self.position[-2]) - 1 >= 0:
                        
                        return True
                else:
                    
                    return False

            elif moved == True:
            
                if layout[int(self.position[-1])][a_h.index(self.position[-2])] == "X" and layout[int(self.position[-1])][a_h.index(self.position[-2])] == layout[int(move[-1]) - 1][a_h.index(move[-2]):
                
                    return True
                
                elif layout[int(self.position[-1])][a_h.index(self.position[-2]) + 1] != "X" and layout[int(self.position[-1])][a_h.index(self.position[-2]) + 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                    
                    if a_h.index(self.position[-2]) + 1 <= 7:
                        
                        return True
                 
                elif layout[int(self.position[-1])][a_h.index(self.position[-2]) - 1] != "X" and layout[int(self.position[-1])][a_h.index(self.position[-2]) - 1] == layout[int(list(move)[-1]) - 1][a_h.index(move[-2])]:
                    
                    if a_h.index(self.position[-2]) - 1 >= 0:
                        
                        return True
                else:
                    
                    return False
                    
    
        