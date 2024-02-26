def win(x,s):
    if (x + s < 45) and ((x + 1 + s >= 45) or (3 * x + s >= 45) or (3 * s + x >= 45)):
        return True
    else:
        return False
def canlose(x,s):
    if (x + s < 45) and (win(x+1,s) or win(x,s+1) or win(x,s*3) or win(3*x,s)):
        return True
    else:
        return False
def lose(x,s):
    if (not(win(x,s))) and (win(x+1,s) and win(x,s+1) and win(x,s*3) and win(3*x,s)):
        return True
    else:
        return False
def win2(x,s):
    if (not(win(x,s))) and (lose(x+1,s) or lose(x,s+1) or lose(x*3,s) or lose(x,s*3)):
        return True
    else:
        return False
print('Решение 19')
x = 4
for s in range(1,40):
    if canlose(x,s):
        print(s)
print('Решение 20')
x = 4
for s in range(1,40):
    if win2(x,s):
        print(s)
print('Решение 21')
x = 4
for s in range(1,40):
    if (not(win(x,s))) and (win(x+1,s) or win2(x+1,s)) and (win(x,s+1) or win2(x,s+1)) and (win(x,s*3) or win2(x,s*3)) and \
        (win(x * 3, s) or win2(x * 3, s)) and ((not(win(x+1,s))) or (not(win(x,s+1))) or (not(win(x*3,s))) or (not(win(x,s*3)))):
        print(s)
