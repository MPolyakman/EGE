f = open('6285.txt')
cnt = f.readline()
xy = []
for string in f:
    string = list(map(int,string.split()))
    xy.append(string)
xy.sort(reverse=True)
line = 1
max_line=1
ryad = 0
for id in range(len(xy)-1):
    if (xy[id])[0] == (xy[id+1])[0] and ((xy[id])[1] - (xy[id+1])[1]) <= 11:
        line += ((xy[id])[1] - (xy[id+1])[1])
    else:
        if line > max_line:
            ryad = xy[id][0]
        max_line = max(max_line,line)
        line = 1
print(max(max_line,line),ryad)