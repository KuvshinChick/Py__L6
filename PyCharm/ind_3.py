#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    wrong = 'иинформаця'
    print(f"Неверное слово: {wrong}")

    #Использование срезов
    print(f'Правильное слово: {wrong[1:9]}{wrong[0]}{wrong[-1]}')