hh = input()
first = hh.find('h')
last = hh.rfind('h')
print(hh[:first]+hh[first:last]+hh[first+1:last]+hh[last:])