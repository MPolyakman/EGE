input_data = input()
# out_put_data = []
# input_data = input_data.split()
# for index in input_data:
#     if int(index) % 2 == 0:
#         out_put_data.append(index)
out_put_data = [int(index) for index in input_data.split() if int(index) % 2 == 0]
print(sum(out_put_data))
print(out_put_data)
