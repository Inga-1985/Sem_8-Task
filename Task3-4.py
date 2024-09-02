# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.  
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.   
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.  
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.  

# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.  

import random

def is_queen_beat(position: list[list[int]]):
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True
    else:
        return False

def generate_queens(n):
    board_list = []
    for i in range(n):
        queens = []
        while len(queens) < n:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if [x, y] not in queens:
                queens.append([x, y])
        board_list.append(queens)
    return board_list

def run():
    result = is_queen_beat([[1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]])
    print(f"Ферзи не бьют друг друга? ", result)
    result = generate_queens(4)
    print(f"Успешные расстановки ферзей: ", result)

if __name__ == "__main__":
    run()