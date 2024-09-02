# Решить задачи, которые не успели решить на семинаре, задача №2

# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, choice
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjkzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def random_names(filename: str | Path, count: int) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            name = ''
            cur_vowel = choice([-1, 1])
            for i in range(randint(MIN_LEN, MAX_LEN)):
                if cur_vowel < 0:
                    name += choice(VOWELS)
                else:
                    name += choice(CONSONANTS)
                cur_vowel *= -1
            print(name.title(), file=f)

if __name__ == '__main__':
    random_names(Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results\\names.txt'), 120)
