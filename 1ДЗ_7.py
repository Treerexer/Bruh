list1 = []
mmax = -10000000000
mmin = 10000000000
for i in range(len(list1)):
    mmax = max(list1[i], mmax)
    mmin = min(list1[i], mmax)
print(mmax, mmin)
