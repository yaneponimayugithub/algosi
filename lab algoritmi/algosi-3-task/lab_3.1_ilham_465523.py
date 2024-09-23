a = open('input.txt', 'r')
b = a.read()
a.close()

b = int(b)

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

if b < 0 or b > 10**7:
    print("Диапазон чисел нарушен")
else:
    m = open('output.txt', 'w')
    m.write(str(fibonacci(b) % 10))
    m.close()
