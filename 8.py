x = int(input())
y = int(input())
if x <= y:
    if (x - 1) % (y - (x - 1)) == 0:
        print('YES')
    else:
        print('NO')
else:
    print("y должен быть больше или равен x")
