def swap_min_max_in_rows():
    n = int(input("Введите количество строк матрицы N: "))
    m = int(input("Введите количество столбцов матрицы M: "))
    matrix = []
    
    print("Введите элементы матрицы (строки через пробел):")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    for i in range(n):
        min_elem = min(matrix[i])
        max_elem = max(matrix[i])
        
        min_index = matrix[i].index(min_elem)
        max_index = matrix[i].index(max_elem)
        
        matrix[i][min_index], matrix[i][max_index] = matrix[i][max_index], matrix[i][min_index]
    
    print("Матрица после изменения:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    swap_min_max_in_rows()
