import unittest, random, time

from lab1.task1.src.insertion_sort import insertion_sort, get_memory_usage
def pr(num):
    print('-'*30,num,"-"*30)

class MyTestCase(unittest.TestCase):
    def test0(self):
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        first = insertion_sort([1, 4, 3, 2, 5, 6])
        final_memory = get_memory_usage()
        self.assertEqual(first, [1, 2, 3, 4, 5, 6])
        pr('test0')
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr('test0')

    def test1(self):
        random_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
        t_start = time.perf_counter()
        initial_memory = get_memory_usage()
        self.assertEqual(insertion_sort(random_list), sorted(random_list))
        final_memory = get_memory_usage()
        pr("test1")
        print(f"Время работы: {time.perf_counter() - t_start:.8f} секунд")
        print(f"Память: {final_memory - initial_memory:.8f} МБ \n")
        pr("test1")


if __name__ == '__main__':
    unittest.main()
