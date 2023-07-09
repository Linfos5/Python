import random
import time

start_time = time.time()

for _ in range(1000000):
    base = random.randint(1000000, 10000000)
    degree = random.randint(1, 100)
    result = base ** degree

end_time = time.time()

execution_time = end_time - start_time 
print(f"Программа выполнилась за {execution_time} секунд")
