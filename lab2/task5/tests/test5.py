import unittest, time, random

from lab2.task5.src.majority_code import Majority, get_memory_usage


def pr(num):
    print('-' * 30, num, "-" * 30)


class MyTestCase(unittest.TestCase):
    def test0(self):
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        first = Majority([1, 4, 3, 2, 5, 6])
        final_memory = get_memory_usage()
        self.assertEqual(first, None)
        pr('test0')
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr('test0')

    def test1(self):
        random_list = [5, 4, 1, 3, 8, 7, 7, 7, 7, 7, 7]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(Majority(random_list), 7)
        final_memory = get_memory_usage()
        pr("test1")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test1")

    def test2(self):
        random_list = [1, 3, 4, 7, 3, 6, 8, 9, 1, 3, 7, 4, 7, 6, 6, 6]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(Majority(random_list), None)
        final_memory = get_memory_usage()
        pr("test2")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test2")

    def test3(self):
        random_list = [6, 1, 3, 6, 4, 6, 6, 6, 7, 3, 6, 8, 6, 9, 6, 1, 3, 6, 6, 7, 4, 7, 6, 6, 6, 5, 6, 6, 3, 6, 5, 6]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(Majority(random_list), 6)
        final_memory = get_memory_usage()
        pr("test3")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test3")


if __name__ == '__main__':
    unittest.main()
