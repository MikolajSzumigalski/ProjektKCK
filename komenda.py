rozkaz = input("Wpisz rozkaz: ")


def potnij_tekst(text):
    words = text.split(" ")
    return words

komendy = potnij_tekst(rozkaz)

print(komendy)


def przeszukuj(tekst):
    wsjo = []
    if "przenies" in tekst:
        print("przenosze")
        wsjo += "przenosze"

    if "ustaw" in tekst:
        print("ustawiam")
        wsjo += "ustawiam"

    if "beczke" in tekst:
        print("biore beczke")
        wsjo += "beczke"
    return wsjo

przeszukuj(rozkaz)