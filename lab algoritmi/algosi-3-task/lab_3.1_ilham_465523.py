a = open('input.txt')
b = a.read()
b = int(b)
a.close()
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
if b < 0 or b > 10**7:
    print("Диапазон чисел нарушен")
else:
    m = open('output.txt', 'w')
    m.write(str(fibonacci(b))[-1])
    m.close()