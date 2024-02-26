f = open('2506.txt')
string = (f.readline())
f.close()
k = ''
answers = []
for i in string:
    if i == 'C':
        k += i
    else:
        answers.append(len(k))
        k = ''
print(max(max(answers),len(k)))

f = open('2506.txt')
string = (f.readline())
for i in range(1,100):
    if 'C'*i in string:
        print(i)
