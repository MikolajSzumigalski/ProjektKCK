import otwieracz, magazyn, szukacz

# rozkaz od uzytkownika
rozkaz = input("Wpisz rozkaz: ").lower()
rozkaz_pociete = otwieracz.potnij(rozkaz)
# sprawdzenie
# print(rozkaz_pociete)

# tablice ze slowami kluczowymi - przedmiot, polecenie, miejsce w magazynie
slownik_przedmiot = otwieracz.potnijPlik("przedmiot.txt")
slownik_polecenie = otwieracz.potnijPlik("czynnosci.txt")
slownik_magazyn = otwieracz.klucze(magazyn.miejsca)
# sprawdzenie
# print(slownik_magazyn)
# print(slownik_polecenie)
# print(slownik_przedmiot)

#porownanie rozkazow wpisanych przez uzytkownika ze slowami kluczowymi w slownikach_
przedmiot = szukacz.przeszukujPolecenie(slownik_polecenie, rozkaz_pociete)
polecenie = szukacz.przeszukujPolecenie(slownik_przedmiot, rozkaz_pociete)
miejsce_skad = szukacz.przeszukujMiejsceSkad(slownik_magazyn, rozkaz_pociete, "z")
miejsce_dokad = szukacz.przeszukujMiejsceDokad(slownik_magazyn, rozkaz_pociete)

print(przedmiot)
print(polecenie)
print("z ", miejsce_skad)
print("do ", miejsce_dokad)