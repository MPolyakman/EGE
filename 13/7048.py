from ipaddress import*
answer = []
for a in range(0,256):
    network = ip_network(f'159.242.{str(a)}.223/255.255.254.0',0)
    for net in network:
        net = bin(int(net))[2:]
        if net[:16].count('0') >= net[16:].count('0'):
            break
    else:
        answer.append(a)
print(max(answer))