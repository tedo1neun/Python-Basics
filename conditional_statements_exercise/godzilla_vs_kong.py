budget = float(input())
statist_quantity = int(input())
price_clothes_statist_single_statist = float(input())

decor = budget * 10/100
price_for_clothes = statist_quantity * price_clothes_statist_single_statist
price_for_movie = decor + price_for_clothes

if statist_quantity > 150:
    discounted_price_clothes_statist = price_for_clothes * 10/100
    price_for_movie -= discounted_price_clothes_statist

diff = abs(budget-price_for_movie)

if budget >= price_for_movie:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")