# Нарисуйте ёлку (вид ёлки произвольный, на картинке только пример) ,
# высоту ёлки должен задавать пользователь

neg_rows = rows = int(input('Введите высоту елки: '))
branch = 1
for i in range(rows):
    print(f'{" " * neg_rows }{"*" * branch}')
    branch += 2
    neg_rows -= 1
