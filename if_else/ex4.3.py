k, n = 5, 7
print(k if k > n else n)

a = 2 
b = 3 
c = -4

max_value = (a if a > c else c) if a > b else (b if b > c else c)
print(max_value)