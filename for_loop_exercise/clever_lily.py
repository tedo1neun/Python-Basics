years_old_Lilly = int(input())
laundry_price = float(input())
price_toy = int(input())

savings = 0

toys_amount = 0

toys_total_price = 0

for i in range(1, years_old_Lilly + 1):

    if i % 2 == 0:
        savings += 10 * (i / 2) - 1
    else:
        toys_amount += 1

total_savings = (toys_amount * price_toy) + savings

diff = abs(total_savings - laundry_price)

if total_savings >= laundry_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')