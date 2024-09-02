from files_pack import create_dir
from files_pack.homework import workhome01
from pathlib import Path
from files_pack.seminar import seminar01, seminar02, seminar03, seminar04, seminar05, seminar06

NAME_DIR = "files"

# Функция меню
def menu():
    dct = {"1": "Генерираци файл случайными числами. (Задача семинара №1)",
           "2": "Генерация псевдоимен. (Задача семинара №2)",
           "3": "Обработка файла из п.1 и п.2. (Задача семинара №3)",
           "4": "Генерирует файлы с заданными параметрами. (Задача семинара №4)",
           "5": "Генерирует файлы с разными расширениями. (Задача семинара №5)",
           "6": "Сортирует файлы. (Задача семинара №6)",
           "7": "Групповое переименование файлов. (Задача домашней работы №2)",
           "8": "Выйти из программы"}
    
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)

# Функция выбора меню
def select_an_operation(is_flag: bool):
    choice = "0"
    choice = input("Введите команду: ")

    if choice == "8":
        is_flag = False
        return is_flag
    
    if is_flag:
        file_name_task01 = "data.txt"
        file_name_task02 = "data_names.txt"
        file_name_task03 = "res.txt"
        extension_task04 = "rnd", 
        new_directory = "new_rnd"
        file_new_name = "wh", 
        extension_task07 = "rnd", 

        path_name = Path.cwd() / NAME_DIR
        count = 10
        if choice == "1":
            seminar01.run(count, path_name / file_name_task01)
        elif choice == "2":
            seminar02.run(count, path_name / file_name_task02)
        elif choice == "3":
            seminar03.run(path_name / file_name_task01, path_name / file_name_task02, path_name / file_name_task03)
        elif choice == "4":
            seminar04.run(extension_task04, path_name / new_directory)
        elif choice == "5":
            seminar05.run(path_name / new_directory)
        elif choice == "6":
            seminar06.run(path_name / new_directory)
        elif choice == "7":
            print(path_name)
            workhome01.run(file_new_name, extension_task07, path_name / new_directory)
        else:
            print("Неверная команда")
    return is_flag

def run():
    create_dir.run(NAME_DIR)
    is_flag = True
    while is_flag:
        menu()
        is_flag = select_an_operation(is_flag)
         
def main():
    run()

if __name__ == "__main__":
    main()