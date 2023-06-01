'''
Created on 9/29/22
@author:   Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system
CS115 - Hw 2
'''
import sys
import functools
from dict import *
# Be sure to submit hw2.py.  Remove the '_template' from the file name.
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
# Implement your functions here.

def letterScore(s, l):
    #Takes input character and list, and returns the respective score value to the letter
    if s == l[0][0]:
        return l[0][1]
    return letterScore(s, l[1:])
    
def wordScore(S, scoreList):
    #Takes input word and list, and returns the corresponding score of the word
    if S == '':
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def wordCheck(rack):
    #Takes input rack and returns if a word is possible
    def test(S):
        #checks if a letter from the rack exists in the word
        if S == '':
            return True
        elif type(S) == str:
            S = list(S)
        elif S == []:
            return True
        elif rack == []:
            return False

        if rack[0] in S:
            S.remove(rack[0])
            return wordCheck(rack[1:])(S)
        return wordCheck(rack[1:])(S)
    return test

def scores(l):
    #takes an input list and returns the list with corresponding scores
    if l == []:
        return []
    return [[l[0], wordScore(l[0], scrabbleScores) ]] + scores(l[1:])

def scoreList(rack):
    #Takes input rack and returns the list of all words and scores possible
    return scores(list(filter(wordCheck(rack), Dictionary)))

def bestWord(rack):
    #Takes input rack and returns the best possible word based on score
    return bestHelp(scoreList(rack))

def bestHelp(l):
    #Helper function for bestWord, takes input list and returns the maximum value
    if l == []:
        return ['', 0]
    if len(l) == 1:
        return l[0]
    elif l[0][1] > l[1][1]:
        return bestHelp(l[1:])
    return bestHelp(l[1:])
