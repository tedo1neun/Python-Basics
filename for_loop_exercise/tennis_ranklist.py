tourneys_amount = int(input())

starting_points = int(input())

points_from_results = 0

won_tourneys = 0

percent_won_tourneys = 0

for i in range(tourneys_amount):
    turneys_result = input()

    if turneys_result == 'W':
        points_from_results += 2000
        won_tourneys += 1
    elif turneys_result == 'F':
        points_from_results += 1200
    elif turneys_result == 'SF':
        points_from_results += 720

percent_won_tourneys = (won_tourneys / tourneys_amount) * 100

average_points = int(points_from_results / tourneys_amount)
total_points = starting_points + points_from_results

print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percent_won_tourneys:.2f}%')