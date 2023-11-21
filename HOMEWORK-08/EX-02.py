"""Напишите функцию, для суммирования всех чисел в списке. Не использовать встроенную функцию sum"""


def list_summary():
    numbers = [8, 2, 3, 0, 7]
    summary = 0
    for i in numbers:
        summary += i
    print(summary)


list_summary()
