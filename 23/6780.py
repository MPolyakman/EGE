def find_path(start, finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    if start == 7:
        return 0
    if start > finish:
        return find_path(start - 1, finish) + find_path(start - 3, finish) + find_path(start // 2, finish)
print (find_path(19,10) * find_path(10,3))