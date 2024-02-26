def f(n):
    if n <2:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n/2) + 1
    if n >= 2 and n % 2 == 1:
        return f(n-3) + 3

for n in range (1000):
    if f(n) == 31:
        print(n, f(n))
        break
