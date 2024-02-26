def win(s):
    if s < 111 and ((s + 1) >= 111 or (s + 3) >= 111 or (s * 4) >= 111):
        return True
    return False

def lose(s):
    if (not (win(s))) and win(s + 1) and win(s + 3) and win(s * 4):
        return True
    return False

def win2(s):
    if (not (win(s))) and (lose(s + 1) or lose(s + 3) or lose(s * 4)):
        return True
    return False


for s in range(1, 111):
    if (win(s + 1) and win(s + 3) and win(s * 4)) and (not (win(s))):
        print(f'19 ответ: {s}')
        break
for s in range(1, 111):
    if win2(s):
        print(f'20 ответ: {s}')
for s in range(1, 111):
    if (not (win(s))) and (win(s + 1) or win2(s + 1)) and (win(s + 3) or win2(s + 3)) and (win(s * 4) or win2(s * 4)):
        if (not (win(s + 1) and win(s + 3) and win(s * 4))):
            print(f'21 ответ: {s} ')
            break
