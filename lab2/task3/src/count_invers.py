from lab2.utils import *


def merge_and_count(arr, L, mid, R):
    left_part = arr[L:mid + 1]
    right_part = arr[mid + 1:R + 1]

    i = 0
    j = 0
    k = L
    inversions = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            inversions += (len(left_part) - i)
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inversions


def merge_sort_and_count(arr, L, R):
    inversions = 0
    if L < R:
        mid = (L + R) // 2
        inversions += merge_sort_and_count(arr, L, mid)
        inversions += merge_sort_and_count(arr, mid + 1, R)
        inversions += merge_and_count(arr, L, mid, R)
    return inversions


with open('../txtf/input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))


@measure_time_and_memory
def task():
    n, unlist = read_input('../txtf/input.txt')
    if not (1 <= n < 10 ** 5):
        print('[Ошибка] количество элементов должно быть от 1 до 100.000!')
        exit(1)
    for num in arr:
        if abs(num) > 10 ** 9:
            print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
            exit(1)

    inversion_count = merge_sort_and_count(arr, 0, n - 1)
    write_output('../txtf/output.txt', inversion_count)
    print(f"Число инверсий: {inversion_count}")

task()