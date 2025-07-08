data = input()

def sort_nums(func):
    def wrapper(*args, **kwargs):
        res = sorted(func(*args, **kwargs))
        return res
    return wrapper


@sort_nums
def get_list(s):
    lst = list(map(int, s.split()))
    return lst


lst = get_list(data)
print(*lst)
