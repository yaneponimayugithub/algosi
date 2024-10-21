from lab2.utils import *


def majority(A):
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

if not (1 <= n <= 10 ** 5):
    print('[Ошибка] количество элементов должно быть от 1 до 100.000!')
    exit(1)

for i in unlist:
    if abs(i) > 10 ** 9:
        print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
        exit(1)

majority_element = majority(unlist)

if majority_element is not None:
    result = 1
else:
    result = 0


@measure_time_and_memory
def task():
    n, unlist = read_input('../txtf/input.txt')
    if not (1 <= n <= 10 ** 5):
        print('[Ошибка] количество элементов должно быть от 1 до 100.000!')
        exit(1)

    for i in unlist:
        if abs(i) > 10 ** 9:
            print('[Ошибка] Числа должны быть не больше 10**9 по модулю!')
            exit(1)
    majority_element = majority(unlist)

    if majority_element is None:
        result = 0
    else:
        result = 1

    write_output('../txtf/output.txt', result)


task()
