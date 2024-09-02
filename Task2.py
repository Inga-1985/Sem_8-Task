# В модуль с проверкой даты добавьте возможность запуска 
# в терминале с передачей даты на проверку.

from sys import argv
from data_modul import cheak_date as cy

if __name__ == '__main__':
    if len(argv) != 2:
        print("Use console comand: python Task2.py dd.mm.yyyy")
    else:
        date_input = str(argv[1])
        try:
            day, month, year = map(int, date_input.split('.'))
            full_date = f'{day:02d}.{month:02d}.{year}'
            result = cy(full_date)
            if result:
                print(f"{full_date} is a leap year.")
            else:
                print(f"{full_date} is not a leap year.")
        except ValueError:
            print("Error: Enter the format dd.mm.yyyy.")