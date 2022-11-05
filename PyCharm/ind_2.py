#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    s_list = list(s)

    for i in range (len(s)):
        if i % 2 != 0:
            s_list[i] = 'ы'

    print(f"Новая строка: {''.join(s_list)}")

