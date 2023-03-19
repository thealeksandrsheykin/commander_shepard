# -*- coding: utf-8 -*-
# !/usr/bin/env python3

def easy(text: str, number: int) -> str:
    """
    The function converts the string
    :param text: original string
    :param number: the number of repetitions original string in the result
    :return: original string multiplied by number in different case
    """
    result = ''
    for i in range(number):
        if i % 2 == 1:
            result += text.upper()
        else:
            result += text
    return result


if __name__ == '__main__':
    print(f'1. {easy("easy", 3)}\n')  # Выведет результат функции

    my_var = easy  # Присвоит переменой "my_var" объект фукнции "easy"
    print(f'2. {my_var}\n')  # Выведет ссылку, где хранится функция в оперативной памяти

    print(f'3. {my_var("my_easy", 4)}')  # Выведет результат функции "easy"
