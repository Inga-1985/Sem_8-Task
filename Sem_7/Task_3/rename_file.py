from pathlib import Path

__all__ = ['group_rename_files']


def group_rename_files(new_end_file_name: str, ext_renamed: str, 
                       count_dig: int, saved_range: range, ext_new: str = None, path: str = None) -> int:
    
    """
    new_end_file_name - Задаёт конечное имя файла.
    count_dig - Количество цифр в порядковом номере.
    ext_renamed - Принимает параметр расширения изменяемого файла, файлы установленого расширения будут переименованы.
    ext_new - принимает параметр нового расширения для изменяемых файлов, если не указан параметр, сохраняется оригинальное расширение файла.
    saved_range - принимает диапазон символов для сохранения оригинального имени.
    path - принимает путь к папке, где будет проходить изменение файлов; если путь не указан, будет использоваться рабочий каталог.
    count_renamed - Определяет начало отсчёта, счётчика файлов.
    """

    path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#7\\Task_2\\Rename_test')
    count_renamed = 1

    if ext_new is None:
        ext_new = ext_renamed
    
    work_path = Path.cwd() if path is None else Path(path)

    for p in work_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}_{new_end_file_name}_{count_renamed:0{count_dig}}{ext_new}"
            p.rename(Path(p.parent, file_name))
            count_renamed += 1

    return count_renamed


if __name__ == '__main__':
    group_rename_files(new_end_file_name="test", count_dig=2, ext_renamed=".txt", ext_new=None, saved_range=(3, 6))
