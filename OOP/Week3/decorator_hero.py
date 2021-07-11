from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):

    def __init__(self,obj):
        super().__init__()
        self.obj = obj


    # def get_positive_effects(self):
    #     self.get_positive_effects()
    #     return positive
    #
    #
    # def get_negative_effects(self):
    #     return self.get_negative_effects()


class AbstractPositive(AbstractEffect):
    pass
    # def get_positive_effects(self):
    #     return self.get_positive_effects()
    #
    # def get_negative_effects(self):
    #     pass


class AbstractNegative(AbstractEffect):
    pass
    # def get_negative_effects(self):
    #     return self.get_negative_effects()
    #
    # def get_positive_effects(self):
    #     pass


class Berserk(AbstractPositive):

    def get_positive_effects(self):
        return self.positive_effects.append('Berserk')

class Blessing(AbstractPositive):

    def get_positive_effects(self):
        self.positive_effects.append('Blessing')


class Weakness(AbstractNegative):
    pass


class Curse(AbstractNegative):
    pass


class EvilEye(AbstractNegative):
    pass


# hero = Hero()
# print(hero.get_stats())
# brs = Berserk(hero)
# print(brs.get_positive_effects())
