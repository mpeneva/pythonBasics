#exam time: hh:mm
exam_begin_hour = int(input())
exam_begin_minutes = int(input())

#student time: hh:mm
student_hour = int(input())
student_minutes = int(input())

exam_minutes = exam_begin_hour * 60 + exam_begin_minutes
arrived_student_minutes = student_hour * 60 + student_minutes

time_diff = exam_minutes - arrived_student_minutes

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print ("On Time")

hours = abs(time_diff) //60
minutes = abs(time_diff) % 60

result = ''
if hours > 0:
    result += f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'

if time_diff > 0:
    result += f' before the start'
elif time_diff < 0:
    result += f' after the start'

print(result)