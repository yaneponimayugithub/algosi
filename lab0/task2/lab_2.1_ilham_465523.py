import time
t_start = time.perf_counter()
f0=0
f1=1
f = open('input.txt')
n = f.read()
f.close()
n = int(n)
if n < 0 or n > 45 :
    print("[Ошибка] Число должно быть не меньше 0 и не больше 45!")
else:
    def fibonacci(number):
        if number <= 1:
            return number
        a, b = 0, 1
        for _ in range(2, number + 1):
            a, b = b, b + a
        return b
    file = open('output.txt', 'w')
    file.write(str(fibonacci(n)))
    file.close()
print("В секундах" , (time.perf_counter() - t_start))