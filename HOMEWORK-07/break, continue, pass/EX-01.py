"""Есть список list1 = [i for i in range(100)],
создайте новый список с пробросом каждого пятого элемента (используйте continue)"""

list1 = [i for i in range(100)]
list2 = []
cnt = 0
for x in list1:
    cnt += 1
    if cnt == 5:
        cnt = 0
        continue
    else:
        list2.append(x)
print(f'{list1}\n{list2}')
