import math
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