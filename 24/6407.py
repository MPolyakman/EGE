from itertools import*
data = open('6407.txt').readline()
borders = set()
for border in permutations('ACF'):
    border = ''.join(border)
    borders.add(border)
index_borders = set()
for i in range(len(data)-2):
    if data[i:i+3] in borders:
        index_borders.add(i)
        index_borders.add(i+1)
        index_borders.add(i+2)
index_borders = sorted(list(index_borders))
index_borders.append(0)
index_borders.append(len(data))
index_borders.sort()
answer = set()
for n in range(1,len(index_borders)):
    answer.add(index_borders[n] - index_borders[n-1])
print(max(answer)-1)
