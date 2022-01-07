"""
Random_Password_Generation
Description: Fully Custom Random Password Generator (Can generate up to a 1,000,000 character password in under 5 minutes!)

Original Design By: Landen Barker
Edited By: EDITOR NAME HERE
"""
import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']',':',';','"','<',',','.','>','/','?']

custom_password = []

char_length = int(input("How many characters would you like your password to be? "))

count = char_length

for i in range(0, count):
    
    index = random.randint(0, 25)
    index2 = random.randint(0, 9)
    index3 = random.randint(0, 28)
    
    if index < 10:
        custom_password.append(lowercase_letters[index])
    elif index > 10 and index < 15:
        custom_password.append(uppercase_letters[index])
    elif index > 15:
        custom_password.append(numbers[index2])
    else:
        custom_password.append(symbols[index3])

print()
print(''.join(custom_password))
