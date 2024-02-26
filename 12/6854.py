list = []
for n in range(4,1000):
    vvodne = '1' + '2'*n
    while '12' in vvodne or '322' in vvodne or '222' in vvodne:
        if '12' in vvodne:
            vvodne = vvodne.replace('12','2',1)
        if '322' in vvodne:
            vvodne = vvodne.replace('322','21',1)
        if '222' in vvodne:
            vvodne = vvodne.replace('222','3',1)
    list.append(vvodne.count('2'))
print(max(list))