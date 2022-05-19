trip_price = float(input())

puzzle_quantity = int(input())
talking_doll_quantity = int(input())
teddy_bears_quantity = int(input())
minions_quantity = int(input())
trucks_quantity = int(input())

total_toys_ordered = puzzle_quantity + talking_doll_quantity + teddy_bears_quantity + minions_quantity + trucks_quantity

puzzle_price = puzzle_quantity * 2.60
talking_doll_price = talking_doll_quantity * 3
teddy_bears_price = teddy_bears_quantity * 4.10
minions_price = minions_quantity * 8.20
trucks_price = trucks_quantity * 2

total_toys_price = puzzle_price + talking_doll_price + teddy_bears_price + minions_price + trucks_price

discount = 0
rent = 0
profit = 0

if total_toys_ordered >= 50:
    discount = total_toys_price * 25/100
    end_price = total_toys_price - discount
    rent = end_price * 10/100
    profit = end_price - rent
else:
    rent = total_toys_price * 10/100
    profit = total_toys_price - rent

trip_or_not = abs(profit - trip_price)
if profit >= trip_price:
    print(f"Yes! {trip_or_not:.2f} lv left.")
else:
    print(f"Not enough money! {trip_or_not:.2f} lv needed.")