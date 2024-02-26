cow = int(input())
if int(str(cow)[-1]) == 0 or 5 or 6 or 7 or 8 or 9:
    print('korov1')
elif str(cow)[-1] == 1:
    if int(str(cow)[0]) == 1 and len(str(cow)) == 2:
        print('korov2')
    else:
        print('korova')
elif int(str(cow)[-1]) == 2 or 3 or 4:
    if int(str(cow)[0]) == 1:
        print('korov3')
    else:
        print('korovy')