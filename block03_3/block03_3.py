# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с которыми
она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.

3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической очистки
кэша в процессе выполнения функций. 3.3 Параметризовать время кэширования в декораторе.
"""