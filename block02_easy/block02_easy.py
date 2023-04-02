# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.
"""

CNT = 0


def my_sum(a: int, b: int) -> int:
    global CNT
    CNT += 1
    c = a + b
    print(f"Функция {my_sum.__name__} запускается {CNT} раз.")
    return c


if __name__ == '__main__':
    import random

    for i in range(10):
        values = [random.randint(-100, 100) for _ in range(2)]
        print(f'{values[0]} + {values[1]} = {my_sum(*values)}')
