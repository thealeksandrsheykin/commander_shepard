# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы, первые 2 аргумента
из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов (если они есть), переданных по
ключу (если они есть).
"""


def hard(a: int, b: int, c: int, d: int, *args: int, **kwargs: int) -> int:
    """
    the function returns the sum of the required arguments
    :param a: integer type number
    :param b: integer type number
    :param c: integer type number
    :param d: integer type number
    :param args: tuple of only integer type numbers
    :param kwargs: dict only where values keys are only integer
    :return: integer type number
    """

    my_list = [(a, b, c, d), args[:2], tuple(kwargs.values())[:2]]

    return sum(list(sum(my_list, ())))


if __name__ == '__main__':
    print(hard(1, 2, 3, 4, 5, 6, 7, 8, e=9, f=10, g=11, h=12))



