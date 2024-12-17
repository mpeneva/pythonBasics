#exam time: hh:mm
exam_begin_hour = int(input())
exam_begin_minute = int(input())

#student time: hh:mm
student_hour = int(input())
student_minute = int(input())

if (exam_begin_hour == student_hour) and (exam_begin_minute == student_minute):
    print("On time")
elif (exam_begin_hour == student_hour + 1) and (exam_begin_minute + 60 >= student_minute + 30):
    counter = 1
    temp_minute_to_hour = 0
    while student_minute == 60:
        temp_minute_to_hour = student_minute + 1
        student_minute += temp_minute_to_hour
        counter += 1


    if counter != 1:
        minute_early = exam_begin_minute - counter
    else:
        minute_early = exam_begin_minute - student_minute
    print("On time")
    print(f"{minute_early} minutes before the start")

elif exam_begin_hour > (student_hour + 1):

    print("Early")

    hour_diff = exam_begin_hour - student_hour
    minutes_temp = hour_diff * 60 + student_minute

    minutes_diff = minutes_temp - exam_begin_minute
    hour_before_start = minutes_diff // 60
    minutes_before_start = minutes_diff % 60

    print(f"{hour_before_start}:{minutes_before_start} hours before the start")

elif (student_hour > exam_begin_hour) or (exam_begin_hour == student_hour) and (exam_begin_minute < student_minute):

    print("Late")
    if (exam_begin_hour == student_hour) and (exam_begin_minute < student_minute):
        minutes_late = student_minute - exam_begin_minute
        print(f"{minutes_late} minutes after the start")
    else:
        diff = student_hour - exam_begin_hour
        exam_temp_hour = exam_begin_hour + diff
        exam_temp_minute = 0
        while diff > 0:
            exam_temp_minute += 60
            diff -= 1
        exam_temp_minute = exam_temp_minute + exam_temp_minute
        exam_temp_minute_diff = exam_temp_minute - student_minute

        hour_late = exam_temp_minute_diff // 60
        minute_late = exam_temp_minute_diff % 60

        if hour_late == 0:
            print(f"{minute_late} minutes after the start")
        else:
            print(f"{hour_late}:{minute_late} minutes after the start")

