import unittest, time

from lab1.task2.src.insert_sort_plus import insertion_sort_plus, get_memory_usage
def pr(num):
    print('-'*30,num,"-"*30)

class MyTestCase(unittest.TestCase):
    def test0(self):
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        first = insertion_sort_plus([1, 4, 3, 2, 5, 6])
        final_memory = get_memory_usage()
        self.assertEqual(first, ([1, 2, 3, 4, 5, 6], [1, 2, 2, 2, 5, 6]))
        pr('test0')
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr('test0')

    def test1(self):
        random_list = [2, 3, 1, -5, 8 ,123]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(insertion_sort_plus(random_list),([-5, 1, 2, 3, 8, 123], [1, 2, 1, 1, 5, 6]))
        final_memory = get_memory_usage()
        pr("test1")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test1")


if __name__ == '__main__':
    unittest.main()
