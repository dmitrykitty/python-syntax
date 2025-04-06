t = [27.4, 24, 32.4, 44.1, -5.7]
print(max(t))  # 44.1
print(min(t))  # -5.7
print(sum(t))  # 122.2
print(sorted(t))  # [-5.7, 24, 27.4, 32.4, 44.1] Nie zmienia listy t
print(sorted(t, reverse=True))  # [44.1, 32.4, 27.4, 24, -5.7] Nie zmienia listy t
del t[0]  # usuwa elemnt pod indexem

m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[::-1])  # [3, 2, 2, 5, 5]
