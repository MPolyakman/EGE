# 5x9x4 12 + 7xx6 14 + 55xx8 16 – 3yx7 19
def simple(n):
    for delitel in range (2,n):
        if n % delitel == 0:
            return False
    else:
        return True
answer = []
alf19 = '0123456789abcdefghi'
alf12 = '0123456789ab'
for x in alf12:
    for y in alf19:
        number = int('5' + str(x) + '9' + str(x) + '4', 12) + int('7' + str(x) + str(x) + '6',14) + int('55' + str(x) + str(x) + '8',16) - int('3' + str(y) + str(x) + '7',19)
        if simple(number):
            answer.append(int(x,12)*int(y,19))
print(max(answer))
