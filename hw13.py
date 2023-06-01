'''
Created on 12/11/22
@author:   Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system.
CS115 - Hw 13
'''
class Board(object):
    def __init__(self, width = 7, height = 6):
        '''initializes the parameters width and height and creates a board'''
        self.width = width
        self.height = height
        board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(' ')
            board.append(row)
        self.board = board
    
    def getWidth(self):
        '''returns the width of the board'''
        return self.width

    def setWidth(self, width):
        '''set's the width of the board'''
        self.width = width
        
    def getHeight(self):
        '''returns the height of the board'''
        return self.height
    
    def setHeight(self, height):
        '''set's the height of the board'''
        self.height = height
    
    def __str__(self):
        '''prints the board'''
        result = ""
        for i in range(0, len(self.board)):
            result += '|'
            for s in self.board[i]:
                result += s + '|'
            result += '\n'
        for i in range(0, len(self.board[0])  * 2 + 1):
            result += '-'
        result += '\n'
        for i in range(0, len(self.board[0])):
            result = result + ' ' + str(i)
        return result
    
    def allowsMove(self, col):
        '''checks if a move is allowed'''
        if col >= 0 and col < self.width:
            for i in range(self.width - 1):
                if self.board[i][col] == ' ':
                    return True
        return False

    def addMove(self, col, ox):
        '''applies a move'''
        if self.allowsMove(col) == True:
            if self.board[self.height - 1][col] == ' ':
                self.board[self.height - 1][col] = ox
            else:
                for row in range(self.width - 2):
                    if self.board[row][col] == ' ' and \
                    self.board[row + 1][col] != ' ':
                        self.board[row][col] = ox
    
    def setBoard( self, moveString ): 
        """ takes in a string of columns and places 
            alternating checkers in those columns, 
            starting with 'X' 
             
            For example, call b.setBoard('012345') 
            to see 'X's and 'O's alternate on the 
            bottom row, or b.setBoard('000000') to 
            see them alternate in the left column. 
 
            moveString must be a string of integers 
        """ 
        nextCh = 'X'   # start by playing 'X' 
        for colString in moveString: 
            col = int(colString) 
            if 0 <= col <= self.width: 
                self.addMove(col, nextCh) 
            if nextCh == 'X': nextCh = 'O' 
            else: nextCh = 'X' 
    
    def winsFor(self, ox):
        '''checks if someone won'''
        output = False
        for r in range(self.height):
            for c in range(self.width - 3):
                if self.board[r][c] == ox and self.board[r][c + 1] == ox and self.board[r][c + 2]  == ox and self.board[r][c + 3] == ox:
                    output = True
        for r in range(self.height - 3):
            for c in range(self.width):
                if self.board[r][c] == ox and self.board[r + 1][c] == ox and self.board[r + 2][c]  == ox and self.board[r + 3][c] == ox:
                    output = True
        for c in range(self.width - 3):
            for r in range(self.height - 3):
                if self.board[r][c] == ox and self.board[r + 1][c + 1] == ox and self.board[r + 2][c + 2]  == ox and self.board[r + 3][c + 3] == ox:
                    output = True
        for r in range(self.height):
            for c in range(self.width - 3):
                if self.board[r][c] == ox and self.board[r - 1][c + 1] == ox and self.board[r - 2][c + 2]  == ox and self.board[r - 3][c + 3] == ox:
                    output = True   
        return output

    def hostGame(self):
        print("Welcome to Connect Four!")
        player = ["X", "O"]
        key = 0
        print(self)
        print()
        x = 0
        while x == 0:
            if key == 0:
                move = int(input("X's choice: "))
            else:
                move = int(input("O's choice: "))
            if self.allowsMove(move):
                if key == 0:
                    self.addMove(move, "X")
                    key = 1
                else:
                    self.addMove(move, "O")
                    key = 0
                print()
            if self.winsFor("X"):
                print()
                print("X wins -- Congratulations!")
                print()
                print(self)
                x = 1
            elif self.winsFor("X"):
                print()
                print("O wins -- Congratulations!")
                print()
                print(self)
                x = 1
