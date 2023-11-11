"""В задании создан словарь, с информацией о разных устройствах.

Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве"""

devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

info = '''
Расположение      {}
Вендор            {}
Модель            {}
Система(ios)      {}
IP адрес          {}
'''

data = input('Введите название устройства [r1/r2/sw1]: ')
location = devices.get(data).get('location')
vendor = devices.get(data).get('vendor')
model = devices.get(data).get('model')
ios = devices.get(data).get('ios')
ip = devices.get(data).get('ip')

print(info.format(location, vendor, model, ios, ip))
