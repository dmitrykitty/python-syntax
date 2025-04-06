print("xa" * 5) #xaxaxaxaxa
b = "la" * 3
print(len(b))  # 6
print("al" in b)  #True
print(ord('K'), ord('k'))  # numer porządkowyt z tabeli 75, 107

a, c = map(str, input().split())
print((a + " ") * 2 + (c + " ") * 3) # a a b b b

s1 = "krystinka"

s3, s4 = input().split()
print(s3[1:len(s4):2] == s4[1::2])