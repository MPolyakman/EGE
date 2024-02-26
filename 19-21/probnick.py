def win(s):
    if (s+1 > 20 or s*2 > 20) and s < 21:
        return True
    return False

def lose(s):
    if win(s+1) and win(s*2) and (not(win(s))):
        return True
    return False

def win2(s):
    if (not(win(s))) and (lose(s+1) or lose(s*2)):
        return True
    return False

def lose2(s):
    if (not(win(s))) and (win(s+1) or (win2(s+1))) and (win(s*2) or win2(s*2)):
        if not(win(s+1) and win(s*2)):
            return True
    return False


# def win3(s):
#     if (not(win(s))) and (not(win2(s))) and (win2(s+2) and win2(s*4) and win2((s+1)*2) and win2(s*2+1)):
#         return True
#     return False


# for s in range(1,20):
#     if (not(win(s))) and (lose(s+1) or lose(s*2)):
#         print(s)
#         break
#
# for s in range(1,20):
#     if (win(s+1) or win2(s+1)) and (win(s*2) or win2(s*2)) and (not(win(s+1) and win(s*2))):
#         print(s)

for s in range(1,20):
    if not(win(s)):
        if lose2(s+1) or lose2(s*2):
            print(s)
