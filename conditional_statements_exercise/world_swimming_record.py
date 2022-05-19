import math

record_in_sec = float(input())
meters_distance = float(input())
seconds_per_meter = float(input())

meters_seconds = meters_distance * seconds_per_meter
resistance_water_sec = math.floor(meters_distance / 15) * 12.5
total_time = meters_seconds + resistance_water_sec
diff = abs(total_time - record_in_sec)
if total_time >= record_in_sec:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")