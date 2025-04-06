m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
strings = m.split("\n")
print(strings)

#min of 3 numbers
a, b, c = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if c < b:
        print(c)
    else:
        print(b)

m, n = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (m ==2 and n==28) or n == 31 or (n == 30 and (m == 4 or m == 6 or m ==9 or m ==11)):
    print(f"{str(m).rjust(2, '0')}.{n-1} {str(m + 1).rjust(2, '0')}.01")
elif n == 1:
    print(f"{str(m - 1).rjust(2, '0')}.{month[m - 2]} {str(m).rjust(2, '0')}.02")
else:
    print(f"{str(m).rjust(2, '0')}.{str(n-1).rjust(2, '0')} {str(m).rjust(2, '0')}.{str(n + 1).rjust(2, '0')}")

