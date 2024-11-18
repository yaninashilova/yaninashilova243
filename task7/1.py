def find_max_and_reverse_array():
    n = int(input("Введите количество элементов массива: "))
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
    max_element = max(arr)
    
    reversed_arr = arr[::-1]
    
    print(f"Максимальный элемент массива: {max_element}")
    print(f"Массив в обратном порядке: {reversed_arr}")

if __name__ == "__main__":
    find_max_and_reverse_array()
