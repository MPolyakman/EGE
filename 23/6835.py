def find_path(start, finish):
    if start == finish:
        return 1
    if start == 23 or start > finish:
        return 0
    if start < finish:
        return find_path(start + 2, finish) + find_path(start * 3, finish) + find_path(start * 5, finish)

print(find_path(1,13) * find_path(13,75))