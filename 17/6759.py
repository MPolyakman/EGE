f = open('17-381.txt')
numbers = [int(number) for number in f]
biggest = max([number for number in numbers if len(str(abs(number))) == 4 and abs(number) % 100 == 39])
answer = []
for i in range(len(numbers) - 1):
    if (len(str(abs(numbers[i]))) == 4 and len(str(abs(numbers[i + 1])))  != 4) or \
            (len(str(abs(numbers[i]))) != 4 and len(str(abs(numbers[i + 1]))) == 4):
        if ((numbers[i] + numbers[i + 1])**2) <= biggest**2:
            answer.append(numbers[i] + numbers[i + 1])
print(len(answer),max(answer))


f.close()