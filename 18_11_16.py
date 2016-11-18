tablica = [["beczka", 0, "beczka", 0], [0, "skrzynka", 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # magazyn 4x4 jako tablica
prz = ""  # string zapisujacy przedmiot
pol = ""  # string zapisujacy polecenie
mag = ""  # string zapisujacy miejsce


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
komendy = potnij_tekst(rozkaz)  # yu tez tniemy polecenie


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
                return s
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


print(komendy)
print(przeszukujpolecenie())
print(komendy)
print(przeszukujprzedmiot())
print(komendy)

skad = przeszukujmiejsce()
print(skad)

cel = przeszukujmiejsce2()
print(cel)

t1=[[0],[0]]
t2=[[0],[0]]

def miejsce_skad1(skad):
	if skad[0] == 'A':
	    return 0
	elif skad[0] == 'B':
		return 1
	elif skad[0] == 'C':
            return 2
	elif skad[0] == 'D':
            return 3
	else:
            return -1

def miejsce_skad2(skad):
    if skad[1] == '1':
        return 0
    elif skad[1] == '2':
        return 1
    elif skad[1] == '3':
        return 2
    elif skad[1] == '4':
        return 3
    else:
        return -1

def miejsce_dokad1(cel):
    if cel[0] == 'A':
        return 0
    elif cel[0] == 'B':
        return 1
    elif cel[0] == 'C':
        return 2
    elif cel[0] == 'D':
        return 3
    else:
        return -1

def miejsce_dokad2(cel):
    if cel[1] == '1':
        return 0
    elif cel[1] == '2':
        return 1
    elif cel[1] == '3':
        return 2
    elif cel[1] == '4':
        return 3
    else:
        return -1

print (miejsce_skad1(skad))
print (miejsce_skad2(skad))
print (miejsce_dokad1(cel))
print (miejsce_dokad2(cel))

tab1 = [[miejsce_skad1(skad)],[miejsce_skad2(skad)]]
print (tab1)
tab2 = [[miejsce_dokad1(cel)],[miejsce_dokad2(cel)]]
print (tab2)

