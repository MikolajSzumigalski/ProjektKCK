plik = open("slownik.txt", "r").read

magazyn = [["beczka",0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # magazyn 4x4 jako tablica
slowa = ""

with open('slownik.txt', 'r') as f:
    for line in f:
        for word in line.split():
            slowa += word
            slowa += " "

def potnij_tekst(text):
    polecenia = text.split(" ")
    return polecenia

pociete = potnij_tekst(slowa)


rozkaz = raw_input("Wpisz rozkaz: ") # Pisalem w Geanny i jak bylo samo input to nie dzialalo...
komendy = potnij_tekst(rozkaz)

i=0
j=0

def przeszukuj(text):
	for i in range(len(i, pociete)):
		for j in range(j, len(komendy)):      #szukanie polecenia do pierwszego wystapienia
			if komendy[j] == pociete[i]
				return  komendy[j]			
		return 0

st = przeszukuj(komendy)

print(st)
print(magazyn[0][0])
