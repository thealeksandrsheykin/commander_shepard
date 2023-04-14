# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той, которая
   была решена для запуска функции суммирования.
2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве
   результата работы из объемлющей функции.
3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на
   экран. Что наблюдаете?
4. Осуществите вызов функции суммирования из полученной переменной.
"""
import random

CNT_FUNC_SUM = 0
CNT_FUNC_SUB = 0
CNT_FUNC_MUL = 0
CNT_FUNC_DIV = 0


def my_sum(a: int, b: int) -> int:
    """
    This function summation
    """
    global CNT_FUNC_SUM
    CNT_FUNC_SUM += 1
    print(f'Функция {my_sum.__name__} запускается {CNT_FUNC_SUM}')
    return a + b


def my_sub(a: int, b: int) -> int:
    """
    This function subtraction
    """
    global CNT_FUNC_SUB
    CNT_FUNC_SUB += 1
    print(f'Функция {my_sub.__name__} запускается {CNT_FUNC_SUB}')
    return a - b


def my_mul(a: int, b: int) -> int:
    """
    This function multiplication
    """
    global CNT_FUNC_MUL
    CNT_FUNC_MUL += 1
    print(f'Функция {my_mul.__name__} запускается {CNT_FUNC_MUL}')
    return a * b


def my_div(a: int, b: int) -> float:
    """
    This function division
    """
    global CNT_FUNC_DIV
    CNT_FUNC_DIV += 1
    print(f'Функция {my_div.__name__} запускается {CNT_FUNC_DIV} раз.')
    return a / b

# -----------------------------------------------------------------------

def main_function():
    print(f'Запускается внешняя функция: {main_function.__name__}')
    def sum_function(a: int, b: int) -> int:
        print(f'Запускается внутреняя функция: {sum_function.__name__}')
        return a+b
    return sum_function


if __name__ == '__main__':
    func_tuple = (my_sum, my_sub, my_mul, my_div)
    for _ in range(20):
        values = [random.randint(-100, 100) for _ in range(2)]
        func = random.choice(func_tuple)
        print(f'Вызываем функцию: {func.__name__} со значениями {values}:')
        print(f'Результат: {func(*values)}')

    # ----------------------------------------------------------------------
    my_var = main_function()
    print(my_var)  # Мы наблюдаем указатель на место хранения функции в памяти
    # ----------------------------------------------------------------------
    print(f'2 + 4 = {my_var(2, 4)}')




