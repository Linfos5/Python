def sum_fib(n):
    c = 1
    p = 0
    s = 0
    while c < n:
        s += c
        c, p = p, c + p
    return s
       
print(sum_fib(int(input("Введите число: "))))    
