n = int(input())
if 5 <= n % 10 <= 9 or n % 10 == 0 or n // 10 == 1:
    print(n, 'коров')
elif n % 10 == 1:
    print(n, 'корова')
else:
    print(n, 'коровы')
