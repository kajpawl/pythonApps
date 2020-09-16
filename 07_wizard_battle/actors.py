import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f'Creature: {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, level, exp=0):
        # you don't have to call super.__init__() if no additional property is set in constructor
        super().__init__(name, level)
        self.exp = exp

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

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


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness=1, breaths_fire=False):
        super().__init__(name, level)
        self.scale_thickness = scale_thickness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scale_thickness / 10

        return base_roll * fire_modifier * scale_modifier
