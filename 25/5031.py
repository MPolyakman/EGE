x = int('79',16)
end = int('1fdedfced',16)
start = int('10ded0ced',16)
for i in reversed(range(x, end + 1, x)):
    h = hex(i)[2:]
    if (str(h))[0] == '1' and (str(h))[2:5] == 'ded' and (str(h))[6:9] =='ced':
        print(i,i/x)