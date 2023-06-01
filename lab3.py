############################################################
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system
# CS115 Lab 3
#  
############################################################

def change(amount, coins):
    #This function takes two inputs, an amount of coins and a list of coin values, and returns the smallest number of coins required to sum up to the amount given.
    if amount <= 0:
        return 0
    if coins == []:
        return float("inf")
    elif len(coins) == 1:
        return 1 + change(amount - 1, coins)
    elif coins[len(coins) - 1] > amount:
        return change(amount, coins[:-1])
    else:
        use_it = 1 + change(amount - coins[len(coins) - 1], coins)
        lose_it = change(amount, coins[:-1])
        return min(use_it, lose_it)
