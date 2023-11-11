"""Напишите код для объединения двух списков в словарь ключ: значение.
СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)"""

list1 = ['management', 'sales', 'hr', 'production', 'admins']
vlan_list = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50']
dict1 = {}
for x in range(len(list1)):
    dict1[list1[x]] = vlan_list[x]
print(f'Список1: {list1}\nСписок2: {vlan_list}\nОбъединенный словарь: {dict1}')
