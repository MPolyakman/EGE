f = open('6792.txt')
num_of_visitors = int(f.readline())
visitors = sorted([[int(visitor.split()[0]),int(visitor.split()[1])] for visitor in f])
timeline = [0]*1441
for visitor in visitors:
    for minute in range(visitor[0],visitor[1]+1):
        timeline[minute] += 1
peak = 0
for minute in range(1,len(timeline)):
    if timeline[minute] == max(timeline) and timeline[minute-1] != max(timeline):
        peak += 1
print(peak,max(timeline))
