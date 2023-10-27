# ** Последовательность Фибоначчи — это серия чисел.
# Следующее число находится путем сложения двух чисел перед ним. В первые два числа 0 и 1 .
# Например, 0 + 1 = 1

NumberEnd = int(input('Конечный номер Фибоначчи: '))
num1 = num2 = 0
while NumberEnd > 0:
    num1, num2 = num2, num1 + num2
    if num2 == 0:
        print(num2, end=' ')
        num2 += 1
    elif num2 >= NumberEnd:
        break

    print(num2, end=' ')
