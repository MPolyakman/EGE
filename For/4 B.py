pervoe = int(input())
vtoroe = int(input())
if pervoe < vtoroe:
    for i in range(pervoe, vtoroe + 1):
        print(i)
else:
    for x in range(pervoe, vtoroe - 1,-1):
        print(x)