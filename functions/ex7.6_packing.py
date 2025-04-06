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

lst = input().split() #[Москва Уфа Тверь Самара]
tup2 = (*lst, ) #('Москва', 'Уфа', 'Тверь', 'Самара')
print(tup)

a1, b1 = map(int, input().split())
lst = [*range(a1, b1, 1)] #creating lst from a1 to b1

lst_d = list(map(float, input().split()))
lst_c = input().split()
lst2 = [*lst_d, *lst_c] #sun of two lst
print(*lst2)

lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

d2 = { x.split("=")[0]: x.split("=")[1] for x in lst_in } #tworzenie dicta ze słownika
menu = {**menu, **d2}

