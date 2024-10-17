f = open('input.txt', 'r')
a =  f.read()
a = a.split(" ")
a[0],a[1]=int(a[0]),int(a[1])
f.close()
if a[0] > 10 ** 9 or a[0] < -10 ** 9 or a[1] > 10 ** 9 or a[1] < -10 ** 9:
    print("число должно быть в диапазоне от -10^9 до 10^9")
else:
    a = a[0] + a[1]**2
    a = str(a)
    z = open('output.txt', 'w')
    z.write(a)
    z.close()