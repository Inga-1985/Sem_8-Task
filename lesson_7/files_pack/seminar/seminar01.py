# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
# Первое число int, второе - float разделены вертикальной чертой. 
# Минимальное число - -1000, максимальное - +1000. 
# Количество строк и имя файла передаются как аргументы функции.

import random as rd

NAME_DIR = "files"
MIN_NUMBER = -1000
MAX_NUMBER = 1000

"""Генерирация файла случайными числами."""
def generate_number_file(count: int, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{rd.randint(MIN_NUMBER, MAX_NUMBER)}|{rd.random() * 2000 - 1000}')
            f.write('\n' if i < count - 1 else "")

def run(count: int, file_name: str):
    generate_number_file(count, file_name)