"""Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7].
напишите программу, которая превращает каждый элемент списка в его квадрат."""

numbers = [1, 2, 3, 4, 5, 6, 7]
sq_numbers = [int(number**2) for number in numbers]
print(f'Список чисел: {numbers}\nCписок квадратов: {sq_numbers}')
