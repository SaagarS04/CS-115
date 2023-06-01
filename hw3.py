'''
Created on 10/12/22
@author:   Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amt, coins):
    '''This function takes input amount and coin system list and returns the smallest number of coins and the list of coins that make up the amount'''
    if amt == 0:
        return [0, []]
    if coins == [] or amt < 0:
        return [float("inf"), []]
    useIt = giveChange(amt - coins[0], coins)
    loseIt = giveChange(amt, coins[1:])
    return [min(1 + useIt[0], float("inf")
    if loseIt[0] == 0 else loseIt[0]), useIt[1] + [coins[0]]
    if useIt[0] < loseIt[0] else loseIt[1]]
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(s, l):
    '''Takes input character and list, and returns the respective score value to the letter'''
    if s == l[0][0]:
        return l[0][1]
    return letterScore(s, l[1:])
    
def wordScore(S, scoreList):
    '''Takes input word and list, and returns the corresponding score of the word'''
    if S == '':
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    ''' This function takes input dictionary and scores and returns the list of words with the corresponding scores to each word'''
    if dct == []:
        return []
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    elif n == 0:
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    elif n == 0:
        return L
    else:
        return drop(n - 1, L[1:])


