import unittest, time, random

from lab2.task3.src.count_invers import merge_sort_and_count, get_memory_usage


def pr(num):
    print('-' * 30, num, "-" * 30)


class MyTestCase(unittest.TestCase):
    def test0(self):
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        first = merge_sort_and_count([1, 4, 3, 2, 5, 6], 0, 5)
        final_memory = get_memory_usage()
        self.assertEqual(first, 3)
        pr('test0')
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr('test0')

    def test1(self):
        random_list = [5, 4, 1, 3, 8, 7]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(merge_sort_and_count(random_list, 0, len(random_list) - 1), 6)
        final_memory = get_memory_usage()
        pr("test1")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test1")


if __name__ == '__main__':
    unittest.main()
