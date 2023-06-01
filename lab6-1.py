'''
Created on 10/20/22
@author:   Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 == 1

'''
Complete base 2 representation of 42:
101010
'''

'''
If you are given an odd base-10 number, the least-significant bit will be a 1 to account for the 1 that makes it odd.
If the number is even, the least-significant bit is 0 because there is no one and it will be able to be created by the even numbers.
'''

'''
If you take a base-2 number, if we take off the last digit, it will reduce by a factor of 2 using integer division:
1010 = 10
101 = 5
10 = 2
1 = 1
'''

'''
In the case that N is odd, you would add a 1 at the end, being the least significant digit.
In the case that N is even, you would add a 0 at the end, being the least significant digit.
'''


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if (n == 0):
        return ''
    elif (isOdd(n)):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'
        

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    else:
        return binaryToNum(s[:-1])*2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('00000000' + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if (n > 0):
        print(s)
        return count(increment(s), n-1)
    print(s)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if (n == 0):
        return ''
    return numToTernary(n//3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if (s == ''):
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])    
