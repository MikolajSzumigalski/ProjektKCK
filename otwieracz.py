# otwiera pliki ze slowami kluczowymi i wrzuca te slowa w
# tablice

def potnijPlik(plik):
    wynik = ""
    with open(plik, 'r') as f:  # plik z przedmiotami
        for line in f:
            for word in line.split():
                wynik += word
                wynik += " "
                pociete = wynik.split(" ")
    return pociete
