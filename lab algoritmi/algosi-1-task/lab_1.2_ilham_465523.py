a, b = map(int ,input().split())
if a > 10**9 or a < -10**9 or b > 10**9 or b < -10**9:
    print("число должно быть в диапазоне от -10^9 до 10^9")
else:
    print(a+b**2)
