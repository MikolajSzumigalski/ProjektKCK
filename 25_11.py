magazyn1 = {'a1': "b", 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0, 'a6': 0, 'a7': 0, 'a8': 0, 'a9': 0,
            'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'b5': 0, 'b6': 0, 'b7': 0, 'b8': 0, 'b9': 0,
            'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'c7': 0, 'c8': 0, 'c9': 0,
            'd1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0, 'd6': 0, 'd7': 0, 'd8': 0, 'd9': 0}
# magazyn jako slownik z kluczami 4x10

prz = ""  # string zapisujacy przedmiot
pol = ""  # string zapisujacy polecenie
mag = ""  # string zapisujacy miejsce

#tworzymy wozek
wozek = {'x': 0, 'y': 0, 'zajety' : "b"}


with open('przedmiot.txt', 'r') as f:  # plik z przedmiotami
    for line in f:
        for word in line.split():
            prz += word
            prz += " "

with open('polecenia.txt', 'r') as g:  # plik z poleceniami
    for line in g:
        for word in line.split():
            pol += word
            pol += " "

with open('miejsce.txt', 'r') as m:  # plik z poleceniami
    for line in m:
        for word in line.split():
            mag += word
            mag += " "


def potnij_tekst(text):  # funkcja do dzielenia slow na pojedyncze
    polecenia = text.split(" ")
    return polecenia


# tu tniemy wszystko
przedmiot = potnij_tekst(prz)
polecenie = potnij_tekst(pol)
magazyn = potnij_tekst(mag)

rozkaz = input("Wpisz rozkaz: ")  # Pisalem w Geanny i jak bylo samo input to nie dzialalo...
rozkaz = rozkaz.lower()
komendy = potnij_tekst(rozkaz)  # yu tez tniemy polecenie
print (komendy)

def przeszukujpolecenie():  # przeszukujemy polecenia, zwracamy i usuwamy je
    i = 0
    j = 0
    for i in range(len(polecenie)):
        for j in range(len(komendy)):  # szukanie polecenia do pierwszego wystapienia
            if komendy[j] == polecenie[i]:
                s = komendy[j]
                komendy.remove(komendy[j])
                return s
    return 0


def przeszukujprzedmiot():  # przeszukujemy przedmioty, zwracamy i usuwamy je
    i = 0
    j = 0
    for i in range(len(przedmiot)):
        for j in range(len(komendy)):  # szukanie przedmiotu do pierwszego wystapienia
            if komendy[j] == przedmiot[i]:
                s = komendy[j]
                komendy.remove(komendy[j])
                return s[0]
    return 0


def przeszukujmiejsce():
    for i in range(len(komendy)):
        if (komendy[i] == "z"):
            for j in range(i, len(komendy)):
                for k in range(len(magazyn)):
                    if komendy[j] == magazyn[k]:
                        return komendy[j]
    return 0

def przeszukujmiejsce2():
    for i in range(len(komendy)):
        if (komendy[i] == ("na" or "do")):
            for j in range(i, len(komendy)):
                for k in range(len(magazyn)):
                    if komendy[j] == magazyn[k]:
                        return komendy[j]
    return 0


przedmiot_1 = przeszukujprzedmiot()


print(komendy)
print(przeszukujpolecenie())
print(komendy)
print(przedmiot_1)
print(komendy)

skad = przeszukujmiejsce()
print(skad)

cel = przeszukujmiejsce2()
print(cel)

#wyswietla magazyn w formie pierwotnej
for key in sorted(magazyn1):
    print ("%s: %s" % (key, magazyn1[key]))


if (magazyn1[skad] == przedmiot_1):
    magazyn1[cel] = magazyn1[skad]
    magazyn1[skad] = 0
else:
    print("Brak wskazanego przedmiotu na podanym miejscu")

# wyswietla magazyn po przeniesieniu przedmiotu
for key in sorted(magazyn1):
    print("%s: %s" % (key, magazyn1[key]))

"""
rozbic komendy,
stan wozka i magazynu pomiedzy nimi
np "wez z A1"

"""