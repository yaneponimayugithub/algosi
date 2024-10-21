import time
import os
import psutil

def get_memory_usage():

    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)
#ДЕКОРАТОР
def measure_time_and_memory(func):
    def wrapper(*args, **kwargs):
        initial_memory = get_memory_usage()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        final_memory = get_memory_usage()
        print("------------------/ start /------------------")
        print(f"Время выполнения: {end_time - start_time:.6f} секунд")
        print(f"Использование памяти: {final_memory - initial_memory:.8f} МБ")
        print("------------------/ end /------------------")
        return result
    return wrapper

def read_input(file_path):

    with open(file_path, 'r') as f:
        n = int(f.readline())
        unlist = list(map(int, f.readline().split()))
    return n, unlist

def write_output(file_path, data):

    with open(file_path, 'w') as f:
        f.write(' '.join(map(str, str(data))))
