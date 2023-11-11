"""Напишите код для суммирования всех значений словаря и вывод среднего арифметического значения"""
num = int(input('Ввведите число: '))
dict1 = {keys: keys**2 for keys in range(1, num+1)}
num_sum = sum(dict1.values())
average = (sum(dict1.values()))/len(dict1)
print(f'Сумма всех значений: {num_sum}\nСреднее арифметическое: {average}')
