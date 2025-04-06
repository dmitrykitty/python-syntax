# import sys
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# print(lst_in)
# result = []
#
# for i in range(len(lst_in)):
#     for j in range(len(lst_in)):
#         if lst_in[i][j] != lst_in[j][i]:
#             result.append(1)
#             break
#     if sum(result) != 0:
#         print("НЕТ")
#         break
# else:
#     print("ДА")

# lst = list(map(int, input().split()))
#
# for i in range(len(lst) - 1):
#     index = i
#     for j in range(i + 1, len(lst)):
#         if lst[index] > lst[j]:
#             index = j
#     lst[i],lst[index] = lst[index],lst[i]
#
# print(*lst)

# lst = list(map(int, input().split()))
#
# for i in range(len(lst) - 1):
#     for j in range(len(lst) - i - 1):
#         if lst[j] > lst[j + 1]:
#             lst[j],lst[j + 1] = lst[j + 1],lst[j]
# print(*lst)

# put your python code here
n = int(input())
arr = [64, 32, 16, 8, 4, 2, 1]
lst = []
i = 0
while n != 0:
    if n < arr[i]:
        i +=1
    else:
        n -= arr[i]
        lst.append(arr[i])
print(*lst)