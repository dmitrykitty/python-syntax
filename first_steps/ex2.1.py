import math
num = 7
print(num)  # dynamic typization
num1, num2 = 1, 2
print(num1, num2)
print(type(num1)), print(type(num2))

a = abs(-5)  # wartosc bezwzgledna
b = pow(2, 3)  # 2**3
round(4.5, 1)  # zaokroglenie, dla - 1 dla dych
c = math.ceil(4.5)
d = math.floor(4.5)
f = math.factorial(4)
m = int(6.9)
print(c, d, f, m)

r, h = map(int, input().split())
n, k = map(int, input().split())

# здесь продолжите программу
print(round(math.sqrt(a**2 + b**2), 2))
print(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

print(round(math.pi, 3))