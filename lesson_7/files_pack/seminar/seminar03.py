# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.  
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:  
# 1. Если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю;  
# 2. Если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.  
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.  
# При достижении конца более короткого файла, возвращайтесь в его начало.  

from pathlib import Path

NAME_DIR = "files"

"""Прочитать строку или продолжить."""
def read_line_or_begin(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]

"""Обработка файла."""
def process_files(file_numbers, file_names, file_res):
    with open(file_numbers, 'r', encoding='utf-8') as f_num:
        with open(file_names, 'r', encoding='utf-8') as f_names:
            with open(file_res, 'w', encoding='utf-8') as f_res:
                length1 = len(f_num.readlines())
                length2 = len(f_names.readlines())
                length = max(length1, length2)
                for i in range(length):
                    line_num = read_line_or_begin(f_num)
                    line_name = read_line_or_begin(f_names)
                    a, b = line_num.split('|')
                    a = int(a)
                    b = float(b)
                    res = a * b
                    if res < 0:
                        res *= -1
                        line_name = line_name.lower()
                    else:
                        res = round(res)
                        line_name = line_name.upper()
                    f_res.write(f'{line_name} {res}')
                    f_res.write('\n' if i < length - 1 else "")


def run(file_numbers: str, file_names: str, file_res: str):
    process_files(file_numbers, file_names, file_res)