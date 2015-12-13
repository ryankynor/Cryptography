"""
cryptography.py
Author: Ryan Kynor
Credit: used Jasmines code to do find the length

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l1 = []
l2 = []

while t != "q":
    find = 1000000*associations
    if command == "q":
        print ("goodbye")
    elif command == e:
        message1 =  input("message: ")
        key = input("key: ")
        for t in message:
            l1.append(associations.find (x))
        for t in key:
            l2.append(associations.find (x))
        if len(l1) > len(l2):
            tvar = len(l1)/len(l2)