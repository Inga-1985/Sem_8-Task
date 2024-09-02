# Доработаем предыдущую задачу.  
# Создайте новую функцию которая генерирует файлы с разными расширениями.  
# Расширения и количество файлов функция принимает в качестве параметров.  
# Количество переданных расширений может быть любым.  
# Количество файлов для каждого расширения различно.  
# Внутри используйте вызов функции из прошлой задачи.  

from lesson_7.files_pack.seminar import seminar04

"""Генерирует файлы с разными расширениями."""
def generate_with_dictionary(new_directory, dictionary: dict):
    for key, value in dictionary.items():
        seminar04.generate_files(key, new_directory, num_files=value)

def run(new_directory: str):
    d = {
        'doc': 5,
        'jpg': 10,
        'png': 23,
        'txt': 15,
    }
    generate_with_dictionary(new_directory, d)