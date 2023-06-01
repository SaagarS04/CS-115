'''
Created on 10/25/22
@author:   Swathi Venkateswaran and Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Hw 6
'''
from functools import reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def count(s):
    '''This function takes string input s and returns a list of all of the consecutive counts of the same digits'''
    if s == '':
        return 0
    if len(s) == 1:
        return 1
    if s[0] == s[1]:
        return 1 + count(s[1:])
    else:
        return 1

def countList(s):
    '''This function takes input s and returns a list of all of the '''
    if s == '':
        return []
    return [count(s)] + countList(s[count(s):])

def split(l):
    '''This function splits the input list l into lengths of size MAX_RUN_LENGTH, given above'''
    if l == []:
        return []
    if l[0] > MAX_RUN_LENGTH:
        l[0] = l[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + split(l)
    return [l[0]] + split(l[1:])

def isOdd(n):
    ''' This function determines if a number is odd'''
    return n % 2 == 1

def numToBinary(n):
    """converts a decimal number to a binary string"""
    if n==0:
        return ""
    else:
        if isOdd(n):
            answer = numToBinary(n//2) + "1"
            return answer
        else:
            answer = numToBinary(n//2) + "0"
            return answer

def fill(n):
    '''This function fills in 0's in empty spaces prior to the number'''
    if (len(n) < COMPRESSED_BLOCK_SIZE):
        return '0' * (COMPRESSED_BLOCK_SIZE - len(n)) + n
    return n

def binaryToNum(s):
    """converts a binary string s to a decimal number"""
    n = len(s)
    if s=="":
        return 0
    else:
        answer = int(s[0])*(2**(n-1)) + binaryToNum(s[1:])
        return answer
    
def add(x, y):
    '''This function returns the sum of two numbers'''
    return x + y

def compress(s):
    '''This function takes input string s and returns the compression of the binary string'''
    if s[0] == '1':
        binaryList = list(map(numToBinary, split(countList(s))))
        fillList = (list(map(fill, binaryList)))
        mult = reduce(add, fillList)
        return '0' * COMPRESSED_BLOCK_SIZE + mult
    binaryList = list(map(numToBinary, split(countList(s))))
    fillList = list(map(fill, binaryList))
    return reduce(add, fillList) 

def uncompress(s):
    '''This function takes binary string s and returns the uncompressed version based on the COMPRESSED_BLOCK_SIZE as given above'''
    def uncompress2(s, c):
        if (s == ''):
            return ''
        if (c % 2 == 0):
            return '0'* binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) + uncompress2(s[COMPRESSED_BLOCK_SIZE:], c + 1)
        return '1' * binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) + uncompress2(s[COMPRESSED_BLOCK_SIZE:], c + 1)
    return uncompress2(s, 0)

def compression(n):
    '''This function returns the ratio of the compression size to the original size'''
    return len(compress(n)) / len(n)
