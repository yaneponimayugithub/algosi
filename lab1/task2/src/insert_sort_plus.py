import time, os, psutil
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)

initial_memory = get_memory_usage()
start_time = time.perf_counter()
def insertion_sort_plus(arr):
    sp_ind = [0] * len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        sp_ind[i] = j + 1
    sp_ind = [index+1 for index in sp_ind]
    return arr, sp_ind

with open('../txtf/input.txt', 'r') as f:
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

sorted_base, indexes = insertion_sort_plus(unsorted_base)

end_time = time.perf_counter()
final_memory = get_memory_usage()
time = end_time - start_time
memory_used = final_memory - initial_memory
print(f"Время сортировки: {time:.6f} секунд")
print(f"Использование памяти: {memory_used:.8f} МБ")


with open('../txtf/output.txt', 'w') as f:
    f.write(' '.join(map(str,indexes))+'\n')
    f.write(' '.join(map(str,sorted_base)))