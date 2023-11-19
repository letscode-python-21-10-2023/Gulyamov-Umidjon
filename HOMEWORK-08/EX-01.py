"""Напишите функцию, чтобы найти максимальное из трех чисел"""


def max_number(num1: int, num2: int, num3: int):
    """
    Выдает максимальное из трех целых чисел,
    принимает на вход три целых числа через запятые.
    """
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3


number = max_number(1, 2, 3)
print(number)
