import random

print('''\nGuess the Number is a fun game!
      
Here\'s how it works:
I am thinking of an integer number between 0 and 10.
You have to guess what that number is!
You have three chances.
Good luck!
''')

#generate a random number
luckyNum = random.randint(0,10)
print(luckyNum)

#get the three gueses
num1 = int(input('Type your first guess here: '))

if num1 == luckyNum:
    print('You\'re the winner!!!')
else:
    num2 = int(input('Try again: '))
    if num2 == luckyNum:
        print('You\'re the winner!!!')
    else:
        num3 = int(input('One more chance to be the winner: '))
        if num3 == luckyNum:
            print('You win!!!')
        else:
            print('Game over')

# must check the imput to be an integer between the range