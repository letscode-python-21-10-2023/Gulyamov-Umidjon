"""Напишите функцию, для умножения всех чисел в списке"""


def list_multi():
    numbers = [8, 2, 3, -1, 7]
    multi = 1
    for i in numbers:
        multi *= i
    print(multi)


list_multi()
