def win1(s):
    if (s+3 >= 301 or s*5 >= 301) and s < 301:
        return True
    return False


def lose(s):
    if (not(win1(s))) and win1(s+3) and win1(s*5):
        return True
    return False


def win2(s):
    if (not(win1(s))) and (lose(s+3) or lose(s*5)):
        return True
    return False


for s in range(1,300):
    if lose(s):
        print(f'ответ к заданию 19: {s}')
        break
cnt = 0
for s in range(1,300):
    if win2(s):
        cnt += 1
        print(f'ответ к заданию 20: {s}')
        if cnt == 2:
            break
for s in range(1,300):
    if ((not(win1(s))) and (win1(s+3) or win2(s+3)) and (win1(s*5) or win2(s*5))) and ((not(win1(s+3))) or (not(win1(s*5)))):
        print(f'ответ к заданию 21: {s}')
        break