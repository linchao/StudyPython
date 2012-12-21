#! /usr/bin/env python3
# Filename: addressbook.py

#import sys
import os
import pickle as p


class Person:
    '''This is the class for person in the addressbook'''
    def __init__(self, name, mail, tele):
        self.name = name
        self.mail = mail
        self.tele = tele
        print ('%s has been added into addressbook.' %self.name)

def travers():
    global ab
    print ('name\tmail\t\t\ttele')
    for per in ab:
        print ("%s\t%s\t%s" % (per.name, per.mail, per.tele))

def lookup_name(name):
    i = 0
    global ab
    for per in ab:
        if (per.name == name):
            return i
        i += 1
    return -1

print ('''Welcome to the addressbook 0.1. \
please have fun.
1. add    person
2. delete person
3. modify
4. look all persons
5. exit''')

# load the addressbook if it is existed
abloc = r'C:\Users\Lin\Desktop\adressbook.data'
ab = []
if os.path.exists(abloc):
    f = open(abloc, 'rb')
    ab = p.load(f)
    
# This is the main function
while True:
    option = int(input('Enter the option --> '))
    if option == 1:
        name = input('name: ')
        mail = input('mail: ')
        tele = input('tele: ')
        per = Person(name, mail, tele)
        ab.append(per)
    elif option == 2:
        name = input('name: ')
        i = lookup_name(name)
        if i >= 0:
            del ab[i]
            print ('%s has been deleted.' %name)
        else:
            print ("%s doesn't exist" %name)
    elif option == 3:
        name = input('The person you want to modify: ')
        i = lookup_name(name)
        if i == -1:
            print ("Sorry, %s doesn't exist" %name)
            continue
        modify_option = int(input('1. for name\n2. for tele'))
        if modify_option == 1:
            newname = input('new name is: ')
            ab[i].name = newname
        elif modify_option == 2:
            newtele = input('new tele is: ')
            ab[i].tele = newtele
    elif option == 4:
        travers()
    elif option == 5:
        print ('Thank you for using this cute program')
        break
    else:
        print ('Unknown options.')
    print()


# save the addressbook
f = open(abloc, 'wb')
p.dump(ab, f)
f.close()
