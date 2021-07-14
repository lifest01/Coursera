from abc import ABC, abstractmethod


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
    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        return self.base.stats.copy()


class AbstractNegative(AbstractEffect):
    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_stats(self):
        return self.base.stats.copy()


class Berserk(AbstractPositive):

    def __init__(self, base):
        super().__init__(base)
        self.get_positive_effects()
        self.get_stats()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] += 7
        self.stats['Endurance'] += 7
        self.stats['Agility'] += 7
        self.stats['Luck'] += 7
        self.stats['Perception'] -= 3
        self.stats['Charisma'] -= 3
        self.stats['Intelligence'] -= 3
        self.stats['HP'] += 50
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append("Berserk")
        return self.positive_effects.copy()


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)
        self.get_positive_effects()
        self.get_stats()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] += 2
        self.stats['Perception'] += 2
        self.stats['Endurance'] += 2
        self.stats['Charisma'] += 2
        self.stats['Intelligence'] += 2
        self.stats['Agility'] += 2
        self.stats['Luck'] += 2
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append("Blessing")
        return self.positive_effects.copy()


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.get_negative_effects()
        self.get_stats()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 4
        self.stats['Endurance'] -= 4
        self.stats['Agility'] -= 4
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("Weakness")
        return self.negative_effects.copy()


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.get_negative_effects()
        self.get_stats()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Luck'] -= 10
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("EvilEye")
        return self.negative_effects.copy()


class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.get_negative_effects()
        self.get_stats()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 2
        self.stats['Perception'] -= 2
        self.stats['Endurance'] -= 2
        self.stats['Charisma'] -= 2
        self.stats['Intelligence'] -= 2
        self.stats['Agility'] -= 2
        self.stats['Luck'] -= 2
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("Curse")
        return self.negative_effects.copy()
