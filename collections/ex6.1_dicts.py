d = {"house": "cottage", "car": "bmw"}

print(d)
print(d["house"])  # zwacanie sie przez klucz
# funkcja dict(key1=value1, key2=value2...( where key - string)

d2 = dict(one=1, two=2, three=3, four='4')  # klucze przetwarzane do stringow
print(d2)

# funkcja dict wygodna do konwetowqania listy z list z 2 elemtow do dict
lst = [["a", 1], ["b", 2], ["c", 3]]
d3 = dict(lst)  # {'a': 1, 'b': 2, 'c': 3}
print(d3)
d[True] = "Prawda" #dodaje się do dicta d
print(d) #{'house': 'cottage', 'car': 'bmw', True: 'Prawda'}
d[True] = "Nieprawda" #zmiana wartosci pod kluczem True

#długosc - len(d), usunąc element del d[True]

lst = list(input().split())
lst_new = [list(pair.split('=')) for pair in lst]
print(lst_new)
for pair in lst_new:
    pair[1] = int(pair[1])

d = dict(lst_new)
print(*sorted(d.items()))

d = dict([x.split('=') for x in input().split()])

str = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"
lst = [[num] for num in str.split()]
for num in lst:
    num.append(num[0][0:2])
    num = num.reverse()
d = {}
for ars in lst:
    if ars[0] not in d:
        d[ars[0]] = [ars[1]]
    else:
        d[ars[0]].append(ars[1])
print(*sorted(d.items()))

prices = [5768, 2662, 456, 37, 554]
budget = 6224
d = {}
for i in range(len(prices)):
    df = budget - prices[i]
    if prices[i] not in d:
        d[df] = i
    else:
        print([d[prices[i]], i])

