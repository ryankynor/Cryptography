"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 = [('a',1),('b',2),('c',3),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9)
"""
associations.find(char)
associations[index]
"""

if command == "e":
    message = input("Message: ")
    key = input("Key: ")
    associations.find(key)
    associations[key]


elif command == "d":
    print ("decrypt")

  
elif command == "q":
    print ("Goodybye!")
    

else:
    print ("Did not understand command, try again.")
    
    
    
    
