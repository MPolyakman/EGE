chet = ['0','2','4','6','8']
nechet = ['1','3','5','7','9']

def b(x):
    for letter in x:
        if letter not in nechet:
            return False
    return True

for n in range(0,10**10,133):
    n = str(n)
    if n[0] == '1' and n[2:6] == '2157' and n[-1] == '4' and n[1] in chet and b(n[6:-1]):
        print(int(n),int(n)//133)