# Создайте функцию, которая создаёт файлы с указанным расширением.  
# Функция принимает следующие параметры:  
# 1. Расширение;    
# 2. Минимальная длина случайно сгенерированного имени, по умолчанию 6;   
# 3. Максимальная длина случайно сгенерированного имени, по умолчанию 30;    
# 4. Минимальное число случайных байт, записанных в файл, по умолчанию 256;    
# 5. Максимальное число случайных байт, записанных в файл, по умолчанию 4096;    
# 6. Количество файлов, по умолчанию 42.    
# Имя файла и его размер должны быть в рамках переданного диапазона.  

import random
import os

NAME_DIR = "files"
MIN_LETTER = ord('a')
MAX_LETTER = ord('z')

"""Генерирует случайное имя файла."""
def generate_text(length):   
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
    return "".join(name)

"""Генерирует файлы с заданными параметрами."""
def generate_files(extension:   str,
                   directory:   str,
                   min_length   = 6,
                   max_length   = 30,
                   min_bytes    = 256,
                   max_bytes    = 4096,
                   num_files    = 42):
    
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        filename = generate_text(name_length)
        text_length = random.randint(min_bytes, max_bytes)
        text = generate_text(text_length)
        while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break

def run(extension: str, directory: str):
    generate_files(extension, directory)