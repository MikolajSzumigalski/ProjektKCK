# wyszukuje polecenia oraz przedmioty z rozkazu wpisanego przez uzytkownika
def przeszukujPolecenie(polecenie, komenda):  # przeszukujemy polecenia, zwracamy i usuwamy je
    i = 0
    j = 0
    s = []
    for i in range(len(komenda)):
        for j in range(len(polecenie)):  # szukanie polecenia do pierwszego wystapienia
            if komenda[i] == polecenie[j]:
                s.append(polecenie[j-j%3]) #dzięki j-j%3 zawsze będzie brał mianownik :)
    return s

# tutaj udało się dać "z" jako parametr
def przeszukujMiejsceSkad(magazyn, komenda, slowo = None):
    for i in range(len(komenda)):
        if (komenda[i] == slowo):
            for j in range(i, len(komenda)):
                for k in range(len(magazyn)):
                    if komenda[j] == magazyn[k]:
                        return komenda[j]
    return 0

# tutaj jak zrobie tak jak powyżej (dodatkowy parametr - słowo) i dam ("na" or "do") jako parametr, to nie widzi "do"
# wiec zostawilem poki co tak jak jest, ale poszukam rozwiazania bo pewnie jakos sie da to zrobic
def przeszukujMiejsceDokad(magazyn, komenda):
    for i in range(len(komenda)):
        if (komenda[i] == ("na" or "do")):
            for j in range(i, len(komenda)):
                for k in range(len(magazyn)):
                    if komenda[j] == magazyn[k]:
                        return komenda[j]
    return 0

""""
zmienic na "jezeli znajdziemy przemiot w danym miejscu,
["z", lokalizacja] jako parametr,
"""
