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

    def __init__(self, base):
        super().__init__()
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

class AbstractNegative(AbstractEffect):

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_positive_effects(self):
        return self.base.get_positive_effects()

class Berserk(AbstractPositive):

    def __init__(self,base):
        super().__init__(base)
        self.positive_effects = self.base.get_positive_effects()
        self.stats = self.base.get_stats()
        self.positive_effects.append("Berserk")
        self.stats['Strength'] += 7
        self.stats['Endurance'] += 7
        self.stats['Agility'] += 7
        self.stats['Luck'] += 7
        self.stats['Perception'] -= 7
        self.stats['Charisma'] -= 7
        self.stats['Intelligence'] -= 3
        self.stats['HP'] += 50

    def get_stats(self):
        return self.stats.copy()

    def get_positive_effects(self):
        return self.positive_effects.copy()

# hero = Hero()
# brs = Berserk(hero)
# "HP": 128,  # health points
#             "MP": 42,  # magic points,
#             "SP": 100,  # skill points
#             "Strength": 15,  # сила
#             "Perception": 4,  # восприятие
#             "Endurance": 8,  # выносливость
#             "Charisma": 2,  # харизма
#             "Intelligence": 3,  # интеллект
#             "Agility": 8,  # ловкость
#             "Luck": 1  # удача

class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)
        self.positive_effects = self.base.get_positive_effects()
        self.stats = self.base.get_stats()
        self.positive_effects.append("Blessing")
        self.stats['Strength'] += 2
        self.stats['Perception'] += 2
        self.stats['Endurance'] += 2
        self.stats['Charisma'] += 2
        self.stats['Intelligence'] += 2
        self.stats['Agility'] += 2
        self.stats['Luck'] += 2

    def get_stats(self):
        return self.stats.copy()

    def get_positive_effects(self):
        return self.positive_effects.copy()


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.negative_effects = self.base.get_negative_effects()
        self.stats = self.base.get_stats()
        self.negative_effects.append("Weakness")
        self.stats['Strength'] -= 4
        self.stats['Endurance'] -= 4
        self.stats['Agility'] -= 4

    def get_stats(self):
        return self.stats.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()


class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.negative_effects = self.base.get_negative_effects()
        self.stats = self.base.get_stats()
        self.negative_effects.append("Curse")
        self.stats['Luck'] -= 10

    def get_stats(self):
        return self.stats.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.negative_effects = self.base.get_negative_effects()
        self.stats = self.base.get_stats()
        self.negative_effects.append("EvilEye")
        self.stats['Strength'] -= 2
        self.stats['Perception'] -= 2
        self.stats['Endurance'] -= 2
        self.stats['Charisma'] -= 2
        self.stats['Intelligence'] -= 2
        self.stats['Agility'] -= 2
        self.stats['Luck'] -= 2

    def get_stats(self):
        return self.stats.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

hero = Hero()
# print(hero.get_stats())
brs = Berserk(hero)
# print(brs.get_positive_effects())
# bls = Blessing(brs)
