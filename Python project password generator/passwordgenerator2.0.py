import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()*&%$#!@"
length = int(input("enter the length: "))
password = ""

for a in range(length):
    password+=random.choice(chars)

print(password)    

 


