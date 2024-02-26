data = open('6905.txt').readline()
# K N L F по краям чётные
# alfabet = set([letter for letter in data])
# uproved = {'L', 'N', 'K', 'F'}
# deleted = {letter for letter in alfabet if letter not in uproved and letter not in '02468'}
# for letter in deleted:
#     data = data.replace(letter,'x')
# for letter in uproved:
#     data = data.replace(letter, 'U')
# print(data)
# for n in reversed(range(100,10**4)):
#     for border in '02468':
#         string = border + n*'U' + border
#         if string in data:
#             print(n)
#             exit()

for letter in data:
    if letter in {'K','N','L','F'}:
        data = data.replace(letter,'1')
for i in reversed(range(1,10000)):
    for k in '02468':
        if k + '1'*i + k in data:
            print(i)
            exit()