"""Есть кортеж a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

Выведите в отдельный кортеж числа, которые меньше или равны 5 и числа, которые больше 5."""

a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
list1 = [number for number in a if number <= 5]
list2 = [number for number in a if number > 5]
tuple1 = tuple(list1)
tuple2 = tuple(list2)
print(f'Список чисел меньших или равных 5 {tuple1}')
print(f'Список чисел больше 5 {tuple2}')
