def sum_and_count_positive_elements_above_diagonal():
    n = int(input("Введите размерность матрицы N: "))
    matrix = []
    
    print("Введите элементы матрицы (строки через пробел):")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    positive_sum = 0
    positive_count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                positive_sum += matrix[i][j]
                positive_count += 1
    
    print(f"Сумма положительных элементов над главной диагональю: {positive_sum}")
    print(f"Количество положительных элементов: {positive_count}")

if __name__ == "__main__":
    sum_and_count_positive_elements_above_diagonal()
