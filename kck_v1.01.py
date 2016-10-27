#wersja 1.01
#
#poprawilem porownywarke, najpierw wrzuca do tablicy slowa w kolejnosci, w jakiej wystepuja w slowniku,
#moze sie przydac przy rozczytywaniu intencji uzytownika
#
#slowa z pliku txt do tablicy
#dalem nazwe pliku jako parametr jakbysmy sie zdecydowali na kilka slownikow, wtedy
#mozna dac jeszcze tablice jako parametr, tab 1, tab2, tab3 itd

def otwieracz(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        tablica=[]
        for linia in plik:
            for slowo in linia.split():
                tablica.append(slowo)
    return tablica

#slowa w slowniku wrzucone do tablicy
slownik = otwieracz('slownik.txt')


#odczytanie komendy od uzytkownika i zamiana duzych liter na male
rozkaz = input("Wpisz rozkaz: ").lower()

#wrzucenie rozkazu do tablicy
def potnij_tekst(tekst):
    words = tekst.split(" ")
    return words

komendy = potnij_tekst(rozkaz)
# print(komendy)

#porownywanie komendy z wpisami w slowniku
tablica_ze_slowani_kluczowymi = []

def porownywarka():
    for s in slownik:
        for k in komendy:
            if s == k:
                tablica_ze_slowani_kluczowymi.append(s)
    return tablica_ze_slowani_kluczowymi

porownywarka()
print(tablica_ze_slowani_kluczowymi)
