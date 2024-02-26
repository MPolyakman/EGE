f = open('6489.txt')
answer = []
numbers = [int(number) for number in f]
min3 = min([number for number in numbers if len(str(abs(number))) == 3 and str(abs(number)) == str(abs(number))[::-1]])
print(min3)
for ind in range(len(numbers)-1):
    if (len(str(abs(numbers[ind]))) == 4 and len(str(abs(numbers[ind + 1]))) != 4) or (len(str(abs(numbers[ind]))) != 4 and len(str(abs(numbers[ind + 1]))) == 4):

        if ((numbers[ind])**2 + (numbers[ind+ 1])**2) % abs(min3) == 0:
            answer.append((numbers[ind])**2 + (numbers[ind+ 1])**2)
print(len(answer),max(answer))
