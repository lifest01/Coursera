from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
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

    def get_stats(self):
        return self.base.stats.copy()


class AbstractNegative(AbstractEffect):

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


# =============================================================================
# конец секции ВАШ КОД
# =============================================================================

if __name__ == '__main__':
    # создадим героя
    hero = Hero()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk', 'Berserk']
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    # проверим правильность удаления эффектов из списка положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')
hero = Hero()
e1 = EvilEye(hero)
e2 = EvilEye(e1)
e3 = EvilEye(e2)
e4 = EvilEye(e3)
e3.base = e1
print(e4.get_negative_effects())
