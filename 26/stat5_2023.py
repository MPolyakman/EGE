f = open('stat5_2023.txt')
cnt_of_cars = int(f.readline())
cars = sorted([[int(car.split()[0]),int(car.split()[1])+int(car.split()[0]),car.split()[2]] for car in f])
A_Park = [0]*80
B_Park = [0]*20
answer = [0,0]
for car in cars:
    flag = 'free'
    if car[-1] == 'A':
        for id in range(len(A_Park)):
            if A_Park[id] <= car[0]:
                A_Park[id] = car[1]
                flag = 'placed'
                answer[0] += 1
                break
        if flag == 'free':
            for id in range(len(B_Park)):
                if B_Park[id] <= car[0]:
                    B_Park[id] = car[1]
                    flag = 'placed'
                    answer[0] += 1
                    break
    else:
        for id in range(len(B_Park)):
            if B_Park[id] <= car[0]:
                B_Park[id] = car[1]
                flag = 'placed'
                break
    if flag == 'free':
        answer[1] += 1
print(answer)