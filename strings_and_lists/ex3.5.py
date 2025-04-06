# FORMATOWANIE STRINGOW
age = 23
name = "Dima"
print("Nazywam się " + name + ". Mam " + str(age) + " lata.")  # Nazywam się Dima. Mam 23 lata.
print("Nazywam się {0}. Mam {1} lata".format(name, age))  # Nazywam się Dima. Mam 23 lata.
print("Nazywam się {fio}. Mam {old} lata".format(fio=name.upper(), old=age))  # Nazywam się Dima. Mam 23 lata.
print(f"Nazywam się {name.upper()}. Mam {age + 1} lata")  # Nazywam się DIMA. Mam 24 lata

a, b = map(int, input().split())
print(min(a, b), max(a, b))

dollar = float(input())
rubles_amount = int(input())
print(f"Вы можете получить {int(rubles_amount//dollar)}$ за {rubles_amount} рублей по курсу {dollar}")