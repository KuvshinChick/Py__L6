#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    signs = ['.', ',', '!', '?', '/', '"', ':']
    
    # Удаление пунктуационных знаков в предложении
    for i in s:
        if i in signs:
            s = s.replace(i, "")

    # Разделить предложение на слова.
    words = s.split(' ')

    # Вывод слов, отличных от слова 'Привет'.
    for i in words:
        if i != "Привет" and i != "привет":
            print(i)
