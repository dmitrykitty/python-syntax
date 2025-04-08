N = 100
WIDTH, HEIGHT = 500, 1000


def my_func():
    N = 20  # 20 21 22 ... użyto lokalnej N
    # zeby wewnąrz jakiegoś namespace zmienić globalną zmienną - global
    # działa tylko jak tej zmiennej jeszcze nie ma w tym namespace
    # rowniez w taki sposob można tworzyc zmienne globalne
    global WIDTH
    WIDTH = 250

    global K
    K = 15

    for i in range(5):
        print(i + N, end=" ")
    print()


my_func()  # 100 101 ... użyto globalnej N
print(N)  # 100 -> lokalna N nie zmienia wartosci globalnej

print(K)

x = 0


def outer():
    x = 1

    def inner():
        # aby móc używać tu x z inner - nonlocal x. wtedy już nie tworzyby x w inner, a używamy tego, co mamy w outer
        #nonlocal tylko dla zewnętrznego localnego namespace
        # outer(x) = 2
        nonlocal x
        x = 2
        print("inner", x)

    inner()
    print("outer", x)


outer()
print("global", x)

# PRZED NONLOCAL
# inner 2
# outer 1
# global 0

# PO NONLOCAL
# inner 2
# outer 2
# global 0
