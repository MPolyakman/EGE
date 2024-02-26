from itertools import*
alf = '014689acefg'
cnt = 0
for number in permutations(alf,6):
    if int(number[0],17) % 2 == 0 and number[0] != '0':
        cnt += 1
print(cnt)
print(7*10*9*8*7*6)