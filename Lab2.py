############################################################
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system
# CS115 Lab 2
#  
############################################################

def dot(L, K):
    #This function takes two lists of integers and computes the dot product and returns that.
    dotProd = 0
    if (len(L) == 0):
        return dotProd
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(s):
    #This function takes a string as an input and returns a list of characters of each character in the string.
    l = []
    if (len(s) == 0):
        return l
    else:
        l.append(s[0])
        l.extend(explode(s[1:]))
    return l

def ind(e, L):
    #This function takes a list input and an element and will return the length of the list if element e is not found in the list, or it will return the first index of element e.
    count = 0
    if(len(L) == 0):
        return 0
    else:
        if(L[0] == e):
            return count
        else:
            return 1 + ind(e, L[1:])

def removeAll(e, L):
    #This function takes a list input and an element input and returns the same list after removing all instances of element e. 
    l = []
    if(L == []):
        return l
    if (L[0] != e):
        l.append(L[0])
    return l + removeAll(e, L[1:])

def deepReverse(L):
    #This function takes a list input and returns a reversal of the elements in the list; any lists within elements are also reversed.
    l = []
    if (L == []):
        return l
    else:
        if (isinstance(L[len(L) - 1], list)):
            l.append(deepReverse(L[len(L)-1]))
        else:
            l.append(L[len(L) - 1])
        return l + deepReverse(L[:-1])
def myFilter(f, l):
    #This function takes a function and list input and only keeps the elements in the list that make the function return true.
    filt = []
    if (l == []):
        return filt
    if (f(l[0]) == True):
        filt.append(l[0])
    return filt + myFilter(f, l[1:])
