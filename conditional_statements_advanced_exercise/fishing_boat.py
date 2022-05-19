budget = int(input())
season = input()
fishers_quantity = int(input())

Spring = ""
Summer = ""
Autumn = ""
Winter = ""

ship_price = 0

if season == "Spring":
    ship_price = 3000
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
elif season == "Winter":
    ship_price = 2600

if fishers_quantity <= 6:
    ship_price -= ship_price * 0.1
    if fishers_quantity % 2 == 0 and season != "Autumn":
        ship_price -= ship_price * 0.05

if 7 < fishers_quantity <= 11:
    ship_price -= ship_price * 0.15
    if fishers_quantity % 2 == 0 and season != "Autumn":
        ship_price -= ship_price * 0.05

if fishers_quantity > 12:
    ship_price -= ship_price * 0.25
    if fishers_quantity % 2 == 0 and season != "Autumn":
        ship_price -= ship_price * 0.05

diff = abs(budget - ship_price)

if budget >= ship_price:
    print(f'Yes! You have {diff:.2f} leva left.')
elif budget < ship_price:
    print(f'Not enough money! You need {diff:.2f} leva.')