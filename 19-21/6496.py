def win(x,s):
    if s < 78 and x < 78:
        if s == x and (x+1>=78 or x+2>=78 or x+3>=78):
            return True
        if s != x and (max(s,x)+1>=78 or max(s,x)+2>=78 or max(s,x)+3>=78 or min(s,x)*2>=78):
            return True
    return False

def lose(x,s):
    if (not(win(x,s))) and s == x and win(x+1,s) and win(x+2,s) and win(x+3,s):
        return True
    if (not(win(x,s))) and s != x and win(max(s,x)+1,min(s,x)) and win(max(s,x)+2,min(s,x)) and win(max(s,x)+3,min(s,x)) and win(min(s,x)*2,max(s,x)):
        return True
    return False

def win2(x,s):
    if (not(win(x,s))):
        if s == x and (lose(x+1,s) or lose(x+2,s) or lose(x+3,s)):
            return True
        if s != x and (lose(max(x,s)+1,min(x,s)) or lose(max(x,s)+2,min(x,s)) or lose(max(x,s)+3,min(x,s)) or lose(min(x,s)*2,max(x,s))):
            return True
    return False


print('Otvet 19')
answer = []
for s in range(1,78):
    for x in range(1,78):
        if win(x,s):
            answer.append(x+s)
print(min(answer))

print('Otvet 20')
x = 25
answer.clear()
for s in range(1,78):
    if s == x and (not(win(x,s))) and (lose(x+1,s) or lose(x+2,s) or lose(x+3,s)):
        answer.append(s)
    if s!=x and (not(win(x, s))) and (lose(max(s,x)+1,min(s,x)) or lose(max(s,x)+2,min(s,x)) or lose(max(s,x)+3,min(s,x)) or lose(min(s,x)*2,max(x,s))):
        answer.append(s)
print(answer)

print('Otvet 21')
x = 69
for s in range(1,78):
    if not(win(x,s)):
        if x == s and (win(x+1,s) or win2(x+1,s)) and (win(x+2,s) or win2(x+2,s)) and (win(x+3,s) or win2(x+3,s)):
            if not(win(x+1,s) and win(x+2,s) and win(x+3,s)):
                print(s)
        if x != s and (win(max(s,x)+1,min(x,s)) or win2(max(s,x)+1,min(x,s))) and (win(max(s,x)+2,min(x,s)) or win2(max(s,x)+2,min(x,s)))\
                and (win(max(s,x)+3,min(x,s)) or win2(max(s,x)+3,min(x,s))) and (win(min(x,s)*2,max(x,s)) or win2(min(x,s)*2,max(x,s))):
            print(s)
