hh = input()
a = hh.find('h')
b = hh.rfind('h')
print(hh[:a]+hh[b+1:])