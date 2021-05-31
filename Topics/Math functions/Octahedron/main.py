import math

length = int(input())
area = round(2 * math.sqrt(3) * length ** 2, 2)
volume = round(1 / 3 * math.sqrt(2) * length ** 3, 2)
print(area, volume)
