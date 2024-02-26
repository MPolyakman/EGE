from ipaddress import*
first_ip = ip_address('121.171.15.70')
second_ip = ip_address('121.171.3.68')
bin1 = (bin(int(first_ip))[2:].zfill(32))
bin2 = (bin(int(second_ip))[2:].zfill(32))
print(bin1)
print(bin2)
print(max([bin1[16:24],bin2[16:24]]))
print(int('11110000',2))