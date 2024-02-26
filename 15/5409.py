def div(n,m):
    return n%m==0


def f(x):
    return (div(a,25) and ((div(x,24) and div(x,75)) <= div(x,a)))


cnt = 0
for a in range(1,10000):
    if all(f(x) for x in range(1,100)):
        cnt += 1
print(cnt)