# Решить задачи, которые не успели решить на семинаре, задача №5

# Доработка предыдущей задачи.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from Task4 import create_file as cf
from pathlib import Path



def generate_file(file_path: str | Path, **kwargs) -> None:
    for extension, amount in kwargs.items():
        cf(file_path, extension, count=amount)


if __name__ == '__main__':
    path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results')
    generate_file(path, bin=2, jpeg=3, txt=1)
