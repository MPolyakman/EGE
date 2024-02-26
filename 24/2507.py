f = open('k8.txt')
string = f.readline()
answer = []
words = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
for i in range(100):
    for letter in words:
        check = letter*i
        if check in string:
            answer.append(len(check))
for i in words:
    if i*max(answer) in string:
        print(i,max(answer),string.find(i*max(answer)))

