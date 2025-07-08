from math import sin, pi
from functools import wraps

# zewnetrzny decorator aby przekazac do wewnetrznego decoratora jakis argument
def df_decorator(dx=0.001):
    def func_decorator(func):
        @wraps(func)
        #a mozna zachowac imię w taki sposob, co jest wygodniej
        def wrapper(x, *args, **kwargs):
            return (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx

        # aby zachowac imię mozna jawnie przekazac imię i opis do wrappera
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator(dx=0.001)
# wywołuje się df_decorator przyjmujący dx, wewnątrz ktorego func_decorator przyjmujący sin_df
def sin_df(x):
    """Liczenie pochodnej z sinusa. """
    return sin(x)


# lub reczna dekoracja
f = df_decorator(0.001)(sin_df)

# problem - znika imię i opis dekorowanej funkcji
# do print(sin_df.__name__, sin_df.__doc__) zwrocono wrapper i None

print(sin_df(pi / 3))
print(sin_df.__name__, sin_df.__doc__)
