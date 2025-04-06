from operator import truediv


def os_path_join(*args, **kwargs): #nieokreslona ilosc parametrow, a ** niokreslona ilosc okreslonjych parametrow
    print(args)
    return kwargs['sep'].join(args) #wewnatrz dict z nazwami parametrow i ich wartosciami

p = os_path_join("D:\\study","\\AGH\\","rekrutacja", sep='%')
print(p)

def get_even(*args):
    return [x for x in args if x % 2 == 0]

def get_longest(*args):
    return max(args, key=len) #key wg ktorego sprawdza sie


def get_data_fig(*args, **kwargs):
    per = 0
    for x in args:
        per += x
    t = (per,)
    if 'tp' in kwargs:
        t += (kwargs['tp'],)
    if 'color' in kwargs:
        t += (kwargs['color'],)
    if 'closed' in kwargs:
        t += (kwargs['closed'],)
    if 'width' in kwargs:
        t += (kwargs['width'],)
    return t

def str_min(str1, str2):
    return str1 if str1 < str2 else str2

def str_min3(str1, str2, str3):
    return str_min(str_min(str1, str2), str3)

def str_min4(str1, str2, str3, str4):
    return str_min(str_min3(str1, str2, str3), str4)

