def replace_zeros_with_average():
    n = int(input("Введите количество элементов массива: "))
    arr = list(map(float, input("Введите элементы массива через пробел: ").split()))

    average = sum(arr) / len(arr)
    
    arr = [average if x == 0 else x for x in arr]
    
    print(f"Массив после замены нулевых элементов: {arr}")

if __name__ == "__main__":
    replace_zeros_with_average()
