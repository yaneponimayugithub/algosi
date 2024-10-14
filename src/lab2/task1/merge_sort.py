import time
import os
import psutil


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)


initial_memory = get_memory_usage()
start_time = time.perf_counter()


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + 1 + j]

    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


with open('input.txt', 'r') as f:
    n = int(f.readline())
    unlist = list(map(int, f.readline().split()))

if not (1 <= n <= 2 * 10 ** 4):
    print('[Ошибка] количество элементов должно быть от 1 до 20.000!')
    exit(1)

for i in unlist:
    if abs(i) > 10 ** 9:
        print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
        exit(1)

# Выполняем сортировку
sorted_list = merge_sort(unlist, 0, n - 1)

end_time = time.perf_counter()
final_memory = get_memory_usage()
time = end_time - start_time
memory_used = final_memory - initial_memory

print(f"Время сортировки: {time:.6f} секунд")
print(f"Использование памяти: {memory_used:.8f} МБ")

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_list)))
