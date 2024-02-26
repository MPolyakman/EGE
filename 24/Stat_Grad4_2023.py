def max_rep(string):
    alf = {letter for letter in string}
    counted = 0
    for letter in alf:
        counted = max(counted,string.count(letter))
    output = ''
    for letter in alf:
        if string.count(letter) == counted:
            output += letter
    return output


f = open('Stat_Grad4_2023.txt')
answer = ''
for string in f:
    letters = ''
    for id in range(len(string)-1):
        if string[id] == 'A':
            letters += string[id+1]
    answer += max_rep(letters)
print(answer.count(max_rep(answer)))
