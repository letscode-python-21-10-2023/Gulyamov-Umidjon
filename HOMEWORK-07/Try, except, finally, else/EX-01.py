"""Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться
конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются."""

num1 = input('Первое значение: ')
num2 = input('Второе значение: ')
try:
    print(int(num1)+int(num2))
except TypeError and ValueError:
    print(str(num1)+str(num2))