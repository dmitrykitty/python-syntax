s = "Kristinka"
print(s.upper())  # KRISTINKA
print(s.lower())  # kristinka
print(s.count("K"))  # count(symbol, start, end nie włącznie) 1
print(s.upper().count("K"))  # 2
print(s.find("i"))  # find(symbnol, start, end) index pierwszego wystąpienia  2
print(s.find("i", 3))  # find(symbnol, start, end) index pierwszego wystąpienia  5
print(s.find("dima"))  # jak ne ma - zawsze (-1)
print(s.rfind("k"))  # jak find tylko od końca słowa 7
# print(s.index("dim")) #jak find tylko daje ValueError gny nie istnieje symbolu
print(s.replace('i', 'm'))  # replace(stary symbol, nowy symbol, ilość zamian) Krmstmnka
print(s.replace('i', 'm', 1))  # Krmstinka
print(s.isalnum())  # True - czy string składa się tylko z liter
print(s.isdigit())  # False - czy string składa się wyłącznie z liczb
print(s.rjust(12, 'D'))  # rjust(nowa długość, wypełnienie(tylko jeden symbol)) DDDKristinka
print(s.rjust(len(s) + 3, 'D'))  # rjust(nowa długość, wypełnienie(tylko jeden symbol)) DDDKristinka
print(s.ljust(15, 'A'))  # tak samo jak rjust tylko do końca dodaje symboli KristinkaAAAAAA
print(s.split("i"))  # rozbija string przez separator na liste ze stringow ['Kr', 'st', 'nka'], default sep = " "
nums = "1, 3,     4, 5, 2, 1,   5,6"
print(nums.replace(" ", "").split(","))  # ['1', '3', '4', '5', '2', '1', '5', '6']
list_of_nums = nums.replace(" ", "").split(",")
print("".join(list_of_nums)) #symbol ktory stoi pomiedzy elementasmi listy.join(lista)     13452156
print(s.strip()) #usuwa spacje i \n na pocZatku i końcu (lstrip na poczatku, rstrip na końcu)
print(s.lower().capitalize()) #pierwsza litera jako duża
print(s.zfill(14)) #wypełnienie zerami do odpowiedniej długosci
lista = [1, 2, 3]
print(len(lista))

print(s.count('m'))
