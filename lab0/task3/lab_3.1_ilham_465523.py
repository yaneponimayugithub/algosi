a = open('input.txt', 'r')
b = a.read()
a.close()

b = int(b)

def fibonacci(number):
    if number <= 1:
        return number
    a, b = 0, 1
    for _ in range(2, number + 1):
        a, b = b, b+a
    return b

if b < 0 or b > 10**7:
    print("Диапазон чисел нарушен")
else:
    m = open('output.txt', 'w')
    m.write(str(fibonacci(b) % 10))
    m.close()
