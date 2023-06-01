############################################################
# Name: Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens honor system
# CS115 Lab 12
#  
############################################################
import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        if (a == 0):
            raise Exception("Coefficient \'a\' cannot be 0 in a quadratic equation.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def discriminant(self):
        val = self.b ** 2 - (4 * self.a * self.c)
        return val
    def root1(self):
        discriminant = self.b ** 2 - (4 * self.a * self.c)
        if (discriminant < 0):
            return
        else:
            root = (-self.b + math.sqrt(discriminant))/(2*self.a)
        return root
    def root2(self):
        discriminant = self.b ** 2 - (4 * self.a * self.c)
        if (discriminant < 0):
            return
        else:
            root = (-self.b - math.sqrt(discriminant))/(2*self.a)
        return root
    def __str__(self):
        output = ''
        if self.__a < 0:
            a_sign = '-'
        else:
            a_sign = ''
        if self.__b < 0 or self.__c < 0:
            b_sign = '-'
        else:
            b_sign = '+'
        if self.__c < 0:
            c_sign = '-'
        else:
            c_sign = '+'
        if self.__a == 1 or self.__a == -1:
            #do not display a
            a = ''
        else:
            a = str(abs(self.__a))
        if self.__b == 0:
            b = ''
        elif self.__b == 1 or self.__b == -1:
            b = b_sign + ' x '
        else:
            b = b_sign + ' ' + str(abs(self.__b)) + 'x '
        if self.__c == 0:
            c = ''
        else:
            c = c_sign + ' ' + str(abs(self.__c)) + ' '
        return a_sign + a + 'x^2 ' + b + c + '= 0'
