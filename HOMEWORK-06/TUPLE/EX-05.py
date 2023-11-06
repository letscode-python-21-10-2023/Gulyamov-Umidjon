"""Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу,
которая превращает каждый элемент кортежа в его квадрат и образует второй кортеж."""

numbers = (1, 2, 3, 4, 5, 6, 7)
sq_numbers = [int(number**2) for number in numbers]
tuple1 = tuple(sq_numbers)
print(f'Кортеж чисел: {numbers}\nКортеж квадратов: {tuple1}')
