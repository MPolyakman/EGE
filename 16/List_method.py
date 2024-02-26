import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 1
    if n >1:
        return n**2 +f(n-1)


print(f(2023)-f(2019))
# Работает

f = [0]*3000
for n in range(1,len(f)):
    if n == 1:
        f[n] = 1
    if n>1:
        f[n] = n**2 + f[n-1]
print(f[2023]-f[2019])

f = [0]*50
for n in range(1,50):
    if n < 3:
        f[n] = 1
    elif n > 2 and n%2==1:
        f[n] = f[n-1]+f[n-2]
    elif n > 2 and n%2==0:
        f[n] = sum(f[:n])
print(f[24])
