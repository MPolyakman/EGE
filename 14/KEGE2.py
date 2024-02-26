result = (5 * 3**1917) + 6*(2**1878) + (7* (3**1870)) - 1991
res17 = ''
alf = '0123456789abcdefg'
list_of_answers = []
while result > 0:
    res17 = alf[result % 17] + res17
    result = result//17
print(res17)
for i in range(0,10):
    print(res17.count(str(i)), i)