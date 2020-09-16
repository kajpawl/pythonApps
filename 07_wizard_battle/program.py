# import actors
import random
import time

from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------------------')
    print('          WIZARD BATTLE')
    print('----------------------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandorf', 75)

    while True:
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('You [a]ttack, [r]un away or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print()
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard return revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for creature in creatures:
                print(' * {} of level {}'.format(creature.name, creature.level))
        else:
            print('OK, exiting game...')
            break

        print()


if __name__ == '__main__':
    main()
