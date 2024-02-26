f = open('9-221.txt')
cnt = 0
for string in f:
    a = list(map(int, string.split()))
    repeated = [a.count(number) for number in a]

    sum_chet = 0
    sum_nechet = 0
    for number in a:
        if number % 2 == 0:
            sum_chet += number
        else:
            sum_nechet += number
    if (sum_nechet > sum_chet and repeated.count(2) != 2) or (sum_nechet <= sum_chet and repeated.count(2) == 2 and repeated.count(1) == 3):
        cnt += 1
print(cnt)
