# 5 цифр неодинаковых четные и нечетные раздельно
scetchik = 0
for i in range (10_000,100_000,5):
    for letter in str(i): # 12345
        if str(i).count(letter) != 1:
            break
    else:
        newb = str(i).replace('2','0').replace('4','0').replace('6','0').replace('8','0')\
            .replace('3','1').replace('5','1').replace('7','1').replace('9','1')
        if '11' not in newb and '00' not in newb:
            scetchik += 1
print(scetchik)