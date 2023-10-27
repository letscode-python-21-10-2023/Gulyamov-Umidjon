# Составить таблицу умножения, как на картинке ниже:—-

for n in range(1, 10):
    for k in range(1, 10):
        result = k * n
        print(f'{result}', end='\t')
    print()
