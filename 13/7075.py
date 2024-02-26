from ipaddress import*
cnt = 0
network = ip_network('192.168.32.160/255.255.255.240')
for ip in network:
    ip = bin(int(ip))[2:].zfill(32)
    if ip.count('0') > 21:
        cnt += 1
print(cnt)