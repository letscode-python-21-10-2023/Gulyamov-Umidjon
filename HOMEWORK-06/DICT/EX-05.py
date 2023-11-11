""" Есть словарь координат городов:
 cities = {
'Moscow': (550, 370),
'London': (510, 510),
'Paris': (480, 480),
}
Составьте словарь расстояний между городами по формуле:
((x1-x2)**2+(y1-y2)**2)**0.5
например расстояние между Лондоном и Парижем:
Используйте часть кода:
distances = {}
moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']"""

cities = {
'Moscow': (550, 370),
'London': (510, 510),
'Paris': (480, 480),
}
distances = {}
moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']
london_paris = round(((london[0]-paris[0])**2+(london[1]-paris[1])**2)**0.5, 4)
london_moscow = round(((london[0]-moscow[0])**2+(london[1]-moscow[1])**2)**0.5, 4)
moscow_paris = round(((paris[0]-moscow[0])**2+(paris[1]-moscow[1])**2)**0.5, 4)
distances['London_Paris'] = london_paris
distances['London_Moscow'] = london_moscow
distances['Moscow_Paris'] = moscow_paris
print(distances)
