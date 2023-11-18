"""Есть список: list1 = [‘micros’, ‘python’, ‘linux’, ‘windows’, ‘bobo’], из него составить новый
список, но без буквы ‘i’, результат: list2 = [‘mcros’, ‘python’, ‘lnux’, ‘wndows’, ‘bobo’] (используйте pass)"""

list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []
word = ''
for i in list1:
    for w in i:
        if w == 'i':
            pass
        else:
            word += w
    else:
        list2.append(word)
        word = ''
print(list2)
