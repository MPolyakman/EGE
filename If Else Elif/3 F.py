# существует ли треугольник
kat = int(input())
storona = int(input())
gipotinuza = int(input())
if kat > storona + gipotinuza or storona > gipotinuza + kat or kat > storona + gipotinuza:
    print('NO')
else:
    print('YES')

