s = set() #pusty set
st = {1, 2, 3, 4, 5}
st.add(6)
st.update([7, "abc", (1, 2, 3)]) #dodaje dowolny obiekt iterowany
print(st)  #{1, 2, 3, 4, 5, 6, 7, 'abc', (1, 2, 3)}
st.discard(4) #usuwanie elementu
st.remove(5) #usuwa, a jak nie ma - błąd
st.pop() #usuwa dowolny element i zwraca go
st.clear()


setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7}
setC = setA & setB #część wspolna
setC = setA.intersection(setB)
setA.intersection_update(setB) #wynik zapisany w setA

setD = setA | setB #suma: zeby zapisac w setA |= setB
setD.union(setB)

setA -= setB #roznica
setA.difference_update(setB)

setA ^= setB #usuwanie wspolnych elementow
setA.symmetric_difference_update(setB)

#operacje intersection, union, difference, symmetric difference
#moga byc stosowane nie tylko dla setow, ale np set & list lub set | tuple

#jezeli B c A to A > B i odwrotnie, a jezeli ex. elem. c do B ale !c do A - porownanie zawsze daje False
print(setC)

num = int(input())
lst = [2, 3, 5, 7]
set_of_deviders = {1}
i = 0
while num > 1 and i < len(lst):
    if num % lst[i] == 0:
        set_of_deviders.add(lst[i])
        num /= lst[i]
    else:
        i += 1
print("ДА") if set_of_deviders >= {2, 3, 5} else print("НЕТ")