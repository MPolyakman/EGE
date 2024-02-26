# for n in range(11,1_000_001):
#     r = oct(n)[2:]
#     if n % 5 == 0:
#         r = r + r[:3]
#     else:
#         r = r + bin(n%5)[2:]
#     if int(r,8) >= 35_000:
#         print(n)
#         break

print((50*(2**23)/(0.2*16*32000*4))/60)