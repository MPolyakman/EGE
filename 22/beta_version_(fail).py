name = int(input('Номер задания? (только число): '))
f = open(f'{name}.txt')
operations = {}
for string in f:
    x=list(map(int,string.replace(';',' ').replace('"','').split()))
    operations[x.pop(0)]=x
    # был создан словарь состоящий из времени выполения и айди требуемых процесов
print(operations)
process = [[0,0]]
for id in operations.keys(): # перебираем все ключи
    start = [] # это переменная должна показывать время окончания всех его предшественников
    for starting_point in (operations[id])[1:]:  # перебираем ключи предшественников нашей операции
        if starting_point == 0: # если ключ предшественника 0 операция начнется сразу
            start.append(0)
        else:
            start.append((process[starting_point])[1]) # иначе += время окончания его предшественника
    start = max(start) # оставляем самого долгого его предшественника
    process.append([start + 1, start + (operations[id])[0]])
print(process)
# мы получили список процессов от нулевого до 15ого с временем начала и конца
# сделаем перебор считающий от первой до секунды без процессов количество идущих одновременно процессов
# каждую секунду мы запишем списком идущих в этот момент процессов
seconds = [[0]] # список секунд который мы заполним происходившеми в это время процессами в них проходящих
for second in range(1,10**7):
    range_of_operates = []
    for operate in process: # перебираем операции с списке начал и концов процессов
        if operate[0] <= second and operate[1] >= second:
            range_of_operates.append(process.index(operate)+1)
    if range_of_operates == []:
        break
    else:
        seconds.append(range_of_operates)
# print(seconds)
print(f'Время выполнения абсолютно всех процессов: {len(seconds)-1}')
# у нас есть список всех секунд и каждого процесса который происходил в каждую секунды в одном списке
# в списке есть нулевая секунда, учтём её отдельно
# узнаем сколько секунд выполнялось одновременно n процессов
number_of_proccess = []
for number in seconds:
    if number == [0]:
        number_of_proccess.append(0)
    else:
        number_of_proccess.append(len(number))
for i in range(1,50):
    if number_of_proccess.count(i) != 0:
        print(f'Количество секунд во время которых выполнялось {i} процесса: {number_of_proccess.count(i)}')
# для выполнения номера 6877 нужно узнать количество секунд ПОДРЯД во время которых выполнялось n>=4 проццесов
# переберём каждую секунду считая кол-во процесов в ней и запишем длинны промежутков при n>=4
print(number_of_proccess)
answer = []
lenght = 0
condition = int(input('Промежуток выполнения скольки процессов одновременно нужен?: '))
for number in number_of_proccess[1:]:
    if number == condition:
        lenght += 1
    if number != condition:
        if lenght > 0:
            answer.append(lenght)
        lenght = 0
print(f'Промежутки: {answer}')
print(f'Наибольший промежуток: {max(answer)}')


