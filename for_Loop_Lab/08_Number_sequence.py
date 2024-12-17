n = int(input())
numbers_list = []

for i in range(n):
    entry = int(input())
    numbers_list.append(entry)

numbers_list.sort()

print(f'Max number: {numbers_list[-1]}')
print(f'Min number: {numbers_list[0]}')