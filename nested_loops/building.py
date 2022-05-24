floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    for room in range(rooms):
        if floor == floors:
            print(f'L{floor}{room}', end=' ')
        if floor % 2 == 0 and floor != floors:
            print(f'O{floor}{room}', end=' ')
        if floor % 2 != 0 and floor != floors:
            print(f'A{floor}{room}', end=' ')
    print()