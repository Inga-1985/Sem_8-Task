from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path

__all__ = ['create_file']

def create_file(file_path: str | Path, extension: str, min_len: int = 6, max_len: int = 30,\
        min_size: int = 256, max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k = randint(min_len, max_len))) + f'.{extension}'
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(file_path / file_name, 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results')
    create_file(path, 'txt', count = 2)
