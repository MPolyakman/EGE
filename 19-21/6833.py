# def win_possible(s):
#     if s < 37 and ((s * 3 >= 37) or (s + 1 >= 37) or (s + 2 >= 37)):
#         return True
#     return False
#
#
# def ought_to_lose(s):
#     if (not(win_possible(s))) and win_possible(s + 1) and win_possible(s + 2) and win_possible(3*s):
#         return True
#     return False
#
#
# def win2_possible(s):
#     if (ought_to_lose(s + 1) or ought_to_lose(s + 2) or ought_to_lose(s*3)) and (not(win_possible(s))):
#         return True
#     return False
#
#
# for s in range(1,37):
#     if (not(win_possible(s))) and win_possible(s + 1) and win_possible(s + 2) and win_possible(3*s):
#         print(f'Ответ 19:{s}')
#         break
#
#
# cnt = []
# for s in range(1,37):
#     if (ought_to_lose(s +1) or ought_to_lose(s + 2) or ought_to_lose(3*s)) and (not(win_possible(s))):
#         cnt.append(s)
# print(f'Ответ 20:{cnt[0]},{cnt[1]}')
#
# for s in (1,37):
#     if (not(win_possible(s))) and (win2_possible(s + 1) or win_possible(s + 1)) and (win2_possible(s + 2) or win_possible(s + 2))\
#         and (win2_possible(s *3) or win_possible(s *3)) and ((not(win_possible(s + 1))) or (not(win_possible(s + 2))) or (not(win_possible(s * 3)))):
#         print(f'Ответ 21:{s}')

def win(s):
    if s < 37 and ((s + 1 >= 37) or (s + 2 >= 37) or (s * 3 >= 37)):
        return True
    return False

def lose(s):
    if (not(win(s))) and win(s + 1) and win(s + 2) and win(s * 3):
        return True
    return False

def win2(s):
    if (not(win(s))) and (lose(s + 1) or lose(s + 2) or lose(s * 3)):
        return True
    return False

for s in range(1, 37):
    if ((not(win(s))) and (win(s + 1) or win2(s + 1)) and (win(s + 2) or win2(s + 2)) and (win(s * 3) or win2(s * 3)) and ((not(win(s + 1))) or (not(win(s + 2))) or (not(win(s * 3))))):
        print(s)