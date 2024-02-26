for n in range(4,10000):
    input = '5'+ '2'*n
    while '52' in input or '2222' in input or '1122' in input:
        if '52' in input:
            input = input.replace('52','11',1)
        if '2222' in input:
            input = input.replace('2222','5',1)
        if '1122' in input:
            input = input.replace('1122','25',1)
    output = 0
    for letter in input:
        output += int(letter)
    if (str(output))[-1] == '7':
        print(n)
        break
