import math

figure = str(input())

if figure == 'square':
    side = float(input())
    VolumeS = side * side
    print(format(VolumeS, ".3f"))
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    VolumeR = side_a * side_b
    print(format(VolumeR, ".3f"))
elif figure == 'circle':
    radius = float(input())
    VolumeC = math.pi * (radius * radius)
    print(format(VolumeC, ".3f"))
elif figure == 'triangle':
    side_a = float(input())
    drop = float(input())
    VolumeT = side_a * drop / 2
    print(format(VolumeT, ".3f"))