from pathlib import Path
from search_directory import directory_reference

def run():
    directory_reference(Path(Path.cwd()))

if __name__ == '__main__':
    run()