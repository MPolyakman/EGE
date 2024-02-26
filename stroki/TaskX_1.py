hh = input()
a = hh.find('h')
b = hh.rfind('h')
posle = hh[b-1:a:-1]
print(hh[:a+1]+posle+hh[b:])