x, *y = (1, 2, 3, 4) #x = 1, y = [2, 3, 4]
a, *b, c = (1, 2, 3, 4, 5) #a = 1, b = [2, 3, 4], c = 5 packing do *b
#to samo zona robic nie tylko z tuplami, ale ze wszystkimi iterowalnymi obiektami
*r, v, m = "Hello Python" #['H', 'e',...], v = 'o', m = 'n'
lst = [1, 2, 3]
tup = (*lst, ) #(1, 2 ,3) unpacking
d = -5, 5
l = list(range(*d)) #[-5, -4 .... 4] lub w taki sposob [*range(*d)]
d = {1: "Bad", 2:"Good"} #{**d} = {1: 'Bad', 2: 'Good'} - to samo, nie ma sensu, ale mozna łączyc kilka słownikow
k = {3:"Exellent"}
q = {**d, **k} #{1: 'Bad', 2: 'Good', 3: 'Exellent'}