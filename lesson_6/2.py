num = input("Введите числа через пробел: ")
lst = num.split()
lst = [float(n) for n in lst]

odd = [n for n in lst if n % 2 != 0]
even = [n for n in lst if n % 2 == 0]

odd_even = odd+even

print(", ".join(str(n) for n in odd_even))
