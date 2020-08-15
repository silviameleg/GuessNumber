import random

def play():
    print('''\nGuess the Number is a fun game!
        
    Here\'s how it works:
    I am thinking of an integer number between 0 and 10.
    You have to guess what that number is!
    You have three chances.
    Good luck!
    ''')

    #generate a random number
    luckyNum = random.randint(0,10)
    #print command is for testing purposes only
    print(luckyNum)

    # must check the imput to be an integer between the range
    permitedRange = range(11)
    def checkImput(imp):
        if imp not in permitedRange:
            print('Please enter an integer number between 0 and 10.\n' + 
            'Let\'s start again!\n')
            play()

    #get the three gueses
    num1 = int(input('Type your first guess here: '))
    checkImput(num1)
    if num1 == luckyNum:
        print('You\'re the winner!!!')
    else:
        num2 = int(input('Try again: '))
        checkImput(num2)
        if num2 == luckyNum:
            print('You\'re the winner!!!')
        else:
            num3 = int(input('One more chance to be the winner: '))
            checkImput(num3)
            if num3 == luckyNum:
                print('You\'re the winner!!!')
            else:
                print('Game over')
play()