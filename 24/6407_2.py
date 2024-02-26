data = open('6407.txt').readline()
razd = ''
for i in range(len(data)):
    if len(razd) == 0 and data[i] in 'AFC':
        razd+=data[i]
    elif len(razd) == 1 and data[i]!=razd and data[i] in 'AFC':
        razd+=data[i]
    elif len(razd) > 1 and data[i] not in razd[-2:] and data[i] in 'AFC':
        razd+=data[i]
    else:
        if len(razd) > 2:
            data = data.replace(razd,len(razd)*' ', 1)
        if data[i] in 'AFC':
            razd = data[i]
        else:
            razd = ''
m = data.split()
maxxim = 0
for i in m:
    maxxim = max(maxxim, len(i))
print(maxxim)