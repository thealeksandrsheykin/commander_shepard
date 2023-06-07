# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов.
    Если введён верный пароль, то функция будет выполнена и вернется результат её работы. Если нет - в консоли
    появляется соответствующее сообщение.

6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль для каждой декорируемой
    функции.
"""
from functools import wraps
from getpass import getpass


def decorator(func: callable) -> callable:
    PASSWORD = "SECRET"
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        user_password = getpass('Enter Password: ')
        if user_password == PASSWORD:
            return func(*args, **kwargs)
        else:
            raise Exception('Ошибка пароля!')
    return inner

def decorator_param(password: str = None) -> callable:
    password_dict = {}
    def decorator(func: callable) -> callable:
        nonlocal password
        if not func.__name__ in password_dict.keys():
            if not password:
                password = getpass(f'Enter the password to secure the function call "{func.__name__}":')
            password_dict[func.__name__] = password
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            user_password = getpass(f'Enter the password to call the function "{func.__name__}": ')
            if user_password == password_dict[func.__name__]:
                return func(*args, **kwargs)
            else:
                raise Exception('Ошибка пароля!')
        return inner
    return decorator


@decorator_param('secret')
def print_message(message: str) -> None:
    print(f'Message: {message}!')

@decorator_param('test')
def print_text(text: str) -> None:
    print(text)


if __name__ == '__main__':
    print_message('Test')
    print_text('Test2')
