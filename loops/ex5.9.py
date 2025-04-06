a = [(i, j) for i in range(3) for j in range(5)]
print(a)  # [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
#           (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
#           (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]

b = [(i, j)
     for i in range(3) if i % 2 == 0
     for j in range(5)
     ]
print(b)  # [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]

c = [f"{i} * {j} = {i * j}"  # tablica umnorzenija
     for i in range(1, 10)
     for j in range(1, 10)]

for i in c:
    print(i)

import sys

# считывание списка из входного потока
lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]

# здесь продолжайте программу (используйте список lst_in)

lst = [x
       for row in lst_in[::-1]
       for x in row[::-1]]
print(*lst)

# from [1, 2, 3, 4, 5, 6, 7, 8, 9] to [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
import math
lst = [int(num) for num in input().split()]

matrix_size = int(math.sqrt(len(lst)))

lst_new = [[i for i in lst[j * 3 : (j + 1) * 3]] for j in range(matrix_size)]
print(lst_new)

t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

lst = [[word for word in string if len(word) > 3] for string in t]
print(lst)