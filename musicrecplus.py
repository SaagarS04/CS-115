'''
Created on 12/2/22
@author:   Saagar Shah, Anthony Dimayo, Caleb Riggs
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Group Project Part 2
'''

from os import path 


def checkForName(name):
    '''checks to see if the name exists (Anthony Dimayo)'''
    database = open('musicrecplus.txt', 'r+')
    for i in database:
        temp = i.split(':')
        if temp[0].lower().strip() == name.lower().strip():
            return temp[1]
    return []


def menu(name, preferences):
    '''displays the menu (Saagar Shah)'''
    if preferences == [] or preferences.strip() == '':
        preferences = newList()
        preferences.sort()
    x = 0
    while x == 0:
        print("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit")
        selection = input()
        if selection == "e":
            preferences = newList()
            preferences.sort()
        elif selection == "r":
            getRecommendations(preferences, name)
        elif selection == "p":
            mostPopularArtist(preferences, name)
        elif selection == "h":
            howPopular(preferences, name)
        elif selection == "m":
            mostLikes(name, len(preferences))
        elif selection == "q":
            saveAndQuit(name, preferences)
            x = 1
        else:
            print("Invalid value")


def newList():
    '''creates a new list for the artists the user likes (Caleb Riggs)'''
    l = []
    while True:
        name = input('Enter an artist that you like (Enter to finish):')
        if name == '':
            break
        l += [name.title()]
    return l


def getRecommendations(preferences, name):
    '''returns reccommendations based on similar users, if none it will return 'no recomendations at this time'(Saagar Shah)'''
    count = 0
    database = open('musicrecplus.txt', 'r+')
    highest = (0, [])
    for line in database:
        x = line.split(':')
        if '$' not in x[0] and x[0] != name:
            count = 0
            if type(preferences) != list:
                y = preferences.split(',')
            else:
                y = preferences
            for i in y:
                i = i.strip()
                if i in x[1].strip():
                    count += 1
                if count > highest[0]:
                    highest = (count, x[1])
                if highest[0] == len(y):
                    highest = (0, [])
    if len(highest[1]) == 0:
        print('No recommendations available at this time.')
    else:
        All = True
        x = highest[1].split(',')
        for i in x:
            if i.strip() not in preferences:
                All = False
                break
        if All:
            print('No recommendations available at this time')
            return
        for i in x:
            if i.strip() not in preferences:
                print(i.strip())


def mostPopularArtist(preferences, name):
    '''prints the top 3 artists that are liked by the most users (Caleb Riggs)'''
    database = open('musicrecplus.txt', 'r+')
    artists = {}
    if type(preferences) != list:
        x = preferences.split(',')
    else:
        x = preferences
    for i in x:
        #print(i)
        i = i.strip()
        if i in artists:
            artists[i] += 1
        else:
            artists[i] = 1
    for line in database:
        x = line.split(':')
        if '$' not in x[0] and x[0].lower().strip() != name.lower().strip():
            y = x[1].split(',')
            for i in y:
                i = i.strip()
                if i in artists:
                    artists[i] += 1
                else:
                    artists[i] = 1
    if len(artists) == 0:
        print('Sorry, no artists found.')
    first = ('', 0)
    second = ('', 0)
    third = ('', 0)
    for i in artists:
        if artists[i] > first[1]:
            first = (i, artists[i])
        elif artists[i] > second[1]:
            second = (i, artists[i])
        elif artists[i] > third[1]:
            third = (i, artists[i])
    if first[0] != '':
        print(first[0].strip())
    if second[0] != '':
        print(second[0].strip())
    if third[0] != '':
        print(third[0].strip())


def howPopular(preferences, name):
    '''Returns how popular the most popular artist is (Anthony Dimayo)'''
    database = open('musicrecplus.txt', 'r+')
    artists = {}
    for i in preferences:
        #print(i)
        i = i.strip()
        if i in artists:
            artists[i] += 1
        else:
            artists[i] = 1
    for line in database:
        x = line.split(':')
        if '$' not in x[0] and x[0].lower().strip() != name.lower().strip():
            y = x[1].split(',')
            for i in y:
                #print(i)
                i = i.strip()
                if i in artists:
                    artists[i] += 1
                else:
                    artists[i] = 1
    if len(artists) == 0:
        print('Sorry, no artists found.')
    first = ('', 0)
    for i in artists:
        if artists[i] > first[1]:
            first = (i, artists[i])
    print(first[1])


def mostLikes(name, number):
    '''Returns the most likes (Caleb Riggs)'''
    database = open('musicrecplus.txt', 'r+')
    highest = (name, number)
    for line in database:
        x = line.split(':')
        y = x[1].split(',')
        if '$' not in x[0]:
            if len(y) > highest[1]:
                highest = (x[0], len(y))
    print(highest[0])


def saveAndQuit(name, preferenceList):
    '''Saves the database with edits (Saagar Shah)'''
    holder = []
    formatting = ''
    for i in range(len(preferenceList)):
        if i != len(preferenceList) - 1:
            formatting += str(preferenceList[i]) + ','
        else:
            formatting += preferenceList[i]
    formatting = str(name) + ':' + formatting
    database = open('musicrecplus.txt', 'r+')
    for line in database:
        if line.split(':')[0] != name:
            holder += [line]
    holder += [formatting]
    holder.sort()
    database = open('musicrecplus.txt', 'w')
    database.write('')
    database = open('musicrecplus.txt', 'a')
    for i in holder:
        if '\n' not in i:
            i += '\n'
        database.write(i)

if path.exists('musicrecplus.txt'):
    '''Checks if path exists'''
    database = open('musicrecplus.txt', 'r+')
else:
    database = open('musicrecplus.txt', 'w+')
name = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
preferences = checkForName(name)
menu(name, preferences)
