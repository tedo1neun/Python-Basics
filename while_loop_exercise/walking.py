steps_sum = 0

while True:
    steps = input()

    if steps == 'Going home':
        steps_towards_home = int(input())
        diff = abs(int(steps_sum + steps_towards_home) - 10000)
        if steps_sum + steps_towards_home < 10000:
            print(f'{diff} more steps to reach goal.')
            break
        elif steps_sum + steps_towards_home >= 10000:
            print(f'Goal reached! Good job!')
            print(f'{diff} steps over the goal!')
            break

    steps_sum += int(steps)
    diff = abs(steps_sum - 10000)

    if steps_sum >= 10000:
        print(f'Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
        break


