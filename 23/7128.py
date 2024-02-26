def find_path(start,finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    if start == 27:
        return 0
    if start > finish:
        return find_path(start-1,finish) + find_path(start-5,finish)
print(find_path(32,26) * find_path(26,24) * find_path(24,17))