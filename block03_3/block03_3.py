# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с которыми
она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
"""

import math
import time
from functools import wraps
from datetime import datetime

def decorator_cache(func: callable) -> callable:
    cache = dict()
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        key = args + tuple(kwargs.values())
        print(f'Run {func.__name__}. Cache: {cache}')
        if not cache.get(key):
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

@decorator_cache
def my_sum(*args, **kwargs):
    return sum(args) + sum(tuple(kwargs.values()))

"""
3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической очистки
кэша в процессе выполнения функций.
"""
def decorator_cache_time(func: callable) -> callable:
    cache = dict()
    start_time = datetime.now()
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        nonlocal start_time
        diff_time = int((datetime.now() - start_time).total_seconds())
        if diff_time > 10:
            cache.clear()
            start_time = datetime.now()
        print(f'Run {func.__name__}. Cache: {cache}. Time: {diff_time}')
        key = args + tuple(kwargs.values())
        if not cache.get(key):
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

@decorator_cache_time
def my_pow(number: int, exp: int) -> int:
    time.sleep(5)
    return math.pow(number, exp)

"""
3.3 Параметризовать время кэширования в декораторе.
"""

def decorator_cache_time_param(timer: int=10) -> callable:
    def decorator_cache_time(func: callable) -> callable:
        cache = dict()
        start_time = datetime.now()
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            nonlocal start_time
            diff_time = int((datetime.now() - start_time).total_seconds())
            if diff_time > timer:
                cache.clear()
                start_time = datetime.now()
            print(f'Run {func.__name__}. Cache: {cache}. Time: {diff_time}')
            key = args + tuple(kwargs.values())
            if not cache.get(key):
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return inner
    return decorator_cache_time
@decorator_cache_time_param(20)
def my_log(number: int) -> float:
    time.sleep(3)
    return math.log2(number)

if __name__ == '__main__':
    sum_args = ({'1':3,'2':4},{'3':5,'4':6},{'5':7,'6':8},{'1':3,'2':4},{'7':9,'8':10},{'3':5,'4':6})
    for x in sum_args:
        print(f'Сумма {tuple(x.values())}: {my_sum(**x)}')
    pow_args = ((1,2),(3,4),(5,6),(1,2),(7,8),(3,4))
    for y in pow_args:
        print(f'Степень {y}: {my_pow(*y)}')
    log_args = (1,2,1,4,5,2,3)
    for z in log_args:
        print(f'Логарифм {z}: {my_log(z)}')

