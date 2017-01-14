# magazyn jako slownik z kluczami 4x9
miejsca = {'a1': "beczka", 'a2': 0, 'a3': "beczka", 'a4': 0, 'a5': "pudelko", 'a6': 0, 'a7': 0, 'a8': "pudelko", 'a9': 0,
            'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'b5': "beczka", 'b6': 0, 'b7': "puszka", 'b8': 0, 'b9': "opona",
            'c1': 0, 'c2': 0, 'c3': 0, 'c4': "puszka", 'c5': 0, 'c6': "butelka", 'c7': 0, 'c8': 0, 'c9': 0,
            'd1': "butelka", 'd2': "butelka", 'd3': 0, 'd4': "opona", 'd5': 0, 'd6': 0, 'd7': 0, 'd8': 0, 'd9': "beczka"}

#wrzuca 0 tam gdzie puste miejsce i 1 tam gdzie zajete w magazynie po kolei do tablicy, 4x9=36 miejsc w tablicy
tab_miejsca = []
def miejsca_do_tablicy(magazyn):
    for key in sorted(magazyn):
        if magazyn[key] == "beczka":
            tab_miejsca.append("beczka")
        elif magazyn[key] == "puszka":
            tab_miejsca.append("puszka")
        elif magazyn[key] == "opona":
            tab_miejsca.append("opona")
        elif magazyn[key] == "butelka":
            tab_miejsca.append("butelka")
        elif magazyn[key] == "pudelko":
            tab_miejsca.append("pudelko")
        else:
            tab_miejsca.append(0)
miejsca_do_tablicy(miejsca)

# OBSŁUGA WÓZKA:
# 1. robimy wózek widłowy
wozek = {'x': 0, 'y': 0, 'stan' : 0}

# sprawdzamy stan - czy wozek jest wolny
def stan_wozka():
    return wozek['stan']

# jak jest wolny to wrzuc na niego przedmiot
def zmien_stan_wozka(stan):
    wozek['stan'] = stan
    return wozek['stan']

def zmien_polozenie_wozka(x, y):
    wozek['x'] = x
    wozek['y'] = y

def polozenie_wozka():
    return wozek['x'], wozek['y']

#OBSŁUGA MAGAZYNU:
# sprawdz, ktore miejsca w magazynie sa zajete, a ktore nie
def sprawdz_stan(lista):
    for k in sorted(lista):
        if lista[k] == 0:
            print("wolne")
        else:
            print("zajete")


def czy_wolne(miejsca, miejsce):
    if miejsca[miejsce] == 0:
        wolne = True
    else:
        wolne = False
    return wolne

#sprawdzamy, co jest w magazynie
def wypisz(stan_magazynu):
    for key in sorted(stan_magazynu):
        print("%s: %s" % (key, stan_magazynu[key]))



#przemieszczamy przedmiot tylko wtedy, gdy:
#1. mamy podane 'skąd' i 'cel' oraz wózek jest wolny; przedmiot znajduje się w miejscu 'skąd' a miejsce 'cel' jest puste
#2. kiedy nie mamy podane 'skąd', ale mamy podany 'cel' i na wózku znajduje się towar


def przemiesc(skad=None, cel=None, przedmiot=None, polecenie=None):
    if stan_wozka() == 0 and skad != "0" and cel != "0" and przedmiot != "[]" and polecenie != "[]":
        if miejsca[(skad)] == przedmiot[2] and miejsca[(cel)] == 0:  #jesli na wskazanym miejscu w magazynie "skąd" jest przedmiot, to przenosimy we wskazane miejsce
            miejsca[(cel)] = miejsca[(skad)]
            print(miejsca[(skad)])
            x = 0
            for k in sorted(miejsca):
                if skad != k:
                    x += 1
                else:
                    tab_miejsca[x] = 0
            x = 0
            for k in sorted(miejsca):
                if cel != k:
                    x += 1
                else:
                    tab_miejsca[x] = miejsca[(skad)]
            miejsca[(skad)] = 0
            zmien_stan_wozka(0)
            return ("Przeniosłem ", przedmiot," z ", skad, " na ", cel)
        elif miejsca[(skad)] != przedmiot[2]:
            zmien_stan_wozka(0)
            return ("Brak wskazanego przedmiotu na podanym miejscu")
        elif miejsca[(cel)] != 0:
            zmien_stan_wozka(0)
            return ("Miejsce docelowe jest zajęte")
    elif skad == "0" and przedmiot == "[]" and stan_wozka() == 0:
        wspolrzedna_x = cel[1]
        wspolrzedna_y = cel[0]
        zmien_polozenie_wozka(wspolrzedna_x, wspolrzedna_y)
        zmien_stan_wozka(0)
        return ("Jestem przy polu ", cel)
    elif stan_wozka() == 0 and skad != "0" and przedmiot != "[]" and polecenie != "[]":
        if miejsca[(skad)] == przedmiot[2]:
            x = 0
            for k in sorted(miejsca):
                if skad != k:
                    x += 1
                else:
                    tab_miejsca[x] = 0
            zmien_stan_wozka(przedmiot[2])
            return ("Wziąłem ", przedmiot)
        else:
            zmien_stan_wozka(0)
            return("Brak wskazanego przedmiotu na podanym miejscu")
    elif stan_wozka() != 0:
        if cel == "0":
            zmien_stan_wozka(przedmiot[2])
            return ("Wózek jest zajęty")
        elif miejsca[(cel)] != 0:
            zmien_stan_wozka(przedmiot[2])
            return ("Miejsce docelowe jest zajęte")
        elif miejsca[(cel)] == 0:
            x = 0
            for k in sorted(miejsca):
                if cel != k:
                    x += 1
                else:
                    tab_miejsca[x] = przedmiot[2]
            zmien_stan_wozka(0)
            return("Postawiłem ", przedmiot, " na polu ", cel)
        else:

            return("Nie rozumiem, doprecyzuj polecenie")
    else:
        return("error")


""""
#sprawdzamy, czy podane miejsce w magazynie jest wolne
print(czy_wolne(miejsca, "b3"))
#sprawdzamy, czy wózek jest wolny(0), czy zajety( != 0)
print(stan_wozka())
#ładujemy na wózek beczke
zmien_stan_wozka("beczka")
print(stan_wozka())
#i ją ściągamy
zmien_stan_wozka(0)
print(stan_wozka())
#polozenie wózka
print(polozenie_wozka())
#zmieniami
zmien_polozenie_wozka(50, 60)
print(polozenie_wozka())

miejsca_do_tablicy(miejsca)
print(tab_miejsca)

"""
