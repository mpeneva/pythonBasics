command_ch = ""

days_count = 1
distance = 5364
distance_per_day = 0

while  (days_count <= 4) and (distance < 8848):

    command_ch = input()
    if command_ch == "END" :
        break

    elif command_ch == 'Yes':
        distance_per_day = int(input())
        distance += distance_per_day
        days_count += 1

    elif command_ch == 'No':
        distance_per_day = int(input())
        distance += distance_per_day

if distance >= 8848:
    print(f"Goal reached for {days_count} days!")

else:
    print(f"Failed!")
    print(f"{distance}")