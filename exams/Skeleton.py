control_time_minutes = int(input())
control_time_seconds = int(input())
length_m = float(input())
length_100m_second = int(input())

control_time = control_time_minutes * 60 + control_time_seconds
slow_time_distance_Count = length_m / 120 #на всеки 120 метра неговото време намаля с 2.5 секунди
ramp_slow_time_sec = slow_time_distance_Count * 2.5
#total Martin's time
total_time_sec =  (length_m / 100) * length_100m_second - ramp_slow_time_sec

if control_time >= total_time_sec:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time_sec:.3f}.")
else:
    print(f"No, Marin failed! He was {total_time_sec-control_time:.3f} second slower.")