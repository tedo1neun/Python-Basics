start_interval = int(input())
final_interval = int(input())
magic_number = int(input())
combination_counter = 0
Condition = False
for i in range(start_interval, final_interval + 1):
    for j in range(start_interval, final_interval + 1):
        combination_counter += 1
        if i + j == magic_number:
            print(f'Combination N:{combination_counter} ({i} + {j} = {magic_number})')
            Condition = True
            break
    if Condition:
        break
if i + j != magic_number:
    print(f'{combination_counter} combinations - neither equals {magic_number}')