# Решить задачи, которые не успели решить на семинаре, задача №3

# Напишите функцию, которая открывает на чтение созданные в прошлых
# задачах файлы с числами и именамми.
# Перемножте пары чисел.
# В новый файл сохраните имя и произведение:
# - если результат умножения отрицательный, сохраните имя записанное
# строчными буквами и произведение по модулю
# - если результат умножения положительный, сохраните имя прописными
# буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.

from typing import TextIO
from pathlib import Path


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.rstrip()


def convert_line(names: str | Path, numbers: str | Path,\
                  results: str | Path) -> None:
    with (
        open('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\numbers.txt', 'r', encoding='utf-8') as f_numbers,
        open('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\names.txt', 'r', encoding='utf-8') as f_names,
        open('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\results.txt', 'a', encoding='utf-8') as f_results,
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_names, len_numbers)

        for _ in range(max_len):
            name = read_line_or_begin(f_names)
            nums_str = read_line_or_begin(f_numbers)
            num_i, num_f = map(float, nums_str.split('|'))
            multiply = num_i * num_f
            if multiply < 0:
                f_results.write(f'{name.lower()} {-multiply}\n')    
            elif multiply > 0:
                f_results.write(f'{name.upper()} {int(multiply)}\n')   


if __name__ == '__main__':
    convert_line(Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\numbers.txt'),
                 Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\names.txt'),
                 Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\results.txt'))
