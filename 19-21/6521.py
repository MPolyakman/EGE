def win(x,s):
    if x>=10 and s>=10 and (x-1<10 or x-3<10 or s-1<10 or s-3<10):
        return True
    return False

def lose(x,s):
    if (not(win(x,s))) and win(x-1,s) and win(x-3,s) and win(x,s-1) and win(x,s-3):
        return True
    return False

def win2(x,s):
    if (not(win(x,s))) and (lose(x-1,s) or lose(x-3,s) or lose(x,s-1) or lose(x,s-3)):
        return True
    return False

print('Otvet na 19:')
for s in range(1,100):
    if (not(win(s,s))) and (win(s-1,s) or win(s-3,s) or win(s,s-1) or win(s,s-3)):
        print(s)
x = 13
print('Otvet na 20:')
for s in range(10,40):
    if (not(win(x,s))) and (lose(x-3,s) or lose(x-1,s) or lose(x,s-3) or lose(x,s-1)):
        print(s)
print('Otvet na 21')
for s in range(10,40):
    if (not(win(x,s))) and (win(x+-1,s) or win2(x-1,s)) and (win(x-3,s) or win2(x-3,s)) and (win(x,s-1) or win2(x,s-1)) and (win(x,s-3) or win2(x,s-3)):
        if not (win(x-1,s) and win(x-3,s) and win(x,s-1) and win(x,s-3)):
            print(s)

