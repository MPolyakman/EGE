file = open('9-226.txt')
for stroka in file:
    a = [int(x) for x in stroka.split()]
    b = [x for x in a if a.count(x)==2]
    c = [x for x in a if a.count(x)==1]
    if len(b)==4 and len(c)==3 and a.count(max(a)) == 1:
        print(sum(a))
        break
