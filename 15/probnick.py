a = set(range(1,1000))
p = {2,4,6,8,10,12,14,16,18,20}
q = {3,6,9,12,15,18,21,24,27,30}
for x in range(1,1000):
    if (((x in a)<=(x in p))and((not(x in q))<=(not(x in a)))) == False:
        a.remove(x)
print(a,len(a))