width = int(input())
length = int(input())
height = int(input())
kbm = width * length * height
boxes_total = 0
while True:
    boxes = input()

    if boxes == 'Done' and boxes_total <= kbm:
        print(f'{abs(kbm - boxes_total)} Cubic meters left.')
        break
    boxes_total += int(boxes)

    if boxes_total > kbm:
        print(f'No more free space! You need {abs(kbm - boxes_total)} Cubic meters more.')
        break

