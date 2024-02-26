def f (n):
    if n == 0:
        return 1
    if n > 0:
        return 7*(n - 1) + f(n - 1)

def simple(k):
    for d in range (2, k):
        if k % d == 0:
            return False
    else:
        return True
cnt = 0
for i in range(2,201):
    if simple(f(i)):
        cnt += 1
print(cnt)