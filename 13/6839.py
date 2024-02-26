from ipaddress import*
cnt = 0
network = ip_network('192.168.32.160/255.255.255.240')
for ip in network:
    if ((bin(int(ip))[2:].zfill(32)).count('1')%2 == 0):
        cnt += 1
print(cnt)
print(bin(240)[2:],bin(160)[2:],sep='\n')