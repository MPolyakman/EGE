f = open('6642.txt')
numbers = [int(number) for number in f]
biggest = [number for number in numbers if number % 17 == 0]
biggest = max(biggest)
answer = []
for i in range(len(numbers) - 1):
    if numbers[i] + numbers[i + 1] > biggest:
        answer.append(numbers[i] + numbers[i + 1])
print(len(answer), max(answer))
