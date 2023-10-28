def fun1(list1):
    for x in list1:
        if list1.count(x) > 1:
            list1.remove(x)


list1 = []
flag = True
while flag:
    inp = input()
    if inp != 'stop input':
        list1.append(inp)
    else:
        flag = False
fun1(list1)
print(list1)
