a = [1,2,3,3,'1234']
b = (1,'asdf', 1.12)
c = []
print(c)
for i in range(1,1025):
    if 1024%i == 0:
        c.append(i)
print(c)
print(min(c))
print(max(c))
print(len(c))
print(c.count(32))
c.insert(3,0)
print(c)
c.pop(3)
print(c)
s = [433243,5,888,123,90]
s.sort()
print(s)
sp = []
for i in range(1,11):
    sp.append(i)
print(sp)
sp2 = [i for i in range (1,11)]
print(sp2)
sp3 = [i for i in range (1,101)
       if i % 3 == 0 and i % 7 == 0]
print(sp3)