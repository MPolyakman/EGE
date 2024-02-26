data = open('k8.txt').readline()
cnt = 1
answer = 0
let_answer = ''
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        cnt += 1
    else:
        if cnt > answer:
            answer = cnt
            let_answer = data[i]
        cnt = 1
answer = max(cnt,answer)
print(let_answer,answer)