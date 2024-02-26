from fnmatch import*
for n in range(1,100_000):
    n = n**2
    if fnmatch(str(n),'1?2*4') and n%2024==0:
        print(n,n//2024)
