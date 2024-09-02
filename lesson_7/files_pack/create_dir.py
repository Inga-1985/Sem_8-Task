from pathlib import Path

"""Создание директории для сохранения файлов."""
def new_create_dir(name_dir: str):
    name = Path(
        Path.cwd() / name_dir) 
    if not name.exists(): 
        name.mkdir() 

def run(name_dir: str):
    new_create_dir(name_dir)

if __name__ == '__main__':
    run("files")