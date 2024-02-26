def win1(x,s):
    if x*s < 123 and ((x+2)*s >= 123 or x*(s+2) >= 123 or x*s*2 >= 123):
        return True
    return False


def lose(x,s):
    if (not(win1(x,s))) and (win1(x+2,s) and win1(x,s+2) and win1(2*x,s) and win1(x,s*2)):
        return True
    return False

def win2(x,s):
    if (not(win1(x,s))) and (lose(x+2,s) or lose(x,s+2) or lose(x*2,s) or lose(x,s*2)):
        return True
    return False

x = 3
for s in reversed(range(1,41)):
    if win1(x+2,s) or win1(x*2,s) or win1(x,s+2) or win1(x,s*2):
        print(f'Ответ 19: {s}')
        break

for s in reversed(range(1,40)):
    if win2(x,s):
        print(s)

for s in reversed(range(1,40)):
    if (not(win1(x,s))) and (win1(x+2,s) or win2(x+2,s)) and (win1(x*2,s) or win2(x*2,s)) and (win1(x,s+2) or win2(x,s+2)) and (win1(x,s*2) or win2(x,s*2)):
        if (not(win1(x+2,s) and win1(x*2,s) and win1(x,s+2) and win1(x,s*2))):
            print(f'ответ к 21: {s}')
            break