command = ''
marks_sum = 0
marks_count = 0

trainers_count = int(input())

while command != 'Finish':
    current_mark = 0

    #presentation name or 'Finish'
    command = input()
    if command == 'Finish':
        break
    else:
        for i in range(1,trainers_count + 1):
            mark = float(input())
            marks_count += 1
            marks_sum += mark
            current_mark += mark

        print(f"{command} - {(current_mark/trainers_count):.2f}.")

print(f"Student's final assessment is {(marks_sum/marks_count):.2f}.")