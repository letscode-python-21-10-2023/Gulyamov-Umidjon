"""Напишите функцию, которое принимает целое число и возвращает сумму цифр целого числа 108 -> 9"""


def integer(number: int):
    numbers = str(number)
    print(sum(int(x) for x in numbers))


integer(108)
