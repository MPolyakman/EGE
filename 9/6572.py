f = open('6572.txt')
strings = [string.split() for string in f]
stroki = []
for string in strings:
    string = list(map(int, string))
    stroki.append(string)
cnt = 0
for string in stroki:
    if string[0] != max(string) and string[0] != min(string):
        if string[-1] != max(string) and string[-1] != min(string):
            string.sort()
            if (string[2] - string[1]) != 0:
                if (max(string) - min(string)) % (string[2] - string[1]) == 0:
                    cnt += 1
print(cnt)