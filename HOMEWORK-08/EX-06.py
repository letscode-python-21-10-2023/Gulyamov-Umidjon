"""Напишите функцию, которая принимает строку и
вычисляет количество букв верхнего и нижнего регистра"""

string1 = 'The quick Brow Fox'


def register():
    cnt1 = 0
    cnt2 = 0
    for i in string1:
        if i.isupper():
            cnt1 += 1
        elif i.islower():
            cnt2 += 1
    print(f'Кол-во символов в верхнем регистре: {cnt1}\nКол-во символов в нижнем регистре: {cnt2}')


register()
