# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
После решения задач написать функцию и задекорировать её сразу несколькими из созданных декораторов и посмотреть на
результат и суметь объяснить его. Потом поменять порядок декорирования и проделать то же самое.
"""
import time
from functools import wraps
from datetime import datetime

def decorator_message(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        print(f'Функция: {func.__name__} c аргументом: {args + tuple(kwargs.values())}')
        return func(*args, **kwargs)
    return inner

def decorator_cache(func: callable) -> callable:
    cache = dict()
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        key = args + tuple(kwargs.values())
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        print(f'Cache: {cache}')
        return cache[key]
    return inner

def decorator_time(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        start_time = datetime.now()
        result = func(*args, **kwargs)
        difference_in_time = datetime.now()-start_time
        print(f'Функция {func.__name__} выполнялась: {difference_in_time}')
        return result
    return inner

# --------------------------------- #

@decorator_cache
@decorator_message
@decorator_time
def bin_to_dec(bin_number: str) -> int:
    result = int(bin_number, 2)
    print(f'Binary number: {bin_number} -> Decimal number: {result}')
    return result

if __name__ == '__main__':
    data = ('111','010','1010101','010','11101010','111')
    for bin_number in data:
        print(f'Результат: {bin_to_dec(bin_number)}')
"""
Результат выполнения функции bin_to_dec при следующем порядке декораторов:
@decorator_time
@decorator_message
@decorator_cache

Функция: bin_to_dec c аргументом: ('111',)
Binary number: 111 -> Decimal number: 7
Cache: {('111',): 7}
Функция bin_to_dec выполнялась: 0:00:12.005158
Результат: 7
Функция: bin_to_dec c аргументом: ('010',)
Binary number: 010 -> Decimal number: 2
Cache: {('111',): 7, ('010',): 2}
Функция bin_to_dec выполнялась: 0:00:12.005126
Результат: 2
Функция: bin_to_dec c аргументом: ('1010101',)
Binary number: 1010101 -> Decimal number: 85
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85}
Функция bin_to_dec выполнялась: 0:00:12.005205
Результат: 85
Функция: bin_to_dec c аргументом: ('010',)
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85}
Функция bin_to_dec выполнялась: 0:00:00.000058
Результат: 2
Функция: bin_to_dec c аргументом: ('11101010',)
Binary number: 11101010 -> Decimal number: 234
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85, ('11101010',): 234}
Функция bin_to_dec выполнялась: 0:00:12.002857
Результат: 234
Функция: bin_to_dec c аргументом: ('111',)
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85, ('11101010',): 234}
Функция bin_to_dec выполнялась: 0:00:00.000052
Результат: 7
-------------------------------------------------------------------------
Результат выполнения функции bin_to_dec при следующем порядке декораторов:
@decorator_cache
@decorator_message
@decorator_time

Функция: bin_to_dec c аргументом: ('111',)
Binary number: 111 -> Decimal number: 7
Функция bin_to_dec выполнялась: 0:00:12.005144
Cache: {('111',): 7}
Результат: 7
Функция: bin_to_dec c аргументом: ('010',)
Binary number: 010 -> Decimal number: 2
Функция bin_to_dec выполнялась: 0:00:12.005017
Cache: {('111',): 7, ('010',): 2}
Результат: 2
Функция: bin_to_dec c аргументом: ('1010101',)
Binary number: 1010101 -> Decimal number: 85
Функция bin_to_dec выполнялась: 0:00:12.000463
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85}
Результат: 85
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85}
Результат: 2
Функция: bin_to_dec c аргументом: ('11101010',)
Binary number: 11101010 -> Decimal number: 234
Функция bin_to_dec выполнялась: 0:00:12.003087
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85, ('11101010',): 234}
Результат: 234
Cache: {('111',): 7, ('010',): 2, ('1010101',): 85, ('11101010',): 234}
Результат: 7

Вывод:
Результаты отличаются. Декораторы можно сравнить с матрешкой, то есть каждый декоратор запаковывает свою ниже стоящую
функцию. И когда мы выполняем код например:

@decorator_cache
@decorator_message
@decorator_time
def bin_to_dec(bin_number: str) -> int:
    result = int(bin_number, 2)
    time.sleep(12)
    print(f'Binary number: {bin_number} -> Decimal number: {result}')
    return result
    
Cначала функция "bin_to_dec" перейдет во владения декоратора "decorator_time", затем декорируемая декоратором 
(decorator_time) функция "bin_to_dec" переходит во владение "decorator_message", а затем следовательно дважды 
декорируемая функция перейдет во владение последнего декоратора "decorator_cache".
func = decorator_cache(decorator_message(decorator_time(bin_to_dec))). И из-за изменения следования декораторов результат
может отличаться, так как выполнение декораторов будет происходить в другом порядке.
"""
