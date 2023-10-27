# Многие спортсмены жаловались, что судья слишком тихо отсчитывает секунды,
# оставшиеся до старта («Три!.. Два!.. Один!..»).
# Фирма Go Ahead купила табло для наглядного отображения оставшегося времени.

import datetime
from time import sleep

data = int(input("Укажите время для таймера (в минутах): "))
timer = str(datetime.timedelta(minutes=data))  # Конвертация минут в ЧАС:МИНУТА:СЕКУНДА
h, m, s = timer.split(":")  # Распаковка элементов списка
h, m, s = int(h), int(m) - 1, int(s)  # всегда должно быть на минуту меньше

for i in range(0, 3600*h+60*m+s+1):
    a = str((str(datetime.timedelta(seconds=(3600*h+60*m+s)-i))).split(':')[0]+" : "
            + (str(datetime.timedelta(seconds=(3600*h+60*m+s+59)-i))).split(':')[1]+" : "
            + (str(datetime.timedelta(seconds=(3600*h+60*m+s+59)-i))).split(':')[2])
    print(f'\r{a}', end=' ')
    sleep(1)
