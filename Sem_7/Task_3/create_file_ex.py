from create_file import create_file as cf
from pathlib import Path

__all__ = ['generate_file']


def generate_file(file_path: str | Path, **kwargs) -> None:
    for extension, amount in kwargs.items():
        cf(file_path, extension, count=amount)


if __name__ == '__main__':
    path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_1\\Results')
    generate_file(path, bin=2, jpeg=3, txt=1)
