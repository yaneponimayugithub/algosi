import time
import os
import psutil

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)

initial_memory = get_memory_usage()
start_time = time.perf_counter()

def Majority(A):
    n = len(A)

    for i in range(n):
        current_element = A[i]
        count = 0

        for j in range(n):
            if A[j] == current_element:
                count += 1

        if count > n // 2:
            return current_element

    return None

with open('../txtf/input.txt', 'r') as f:
    n = int(f.readline())
    unlist = list(map(int, f.readline().split()))

if not (1 <= n <= 10**5):
    print('[Ошибка] количество элементов должно быть от 1 до 100.000!')
    exit(1)

for i in unlist:
    if abs(i) > 10 ** 9:
        print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
        exit(1)


majority_element = Majority(unlist)

end_time = time.perf_counter()
final_memory = get_memory_usage()
time_elapsed = end_time - start_time
memory_used = final_memory - initial_memory

if majority_element is not None:
    result = 1
else:
    result = 0

print(f"Время выполнения: {time_elapsed:.6f} секунд")
print(f"Использование памяти: {memory_used:.8f} МБ")

# Записываем результат в файл
with open('../txtf/output.txt', 'w') as f:
    f.write(str(result))
