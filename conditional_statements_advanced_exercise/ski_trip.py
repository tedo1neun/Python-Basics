trip_days = int(input())
trip_room = input()
trip_review = input()

trip_room_price = 0

if trip_room == 'room for one person':
    trip_room_price = (trip_days - 1) * 18.00
elif trip_room == 'apartment':
    trip_room_price = (trip_days - 1) * 25.00
elif trip_room == 'president apartment':
    trip_room_price = (trip_days - 1) * 35.00

if trip_days - 1 <= 10:
    if trip_room == 'room for one person':
        pass
    elif trip_room == 'apartment':
        trip_room_price -= trip_room_price * 0.3
    elif trip_room == 'president_apartment':
        trip_room_price -= trip_room_price * 0.1
if 10 < trip_days - 1 < 15:
    if trip_room == 'room for one person':
        pass
    elif trip_room == 'apartment':
        trip_room_price -= trip_room_price * 0.35
    elif trip_room == 'president apartment':
        trip_room_price -= trip_room_price * 0.15
if trip_days - 1 > 15:
    if trip_room == 'room for one person':
        pass
    elif trip_room == 'apartment':
        trip_room_price -= trip_room_price * 0.5
    elif trip_room == 'president apartment':
        trip_room_price -= trip_room_price * 0.2

if trip_review == 'positive':
    trip_room_price += trip_room_price * 0.25
elif trip_review == 'negative':
    trip_room_price -= trip_room_price * 0.10

print(f'{trip_room_price:.2f}')