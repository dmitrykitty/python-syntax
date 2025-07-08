def say_hello(name):
    def print_name():
        print("Hello, " + name + "!")

    return print_name


hello = say_hello("Dima")
# hello - globalny link do say_hello
# dzieki temu istnieje dostep do name i print_name
hello()


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_two_numbers = outer_function(2)
# add_two_numbers - alias dla zwracanej funkcji(inner_function)
# x jest przekazany do outer_function
# W momencie wywołania tworzony jest obiekt funkcji inner_function,
# który „zapamiętuje” wartość x = 2 (to nazywamy klauzurą, czyli zamknięciem).
print(add_two_numbers(5))


def counter(start_number=0):
    def increment():
        nonlocal start_number
        start_number += 1
        return start_number

    return increment

cnt1 = counter(10)
cnt2 = counter()

print(cnt1(), cnt2()) #11, 1
print(cnt1(), cnt2()) #12, 2
print(cnt1(), cnt2()) #13, 3

def tag_string(tag = "Moja Lubov"):
    def add_tag(string):
        st = '<' + tag + '>' + string + '</' + tag + '>'
        return st
    return add_tag

tagging = tag_string()
print(tagging("Kristinka"))

def change_type(tp):
    def convert(string):
        lst = list(map(int, string.split()))
        return lst if tp == "list" else tuple(lst)
    return convert
tp = input()
data = input()

converter = change_type(tp)
lst = converter(data)
print(lst)