# 12345?6?8
for i in range(17,(10**9)+1,17):
    if str(i)[0:5] == '12345' and len(str(i)) == 9 and str(i)[6] == '6' and str(i)[-1] == '8':
        print(i, i//17)