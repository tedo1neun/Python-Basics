number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif 100 < number < 1000:
    bonus = 20 / 100 * number
elif number > 1000:
    bonus = 10 / 100 * number

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)
