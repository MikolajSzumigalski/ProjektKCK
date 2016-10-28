magazyn = [["beczka",0,"beczka",0],[0,"skrzynka",0,0],[0,0,0,0],[0,0,0,0]] # magazyn 4x4 jako tablica
prz = "" #string zapisujacy przedmiot
pol = "" #string zapisujacy polecenie
msc = "" #string zapisujacy miejsce

with open('przedmiot.txt', 'r') as f: #plik z przedmiotami
    for line in f:
        for word in line.split():
            prz += word
            prz += " "

with open('polecenia.txt', 'r') as g: #plik z poleceniami
    for line in g:
        for word in line.split():
            pol += word
            pol += " "

def potnij_tekst(text): #funkcja do dzielenia slow na pojedyncze
    polecenia = text.split(" ")
    return polecenia

przedmiot = potnij_tekst(prz) #tu tniemy wszystko
polecenie = potnij_tekst(pol) 


rozkaz = raw_input("Wpisz rozkaz: ") # Pisalem w Geanny i jak bylo samo input to nie dzialalo...
komendy = potnij_tekst(rozkaz) #yu tez tniemy polecenie


def przeszukujpolecenie(text): #przeszukujemy polecenia, zwracamy i usuwamy je
	i=0
	j=0
	for i in range(len(polecenie)):
		for j in range(len(komendy)):      #szukanie polecenia do pierwszego wystapienia
			if komendy[j] == polecenie[i]:
				s = komendy[j]
				komendy.remove(komendy[j])
				return s
	return 0
	
def przeszukujprzedmiot(text): #przeszukujemy przedmioty, zwracamy i usuwamy je
	i=0
	j=0
	for i in range(len(przedmiot)):
		for j in range(len(komendy)):      #szukanie przedmiotu do pierwszego wystapienia
			if komendy[j] == przedmiot[i]:
				s = komendy[j]
				komendy.remove(komendy[j])
				return s
	return 0
	
def przeszukujmiejsce(text): #przeszukujemy miejsca, zwracamy i usuwamy je
	i=0
	j=0
	for i in range(i, len(slownik)):
		for j in range(j, len(komendy)):      #szukanie miejsca do pierwszego wystapienia
			if komendy[j] == slownik[i]:
				return komendy[j]	
	return 0
	
print(komendy)	
print(przeszukujpolecenie(komendy))
print(komendy)
print(przeszukujprzedmiot(komendy))
print(komendy)


