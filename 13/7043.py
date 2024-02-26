from ipaddress import*
answer = []
for a in range(0,256):
    try:
        network = ip_network(f'134.97.250.117/255.255.{str(a)}.0',0)
        for net in network:
            net = bin(int(net))[2:]
            if net[:16].count('0') < net[16:].count('0'):
                break
        else:
            answer.append(a)
            print(a)
    except:
        continue
print(f'Otvet:{min(answer)}')
