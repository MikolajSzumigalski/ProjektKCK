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



def miejsce_skad():
	if skad[0] == 'A':
		i=0
	elif skad[0] == 'B':
		i=1
	elif skad[0] == 'C':
		i=2
	elif skad[0] == 'D':
		i=3
	else:
		print("Podaj miejsce")

	if skad[1] == '1':
		j=0
	elif skad[1] == '2':
		j=1
	elif skad[1] == '3':
		j=2
	elif skad[1] == '4':
		j=3
	else:
		print("Podaj miejsce skad zabrac towar(np, z A2, z B4)")

def miejsce_dokad():
	if cel[0] == 'A':
		i=0
	elif cel[0] == 'B':
		i=1
	elif cel[0] == 'C':
		i=2
	elif cel[0] == 'D':
		i=3
	else:
		print("Podaj gdzie przemiescic towar (np. na B1, do A2)")

	if cel[1] == '1':
		j=0
	elif cel[1] == '2':
		j=1
	elif cel[1] == '3':
		j=2
	elif cel[1] == '4':
		j=3
	else:
		print("Podaj gdzie przemiescic towar (np. na B1, do A2)")
