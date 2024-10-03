import time, os, psutil
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)

initial_memory = get_memory_usage()
start_time = time.perf_counter()
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

with open('input.txt', 'r') as f:
    n = int(f.readline())
    unsorted_base = list(map(int,f.readline().split()))
#ПРОВЕРКИ
if 1 <= n <= 1000:
    pass
else:
    print('[Ошибка] Количество элементов должно быть от 1 до 1000!')
    exit(2)

if len(unsorted_base) != n:
    print('[Ошибка] Количество элементов и введенное число элементов не совпадает!')
    exit(3)

for i in unsorted_base:
    if abs(4) > 10**9:
        print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
        exit(1)
#ПРОВЕРКИ

sorted_base = selection_sort(unsorted_base)

end_time = time.perf_counter()
final_memory = get_memory_usage()
time = end_time - start_time
memory_used = final_memory - initial_memory
print(f"Время сортировки: {time:.6f} секунд")
print(f"Использование памяти: {memory_used:.8f} МБ")



with open('output.txt', 'w') as f:
    f.write(' '.join(map(str,sorted_base)))