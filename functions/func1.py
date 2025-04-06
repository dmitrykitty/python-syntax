def area(a ,b, c):
    return a * b * c

v = area(10, 20, 30 )
v2 = area(b = 5, c = 1, a = 7)
v3 = area(7, c = 11, b = 6) #bez nazwy zmiennej na poczatku

def add_value(value, lst = None): #gdyby zamoast None był [] - zaswsze by był link do tego samego miejsca w pamieci i
    # lista by się ciagle zwiekszała
    if lst is None:
        lst = []
    lst.append(value)
    return lst


lst = add_value(1)
lst2 = add_value(2)
lst3 = add_value(3, lst)
print(lst) #[1, 3]
