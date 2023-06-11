fact1 = 1
fact2 = 1000
n = 1
i = 0

while fact1 <= fact2:
    if n > 1:
        print(fact1, "=", str(i) + "!")
    fact1 *= n
    n += 1
    i += 1
