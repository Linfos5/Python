import math

choice = input("Что вы хотите ввести: радиус или диаметр? ")

if choice == "радиус":
    radius = float(input("Введите радиус круга: "))
    diameter = 2 * radius
elif choice == "диаметр":
    diameter = float(input("Введите диаметр круга: "))
    radius = diameter / 2
else:
    print("Ошибка ввода!")

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Длина окружности:", circumference)
print("Площадь круга:", area)
