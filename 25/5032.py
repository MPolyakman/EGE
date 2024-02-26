# 1?DED?BABA
for i in reversed(range(0, (int('1fdedfbaba',16)+1),int('ba',16))):
    if hex(i)[-4:] == 'baba' and hex(i)[2] == '1' and hex(i)[4:7] == 'ded':
        print(i, i/int('ba',16))