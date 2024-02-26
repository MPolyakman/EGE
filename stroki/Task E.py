fstroka = input()
if fstroka.find('f') == fstroka.rfind('f') and fstroka.find('f') != -1:
    print(fstroka.find('f'))
elif fstroka.find('f') != fstroka.rfind('f'):
    print(fstroka.find('f'), fstroka.rfind('f'))