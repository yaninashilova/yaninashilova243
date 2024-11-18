def calculate_sum_and_average():
    arrays = []
    for i in range(1, 4):
        arr = list(map(int, input(f"Введите элементы массива {i} через пробел: ").split()))
        arrays.append(arr)
    
    for i, arr in enumerate(arrays, 1):
        total_sum = sum(arr)
        average = total_sum / len(arr)
        print(f"Массив {i}: Сумма = {total_sum}, Среднее арифметическое = {average}")

if __name__ == "__main__":
    calculate_sum_and_average()
