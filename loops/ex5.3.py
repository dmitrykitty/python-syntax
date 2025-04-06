# for i in <...> - iteracja po każdym elemencie w obiekcie

for x in "python":
    print(x)

for i in [1, 2, 3, 4, 5]:
    print(i)

p = 1
d = [1, 2, 3, 4, 5]
for k in d:
    p *= k

print(p)

# range(start, stop, step)
# od 0 do 4
# range(5) or range(0, 5) or range(0,5,1)

print(list(range(0, 5)))  # [0, 1, 2, 3, 4]
list(range(0))  # []

print(list(range(-11, -1, 2)))  # [-11, -9, -7, -5, -3]
print(list(range(-4, -20, -2)))  # [-4, -6, -8, -10, -12, -14, -16, -18]
r = [5, 4, 3, 2, 1]
for i in range(len(r)):
    if r[i] % 2 == 0:
        r[i] *= 2
    else:
        r[i] /= 2
print(r)
#
# n = int(input("Enter a number: "))
# suma = 0
# for i in range(2, n + 1): # sum of 1/2 + 1/3 + ...  1/n
#     suma += 1/i
#
# print(suma)
#
# print(*range(11))  # od razu razpakuje bez tworzenia listy


n = int(input())
lst = []
for i in range(2, int(n**0.5 + 1)):
    if n % i == 0:
        lst.append(1)


print("НЕТ") if sum(lst) >= 1 else print("ДА")

#posledniaja bukwa perwogo goroda = perwoj wtorogo
#Москва Астрахань Новгород Димитровград Душанбе - DA

#1
cities = input().split()
for i in range(0, len(cities) -  1):
    if cities[i][-1] == 'ъ' or cities[i][-1] == 'ы' or cities[i][-1] == 'ь':
        if cities[i][-2] != cities[i + 1].lower()[0]:
            print("НЕТ")
            break
    else:
        if cities[i][-1] != cities[i + 1].lower()[0]:
            print("НЕТ")
            break
else:
    print("ДА")

#2
cities = input().split()
for i in range(len(cities)):
    cities[i] = cities[i].lower().rstrip('ъыь')
for i in range(len(cities) - 1):
    if cities[i][-1] != cities[i + 1][0]:
        print("НЕТ")
        break
else:
    print("ДА")
