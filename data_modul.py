import sys

def _is_leap(year: int) -> bool:
    """Проверка, является ли год високосным."""
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def check_date(full_date: str) -> bool:
    """Проверка корректности заданной даты в формате DD.MM.YYYY."""
    day, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2 and day > 29:
        return False
    elif month == 2 and day == 29 and not _is_leap(year):
        return False
    else:
        return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py DD.MM.YYYY")
    else:
        date_input = sys.argv[1]
        if check_date(date_input):
            print(f"Дата '{date_input}' корректна.")
        else:
            print(f"Дата '{date_input}' некорректна.")

#python data_modul.py 02.09.2024
#Дата '02.09.2024' корректна.