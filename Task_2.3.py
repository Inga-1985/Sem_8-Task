from fractions import Fraction

def calculate_fraction_sum_and_product(fraction1, fraction2):
    # Разделяем входные дроби на числитель и знаменатель
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    # Создаем объекты Fraction и вычисляем сумму и произведение
    fraction_sum = Fraction(num1, den1) + Fraction(num2, den2)
    fraction_product = Fraction(num1, den1) * Fraction(num2, den2)

    return fraction_sum, fraction_product

# Ввод от пользователя
fraction1 = input("Введите первую дробь (в формате 'a/b'): ")
fraction2 = input("Введите вторую дробь (в формате 'a/b'): ")

# Вычисляем сумму и произведение дробей
result_sum, result_product = calculate_fraction_sum_and_product(fraction1, fraction2)

# Выводим результаты
print("Сумма дробей:", result_sum)
print("Произведение дробей:", result_product)