f = open('9-6724.txt')
cnt = 0
for string in f:
    numbers = list(map(int, string.split()))
    count_numbers = [numbers.count(number) for number in numbers]
    if numbers.count(max(numbers)) == 2 and numbers.count(min(numbers)) == 2:
        cnt += 1
print(cnt)
