"""Напишите функцию, для вычисления
факториала числа (неотрицательное целое число). Функция принимает число в качестве аргумента"""

N = int(input('Факториал числа: '))


def num_factorial():
    factorial = 1
    for num in range(2, N + 1):
        factorial *= num
    print(factorial)


num_factorial()
