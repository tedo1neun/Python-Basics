condition = False

while True:
    destination = input()
    if destination == 'End':
        break
    minimal_budget = float(input())
    sum_money = 0
    for i in range(int(minimal_budget) + 1):
        saved_money = float(input())
        sum_money += saved_money
        if sum_money >= float(minimal_budget):
            print(f'Going to {destination}!')
            break
    if condition:
        break