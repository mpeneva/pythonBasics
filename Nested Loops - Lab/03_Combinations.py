#x1 + x2 + x3 = n

n = int(input())
combinations_count = 0

for i in range(0, n+1):
    for j in range(0, n+1):
        for k in range(0, n+1):
            if i+j+k == n:
                combinations_count += 1

print(combinations_count)
