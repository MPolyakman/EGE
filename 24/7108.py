f = open('7108.txt')
string = f.readline()
alf = 'QWERTYUIOPASDFGHJKLZXCVBNM'
alf = sorted(alf)[6:]
for i in alf:
    string = string.replace(i,' ')
string = string.split()
stroka = max([len(i.lstrip('0')) for i in string])
print(stroka)