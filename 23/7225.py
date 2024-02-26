def find_path(start,finish,previous_move):
    if start == finish:
        return 1
    if start > finish:
        return 0
    if start < finish and previous_move != 'A':
        return find_path(start+3,finish,'A') + find_path(start*5,finish,'B') + find_path(start*7,finish,'C')
    if start < finish and previous_move == 'A':
        return find_path(start+3,finish,'A') + find_path(start*7,finish,'C')
print(find_path(1,1000,'0'))
