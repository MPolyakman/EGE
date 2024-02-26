def summ(n):
    summm = 0
    for letter in str(n):
        summm += int(letter)
    return summm


su = []
answer = []
for n in range(2023 * 494316, 10_000_000_000, 2023):
    if str(n)[0] == '1' and str(n)[-1] == '1':
        su.append(summ(n))
        answer.append(n)
for i in reversed(answer):
    if summ(i) == max(su):
        print(i, i // 2023)
