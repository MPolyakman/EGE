# 12*45*
for i in range(51,(10**6)+1,51):
    if str(i)[0:2] == '12' and str(i).find('45') != -1:
        print(i, i//51)