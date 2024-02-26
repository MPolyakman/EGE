for n in range(4,1000):
    input_data = '5' + ('2'*n)
    while '52' in input_data or '222' in input_data or '122' in input_data:
        if '52' in input_data:
            input_data = input_data.replace('52','11',1)
        if '222' in input_data:
            input_data = input_data.replace('222', '15', 1)
        if '122' in input_data:
            input_data = input_data.replace('122','21',1)
    sum = 0
    for letter in input_data:
        sum += int(letter)
    if sum**0.5 == int(sum**0.5):
        print(n)