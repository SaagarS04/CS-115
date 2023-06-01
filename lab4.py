############################################################
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system
# CS115 Lab 4
#  
############################################################
from functools import reduce
def knapsack(capacity, itemList):
    '''This function takes an input capacity and item list and returns the corresponding list of items with the largest value while being within the specified capacity'''
    if capacity <= 0:
        return [0, []]
    elif itemList == []:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        useIt = knapsack(capacity - itemList[0][0], itemList[1:])
        loseIt = knapsack(capacity, itemList[1:])
        if loseIt[0] < itemList[0][1] + useIt[0]:
            return [itemList[0][1] + useIt[0]] + [[itemList[0]] + useIt[1]]
        else:
            return [loseIt[0]] + [loseIt[1]]
