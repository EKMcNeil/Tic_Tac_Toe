#!/usr/bin/python3

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def board():
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)
    print(board)

board()

import sys

if len(sys.argv) != 1:
    print("Incorrect Number of Arguments")
    sys.exit(1)

move = sys.argv

if move = 
