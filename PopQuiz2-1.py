# pop quiz

# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system

# Question 1
# Implement this function so it works correctly.
# Use recursion
# You can write helper functions
# Hint: The base case is a one-element list which you can check as len(L)==1.

def myAverage(L):
    '''Assume L is a non-empty list of numbers.  Return the average of the list.'''
    # This function takes a list input and returns the average
    return Sum(L)/len(L)

def Sum(l):
    # This function takes a list input and returns the sum of the list
    if len(l) == 0:
        return 0
    else:
        return l[0] + Sum(l[1:])

def test():
    '''Prints True for each successful test'''
    # This function checks the myAverage function with 3 cases
    print( myAverage([1,2,3]) == 2 )
    print( myAverage([12,15,5,8,10]) == 10 )
    print( myAverage([12]) == 12 )

# Question 2
# Trace function call mystery(502)
def mystery(n):
    return m_help(n, 0)
def m_help(n, r):
    if n == 0:
        return r
    return m_help(n // 10, r * 10 + n % 10)
print(mystery(502)) # TRACE THIS

### Write your trace here
#n is not equal to 0, m_help with input n = 50, r = 2 is called
#then, n is still not equal to 0, m_help with input n = 5, r = 20 is called
#then, n is still not equal to 0, m_help with input n = 0, r = 205 is called
#then, n is equal to 0 so r is returned, the value is 205
#
#mystery(502) -> m_help(502, 0) -> m_help(50, 2) -> m_help(5, 20) -> m_help(0, 205)
#
###

