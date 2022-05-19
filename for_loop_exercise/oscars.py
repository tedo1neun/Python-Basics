actor_name = input()
points_academy = float(input())
rater_amount = int(input())
total_points = 0
points = 0

for i in range(rater_amount):
    rater_name = input()
    points_from_rater = float(input())

    points += (len(rater_name) * points_from_rater) / 2
    total_points = points + points_academy

    if total_points > 1250.5:
        break

diff = abs(total_points - 1250.5)

if total_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

elif total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")