f = open('17.txt')
# print(f.read()) # Считать весь файл
# print(f,readline()) # Считать первую строку
# numbers = []
# for number in f:
#     numbers.append(int(number))
# print(numbers)
widest = []
numbers = [int(number) for number in f]
biggest = max([number for number in numbers if number % 100 == 17])
for i in range(len(numbers) - 2):
    troika = [numbers[i],numbers[i+1],numbers[i+2]]
    cnt_4 = 0
    yslovie2 = 0
    for n in troika:
        if len(str(n)) == 4:
            cnt_4 += 1
        if n % 5 == 0:
            yslovie2 += 1
    if sum(troika) > biggest and cnt_4 == 2 and yslovie2 > 0:
        widest.append(sum(troika))
print(len(widest),max(widest))

f.close()