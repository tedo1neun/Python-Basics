pages_of_book = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

hours_to_read_per_day = (pages_of_book / pages_per_hour) / days_to_read
print(int(hours_to_read_per_day))