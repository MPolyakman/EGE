def f (n):
    if n < 2:
        return n
    if n >= 2:
        return f(n // 2) + f(n % 2)

cnt = 0
for n in range(1,2**30):
    if f(n) == 27:
        cnt += 1
print(cnt)
