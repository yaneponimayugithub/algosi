import time, os, psutil

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)

initial_memory = get_memory_usage()
start_time = time.perf_counter()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

with open('../txtf/input.txt', 'r') as f:
    n = int(f.readline())
    M = list(map(float, f.readline().split()))

M_old = M[:]
M = insertion_sort(M)

min_man = M[0]
middle_man = M[n // 2]
max_man = M[-1]

min_index = M_old.index(min_man) + 1
middle_index = M_old.index(middle_man) + 1
max_index = M_old.index(max_man) + 1

with open('../txtf/output.txt', 'w') as f:
    f.write(f"{min_index} {middle_index} {max_index}")

end_time = time.perf_counter()
final_memory = get_memory_usage()

elapsed_time = end_time - start_time
memory_used = final_memory - initial_memory

print(f"Время сортировки: {elapsed_time:.6f} секунд")
print(f"Использование памяти: {memory_used:.8f} МБ")

