import math

first = int(input())
second = int(input())
third = int(input())

total = first + second + third

minutes = total // 60
seconds = total % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')