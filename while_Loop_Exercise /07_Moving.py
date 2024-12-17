
width = int(input())
length = int(input())
height = int(input())

capacity = width * length * height
cubic_meters = 0
result = ''

while capacity > cubic_meters:
    command = input()

    if command == 'Done':
        result = f'{capacity - cubic_meters} Cubic meters left.'
        break

    cubic_meters += int(command)
else:
    result = f'No more free space! You need {cubic_meters - capacity} Cubic meters more.'

print(result)

