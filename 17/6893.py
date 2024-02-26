def yslovie(troika):
    for n in troika:
        if '3' not in str(n):
            return False
    for delitel in range(2,sum(troika)):
        if sum(troika) % delitel == 0:
            return False
    return True

f = open('6893.txt')
numbers = [int(number) for number in f]
otvet = []
for i in range(len(numbers)-2):
    troika = [numbers[i],numbers[i+1],numbers[i+2]]
    if yslovie(troika):
        otvet.append(sum(troika))
print(len(otvet),min(otvet))