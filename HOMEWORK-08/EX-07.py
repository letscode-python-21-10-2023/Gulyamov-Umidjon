"""Напишите функцию, которая принимает слово и определяет является ли оно палиндромом
(палиндром — Слово или фраза, которые одинаково читаются слева направо и справа налево.)"""

word = input()


def palindrome():
    if word == word[::-1]:
        print('Слово - палиндром')
    else:
        print('Слово - не палиндром')


palindrome()