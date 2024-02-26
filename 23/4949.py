def find_path(start, finish,plus_count):
    if start == finish:
        return 1
    if start > finish:
        return 0
    if start < finish and plus_count != '+2':
        return find_path(start + 1, finish, '+1') + find_path(start + 2,finish,'+2')\
    + find_path(start * 2, finish, '*2')
    else:
        return find_path(start * 2, finish,'*2') + find_path(start + 1, finish, '+1')
print(find_path(1,12,''))