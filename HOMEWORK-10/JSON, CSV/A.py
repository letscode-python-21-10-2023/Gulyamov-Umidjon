"""На основе WEB ресурса Создать свои JSON файлы"""
import requests
import json

URL = 'https://jsonplaceholder.typicode.com/posts'
posts = requests.get(URL).json()
DATA1 = []
for post in posts:
    userId = post.get('userId')
    ID = post.get('id')
    title = post.get('title')
    body = post.get('body')
    DATA1.append({
        'Айди пользователя': userId,
        'Айди': ID,
        'Заголовок': title,
        'Тело': body,
    })

with open('posts.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA1, file, ensure_ascii=False, indent=4)

URL = 'https://jsonplaceholder.typicode.com/comments'
comments = requests.get(URL).json()
DATA2 = []
for comment in comments:
    postId = comment.get('postId')
    ID = comment.get('id')
    name = comment.get('name')
    email = comment.get('email')
    body = comment.get('body')
    DATA2.append({
        'Айди поста': postId,
        'Айди': ID,
        'Имя': name,
        'Почта': email,
        'Тело': body
    })

with open('comments.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA2, file, ensure_ascii=False, indent=4)

URL = 'https://jsonplaceholder.typicode.com/albums'
albums = requests.get(URL).json()
DATA3 = []
for album in albums:
    userId = album.get('userId')
    ID = album.get('id')
    title = album.get('title')
    DATA3.append({
        'Айди пользователя': userId,
        'Айди': ID,
        'Заголовок': title,
    })

with open('albums.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA3, file, ensure_ascii=False, indent=4)


URL = 'https://jsonplaceholder.typicode.com/photos'
photos = requests.get(URL).json()
DATA4 = []
for photo in photos:
    albumId = photo.get('albumId')
    ID = photo.get('id')
    title = photo.get('title')
    url = photo.get('url')
    thumbnailUrl = photo.get('thumbnailUrl')
    DATA4.append({
        'Айди альбома': albumId,
        'Айди': ID,
        'Заголовок': title,
        'URL': url,
        'URL миниатюры': thumbnailUrl
    })

with open('photos.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA4, file, ensure_ascii=False, indent=4)


URL = 'https://jsonplaceholder.typicode.com/todos'
todos = requests.get(URL).json()
DATA5 = []
for todo in todos:
    userId = todo.get('userId')
    ID = todo.get('id')
    title = todo.get('title')
    completed = todo.get('completed')
    DATA5.append({
        'Айди пользователя': userId,
        'Айди': ID,
        'Заголовок': title,
        'Завершение': completed,
    })

with open('todos.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA5, file, ensure_ascii=False, indent=4)


URL = 'https://jsonplaceholder.typicode.com/users'
users = requests.get(URL).json()
DATA = []
for user in users:
    full_name = user.get('name')
    username = user.get('username')
    email = user.get('email')
    phone = user.get('phone')
    address = f"Город {user.get('address').get('city')}, улица {user.get('address').get('street')}"
    DATA.append({
        'Имя': full_name,
        'Логин': username,
        'Почта': email,
        'Номер': phone,
        'Адрес': address
    })


with open('users.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA, file, ensure_ascii=False, indent=4)
