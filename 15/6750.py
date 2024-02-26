def div(x,n):
    if x%n == 0:
        return True
    return False


def f (x,a):
    return (div(x,10) and div(x,26) and (x>=300)) <= (a<=x)


for a in reversed(range(1,1000)):
    if all(f(x,a) == 1 for x in range(1,1000)):
        print(a)
        break