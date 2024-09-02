# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени
# файла. К ним прибавляется желаемое конечное имя, если оно передано. 
# Далее счётчик файлов и расширение.

#-----------
# Вариант №1
#-----------

# from pathlib import Path


# def group_rename_files(new_end_file_name: str, ext_renamed: str, 
#                        count_dig: int, saved_range: range, ext_new: str = None, path: str = None) -> int:
    
#     """
#     new_end_file_name - Задаёт конечное имя файла.
#     count_dig - Количество цифр в порядковом номере.
#     ext_renamed - Принимает параметр расширения изменяемого файла, файлы установленого расширения будут переименованы.
#     ext_new - принимает параметр нового расширения для изменяемых файлов, если не указан параметр, сохраняется оригинальное расширение файла.
#     saved_range - принимает диапазон символов для сохранения оригинального имени.
#     path - принимает путь к папке, где будет проходить изменение файлов; если путь не указан, будет использоваться рабочий каталог.
#     count_renamed - Определяет начало отсчёта, счётчика файлов.
#     """

#     path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_2\\Rename_test')
#     count_renamed = 1

#     if ext_new is None:
#         ext_new = ext_renamed
    
#     work_path = Path.cwd() if path is None else Path(path)

#     for p in work_path.iterdir():
#         if p.is_file() and p.suffix == ext_renamed:
#             file_name = f"{p.stem[saved_range[0]:saved_range[1]]}_{new_end_file_name}_{count_renamed:0{count_dig}}{ext_new}"
#             p.rename(Path(p.parent, file_name))
#             count_renamed += 1

#     return count_renamed


# if __name__ == '__main__':
#     group_rename_files(new_end_file_name="test", count_dig=2, ext_renamed=".txt", ext_new=None, saved_range=(3, 6))

#-----------
# Вариант №2
#-----------

from pathlib import Path


def group_rename_files(new_end_file_name: str, count_dig: int, ext_renamed: str, ext_new: str='', saved_range: range=(0, -1), path: str=None) -> int:
    
    """
    new_end_file_name - Задаёт конечное имя файла.
    count_dig - Количество цифр в порядковом номере.
    ext_renamed - Принимает параметр расширения изменяемого файла, файлы установленого расширения будут переименованы.
    ext_new - принимает параметр нового расширения для изменяемых файлов, если не указан параметр, сохраняется оригинальное расширение файла.
    saved_range - принимает диапазон символов для сохранения оригинального имени.
    path - принимает путь к папке, где будет проходить изменение файлов; если путь не указан, будет использоваться рабочий каталог.
    count_renamed - Определяет начало отсчёта, счётчика файлов.
    """
    
    path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_2\\Rename_test') if path is None else Path(path)
    
    file_list = [file for file in path.iterdir() if file.name.endswith(ext_renamed) and file.is_file()]

    if not file_list:
        print(f"No files with the extension '{ext_renamed}' found in the directory.")
        return

    count_renamed = 1

    for file in file_list:
        original_name, ext = file.stem, file.suffix
        if saved_range[1] == -1:
            new_name = f"{original_name[saved_range[0]:]}_{new_end_file_name}_{count_renamed:0{count_dig}d}{ext_new or ext_renamed}"
        else:
            new_name = f"{original_name[saved_range[0]:saved_range[1]+1]}_{new_end_file_name}_{count_renamed:0{count_dig}d}{ext_new or ext_renamed}"
        
        new_path = path.joinpath(new_name)
        file.rename(new_path)
        count_renamed += 1


if __name__ == '__main__':
    group_rename_files("test", 3, ".txt", ".doc", (3, 6))
