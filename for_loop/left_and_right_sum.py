n = int(input())

numbers = 0
left_part = 0
right_part = 0

for i in range(n):
    numbers = int(input())
    left_part += numbers

for i in range(n):
    numbers = int(input())
    right_part += numbers

if left_part == right_part:
    print(f'Yes, sum = {left_part}')
elif left_part != right_part:
    print(f'No, diff = {abs(left_part-right_part)}')