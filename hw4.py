'''
Created on 10/18/22
@author:   Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Hw 4
'''

def pascal_row(n):
    '''This function takes input n and outputs the corresponding row of the pascal's triangle'''
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    return [1] + pascHelp(pascal_row(n - 1))

def pascHelp(l):
    '''This function takes input l and outputs the corresponding list of values in the pascal row by adding the values'''
    if l == []:
        return []
    if len(l) == 1:
        return [1]
    return [l[0] + l[1]] + pascHelp(l[1:])

def pascal_triangle(n):
    '''This function takes input n and returns a pascal triangle with n rows'''
    if n == 0:
        return [[1]]
    elif n == 1:
        return [[1], [1, 1]]
    return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''This function tests the pascal_row function'''
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]

def test_pascal_triangle():
    '''This function tests the pascal_triangle function'''
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
