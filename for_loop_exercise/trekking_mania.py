group_amount = int(input())

mountain = ''

Musala_percentage = 0
Monblan_percentage = 0
Kilimanjaro_percentage = 0
K2_percentage = 0
Everest_percentage = 0

people_count = 0

for i in range(group_amount):
    group_people_amount = int(input())
    people_count += group_people_amount

    if group_people_amount <= 5:
        mountain = 'Musala'
        Musala_percentage += group_people_amount
    elif 6 <= group_people_amount <= 12:
        mountain = 'Monblan'
        Monblan_percentage += group_people_amount
    elif 13 <= group_people_amount <= 25:
        mountain = 'Kilimanjaro'
        Kilimanjaro_percentage += group_people_amount
    elif 26 <= group_people_amount <= 40:
        mountain = 'K2'
        K2_percentage += group_people_amount
    elif group_people_amount >= 41:
        mountain = 'Everest'
        Everest_percentage += group_people_amount

print(f'{(Musala_percentage / people_count) * 100:.2f}%')
print(f'{(Monblan_percentage / people_count) * 100:.2f}%')
print(f'{(Kilimanjaro_percentage / people_count) * 100:.2f}%')
print(f'{(K2_percentage / people_count) * 100:.2f}%')
print(f'{(Everest_percentage / people_count) * 100:.2f}%')