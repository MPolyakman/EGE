from itertools import*
def f(x, y, z, w):
    return (((x <= y) or (z <= w )) and (not(x <= w)))
for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tabs = [(1,0,1, a1), (1, a2, a3, 1), (a4, a5, 1, 0)]
    if len(tabs) == len(set(tabs)):
        for order_of_letters in permutations('xyzw'):
            if [f(**dict(zip(order_of_letters,tab))) for tab in tabs] == [0, 1, 1]:
                print(order_of_letters)
