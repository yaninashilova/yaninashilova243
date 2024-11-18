import math

def calculate_area():
    print("Выберите фигуру для вычисления площади:")
    print("1. Круг")
    print("2. Прямоугольник")
    print("3. Треугольник")
    
    choice = int(input("Введите номер фигуры: "))
    
    if choice == 1:
        radius = float(input("Введите радиус круга: "))
        area = math.pi * radius ** 2
        print(f"Площадь круга: {area}")
        
    elif choice == 2:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = length * width
        print(f"Площадь прямоугольника: {area}")
        
    elif choice == 3:
        a = float(input("Введите длину первой стороны: "))
        b = float(input("Введите длину второй стороны: "))
        c = float(input("Введите длину третьей стороны: "))
        
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Площадь треугольника: {area}")
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    calculate_area()
