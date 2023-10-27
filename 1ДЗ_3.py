numbers = [2, -5, 13, -7, 6, -4]
size = 6
count = 0
index = 0
while index < size:
    if numbers[index] > 0:
        count += 1
        index += 1
    else:
        index += 1
else:
    print(count)
