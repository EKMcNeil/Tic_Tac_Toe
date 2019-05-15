#!/usr/bin/python3

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def board(move = 0, row = 0, column = 0, display = False):
    try:
	if not display:
            game[row][column] = move
            print("   0  1  2")
        for count, row in enumerate(game):
            print(count, row)
        return game
    except:
        print("Move may be outside board parameters")
        return False 

board(display = True)
board(move = 1, row = 1, column = 2)


#import sys

#if len(sys.argv) != 1:
#    print("Incorrect Number of Arguments")
#    sys.exit(1)

#move = sys.argv

#if move = 
