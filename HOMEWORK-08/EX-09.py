"""С помощью функции извлеките из списка числа, делимые на 15"""

nums = [45, 55, 60, 37, 100, 105, 220]


def slash():
    for x in nums:
        if x % 15 == 0:
            print(f'{x} число делимое на 15')
    else:
        pass


slash()
