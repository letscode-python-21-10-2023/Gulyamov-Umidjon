"""Тот же самый пример, с сообщением после каждой итерации о том что элемент N добавлен"""

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
list2 = []
list3 = []
for x in list1:
    if type(x) is int:
        list2.append(x)
        print(f'Элемент {x} добавлен')
    else:
        list3.append(x)
        print(f'Элемент {x} добавлен')
print(list2)
print(list3)
