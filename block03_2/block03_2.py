# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и не удастся
выполнить успешно, то бросать исключение.
"""
from functools import wraps

def decorator(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs) -> any:
        counter = 10
        loop_counter = 1
        while True:
            try:
                result = func(*args,**kwargs)
                print('Все прошло успешно!')
                return result
            except ZeroDivisionError as error:
                if not counter:
                    print(f'Увы... Мы cтарались (Кол-во попыток: {loop_counter-1})')
                    raise error
                else:
                    print(f'Что-то пошло не так. Попробуем еще раз! Попытка №{loop_counter}')
                    counter -= 1
                    loop_counter += 1
    return inner

@decorator
def my_div_1(dividend, divider) -> float:
    print('Ну что? Поделим?')
    return dividend / divider


"""
2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как параметр
во время декорирования.
"""
def decorator_param(param: int = 10) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def inner(*args, **kwargs) -> any:
            counter = param
            loop_counter = 1
            while True:
                try:
                    result = func(*args,**kwargs)
                    print('Все прошло успешно!')
                    return result
                except ZeroDivisionError as error:
                    if not counter:
                        print(f'Увы... Мы cтарались (Кол-во попыток: {loop_counter-1})')
                        raise error
                    else:
                        print(f'Что-то пошло не так. Попробуем еще раз! Попытка №{loop_counter}')
                        counter -= 1
                        loop_counter += 1
        return inner
    return decorator
@decorator_param(param=5)
def my_div_2(dividend, divider) -> float:
    print('Попробуем поделить еща разок?')
    return dividend / divider

if __name__ == '__main__':
    dividend = 10
    divider = 0
    print(f'Частное: {my_div_1(dividend, divider)}')
    print(f'Частное: {my_div_2(dividend, divider)}')

