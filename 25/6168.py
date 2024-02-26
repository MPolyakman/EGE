for i in range(0,10**10+1,50068):
    if '0' in str(i) and str(i)[0] == '9' and str(i)[2:5] == '979' and str(i)[-1] == '8':
        print(i,i//50068)