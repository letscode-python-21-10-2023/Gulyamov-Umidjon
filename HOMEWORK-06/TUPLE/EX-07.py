"""Есть кортеж с данными
numbers = (12, 33, 44, 33, 12, 45, 11, 55, ’44’, 30, 10), создайте список и кортеж данных без дубликатов"""

numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
set1 = {int(num) for num in numbers}
print(f'{list(set1)}\n{tuple(set1)}')