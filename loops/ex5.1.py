
#Sample Input: osnovnye--metody-----slovarey

#Sample Output: osnovnye-metody-slovarey

s = input()
while s.count("--") > 0:
    s = s.replace("--", '-')
print(s)


num = int(input())
result = 1

while num // 10 >= 0 and num != 0:
    result *= num % 10
    num //= 10
print(result)

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
i = 0
while i < len(lst_in):
    if len(lst_in[i].split()) > 1:
        lst_in.pop(i)
        i += 1
    i += 1
print(*lst_in)