'''
Created on 12/6/22
@author:   Saagar Shah
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day
    
    def tomorrow(self):
        '''Changes self to be one date ahead'''
        if self.day < DAYS_IN_MONTH[self.month]:
            self.day += 1
        else:
            if self.isLeapYear() and self.month == 2 and self.day < 29:
                self.day += 1
            else:
                self.day = 1
                if self.month < 12:
                    self.month += 1
                else:
                    self.month = 1
                    self.year += 1

    def yesterday(self):
        '''Changes self to be one date behind'''
        if self.day - 1 > 0:
            self.day -= 1
        else:
            if self.month == 3 and self.isLeapYear():
                self.day = 29
                self.month = 2
            else:
                if self.month == 1:
                    self.month = 12
                    self.day = 31
                    self.year -= 1
                else:
                    self.day = DAYS_IN_MONTH[self.month - 1]
                    self.month -= 1

    def addNDays(self, N):
        '''Add's N days to the current date'''
        for i in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''Takes away N days from the current date'''
        for i in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''Checks if self is before d2 on the calendar'''
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        else:
            if self.month < d2.month:
                return True
            elif self.month > d2.month:
                return False
            else:
                if self.day < d2.day:
                    return True
                elif self.day > d2.day:
                    return False
                else:
                    return False

    def isAfter(self, d2):
        '''Checks if self is after d2 on the calendar'''
        if self.year > d2.year:
            return True
        elif self.year < d2.year:
            return False
        else:
            if self.month > d2.month:
                return True
            elif self.month < d2.month:
                return False
            else:
                if self.day > d2.day:
                    return True
                elif self.day < d2.day:
                    return False
                else:
                    return False

    def diff(self, d2):
        '''Counts the days between self and d2'''
        temp = Date(self.month, self.day, self.year)
        count = 0
        if self.equals(d2):
            return 0
        elif self.isBefore(d2):
            while (temp.equals(d2) == False):
                count -= 1
                temp.tomorrow()
            return count
        else:
            while (temp.equals(d2) == False):
                count += 1
                temp.yesterday()
            return count

    def dow(self):
        '''returns the day of the week self is '''
        temp = self.diff(Date(11, 9, 2011))
        temp = temp % 7
        daysOfWeek = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        return daysOfWeek[temp]
