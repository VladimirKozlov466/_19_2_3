import pytest
from app.calcilator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        """Проверка операции умножения первую переменную умножает на вторую"""
        assert self.calc.multiply(self, 2, 5) == 10

    def test_division_calculate_correctly(self):
        """Проверка операции деления первую переменную делит на вторую"""
        assert self.calc.division(self, 6, 3) == 2
        # Проверка деления на "ноль" в калькуляторе отсутствует

    def test_subtraction_calculate_correctly(self):
        """Проверка операции вычитания из первой переменной вычитается вторая"""
        assert self.calc.subtraction(self, 8, 12) == -4

    def test_adding_calculate_correctly(self):
        """Проверка операции сложения первая складывается со второй"""
        assert self.calc.adding(self, 4, 2) == 6
