import random


class Wizard:
    def __init__(self, name, level, exp=0):
        self.exp = exp
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature, creature_roll))

        if my_roll >= creature_roll:
            print('{} has handily triumphed over {}.'.format(self.name, creature.name))
            self.exp += creature.level
            return True
        else:
            print('{} has been DEFEATED!!!'.format(self.name))
            return False

    def __repr__(self):
        return f'Wizard: {self.name} of level {self.level}, {self.exp} XP'


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f'Creature: {self.name} of level {self.level}'
