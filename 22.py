import math
a = 12+13
print(a)
b = 78-66
print(b)
c = 11*22
print(c)
d = 52/2
print(d)
e = 6**2
print(e)
a = 5
b = 2
c = a*b
print("面积为:", c)
a = 12*5
print(a)
b = "有没有人告诉你."
print(b)


a = input()
b = input()
if float(a) == 0.0:
    print("0")
else:
    print("结果为:", float(b) / float(a))

a = float(input(1))
b = float(input(2))
c = float(input(1))
delta = b ** 2 - 4 * a * c

if delta < 0:
    print("无实数根")
elif delta == 0:
    x12 = b /(2 * a)
    print("有两个相等的实数根:", x12)
else:
    x1 = (b - math.sqrt(delta)) / (2 * a)
    x2 = (b - math.sqrt(delta)) / (2 * a)
    print("有两个不相等的实数根为:", x1, x2)












