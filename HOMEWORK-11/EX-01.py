"""Создать класс компьютер

C параметрами: Владелец, Процессор, ОЗУ, Объём жесткого диска, Монитор
Прописать метод строкового представления класса
Создать метод который будет возвращать имя владельца компьютера:
Запускать его самостоятельно (через указания вручную),
Сделать чтоб он запускался в конструкторе (автоматически)
Создать метод который будет сравнивать два класса по их ОЗУ"""


class PC:
    def __init__(self, owner: str, processor: str, RAM: int, HDD_OR_SSD: int, monitor: str):
        self.owner = owner
        self.processor = processor
        self.RAM = RAM
        self.HDD_OR_SSD = HDD_OR_SSD
        self.monitor = monitor

    def __str__(self):
        return self.owner


PC1 = PC('UMID', 'i5-12400F', 16, 512, 'BENQ27')
PC2 = PC('MAMUR', 'i5-10400F', 16, 1024, 'LG')
if PC1.RAM > PC2.RAM:
    print(f'RAM у пользователя {PC1} больше ')
elif PC1.RAM < PC2.RAM:
    print(f'RAM у пользователя {PC2} больше ')
elif PC1.RAM == PC2.RAM:
    print(f'RAM у пользователей равна')
