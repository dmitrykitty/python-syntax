lst = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j], end=' ')
    print()
lst1 = []

for i in range(10):
    lst1.append([])
    for j in range(10):
        lst1[i].append(1)

for i in range(10):
    lst1[0][i] = lst1[i][0] = i + 1

for i in range(1, len(lst1)):
    for j in range(1, len(lst1[0])):
        lst1[i][j] = lst1[i][0] * lst1[0][j]
# for i in range(len(lst1)):
#     for j in range(len(lst1[0])):
#         lst1[i][j] = i * j
#
# for i in range(len(lst1)):
#     for j in range(len(lst1[0])):
#         print(str(lst1[i][j]).rjust(3, ' '), end=' ')
#     print()
#
# for i in range(1, 4):
#     for j in range(1, 6):
#         print(f"i = {i}, j = {j}", end=' ')
#     print()
#
# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
# c = []
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print(a[i][j], end=' ')
#     print()
# for i in range(len(b)):
#     for j in range(len(b[0])):
#         print(b[i][j], end=' ')
#     print()
#
# for i in range(len(a)):
#     c.append([])
#     for j in range(len(a[0])):
#         c[i].append(a[i][j] + b[i][j])
#
# for i in range(len(c)):
#     for j in range(len(c[0])):
#         print(c[i][j], end=' ')
#     print()

import sys
sys.stdin = open(0)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i in range(len(lst_in)):
    while lst_in[i].count("  ") != 0:
        lst_in[i] = lst_in[i].replace("  ", ' ')
    lst_in[i] = lst_in[i].replace(' ', '-')
print(lst_in)

#

# n = int(input())
# lst1 = [2]
# for i in range(3, n):
#     lst2 = []
#     for j in range(2, int(i ** 0.5 + 1)):
#         if i % j != 0:
#             lst2.append(0)
#         else:
#             lst2.append(1)
#     if sum(lst2) == 0:
#         lst1.append(i)
# print(*lst1)

# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# suma = 0
# for i in range(len(lst_in)):
#     for j in range(len(lst_in[0])):
#         if lst_in[i][j] == 1:
#             if i > 0 and j > 0:
#                 suma += lst_in[i - 1][j - 1]
#             if i > 0  and j < len(lst_in[0]) - 1:
#                 suma += lst_in[i - 1][j + 1]
#             if i < len(lst_in) - 1 and j > 0:
#                 suma += lst_in[i + 1][j - 1]
#             if i < len(lst_in) - 1 and j < len(lst_in[0]) - 1:
#                 suma += lst_in[i + 1][j + 1]
#             if i > 0:
#                 suma += lst_in[i - 1][j]
#             if j > 0:
#                 suma += lst_in[i][j - 1]
#             if i < len(lst_in) - 1:
#                 suma += lst_in[i + 1][j]
#             if j < len(lst_in[0]) - 1:
#                 suma += lst_in[i][j + 1]
#         if suma != 0:
#             print("НЕТ")
#             break
#     if suma != 0:
#         break
# else:
#     print("ДА")
# print(lst_in)
# suma = 0
# for i in range(len(lst_in)-1):
#     for j in range(len(lst_in[0])-1):
#         suma += lst_in[i][j]
#         suma += lst_in[i+1][j]
#         suma += lst_in[i][j+1]
#         suma += lst_in[i+1][j+1]
#         if suma > 1:
#             break
#         suma = 0
# if suma > 1:
#     print("НЕТ")
# else:
#     print("ДА")


