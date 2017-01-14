# magazyn jako slownik z kluczami 4x9
miejsca = {'a1': "b", 'a2': 0, 'a3': "b", 'a4': 0, 'a5': 0, 'a6': 0, 'a7': 0, 'a8': 0, 'a9': 0,
            'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'b5': "b", 'b6': 0, 'b7': 0, 'b8': 0, 'b9': 0,
            'c1': 0, 'c2': 0, 'c3': 0, 'c4': "c", 'c5': 0, 'c6': 0, 'c7': 0, 'c8': 0, 'c9': 0,
            'd1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0, 'd6': 0, 'd7': 0, 'd8': 0, 'd9': "b"}

#wrzuca 0 tam gdzie puste miejsce i 1 tam gdzie zajete w magazynie po kolei do tablicy, 4x9=36 miejsc w tablicy
tab_miejsca = []
def miejsca_do_tablicy(magazyn):
    for key in sorted(magazyn):
        if magazyn[key] == "b":
            tab_miejsca.append(1)
        elif magazyn[key] == "c":
            tab_miejsca.append(2)
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
def zmien_stan_wozka(przedmiot):
    wozek['stan'] = przedmiot
    print (wozek['stan'])

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
def przemiesc(skad=None, cel=None):
    if stan_wozka() == 0:
        if skad != None:
            if (miejsca[(skad)] != 0): #jesli na wskazanym miejscu w magazynie "skąd" jest przedmiot, to przenosimy we wskazane miejsce
                miejsca[(cel)] = "b"
                miejsca[(skad)] = 0
                if cel==None:
                    return ("Przedmiot na wózku")
                else:
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
                            tab_miejsca[x] = 1
                    return ("Przeniesiono z ", skad, " na ", cel)

    # skopiowane tylko do sprawdzenia stanu wózka, trzeba przerobić
    elif stan_wozka() != 0:
        if skad != None:
            if (miejsca[(skad)] != 0): #jesli na wskazanym miejscu w magazynie "skąd" jest przedmiot, to przenosimy we wskazane miejsce
                miejsca[(cel)] = "b"
                miejsca[(skad)] = 0
                if cel==None:
                    return ("Przedmiot na wózku")
                else:
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
                            tab_miejsca[x] = 1
                    return ("Przeniesiono z ", skad, " na ", cel)
    else:
        return ("Brak wskazanego przedmiotu na podanym miejscu")


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
