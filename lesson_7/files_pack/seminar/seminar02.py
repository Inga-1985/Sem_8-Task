# Напишите функцию, которая генерирует псевдоимена. 
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
# среди которых обязательно должны быть гласные. 
# Полученные имена сохраните в файл.

import random as rn

NAME_DIR = "files"
MAX_LEN = 7
MIN_LEN = 4
MIN_LETTER = ord('a')
MAX_LETTER = ord('z')
VOWELS = {'a','o','y','i','u','e'}

"""Генерация псевдоимен."""
def generate_name_file(count_name: int, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        for j in range(count_name):
            len_name = rn.randint(MIN_LEN, MAX_LEN)
            name = []
            for i in range(len_name):
                name.append(chr(rn.randint(MIN_LETTER, MAX_LETTER)))
            has_vowels = False
            for letter in name:
                if letter in VOWELS:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = rn.randint(0, len_name-1)
                letter = rn.choice(list(VOWELS))
                name[ind] = letter
            print(f'{"".join(name).capitalize()}', file=f, end='')
            f.write('\n' if j < count_name - 1 else "")

def run(count_name: int, filename: str):
    generate_name_file(count_name, filename)