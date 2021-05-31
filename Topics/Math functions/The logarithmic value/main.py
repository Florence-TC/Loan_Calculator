import math

integer = int(input())
base = int(input())

if base <= 0 or base == 1:
    print(round(math.log(integer), 2))
else:
    print(round(math.log(integer, base), 2))
