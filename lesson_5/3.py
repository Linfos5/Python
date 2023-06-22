def fib_sum(n):
    s = 0
    a, b = 0, 1
    i = 0
    while i < n:
        s += b
        a, b = b, a + b
        i += 1
    return s

print(fib_sum(int(input("Количество фибоначчи: "))))
