# Составить программу, которая спрашивает возраст человека и, если ему 18 лет и больше,
# сообщает “Замечательно. Вы уже можете водить автомобиль”,
# а в противном случае – “К сожалению, водить автомобиль Bам рановато”.
# (так же можете сами придумать и добавить вывод сообщения в зависимости от возраста)

while True:
    a = int(input('Введите ваш возраст: '))
    if a >= 18:
        print('Замечательно. Вы уже можете водить автомобиль')
        pause = str(input('Продолжим [Y/N]: '))
        if pause == 'Y':
            print()
        else:
            print()
            break
    else:
        print('К сожалению, водить автомобиль Bам рановато')
        pause1 = str(input('Продолжим [Y/N]: '))
        if pause1 == 'Y':
            print()
        else:
            print()
            break
