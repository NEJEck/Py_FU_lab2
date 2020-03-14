a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1 >= b1 >= c1:
    s1 = a1
    s2 = b1
    s3 = c1
elif b1 <= a1 <= c1:
    s1 = c1
    s2 = a1
    s3 = b1
elif a1 >= c1 >= b1:
    s1 = a1
    s2 = c1
    s3 = b1
elif b1 >= a1 and b1 >= c1:
    s1 = b1
    s2 = a1
    s3 = c1
elif b1 >= c1 > a1:
    s1 = b1
    s2 = c1
    s3 = a1
elif c1 > a1 and b1 > a1:
    s1 = c1
    s2 = b1
    s3 = a1
if a2 >= b2 >= c2:
    w1 = a2
    w2 = b2
    w3 = c2
elif b2 <= a2 < c2:
    w1 = c2
    w2 = a2
    w3 = b2
elif a2 >= c2 > b2:
    w1 = a2
    w2 = c2
    w3 = b2
elif b2 > a2 >= c2:
    w1 = b2
    w2 = a2
    w3 = c2
elif b2 >= c2 > a2:
    w1 = b2
    w2 = c2
    w3 = a2
elif c2 > a2 and b2 > a2:
    w1 = c2
    w2 = b2
    w3 = a2
if s1 == w1 and s2 == w2 and s3 == w3:
    print("Boxes are equal")
elif s1 >= w1 and s2 >= w2 and s3 >= w3:
    print("The first box is larger than the second one")
elif w1 > s1 and w2 > s2 and w3 > s3:
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
