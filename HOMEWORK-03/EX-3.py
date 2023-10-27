# Создайте игру «Угадай число»,
# программа генирирует рандомное число в заданном интервале,
# и предлагает пользователю угадать,
# игра продолжается до тех пор пока пользователь угадает число,
# пример игры на картинке ниже:
import random

print('Python: Привет, как вас зовут?')
name = input('ваше имя: ')
print(f'Что ж {name}, я загадываю число от 1 до 5')
num = (random.randrange(1, 6))
cnt = 0
while True:
    cnt += 1
    print('Попробуй угадать')
    your_num = int(input())
    if num == your_num:
        print(f'Отлично, вы угадали число! Вы справились за {cnt} попыток')
        break
    elif your_num - num >= 2:
        print('Ваше число слишком большое')
    elif your_num - num <= -2:
        print('Ваше число слишком маленькое')
    elif your_num - num >= 1:
        print('Ваше число большое')
    elif your_num - num >= -1:
        print('Ваше число маленькое')
