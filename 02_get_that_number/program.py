import random

print('-----------------------------')
print('------Guess that number------')
print('-----------------------------')
print()

the_number = random.randint(1, 100)
guess = -1

while guess != the_number:
    guess_text = input('What number am I thinking of? (1-100) ')
    guess = int(guess_text)

    if guess < the_number:
        print('Too low!')
    elif guess > the_number:
        print('Too high!')
    else:
        print('Congratulations, you got it!')

    print()

print('Game finished.')