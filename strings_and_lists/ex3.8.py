a = [1, -54, 3, 23, 43, -45, 0]
a.append(100)  # dodaje element na koniec  [1, -54, 3, 23, 43, -45, 0, 100] tylko jeden argument
print(a)
a.insert(3, -100)  # dodaje element pod wskazany index [1, -54, 3, -100, 23, 43, -45, 0, 100]
print(a)
a.remove(100)  # usuwa przez wartosc elementa [1, -54, 3, -100, 23, 43, -45, 0] jak nie istnieje - ValueError
print(a)
a.pop()  # usuwa ostatni element listy [1, -54, 3, -100, 23, 43, -45]
print(a)
a.pop(3)  # usuwa element pod wskazanym indeksem [1, -54, 3, 23, 43, -45]
print(a)
b = a.pop(0)  # pierwszy element listy a b = 1, a = [-54, 3, 23, 43, -45]
# a.clear() #oczyszczenie listy []

# kopia listy z nowym ID
c = a.copy()
c = a[:]
c = list(a)

counter = c.count(23)  # ilość wystąpień wskazanego elementu 1
print(counter)
c.append(23)
counter = c.count(23)  # 2
print(counter)
#c.index(1) #indekx wskazanej liczby od wybranego indeksu (drugi argument) - jak nie ma ValueError
c.reverse() #odwraca kolejność
c.sort() #sortowanie, zmienia listę


# lst = input().split()
# lst.pop(0)
# lst[lst.index('7')] = '8'
# lst.remove('-')
# print("".join(lst))

# s = input()
# lst = s.split()
# print(lst)
# print(lst[0])
# print(f"{lst[2]} {lst[0][0]}. {lst[1][0]}.")

ar = [1, 3, 5, 3, 1, 1, 1, 1, 1, 1]

def del_num(ar, num):
    for i in range(len(ar) - 1, -1, -1):
        if ar[i] == num:
            ar.pop(i)
    return ar

print(del_num(ar, 1))