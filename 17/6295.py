# f = open('6295.txt')
# numbers = [int(number) for number in f]
# output = []
# average = [number for number in numbers if (abs(number)%100)//10 == abs(number)%10]
# average = sum(average)/len(average)
# for i in range(len(numbers)-1):
#     if (abs(numbers[i]) % 100)//10 == abs(numbers[i+1]) % 10 or (abs(numbers[i+1]) % 100)//10 == abs(numbers[i]) % 10:
#         if (numbers[i] % 11 == 0 and numbers[i+1] % 11 != 0) or (numbers[i+1] % 11 == 0 and numbers[i] % 11 != 0):
#             if ((numbers[i])**2 + (numbers[i+1])**2) >= average:
#                 output.append((numbers[i])**2 + (numbers[i+1])**2)
# print(len(output), max(output))

#для двух любых элементов

f = open('6295.txt')
numbers = [int(number) for number in f]
output = []
average = [number for number in numbers if (abs(number)%100)//10 == abs(number)%10]
average = sum(average)/len(average)
for i in range(len(numbers)):
    for k in range(i+1,len(numbers)):
        if (abs(numbers[i]) % 100)//10 == abs(numbers[k]) % 10 or (abs(numbers[k]) % 100)//10 == abs(numbers[i]) % 10:
            if (numbers[i] % 11 == 0 and numbers[k] % 11 != 0) or (numbers[k] % 11 == 0 and numbers[i] % 11 != 0):
                if ((numbers[i])**2 + (numbers[k])**2) >= average:
                    output.append((numbers[i])**2 + (numbers[k])**2)
print(len(output), max(output))