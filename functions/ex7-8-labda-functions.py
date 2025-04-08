a, b = 5, 10

var = lambda a, b: a + b #lambda <co przyjmuje> : <wynik, ktory zwraca po działaniach>
#moze byc elementem dowolnej konstrukcji
var(a, b)

lst = [4, 5, lambda: print("lambda!!!"), 7, 8 ]
lst[2]() #lambda!!!


lst2 = [5, 3, 0, -6, 7, 10, -1]

def get_filter(arr, filter_func=None):
    if filter_func is None:
        return arr
    res = []
    for item in arr:
        if filter_func(item):
            res.append(item)

    return res

r = get_filter(lst2, lambda x: x & 1 != 1 )

x = float(input())

res = lambda  x : x * (-1) if x < 0 else x
print(res(x))


get_div = lambda c, d: c / d if d else None

print(r)

print((lambda s: "ra" in s)(input()))

digs = list(map(int, input().split()))
print(digs)