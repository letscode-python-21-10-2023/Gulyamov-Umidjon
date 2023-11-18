"""Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’],
необходимо разделить на два списка, в первом только цифровые значения, а во втором только строки"""

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
list2 = []
list3 = []
for x in list1:
    if type(x) is int:
        list2.append(x)
    else:
        list3.append(x)
print(list2)
print(list3)
