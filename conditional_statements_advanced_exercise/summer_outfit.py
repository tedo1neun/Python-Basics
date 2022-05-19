tempеrature = int(input())
day_time = input()
Outfit = ""
Shoes = ""

if 10 <= tempеrature <= 18:
    if day_time == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif day_time == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif day_time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
if 18 < tempеrature <= 24:
    if day_time == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif day_time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
if tempеrature >= 25:
    if day_time == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif day_time == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
    elif day_time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {tempеrature} degrees, get your {Outfit} and {Shoes}.")