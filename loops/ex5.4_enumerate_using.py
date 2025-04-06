# factorial

# n1 = int(input('Enter a number: '))
#
# p = 1
# for i in range(1, n1 + 1):
#     p *= i
# print(f"factorial of {n1} = {p}")

# cristmas tree
#
# n2 = int(input('Enter a height of boobies tree: '))
# print('(.)'.rjust(2 * n2 + n2, ' '))
# for i in range(1, n2):
#     lvl = '(.)' * i
#     print(lvl.rjust(n2  * 2 + n2//2 , ' ') + '(.)' + lvl)

lst = []
print(ord('b'))  # ord zwraca numr porządkowy symbolu z tablicy

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
     'shch', '', 'y', '', 'e', 'yu', 'ya'
     ]

start_index = ord('а')
str1 = "Программирование на Python - лучший курс"
new_str = ""

for letter in str1.lower():
    if 'а' <= letter <= 'я':
        current_index = ord(letter)
        new_str += t[current_index - start_index]
    elif letter == 'ё':
        new_str += 'yo '
    else:
        new_str += letter
print(new_str)

# put your python code here
# s = input()
# lst = []
# start_index = 0
# if s.count("ра") == 0:
#     print(-1)
# else:
#     for i in range(s.count("ра")):
#         lst.append(s.find("ра", start_index))
#         start_index = lst[i] + 1
#
# print(*lst)

#
# num = input()
# mask ="+7(xxx)xxx-xx-xx"
# for i, d in enumerate(mask):
#     if d =='x':
#         if not num[i].isdigit():
#             print("НЕТ")
#             break
#         else:
#             continue
#     if d != num[i]:
#         print("НЕТ")
#         break
# else:
#     print("ДА")
#
# num = input()
# indexes = [0, 2, 6, 10, 13]
# chars = ['+', '(', ')', '-', '-']
# j = 0
# for i in range(len(num)):
#     if i not in indexes:
#         if not num[i].isdigit():
#             print("НЕТ")
#             break
#         else:
#             continue
#     if num[i] != chars[j]:
#         print("НЕТ")
#         break
#     else:
#         j += 1
# else:
#     print("ДА")

# put your python code here
# s = input()
# digits = s.replace('+',' ').replace('-',' ')
# lst = list(map(int, digits.split()))
# ind = 1
# suma = lst[0]
#
# for i in s:
#     if i == '+':
#         suma += lst[ind]
#         ind += 1
#     elif i == '-':
#         suma -= lst[ind]
#         ind += 1
#
# print(suma)


# s = input()
# digits = s.replace(' ', '').replace('+',' ').replace('-',' -')
# lst = list(map(int, digits.split()))
# print(sum(lst))
#
lst = list(map(int, input().split()))
l = len(lst)
for i in range(l):
    lst.insert(l - i, lst[l - i - 1])
print(*lst)
