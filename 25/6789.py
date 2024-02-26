maska = []
for numbers in range(2025, 10 ** 8, 2025):
    if str(numbers)[:2] == '12' and str(numbers)[-4:-2] == '34' and str(numbers)[-1] == '5':
        maska.append(print(numbers, numbers // 2025))
