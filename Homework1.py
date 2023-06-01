############################################################
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system
# CS115 Homework 1
#  
############################################################
from functools import reduce
def mult(x, y):
    #Returns the product of x and y
    return x * y
def factorial(n):
    #Applies the reduce function using the mult function to multiply each number in a list created by the range function and the given number. Returns the factorial of n.
    return reduce(mult, range(1,n+1))
def add(x, y):
    return x + y
def mean(L):
    #Uses the reduce function and add function to sum up the parts of a list, then returns the average by dividing the sum by the size.
    size = len(L)
    return (reduce(add, L))/size
    
