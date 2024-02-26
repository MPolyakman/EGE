from itertools import*
cnt = 0
for i in product('ество',repeat=8):
    word = ''.join(i)
    word = word.replace('е','0').replace('о','0')
    word = word.replace('с','1').replace('т','1').replace('в','1')
    if word.count('0') >= 3 and word.count('1') >= 4 and '00' not in word:
        cnt += 1
print(cnt) 