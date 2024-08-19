try:
    number = int(input("Введите целое число: "))
    hex_number = hex(number)
    print("Шестнадцатеричное представление числа:", hex_number[2:])
except ValueError:
    print("Ошибка: Пожалуйста, введите целое число.")
    