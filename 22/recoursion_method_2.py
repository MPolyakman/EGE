def find_the_end(key,operations):
    time = (operations[key])[0]
    if (operations[key])[1] == 0:
        return time
    time_of_ancestors = max([find_the_end(ancestor_key,operations) for ancestor_key in (operations[key])[1:]])
    return time + time_of_ancestors


name = int(input('Номер задания? (только число): '))
f = open(f'{name}.txt')
operations = {}
for string in f:
    x=list(map(int,string.replace(';',' ').replace('"','').split()))
    operations[x.pop(0)]=x
print(operations)
operations_range = []
for key in operations.keys():
    operations_range.append([find_the_end(key,operations)-(operations[key])[0]+1,find_the_end(key,operations)])

for i in range(len(operations_range)):
    print(i+1,operations_range[i])

seconds = []
for second in range(1,10**7):
    operations_at_the_moment = 0
    for operation in operations_range:
        if second >= operation[0] and second <= operation[1]:
            operations_at_the_moment += 1
    if operations_at_the_moment == 0:
        break
    seconds.append(operations_at_the_moment)
# print(seconds)

length = 0
answer = []
for second in seconds:
    if second == 4:
         length += 1
    else:
        if length > 0:
            answer.append(length)
            length = 0
print(answer)
