plik = open("slownik.txt", "r")
print(plik.read())

slowa = ""

with open('slownik.txt', 'r') as f:
    for line in f:
        for word in line.split():
            print(word)
            slowa += word
            slowa += " "

def potnij_tekst(text):
    words = text.split(" ")
    return words

pociete = potnij_tekst(slowa)
print(pociete)