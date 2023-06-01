#
# life.py - Game of Life lab
#
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system.
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''Creates a board with width and height'''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    '''Prints out the board'''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
        
def diagonalize(width, height):
    '''Creates a board with diagonal 1's'''
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width, height):
    '''Creates a board with innner cells as 1's'''
    A = createBoard(width, height)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            A[row][col] = 1
    return A

def randomCells(width, height):
    '''Creates a board with random cells besides the outer boarder'''
    A = innerCells(width, height)
    for row in range(height):
        for col in range(width):
            if A[row][col] == 1:
                A[row][col] = random.choice([0, 1])
    return A

def copy(A):
    '''Copy's a board and returns the copy'''
    newA = []
    for row in range(len(A)):
        newRow = []
        for col in range(len(A[row])):
            newRow.append(A[row][col])
        newA.append(newRow)
    return newA

def innerReverse(A):
    '''Reverses the inner values'''
    newA = copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if newA[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA

def neighborCount(A, r, c):
    '''Counts the neighbors around an element'''
    temp = 0
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            if not(row == r and col == c) and A[row][col] == 1:
                count+=1
    return count

def next_life_generation(A)
    '''Runs the game and using the rules specified returns the proceeding game level'''
    newA = copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                newA[row][col] = 0
            elif neighborCount(A, row, col) < 2:
                newA[row][col] = 0
            elif neighborCount(A, row, col) > 3:
                newA[row][col] = 1
            elif neighborCount(A, row, col) == 3 and newA[row][col] == 0:
                newA[row][col] = 1
    return newA
