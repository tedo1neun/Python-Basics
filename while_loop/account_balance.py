total = 0

while True:
    deposit = input()

    if deposit == 'NoMoreMoney':
        break

    if float(deposit) < 0:
        print('Invalid operation!')
        break

    if float(deposit) > 0:
        print(f'Increase: {float(deposit):.2f}')
        total += float(deposit)

print(f'Total: {total:.2f}')