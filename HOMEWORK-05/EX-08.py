"""Создайте переменную user_num, которая будет принимать от пользователя число.
Создайте числовой список от 1 до значения из переменной user_num (значение из переменной включительно).
Выведите сам список и сумму его чисел."""

user_num = int(input('Введите число: '))
list1 = [int(num) for num in range(1, user_num+1)]
print(f'Список чисел в диапазоне от 1 до {user_num}: {list1}\nСумма списка чисел равна: {(sum(list1))}')