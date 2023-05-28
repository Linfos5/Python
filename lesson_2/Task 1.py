Day = 28
Month = 5
Year = 2023

Day_of_birth = int(input("Введите день своего рождения: "))
Month_of_birth = int(input("Введите месяц своего рождения: "))
Year_of_birth = int(input("Введите год своего рождения: "))

if Day_of_birth < 0:
    print("Ошибка: день не может быть отрицательным")
elif Day_of_birth > 31:
    print("Ошибка: день не может быть больше 31")

if Month_of_birth < 0:
    print("Ошибка: месяц не может быть отрицательным")
elif Month_of_birth > 12:
    print("Ошибка: месяц не может быть больше 12")

if Year - Year_of_birth - ((Month, Day) < (Month_of_birth, Day_of_birth)) < 18:
    print("Ошибка: тебе нет 18 лет")
else:
    print("Вход выполнен!")
