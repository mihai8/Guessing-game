from random import randint
randomNumber=randint (1, 100)
yourNumber=int(input("Enter any number between 1 & 100: "))
tries=1
def if_else ():
    if (randomNumber==yourNumber):
        print("You won! It took you",coups,"tries.")
    elif (randomNumber<yourNumber):
        print("Too high, try again")
    else:
        print("Too low, try again")
if_else()
while (randomNumber>yourNumber or randomNumber<yourNumber):
    tries = tries+1
    yourNumber=int(input("Enter any number between 1 & 100: "))
    if_else()
