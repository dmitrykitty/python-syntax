import time


def func_decorator(func):
    # definiujemy dekorator, który przyjmuje funkcję func
    def wrapper():
        # to, co dzieje się przed wywołaniem oryginalnej funkcji:
        print("Before function")
        func()               # wywołujemy oryginalną funkcję bez argumentów
        print("After function")
    return wrapper          # zwracamy nową funkcję „opakowaną”


# przykładowa funkcja, którą rozszerzymy dekoratorem
def some_func():
    print("Inside")



# ręcznie dekorujemy some_func: teraz some_func to już wrapper
some_func = func_decorator(some_func)
some_func()  # -> wydrukuje Before function, Inside, After function


# aby dekorator był uniwersalny - przekazujemy do wrappera args, kwargs
def test_time(func):
    # wrapper przyjmuje dowolne argumenty pozycyjne i nazwane
    def wrapper(*args, **kwargs):
        start_time = time.time()  # rozpoczęcie czasu
        func(*args, **kwargs)  # wywołanie funkcji do testowania
        end_time = time.time()  # koniec
        return end_time - start_time

    return wrapper

@test_time
def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

#pisząc to nie trzeba bezposrednio przekazywac funkcje do dekoratora
@test_time
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# wywołujemy obie funkcje z dekoratorem test_time;
# slow_res i fast_res to odpowiednio czasy wykonania rec_fib(40) i fib(40)
# slow_res = rec_fib(40)
# fast_res = fib(40)


# slower = test_time(rec_fib)
# faster = test_time(fib)

print(rec_fib(30), fib(30))
