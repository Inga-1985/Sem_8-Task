# Напишите функцию группового переименования файлов. Она должна:
# 1. Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер;  
# 2. Принимать параметр количество цифр в порядковом номере;  
# 3. Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога;    
# 4. Принимать параметр расширение конечного файла;  
# 5. Принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
#    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path

def group_rename_files(new_name: str, ext_renamed: str, work_path: str):
    ext_new: str = None
    saved_range: range = (3, 6)
    if ext_new is None:
        ext_new = ext_renamed
    count_renamed = 0
    for p in work_path.iterdir():
        if p.is_file() and p.suffix == f".{ext_renamed}":
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{count_renamed:03}{ext_new}"
            p.rename(Path(p.parent, file_name))
            count_renamed += 1

def run(file_new_name: str, extension: str, work_path: str):
    group_rename_files(file_new_name, extension, work_path)