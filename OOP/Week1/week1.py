import unittest


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        """проверяет, что передаваемый в функцию аргумент типа float или str вызывает исключение TypeError.
        Тестовый набор входных данных:  'string',  1.5"""
        for x in (1.5, 'string'):
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        """проверяет, что передача в функцию factorize отрицательного числа вызывает исключение ValueError.
        Тестовый набор входных данных:   -1,  -10,  -100"""
        for x in (-1, -10, -100):
            with self.subTest(i=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        """проверяет, что при передаче в функцию целых чисел 0 и 1, возвращаются соответственно кортежи (0,) и (1,).
        Набор тестовых данных: 0 → (0,),  1 → (1,)"""
        for x, t in (0, (0, )), (1, (1, )):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), t)

    def test_simple_numbers(self):
        """что для простых чисел возвращается кортеж, содержащий одно данное число.
        Набор тестовых данных: 3 → (3, ),  13 → (13, ),   29 → (29, )"""
        for x, t in (3, (3, )), (13, (13, )), (29, (29, )):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), t)

    def test_two_simple_multipliers(self):
        """проверяет случаи, когда передаются числа для которых функция factorize возвращает кортеж с числом
        элементов равным 2. Набор тестовых данных: 6 → (2, 3),   26 → (2, 13),   121 --> (11, 11)"""
        for x, t in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), t)

    def test_many_multipliers(self):
        """проверяет случаи, когда передаются числа для которых функция factorize возвращает кортеж с числом
        элементов больше 2. Набор тестовых данных: 1001 → (7, 11, 13) ,   9699690 → (2, 3, 5, 7, 11, 13, 17, 19)"""
        for x, t in (1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), t)
