# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.

7.2 Модернизировать декоратор таким образом, чтобы можно было не только осуществлять запись в файл, но и в целом
производить любую операцию логирования или оповещения.

7.3 Доработать декоратор таким образом, чтобы можно было при декорировании можно было передавать список нотификаторов.
"""
from functools import wraps
from datetime import datetime

def decorator(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        with open(r'result.txt', 'a') as output:
            result = func(*args,**kwargs)
            output.write(f'{result}\n')
        return result
    return inner

@decorator
def repeat_message (message: str = 'Empty Message', number: int = 1) -> str:
    return f"Message: {' '.join([message for _ in range(number)])}"

# --------------------------------------------------------------------------

def decorator_param(act: callable) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            result = func(*args, **kwargs)
            act(f'{func.__name__}',result)
            return result
        return inner
    return decorator

def write_to_file(func: str, input: str) -> None:
    with open (f'result_{func}', 'a') as output:
        output.write(f'{input}\n')

def print_to_screen(func: str, input: str) -> None:
    print(f'{func}: {input}')
@decorator_param(print_to_screen)
@decorator_param(write_to_file)
def print_message(message: str = 'Empty Message') -> str:
    return f'Message: {message}'

# --------------------------------------------------------------------------

def notifier(notifiers_tuple: tuple) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            result = func(*args, **kwargs)
            for notifier in notifiers_tuple:
                notifier(f'{func.__name__}',result)
        return inner
    return decorator

def write_to_log(func: str, input: str) -> None:
        now = datetime.now()
        with open(f'log_{now.strftime("%d%m%y")}_{func}', 'a') as output:
            output.write(f'{now.strftime("%H:%M:%S")}\t{input}\n')
def print_log_to_screen(func: str, input: str) -> None:
    now = datetime.now()
    print((f'{now.strftime("%H:%M:%S")}\t{func}\t{input}\n'))

@notifier(notifiers_tuple=(write_to_log,print_log_to_screen))
def test_message(meesage: str = 'Empty Message') -> str:
    return f'My Test Message: {meesage}'

if __name__ == '__main__':
    repeat_message('Test #1', 5)
    print_message('Test #2')
    test_message('Test #3')