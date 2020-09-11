import random

print('-----------------------------')
print('      Guess that number      ')
print('-----------------------------')
print()

the_number = random.randint(1, 100)
guess = -1
tries = 0

name = input('What is your name? ')
print()

while guess != the_number:
    guess_text = input('{0}, what number am I thinking of? (1-100) '.format(name))
    guess = int(guess_text)
    tries = tries + 1

    if guess < the_number:
        print('Sorry {0}, your guess of {1} was too LOW.'.format(name, guess))  # indices of passed can be omitted
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    else:
        print('Congratulations {}, you got it! The number was {}. ({} tries)'.format(name, guess, tries))

    print()

print('Game finished.')
