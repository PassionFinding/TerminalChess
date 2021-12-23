class Bishop:
  def __init__(self, color, notation, position, moved):
    super().__init__(color, notation, position, moved)
  

#So every square on a bishop's diagonal adds or subtracts the same number from the bishop's coordinates
#It goes four directions, with 1 and -1, -1 and 1, 1 and 1, and -1 and -1. 
#you can perform those operations on the index numbers of the piece's positions and stop once a value is at zero, at 7, or the pair of number coordinates on the layout don't equal an empty space
  def legal(self, move):
    legal_list = []
    