f = open('17_KEGE2.txt')
def six(x):
    x = abs(x)
    xsix = ''
    while x > 0:
        xsix = str(x % 6) + xsix
        x //= 6
    if xsix[-2:] == '23' and len(xsix) >= 2:
        return True
    else:
        return False

numbers = [int(stroka) for stroka in f]
biggest = max([number for number in numbers if six(number)])
print(biggest)
answer = []
for i in range(len(numbers) - 2):
    troika = [numbers[i], numbers[i+1], numbers[i+2]]
    if len([number for number in troika if len(str(abs(number))) == 4]) == 1:
        if sum(troika) % biggest == 0:
            answer.append(sum(troika))
print(len(answer),max(answer))
