n = int(input("matrix size: "))

pointer = 1
value = 2
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(1)

while pointer < (n // 2 + n % 2):
    for i in range(pointer, n - pointer):
        for j in range(pointer, n - pointer):
            matrix[i][j] = value
    pointer += 1
    value += 1

for i in range(len(matrix)):
    print(*matrix[i])
