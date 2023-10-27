ynum = int(input())
if (ynum % 4 == 0 and ynum % 100 != 0) or ynum % 400 == 0:
    print('YES')
else:
    print('NO')
