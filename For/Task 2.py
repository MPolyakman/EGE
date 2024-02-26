# вывести элемент строки попарно
x = input()
for i in range(len(x)-2):
    print(x[i]+x[i+1]+x[i+2])