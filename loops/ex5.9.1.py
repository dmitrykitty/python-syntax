t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

lst = [[word for word in string.split() if len(word) > 3] for string in t]
print(lst)

lst_in = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [5, 4, 3]]

A = [[row[j] for row in lst_in] for j in range(len(lst_in[0]))]

for row in A:
    print(*row)