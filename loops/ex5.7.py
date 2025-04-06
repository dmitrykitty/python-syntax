n = int(input())
pascal = []

for i in range(n):
    pascal.append([])
    for j in range(i + 1):
        if j == 0 or j == i:
            pascal[i].append(1)
        else:
            pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])


# width = len(' '.join(f"{x}" for x in pascal[-1]))
#
# for row in pascal:
#     print(f"{' '.join(f'{x}' for x in row):^{width}}")

line = len(' '.join(map(str, pascal[-1])))

for i in pascal:
    print(' '.join(map(str, i)).center(line + 2))