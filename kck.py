#slowa z pliku txt do tablicy
#dalem nazwe pliku jako parametr jakbysmy sie zdecydowali na kilka slownikow, wtedy
#mozna dac jeszcze tablice jako parametr, tab 1, tab2, tab3 itd
def otwieracz(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        tablica=[]
        for line in plik:
            for slowo in line.split():
                tablica.append(slowo)
    return tablica

#slowa w slowniku wrzucone do tablicy
slown = otwieracz('slownik.txt')
# print(slown)
#DLUGOSC slownika
# print (len(slown))

#odczytanie komendy od uzytkownika
rozkaz = input("Wpisz rozkaz: ")

#wrzucenie rozkazu do tablicy
def potnij_tekst(tekst):
    words = tekst.split(" ")
    return words

komendy = potnij_tekst(rozkaz)
# print(komendy)

#porownywanie komendy z wpisami w slowniku
tablica_ze_slowani_kluczowymi = []

def porownywarka():
    for i in range(len(komendy)):
        for j in range(len(slown)):
            if komendy[i] == slown[j]:
                tablica_ze_slowani_kluczowymi.append(komendy[i])
    return tablica_ze_slowani_kluczowymi

porownywarka()
print(tablica_ze_slowani_kluczowymi)