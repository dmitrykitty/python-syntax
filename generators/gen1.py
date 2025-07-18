gen = (abs(x) for x in range(-3, 3 + 1))  # generator - nie przechowywuje w pamieci wszystkie elementy

for _ in range(5):
    print(next(gen))

"""generator function and yield"""


def gen_func():
    for i in range(3):
        yield i  # zwraca wartość i i kontynje funkcje (robi z kazdej funkcji generator)


a = gen_func()  # obiekt generator

for x in a:
    print(x)

"-----------------------------------------------------------------"


def gen_func2():
    for i in range(1, 10):
        nums = range(i, 11)
        yield sum(nums) / len(nums)


"-----------------------------------------------------------------"


def find_word(word, file):
    # line_index: całkowita liczba znaków przetworzonych z poprzednich linii
    line_index = 0
    # iterujemy po każdej linii w pliku
    for line in file:
        # index: pozycja w bieżącej linii od której szukamy słowa
        index = 0
        # pętla szuka w linii wszystkie wystąpienia słowa
        while index != -1:
            # find zwraca indeks pierwszego wystąpienia od pozycji 'index', albo -1 jeśli brak
            index = line.find(word, index)
            if index != -1:
                # yield zwraca pozycję słowa względem początku pliku
                yield line_index + index
                # przesuwamy start wyszukiwania o 1, by znaleźć kolejne wystąpienia
                index += 1
        # po przeszukaniu linii dodajemy do line_index długość tej linii
        line_index += len(line)


try:
    # otwieramy plik text.txt w trybie odczytu (r)
    with open("text.txt", "r") as f:
        # tworzymy generator find_word, przekażemy słowo i uchwyt do pliku
        c = find_word("python", f)
        # konwertujemy generator na listę wyników i wypisujemy
        print(list(c))
except FileNotFoundError:
    # jeśli plik nie istnieje, wyłapujemy wyjątek i informujemy
    print("File not found")

n = int(input())

"-----------------------------------------------------------------"

def balak_seq(max_len):
    a, b, c = 1, 1, 1
    for i in range(n):
        yield a
        a, b, c, = b, c, a + b + c


print(*balak_seq(n))