cake_length = int(input())
cake_width = int(input())
pieces = cake_length * cake_width
total_pieces = 0

while True:
    taken_pieces = input()
    if taken_pieces == 'STOP':
        print(f'{abs(pieces - total_pieces)} pieces are left.')
        break

    total_pieces += int(taken_pieces)

    if total_pieces >= pieces:
        print(f'No more cake left! You need {abs(pieces - total_pieces)} pieces more.')
        break

