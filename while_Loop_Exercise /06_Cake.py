#cake size

width = int(input())
height = int(input())
cake_size = width * height

count_pieces = 0
result = ''

while cake_size > count_pieces:
    command = input()

    if command == 'STOP':
        result = f'{cake_size - count_pieces} pieces are left.'
        break

    count_pieces += int(command)
else:
    result = f"No more cake left! You need {count_pieces - cake_size} pieces more."

print(result)