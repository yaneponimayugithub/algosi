import time, os, psutil


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)


initial_memory = get_memory_usage()
start_time = time.perf_counter()


def merge_nofl(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + 1 + j]

    i, j, k = 0, 0, p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:  # Копируем оставшиеся элементы L, если есть
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:  # Копируем оставшиеся элементы R, если есть
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge_nofl(A, p, q, r)
    return A


with open('../txtf/input.txt', 'r') as f:
    n = int(f.readline())
    unlist = list(map(int, f.readline().split()))

if not (1 <= n <= 2 * 10 ** 4):
    print('[Ошибка] количество элементов должно быть от 1 до 20.000!')
    exit(1)

for i in unlist:
    if abs(i) > 10 ** 9:
        print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
        exit(1)

merge_sort(unlist, 0, n - 1)

end_time = time.perf_counter()
final_memory = get_memory_usage()
time = end_time - start_time
memory_used = final_memory - initial_memory

print(f"Время сортировки: {time:.6f} секунд")
print(f"Использование памяти: {memory_used:.8f} МБ")

with open('../txtf/output.txt', 'w') as f:
    f.write(' '.join(map(str, unlist)))
