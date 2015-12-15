"""
cryptography.py
Author: Ryan Kynor
Credit: used Jasmines code to do find the length and for line 37 (I couldnt figure out that part)

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
import math
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command = 7
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


t = ""

while command != "q":
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    find = 1000000*associations
    if command == "q":
        print ("goodbye")
    elif command == "e":
        l1 = []
        l2 = []
        message1 =  input("message: ")
        key = input("key: ")
        for t in message1:
            l1.append(associations.find (t))
        for t in key:
            l2.append(associations.find (t))
        if len(l1) > len(l2):
            tvar = len(l1)/len(l2)
            c = math.ceil(tvar)
            l2 = c*l2
            l2a = zip(l1,l2)
            encryption = [t+x for t, x in l2a]
        for x in encryption:
            print (associations[x],end="")
        #print ("done")
    elif command == "d":
        L1 = []
        L2 = []
        message2 = input("Message: ")
        key2 = input("Key: ")
        for g in message2:
            L1.append(associations.find(g))
        for g in key2:
            L2.append(associations.find(g))
        if len(L1) > len(L2):
            tvar2 = float (len(L1)/len(L2))
            c = math.ceil(tvar2)
            L2a = c*L1
            L2a = zip(l1a, l2)
            decryption = [t-x for t, x in L2a]
        else:
            may = (len(L2)/len(L1))
            f = math.ceil(may)
            L3 = l1a*may
            L4 = zip(L3, c)
            decryption = (z-x for z, x in L4)
        for x in decryption:
            print (associations[x],end="")
       # print ("done")
    else:
        print ("Did not understand command, please try again.")
else:
    print ("goodbye")
            
            
            
            
            
            
            