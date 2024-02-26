def find_path(start, finish, multiply_count):
    if start == finish and multiply_count <= 5:
        return 1
    if start > finish or multiply_count > 5:
        return 0
    if start < finish:
        return (find_path(start+1,finish, multiply_count) + find_path(start*3,finish, multiply_count + 1)\
                + find_path(start* 4, finish,multiply_count + 1))
print(find_path(3, 300,0))
