import unittest, time, random

from lab2.task1.src.merge_sort_rewrite import merge_sort, get_memory_usage


def pr(num):
    print('-' * 30, num, "-" * 30)


class MyTestCase(unittest.TestCase):
    def test0(self):
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        first = merge_sort([1, 4, 3, 2, 5, 6], 0, 5)
        final_memory = get_memory_usage()
        self.assertEqual(first, [1, 2, 3, 4, 5, 6])
        pr('test0')
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr('test0')

    def test1(self):
        random_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(merge_sort(random_list, 0, len(random_list) - 1), sorted(random_list))
        final_memory = get_memory_usage()
        pr("test1")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test1")


if __name__ == '__main__':
    unittest.main()
