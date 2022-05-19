budget = float(input())
season = input()

winter = ""
summer = ""
destination = ""
place = ""
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = "Camp"
        budget = budget * 0.3
    elif season == 'winter':
        place = "Hotel"
        budget = budget * 0.7
if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        budget = budget * 0.4
    elif season == 'winter':
        place = 'Hotel'
        budget = budget * 0.8
if budget > 1000:
    destination = 'Europe'
    place = 'Hotel'
    budget = budget * 0.9

print(f"Somewhere in {destination}")
print(f'{place} - {budget:.2f}')