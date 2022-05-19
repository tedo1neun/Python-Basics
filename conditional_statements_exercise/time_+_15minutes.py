hours = int(input())
minutes = int(input())

hours_min_15min = (hours * 60) + minutes + 15

current_hours = hours_min_15min // 60
current_minutes = hours_min_15min % 60

if current_hours > 23:
    print(f'0:{current_minutes:02d}')
else:
    print(f'{current_hours}:{current_minutes:02d}')