a = (1,) #tuple z jednego elementu
b = a[:] #nie robi się kopia
#mozna stosowac jako key dla dict
#zajmuja mniej pamieci
c = ()
c = c + (1,) #zmiana tuple
d = tuple([1, 2, 3])
lst = list(d)

g = (True, [1, 2, 3], "hello", 5)
g[1].append(5) #mozna zmieniac zmieniajace sie elemnty

a.count(1) #liczy ilosc wystepowan elementu
a.index(1) #zwraca index pierwszego znalezionego elementu, mozna dac start idnex oraz end index

# put your python code here
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

N = int(input())
t2 = ()
for i in range(N):
    t2 += (t[i][:N],)




