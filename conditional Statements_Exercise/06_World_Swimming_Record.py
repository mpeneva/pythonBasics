record_in_seconds = float(input())
distance = float(input())

time_swimming_in_seconds_1m = float(input())

time_for_distance = distance * time_swimming_in_seconds_1m
water_bonus_time = 12.5

#every 15m add extra 12.5 sec to total swimming time
exrta_swimming_time = (distance // 15) * 12.5
total_swimming_time = exrta_swimming_time + time_for_distance

if total_swimming_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_in_seconds - total_swimming_time):.2f} seconds slower.")
