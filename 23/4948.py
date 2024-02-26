def find_path(start, finish, multiply_count):
    if start == finish and multiply_count < 2:
        return 1
    if start > finish or multiply_count > 1:
        return 0
    if start < finish and multiply_count < 1:
        return find_path(start+1, finish, multiply_count * 0) + find_path(start+2, finish, multiply_count * 0) + find_path(start * 2, finish, multiply_count + 1)
    if start < finish and multiply_count > 0:
        return find_path(start+1, finish, multiply_count * 0) + find_path(start+2, finish, multiply_count * 0)

print(find_path(1,15,0))