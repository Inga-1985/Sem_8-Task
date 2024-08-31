# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.  
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.  

import os

def get_absolute_path(path_file):
    path, filename = os.path.split(path_file)
    name, extension = filename.split('.')
    return path, name, extension

if __name__ == '__main__':
    path = "D:\Обучение\Python_5\task_02.py"
    print(f"Абсолютный путь до файла: {path}")
    print(f"Кортеж из трёх элементов: {get_absolute_path(path)}")