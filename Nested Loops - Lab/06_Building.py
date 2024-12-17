floor_count = int(input())
flats_per_floor = int(input())

flat_name = ''

for i in range(floor_count, 0, -1):
    for j in range (flats_per_floor):
        if i == floor_count:
            flat_name = f'L{i}{j}'
        elif i % 2 == 0:
             flat_name = f'O{i}{j}'
        else:
            flat_name = f'A{i}{j}'
        print(flat_name, end = ' ')
    print()