n = int(input())
m = int(input())
k = int(input())
amount = n*m
length = max(n, m)
width = min(n, m)
result = None
if k > amount:
    result = 'Нельзя'
else:
    for i in range(length):
        if k == length*width:
            result = 'Можно'
            break
        else:
            length -= 1
    if result != 'Можно':
        length = max(n, m)
        for j in range(width):
            if k == length*width:
                result = 'Можно'
                break
            else:
                width -= 1
if result != 'Можно':
    result = 'Нельзя'
print(result)
