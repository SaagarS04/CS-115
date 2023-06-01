############################################################
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    return(1/x)

def e(n):
    return 1 + sum(list(map(inverse, map(factorial, range(1, n+1)))))


