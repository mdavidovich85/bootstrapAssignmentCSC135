# CST100 Spring 2016 Term B
# Assignment Four 
# by Mike Davidovich
# last modified 4/11/16

#part 1, 1, part a

for i in range(10):         #prints 10 rows
    for j in range(10): 
        print(j,end=' ')    #prints range horizontally on each line
    print('\n')

#part 1, 1, part b
    
number = 0
for i in range(10):         #prints 10 rows
    for j in range(10):
        print(number,end=' ')    #prints number 10 times horizontally
    number = number + 1         #advances to next number
    print('\n')

#part 1, 2

n=1
for i in range(10):     #prints 10 rows
    for j in range(n):
        print(j,end=' ')    #prints current range for row
    n = n + 1               #advances range for row
    print('\n')

# extra credit

counter = 0
x = 10          #sets beginning range
y = 11
for i in range(9):          
    for j in range(x,y):
        print(j,end=' ')
    counter = counter + 1   #advances range as needed
    x = x + counter
    y = x + counter + 1
    print('\n')

# encryption tool

def encrypt(messageReg, key):     #function to encrypt message
    for char in messageReg:
        n = (ord(char))            #find ordnial value of each string
        if (n + int(key)) > 126:    #algorithms to assign new value
            encryptedChar = ((n + int(key)) - 127) + 32
        else:
            encryptedChar = n + int(key)
        print(chr(encryptedChar),end='')  #converts each chacter to encrpyed character

def decrypt(messageEnc):    #function to decrypt message
    for key in range(1,101):   #checks all keys 1-100
        print('\n')
        decryptedChar = ""  
        for char in messageEnc:
            n = (ord(char))
            if (n - int(key)) < 32:       #algorthims to decrypt
                decryptedChar = decryptedChar + chr(n - int(key) + 127 - 32)
            else:
                decryptedChar = decryptedChar + chr(n - int(key))
        print('Key: {} -> Decoded Message:'.format(key), decryptedChar)

            
while True:          #statements to call encrypt/decrpyt functions
    question = input("(E)ncrypting or (D)ecrypting?")
    if question.capitalize() == "E":
        messageReg = input(str("Enter a regular message to encode:"))        
        key = input("Enter a key value (between 0 and 100) for enconding:")
        encrypt(messageReg, key)    #call function
        break
    elif question.capitalize() == "D":
        messageEnc = input(str("Enter an encrypted message to decode:"))
        decrypt(messageEnc)     #call function
        break
    else:
        print("That is not a valid input")
                

