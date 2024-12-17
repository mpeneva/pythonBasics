from math import ceil

serial_title = input()

one_episod_duration = int(input())
break_duration = float(input())

lunch_time = 1/8 * break_duration
relax_time = 1/4 * break_duration

total_free_time = lunch_time + relax_time
relax_time_left = break_duration - total_free_time

if relax_time_left >= one_episod_duration:
    print(f"You have enough time to watch {serial_title} "
          f"and left with {ceil(relax_time_left - one_episod_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_title}, "
          f"you need {ceil(one_episod_duration - relax_time_left)} more minutes.")
