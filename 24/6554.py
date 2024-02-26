data = open('6554.txt').readline()
data = data.replace('0','2').replace('4','2').replace('6','2').replace('8','2')
data = data.replace('1','3').replace('5','3').replace('7','3').replace('9','3')
borders = set()
for id in range(len(data)-1):
    if data[id:id+2] == '23' or data[id:id+2] == '32':
        borders.add(id)
        borders.add(id)
lengths = []
borders = list(borders)
borders.append(0)
borders.append(len(data)-1)
borders.sort()
for id in range(1,len(borders)-1):
    lengths.append(borders[id] - borders[id-1])
print(max(lengths))
