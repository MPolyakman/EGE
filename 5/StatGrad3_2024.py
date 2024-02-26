nums = []
for n in range(1,101):
    r = bin(n)[2:]
    r = r + bin(n%4)[2:]
    nums.append(int(r,2))
print(sorted(nums))