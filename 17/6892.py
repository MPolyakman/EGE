def summ(number):
    summm = 0
    for letter in str(number):
        summm += int(letter)
    return summm


f = open('17_6892.txt')
numbers = [int(number) for number in f]
smallest = min([summ(s) for s in numbers])
biggest = max([n for n in numbers if summ(n) == smallest])
answer = []
for i in range(len(numbers) - 1):
    if numbers[i] > biggest and numbers[i+1] > biggest:
        answer.append(summ(numbers[i]) + summ(numbers[i + 1]))
print(len(answer), max(answer))
