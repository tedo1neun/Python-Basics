favorite_book = input()
count = 0
while True:
    searched_book = input()

    if favorite_book == searched_book:
        print(f'You checked {count} books and found it.')
        break

    if searched_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {count} books.')
        break

    count += 1