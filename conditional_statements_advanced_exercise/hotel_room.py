month = input()
nights_quantity = int(input())

Studio = ""
Apartment = ""

price = 0

if month == 'May' or month == 'October':
    Studio = 50 * nights_quantity
    if 7 < nights_quantity < 14:
        Studio -= 0.05 * Studio
    if 14 < nights_quantity:
            Studio -= 0.30 * Studio
    Apartment = 65 * nights_quantity
    if nights_quantity > 14:
        Apartment -= 0.10 * Apartment

if month == 'June' or month == 'September':
   Studio = 75.20 * nights_quantity
   Apartment = 68.70 * nights_quantity
   if 14 < nights_quantity:
       Studio -= 0.20 * Studio
       if nights_quantity > 14:
           Apartment -= 0.10 * Apartment

if month == 'July' or month == 'August':
    Studio = 76 * nights_quantity
    Apartment = 77 * nights_quantity
    if nights_quantity > 14:
        Apartment -= 0.10 * Apartment

print(f'Apartment: {Apartment:.2f} lv.')
print(f'Studio: {Studio:.2f} lv.')