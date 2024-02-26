n = int(input())
delitel = 2
while delitel <= n:
    if n % delitel == 0:
        print(delitel)
        break
    delitel += 1