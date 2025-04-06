def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

p = factorial(5)

F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}

def get_structure(path, depth=0):
    for item in path:
        print(" " * 2 * depth, item)
        if type(path[item]) != list:
            get_structure(path[item], depth + 1)
        else:
            print(" " * 2 * (depth + 1), " ".join(path[item]) )

get_structure(F)

N = int(input())

def get_rec_n(num):
    if num > 0:
        get_rec_n(num - 1)
        print(num)

get_rec_n(N)

lst = [8, 11, -5, 4, 3]
n = len(lst) - 1
def get_rec_sum(lst_nums):
    if len(lst_nums) == 1:
        return lst_nums[0]
    else:
        return lst_nums[0] + get_rec_sum(lst_nums[1:])

N = 7

def fib_rec(N, f=[1, 1]):
    if N == 0:
        return f
    else:
        f.append(f[-1] + f[-2])
        return fib_rec(N - 1, f)
print(fib_rec(N))



print(get_rec_sum(lst))