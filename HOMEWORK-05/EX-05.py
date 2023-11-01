"""Напишите программу, которая будет
принимать три имени в качестве входных данных от пользователя
в одном input() вызове функции."""

user_example = input('Введите три любых имени разделенных между собой пробелом: ')
name_list = [str(names) for names in user_example.split(' ')]
print(f'Первое имя: {name_list[0]}\nВторое имя: {name_list[1]}\nТретье имя: {name_list[2]}')