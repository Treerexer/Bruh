numbers = [1, -5, 15, 14, -8, -7, 4]
index = []
count = 0
for i in range(len(numbers)):
    if numbers[i] < 0:
        index.append(i)
for i in range(len(index)):
    numbers.pop(index[i]-count)
    count += 1
print(numbers)
