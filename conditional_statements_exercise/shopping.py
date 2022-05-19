budget = float(input())

quantity_GPU = int(input())
quantity_CPU = int(input())
quantity_RAM = int(input())

price_GPU = quantity_GPU * 250
price_CPU = quantity_CPU * (35/100 * price_GPU)
price_RAM = quantity_RAM * (10/100 * price_GPU)

total_price = price_GPU + price_CPU + price_RAM

if quantity_GPU > quantity_CPU:
    total_price = total_price - (total_price * 15/100)

diff = abs(budget-total_price)
if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")