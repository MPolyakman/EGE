def win(s):
    if s < 108:
        if s % 2 == 0 and (s+1 >= 108 or s*1.5 >= 108):
            return True
        if s % 2 == 1 and (s+1 >= 108 or s*2 >= 108):
            return True
    return False

def lose(s):
    if (not(win(s))):
        if s%2==0 and win(s+1) and win(s*1.5):
            return True
        if s%2==1 and win(s+1) and win(s*2):
            return True
    return False

def win2(s):
    if (not(win(s))) and s%2 == 0 and (lose(s+1) or lose(s*1.5)):
        return True
    if (not(win(s))) and s%2 == 1 and (lose(s+1) or lose(s*2)):
        return True


print('Otvet 19')

for s in reversed(range(1,108)):
    if s%2 == 0:
        if (not(win(s))) and (win(s+1) and win(s*1.5)):
            print(s)
            break
    if s%2 == 1:
        if (not(win(s))) and (win(s+1) and win(s*2)):
            print(s)
            break

print('Otvet 20')

for s in range(1,108):
    if s%2 == 0 and (not(win(s))) and (lose(s+1) or lose(s*1.5)):
        print(s)
    if s%2 == 1 and (not(win(s))) and (lose(s+1) or lose(s*2)):
        print(s)

print('Otvet 21')

for s in reversed(range(1,108)):
    if s%2 == 0 and (not(win(s))):
        if (win(s+1) or win2(s+1)) and (win(s*1.5) or win2(s*1.5)) and (not(win(s+1) and win(s*1.5))):
            print(s)
            break
    if s%2 == 1 and (not(win(s))):
        if (win(s+1) or win2(s+1)) and (win(s*2) or win2(s*2)) and (not(win(s+1) and win(s*2))):
            print(s)
            break