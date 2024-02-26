import sys
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n - 1)
cnt = 0
for n in range(1,101):
    if (f(2023) // f(n)) % 2 == 0:
        cnt += 1
print(cnt)