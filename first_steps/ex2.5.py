import math
a = int(float(input()))
print(a % 3 == 0)

# lub
a = math.trunc(float(input()))
print(a % 3 == 0)

#6
a = float(input())
b = 100*(a - int(a))
print(b > 50)

a = float(input())
print((0 <= a <= 2) or (10<=a<=20))