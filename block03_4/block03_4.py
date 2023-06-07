# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать во время
    декорирования, как параметр.
"""
import os
import time
from functools import wraps
from datetime import datetime


def decorator_time(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        start_time = datetime.now()
        func(*args, **kwargs)
        print(f'Функция выполнялась: {datetime.now()-start_time}')
    return inner

def decorator_time_func_name(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        start_time = datetime.now()
        func(*args, **kwargs)
        print(f'Функция "{func.__name__}" выполнялась: {datetime.now()-start_time}')
    return inner

def decorator_time_file_log(path: str=f"log/log_{(datetime.now()).strftime('%d%m%Y')}")-> callable:
    try:
        os.makedirs(os.path.dirname(path))
    except FileExistsError:
        pass
    def decorator_time_func_name(func: callable) -> callable:
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            start_time = datetime.now()
            func(*args, **kwargs)
            message = f'Функция "{func.__name__}" выполнялась: {datetime.now() - start_time}'
            with open(path, 'a') as file:
                file.write(f'{(datetime.now()).strftime("%H:%m:%S")}\t{message}\n')
            print(message)
        return inner
    return decorator_time_func_name

# ---------------------------------------------- #
@decorator_time_file_log()
@decorator_time_func_name
@decorator_time
def print_message(message: str="Test") -> None:
    time.sleep(10)
    print(f'{message*2}')

if __name__ == '__main__':
    print_message()
