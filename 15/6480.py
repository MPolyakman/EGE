from itertools import*
P = range(10,22)
Q = range(13,39)
R = range(18,26)
def f(x):
    p = x in P
    q = x in Q
    r = x in R
    return (not(q <= (p or r))) <= ((not(a1 <= x <= a2)) <= (not q))


answer = []
OX = list(range(100))
for a1, a2 in combinations(OX,2):
    if all(f(x) for x in OX):
        answer.append(a2-a1)
print(min(answer))