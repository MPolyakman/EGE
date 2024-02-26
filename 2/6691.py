from itertools import*
def f(x, y, z, w):
    return (z == (not(y))) and ((not(x)) or y) and w


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tabs = [(1,a1,a2, 0), (0, 0, a3, 1), (a4, a5, a6, 1)]
    if len(tabs) == len(set(tabs)):
        for order_of_letters in permutations('xyzw'):
            if [f(**dict(zip(order_of_letters,tab))) for tab in tabs] == [1, 1, 1]:
                print(order_of_letters)
