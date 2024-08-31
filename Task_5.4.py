# Создайте функцию генератор чисел Фибоначчи  
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8    

def fibonacci(n):
    current, after = 0, 1
    for i in range(n):
        yield current
        current, after = after, current + after

if __name__ == '__main__':
    n = int(input("Введите число: "))
    if n < 0:
        print("Введите положительное число.")
    else:
        print(f"Результат: {list(fibonacci(n))} ")