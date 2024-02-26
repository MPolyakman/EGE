from ipaddress import*
cnt = 0
network = ip_network('140.19.96.0/255.255.248.0')
for ip in network:
    bip = bin(int(ip))[2:]
    part1 = bip[:8].count('1')
    part2 = bip[8:16].count('1')
    part3 = bip[16:24].count('1')
    part4 = bip[24:].count('1')
    if len({part1,part2,part3,part4}) == 1:
        cnt += 1
print(cnt)