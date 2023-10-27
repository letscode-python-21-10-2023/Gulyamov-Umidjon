# Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая выводит
# на экран все доступные счастливые билеты с подсчетом их количество

cnt = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if a+b+c == d+e+f:
                            cnt += 1
                            print(f'Счастливый билет №{cnt}:', a, b, c, d, e, f)

print(f'Всего {round(cnt*100/999999, 2)}% счастливых билетов, а их количество {cnt}')
