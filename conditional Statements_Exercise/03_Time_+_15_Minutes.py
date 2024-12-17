hour = int(input())
if 0 > hour > 23 :
    print('wrong hour')

minutes = int(input())
if 0 > minutes > 59 :
    print('wrong minutes')
else:
    #add +15min
    minutes = minutes + 15
    if minutes >= 60:
        minutes = minutes - 60
        hour += 1
        if hour > 24:
            hour = hour - 24
        elif hour == 24:
            hour = 0
        if minutes < 10:
            print(f"{hour}:0{minutes}")
        else:
            print(f"{hour}:{minutes}")
    else:
        print(f"{hour}:{minutes}")




