# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать в
консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
"""
from functools import wraps


def decorator(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        print(f'Покупайте наших котиков!')
        return func(*args, **kwargs)

    return inner


@decorator
def print_message(message: str):
    print(f'{message * 2}')


"""
1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
как параметр во время декорирования.
"""


def decorator_param(param: str = 'Покупайте наших котиков!') -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            print(f'{param}')
            return func(*args, **kwargs)

        return inner
    return decorator


@decorator_param(param='Сможешь просуммировать?')
def my_sum(*args, **kwargs):
    print(f'Я суммирую всех и вся!')
    return sum(args) + sum(tuple(kwargs.values()))


if __name__ == '__main__':
    print_message('test')
    args = (3, 4)
    kwargs = {'1': 1, '2': 2}
    print(f'Сумма: {my_sum(*args, **kwargs)}')
