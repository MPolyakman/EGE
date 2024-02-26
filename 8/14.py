x = 'ПИР'
k = 0
for w1 in x:
    for w2 in x:
        for w3 in x:
            for w4 in x:
                for w5 in x:
                    word = w1+w2+w3+w4+w5
                    if word.count('П') == 1:
                        k+=1
print(k)