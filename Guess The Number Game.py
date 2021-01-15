import random


def guess_number ():
    global guess
    for i in range(1, 4):
        print ('Try To Guess The Number')
        guess = int(input('Enter A Number Between 1 and 20: '))

        if guess < secretNumber:
            print ('That Number Is Too Low')
        elif guess > secretNumber:
            print ('That Number Is Too High')
        else:
            break       
    return guess

def check (guess,secretNumber):
    if guess == secretNumber:
        print ('CONGRATULATIONS!! You Guessed The Number!!')
    else:
        print('Better Luck Next Time, The Correct Number Was ' + str(secretNumber))


secretNumber = random.randint(1,20)
print('Scott Is Thinking Of A Number, What Do You Think It Is?')

guess = guess_number()
check(guess, secretNumber)
    
