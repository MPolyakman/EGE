#34722222
#45138887
for n in range(34722222,34722222+1):
    r = bin(n)[2:]
    r = r + bin(n%3)[2:].rjust(2,'0')
    r = r + bin(int(r,2)%5)[2:].rjust(3,'0')
    print(n,int(r,2))
# n = int((bin(1_444_444_416)[2:-5]),2)
# print(n)
print(45138887-34722223+1)