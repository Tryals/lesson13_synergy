import random

def create_matrix(rows, cols, min_val=-50, max_val=50):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def print_matrix(matrix, name="Матрица"):
    print(f"\n{name} ({len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(row)

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

min_val = int(input("Введите минимальное значение для случайных чисел: "))
max_val = int(input("Введите максимальное значение для случайных чисел: "))

matrix1 = create_matrix(rows, cols, min_val, max_val)
matrix2 = create_matrix(rows, cols, min_val, max_val)

print_matrix(matrix1, "Матрица 1")
print_matrix(matrix2, "Матрица 2")

matrix3 = add_matrices(matrix1, matrix2)
print_matrix(matrix3, "Сумма матриц (Матрица 3)")