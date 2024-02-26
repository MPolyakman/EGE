def find_start(key,operations): # найди время выполнения предшественников этой операции
    for reference_key in (operations[key])[1:]: # переберём ключи предшественников
        if reference_key == 0:
            return 0
        if reference_key != 0: # если есть ещё предшественники
            return find_start(reference_key,operations) + (operations[reference_key])[0]

name = int(input('Номер задания? (только число): '))
f = open(f'{name}.txt')
operations = {}
for string in f:
    x=list(map(int,string.replace(';',' ').replace('"','').split()))
    operations[x.pop(0)]=x
    # был создан словарь состоящий из времени выполения и айди требуемых процесов
operations_range = [] # cюда запишем первую и последнюю секунду работы кадого процесса
for key in operations.keys(): # перебирём ключи
    operations_range.append([find_start(key,operations)+1,find_start(key,operations)+(operations[key])[0]])
print(operations_range)
