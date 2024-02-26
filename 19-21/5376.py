def win(x,s):
    if x + s < 259 and (x+s+1 >= 259 or x+(s*2) >= 259 or (x*2)+s >= 259):
        return True
    return False

def lose(x,s):
    if (not(win(x,s))) + s and win(x, s + 1) and win(x, s*2) and win(x*2, s) and win(x+1, s):
        return True
    return False

def win2(x,s):
    if (not(win(x,s))) and (lose(x,s+1) or lose(x*2,s) or lose(x,s*2) or lose(x+1,s)):
        return True
    return False

x = 17
for s in range(1,142):
    if (not(win(x,s))) and (win(x,s+1) or win(x*2,s) or win(x,s*2)):
        print(f'Ответ к 19: {s}')
        break
for s in range(1,142):
    if win2(x,s):
        print(f'Ответ к 20: {s}')
for s in range(1,142):
    if (not(win(x,s))) and (win(x,s+1) or win2(x,s+1)) and (win(x,s*2) or win2(x,s*2)) and (win(x+1,s) or win2(x+1,s))\
        and (win(x*2,s) or win2(x*2,s)):
        if (not(win(x+1,s) and (win(x,s+1)) and (win(x*2,s)) and (win(x,s*2)))):
            print(f'Ответ к 21: {s}')
            break
