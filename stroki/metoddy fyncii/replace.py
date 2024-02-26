# x.replace('old','new') - заменяет подстроку old на подстроку new в строке x
x = 'барабан'
x.replace('а','о')
x.count('a')
x.find('б')
print(x) # не изменилось, барабан
print(x.replace('а','о')) # боробон
y = x.replace('а','о')
print(x)
print(y)
# x.replace('old','new','count') - заменяет подстроку old на подстроку new первые count раз в строке x
x = x.replace('а','о',2)
print(x)
