import math
show_name = input()
length_episode = int(input())
length_rest = int(input())

lunch_break = 1/8 * length_rest
relax_break = 1/4 * length_rest

time_left = abs(length_rest - lunch_break - relax_break)
enough_time_or_not = math.ceil(abs(length_episode - time_left))
if time_left >= length_episode:
    print(f"You have enough time to watch {show_name} and left with {int(enough_time_or_not)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {int(enough_time_or_not)} more minutes.")