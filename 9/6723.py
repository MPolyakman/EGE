f = open('6723.txt')
cnt = 0
for string in f:
    numbers = list(map(int, string.split()))
    count_numbers = [numbers.count(number) for number in numbers]
    if count_numbers.count(3) == 3 and count_numbers.count(1) == 4:
        average = 0
        repeated = 0
        for number in numbers:
            if numbers.count(number) == 1:
                average += number
            else:
                repeated = number
        average = average / 4
        if average <= repeated:
            cnt += 1
print(cnt)
