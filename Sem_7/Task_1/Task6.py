# Решить задачи, которые не успели решить на семинаре, задача №6

# Добавьте функции из предыдущих задач.
# Генерируйте файлы в указанную директорию - отдельный параметр функции.
# Отсуствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте/проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения
# имён.

from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
from os import chdir


def create_file(file_path: str | Path, extension: str, min_len: int = 6, max_len: int = 30,\
        min_size: int = 256, max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        print(Path.cwd())
        while True:
            file_name = ''.join(choices(ascii_lowercase + digits + '_', k = randint(min_len, max_len))) + f'.{extension}'
            if not Path(file_name).is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(file_path / file_name, 'wb') as f:
            f.write(data)


def generate_file(file_path: str | Path, **kwargs) -> None:
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.is_dir():
        file_path.mkdir(parents=True)    
    chdir(file_path)
    for extension, amount in kwargs.items():
        create_file(file_path, extension, count=amount)


if __name__ == '__main__':
    path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results')
    generate_file(path / 'new', txt=1)
