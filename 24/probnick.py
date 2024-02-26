#VWXYZ
data = open('probnick.txt').readline()
line = 'VWXYZV'
answer = []
length = 1
for index in range(len(data)-1):
    if data[index:index+2] in line:
        length += 1
    else:
        answer.append(length)
        length = 1
answer.append(length)
print(max(answer))
