text = input()
char_table = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

sum = 0
output = ''
for char in text:
    if char in char_table:
        sum += int(char_table[char])
        output += char + ' + '

print(sum)
# output_length = len(output)
# result = output[0:output_length-2]
# result = output[len(output)-1]
# print(f'{result} = {sum}')
