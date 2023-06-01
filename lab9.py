# mandelbrot.py
# Lab 9
#
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system.

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c, n):
    '''This function takes input c and n using repeated addition n times and accumulating the result, then returning it'''
    result = 0
    for i in range(n):
        result += c
    return result

def update(c, n):
    '''This function takes input c and n and returns an accumulating value of z, which is initially 0 then becomes z^2 + c repeatedly n times'''
    z = 0
    for i in range(n):
        z = z ** 2 + c
    return z

def inMSet(c, n):
    '''This function takes input c and n and using n as the number of test cases sees if c follows an MSet'''
    z = 0
    for i in range(n):
        z = z ** 2 + c
        if (abs(z) > 2):
            return False
    return True

def weWantThisPixel(col, row):
    '''This function checks to see if the column or row values are divisible by 10'''
    if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False

def test():
    '''If we were to chnge the col % 10 == 0 and row % 10 == 0 line to col % 10 == 0 or col % 10 == 0, it would create a grid.'''
    '''This function tests the weWantThisPixel function and creates an image, which is a grid'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)
    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    '''This function takes four inputs and returns the corresponding place of the pixel'''
    tempRange = floatMax - floatMin
    temp = (pix/pixMax) * tempRange + floatMin
    return temp

def mset():
    '''This function creats a fractal using the values that make the mset true'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            xVal = scale(col, width, -2, 1)
            yVal = scale(row, height, -1, 1)
            c = xVal + yVal*1j
            n = 25
            if inMSet(c, n) == True:
                image.plotPoint(col, row)
    image.saveFile()
