def matrix_transpositions(matrix):
    # Напишите функцию для транспонирования матрицы
    
    # Создаем транспонированную матрицу с правильными размерами
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    # Заполняем транспонированную матрицу
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [9, 8, 7, 6],
              [1, 4, 7, 0],
              [5, 5, 5, 5]]
    
    print(f"Изначальная матрица: ")
    for row in matrix:
        print(row)
        
    transposed = matrix_transpositions(matrix)
    print(f"Транспонированная матрица: ")
    for row in transposed:
        print(row)