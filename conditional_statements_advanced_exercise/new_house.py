type_flower = input()
flower_quantity = int(input())
budget = int(input())

price = 0

Roses = ""
Dahlias = ""
Tulips = ""
Narcissus = ""
Gladiolus = ""

if type_flower == 'Roses':
    price = flower_quantity * 5
elif type_flower == 'Dahlias':
    price = flower_quantity * 3.80
elif type_flower == 'Tulips':
    price = flower_quantity * 2.80
elif type_flower == 'Narcissus':
    price = flower_quantity * 3
elif type_flower == 'Gladiolus':
    price = flower_quantity * 2.50

discount = False
more_tax = False

if flower_quantity > 80 and type_flower == 'Roses':
    price -= price * 0.1
    discount = True
elif flower_quantity > 90 and type_flower == 'Dahlias':
    price -= price * 0.15
    discount = True
elif flower_quantity > 80 and type_flower == 'Tulips':
    price -= price * 0.15
    discount = True
elif flower_quantity < 120 and type_flower == 'Narcissus':
    price += price * 0.15
    more_tax = True
elif flower_quantity < 80 and type_flower == 'Gladiolus':
    price += price * 0.20
    more_tax = True

money_left_discount = abs(budget - price)

if budget >= price and discount == 'True':
    print(f"Hey, you have a great garden with {flower_quantity} {type_flower} "
          f"and {money_left_discount:.2f} leva left.")
elif budget < price and discount == 'True':
    print(f"Not enough money, you need {money_left_discount:.2f} leva more.")

money_left = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {flower_quantity} {type_flower} and {money_left:.2f} leva left.')
elif budget < price:
    print(f'Not enough money, you need {money_left:.2f} leva more.')


if budget >= price and more_tax == 'True':
    print(f'Hey, you have a great garden with {flower_quantity} {type_flower} and {money_left:.2f} leva left.')
elif budget < price and more_tax == 'True':
    print(f'Not enough money, you need {money_left:.2f} leva more.')

