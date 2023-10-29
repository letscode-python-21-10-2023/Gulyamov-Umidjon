"""Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые больше 5."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list1 = []
# list2 = []
# for number in a:
#     if number <= 5:
#         list1.append(number)
#     else:
#         list2.append(number)
# print(list1)
# print(list2)
list1 = [number for number in a if number <= 5]
list2 = [number for number in a if number > 5]
print(f'Список чисел меньших или равных 5 {list1}')
print(f'Список чисел больше 5 {list2}')
