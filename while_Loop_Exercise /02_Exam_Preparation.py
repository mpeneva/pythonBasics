from os import makedev
tries = int(input())
task_name = input()

bad_mark = 4
good_mark = 0
task_counter = 0
bad_task_counter = 0
last_task = ''

marks_sum = 0
while task_name != 'Enough':
    mark = float(input())
    if mark <= bad_mark :
        bad_task_counter += 1
        if bad_task_counter == tries:
            print(f"You need a break, {bad_task_counter} poor grades.")
            break
    task_counter += 1
    marks_sum += mark
    last_task = task_name
    task_name = input()
    continue

else:
    avarage = marks_sum / task_counter
    print(f"Average score: {avarage:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task}")

