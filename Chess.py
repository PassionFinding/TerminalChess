from string import ascii_uppercase as wordbabies
layout = [["X" for i in range(8)] for i in range(8)]
a_h = list(wordbabies[:8])

def printboard():
    for thing in layout:
        print(" ".join(thing))

def move():
    player_move = input("Enter move. ")

printboard()


# while True:
#     player_move = input("Enter move. ")

#     player_move = list(player_move)

#     layout[int(player_move[1])-1][a_h.index(player_move[0])] = "p"

#     printboard()