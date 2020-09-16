class Wizard:
    def __init__(self, name, level, exp=0):
        self.exp = exp
        self.name = name
        self.level = level

    def __repr__(self):
        return f'Wizard: {self.name} of level {self.level}, {self.exp} XP'


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f'Creature: {self.name} of level {self.level}'
