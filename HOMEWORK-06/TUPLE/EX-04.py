"""Напишите программу, которая будет принимать три имени в качестве входных данных от
пользователя в одном input()
 и превращать данные в кортеж, ну а затем доставать их:"""

user_example = input('Введите три любых имени разделенных между собой пробелом: ')
name_list = [str(names) for names in user_example.split(' ')]
tuple_names = tuple(name_list)
print(f'Кортеж имен: {tuple_names}\nПервое имя: '
      f'{tuple_names[0]}\nВторое имя: {tuple_names[1]}\nТретье имя: {tuple_names[2]}')
