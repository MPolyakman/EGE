def find_path(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    if start < finish:
        if str(start)[-2] == '9':
            return find_path(start + 1, finish)
        else:
            return find_path(start + 1, finish) + find_path(start + 10,finish)
print(find_path(10,33))
