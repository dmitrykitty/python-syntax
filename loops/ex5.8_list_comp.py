squere_list = [x**2 for x in range(11)]
print(squere_list) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst2 = [x + 1 for x in range(10)]
print(lst2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst3 = [x / 2 if x % 2 else x for x in range(1, 11)]
print(lst3) #[0.5, 2, 1.5, 4, 2.5, 6, 3.5, 8, 4.5, 10]



# a = [int(x) for x in input("Wrowadz liczby: ").split()]
# print(a)

N = int(input())
lst = [[1 if x == k else 0 for  x in range(N)] for k in range(N)]

for i in lst:
    print(*i)


n = int(input())
lst = [x for x in range(1, n + 1) if n % x == 0]
print(*lst)

import time

lst = [float(num) for num in input().split()]

start_time1 = time.time()  # Zaczynamy pomiar
new_lst = [lst[x] for x in range(0, len(lst), 2)]
end_time1 = time.time()  # Kończymy pomiar

start_time2 = time.time()  # Zaczynamy pomiar
new_lst2 = [num  for i, num in enumerate(lst) if i % 2 == 0]
end_time2 = time.time()  # Kończymy pomiar

print(f"Czas wykonania: {end_time1 - start_time1:.6f} sekundy")
print(f"Czas wykonania: {end_time2 - start_time2:.6f} sekundy")