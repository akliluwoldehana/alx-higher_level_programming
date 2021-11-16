#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = number % 10
if(LastDigit == 0):
    print("Last digit of {:d} is {:d} and is 0")
elif(LastDigit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5")
elif(LastDigit < 6):
    print("Last digit of {:d} is {:d} and is  less than 6 and not 0")
