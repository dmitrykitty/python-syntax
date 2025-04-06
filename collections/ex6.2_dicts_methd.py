lst = ['+7', '+5', '+6']

a = dict.fromkeys(lst) #tworzy dict z kluczami z listy
#{'+7': None, '+5': None, '+6': None}
b = dict.fromkeys(lst, "DOM") #z value
#{'+7': 'DOM', '+5': 'DOM', '+6': 'DOM'}
a.clear() #robi empty dict a = {}

#kopiowanie dict
c = a.copy()
c = dict(a)

d = {1:'one', 2:'two', 3:'three'}
d.get(1) #otrzymanie cwartosci by key, nie daje Error jak d[1]
#mozna wskazywac co zwroci get: d.get(1, False) zwraca false jak klucza nie ma

d.setdefault(4, "four") #dodaje klucz 4 jak go nie ma, jak jest - nic nie robi
d.pop(1, False) #zwraca wartosc d[1] i usuwa tą parę z dictu (jak nie ma, zwroci False)
d.keys() #zwraca klucze (2 3 4)
for key in d:
    print(key, end=' ')
d.values() #zwraca wartosci (two three four)
for value in d.values():
    print(value, end=' ')
d.items() #zwraca tuples with pairs (key, value) ((2, 'two') (3, 'three') (4, 'four'))
for pair in d.items():
    print(pair, end=' ')
for key, value in d.items(): #(2 = two); (3 = three); (4 = four);
    print(f"({key} = {value});", end=' ')

print()

d.update(b) #dodaje klucze i values z b, a jak klucze się powtarzają, przepisuje pare klucz-value z b
print(d)

# połączyc dwa słowniki
# d3 = {**d, **b} wartosci z jednakowymi kluczami sa brane z drugiego słownika (b)
# z python 3.9 mozna w taki sposob d3 = d | b