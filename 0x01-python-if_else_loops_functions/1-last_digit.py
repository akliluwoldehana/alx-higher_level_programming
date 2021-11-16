import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
LastDigit = number % 10
if LastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, LastDigit))
elif number == 0: 
    print("Last digit of {:d} is {:d} and is 0".format(number, LastDigit))
elif LastDigit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, LastDigit))

