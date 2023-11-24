"""Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых. Написать функцию bank,
принимающая количество денег и лет, и возвращающую сумму, которая будет на счете через years лет"""

money = int(input('Введите сумму вклада: '))
years = int(input('Введите количество лет для вклада: '))


def deposit():
    print(f'{cnt} год: {round(money)} $')
    print(f'За {cnt} лет вы соберете: {round(money)} $')


cnt = 0
for year in range(years):
    cnt += 1
    money = money + (money * 10 / 100)

deposit()
