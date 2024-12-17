time_first = int(input())
time_second= int(input())
time_third= int(input())

#total time in seconds
time_total = time_first + time_second + time_third

time_total_minute = time_total // 60 # ? minutes
time_total_seconds = time_total % 60 # ? seconds

if time_total_seconds < 10:
    print(f'{time_total_minute}:0{time_total_seconds}')
else:
    print(f'{time_total_minute}:{time_total_seconds}')