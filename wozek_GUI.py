import otwieracz, magazyn, szukacz
from tkinter import *

slownik_przedmiot = otwieracz.potnijPlik("przedmiot.txt")
slownik_polecenie = otwieracz.potnijPlik("czynnosci.txt")
slownik_magazyn = otwieracz.klucze(magazyn.miejsca)

class Application(Frame):
    def __init__(self, okno):
        super(Application, self).__init__(okno)
        self.grid()
        self.okno_polecenia()

    def okno_polecenia(self):
        Label(self, text = "Wpisz polecenie: ").grid(row=0, column=0, sticky=W)
        self.polecenie_txt = Entry(self, width=50)
        self.polecenie_txt.grid(row=1,  column=0, columnspan=2, sticky=W)

        self.wyslij = Button(self, text = "Wyslij",  command = self.wykonaj)
        self.wyslij.grid(row=2, column=0, sticky=W)

        Label(self, text="Przedmiot: ").grid(row=4, column=0, sticky=W)
        self.przedmiot = Text(self, width=30, height=1, wrap=WORD)
        self.przedmiot.grid(row=4, column=1, sticky=W)

        Label(self, text="Przedmiot: ").grid(row=4, column=0, sticky=W)
        self.przedmiot = Text(self, width=30, height=1, wrap=WORD)
        self.przedmiot.grid(row=4, column=1, sticky=W)

        Label(self, text="Skąd: ").grid(row=5, column=0, sticky=W)
        self.skad = Text(self, width=30, height=1, wrap=WORD)
        self.skad.grid(row=5, column=1, sticky=W)

        Label(self, text="Dokąd: ").grid(row=6, column=0, sticky=W)
        self.dokad = Text(self, width=30, height=1, wrap=WORD)
        self.dokad.grid(row=6, column=1, sticky=W)

        Label(self, text="Efekt: ").grid(row=7, column=0, sticky=W)
        self.efekt = Text(self, width=30, height=2, wrap=WORD)
        self.efekt.grid(row=7, column=1, sticky=W)


    def wykonaj(self):

        rozkaz_pociete = self.polecenie_txt.get().split(" ")

        polecenie_szukaj = str(szukacz.przeszukujPolecenie(slownik_polecenie, rozkaz_pociete))
        przedmiot_szukaj = str(szukacz.przeszukujPolecenie(slownik_przedmiot, rozkaz_pociete))

        miejsce_skad = str(szukacz.przeszukujMiejsceSkad(slownik_magazyn, rozkaz_pociete, "z"))
        miejsce_dokad = str(szukacz.przeszukujMiejsceDokad(slownik_magazyn, rozkaz_pociete))

        magazyn.wypisz(magazyn.miejsca)

        skad = ""
        skad += miejsce_skad
        self.skad.delete(0.0, END)
        self.skad.insert(0.0, skad)

        dokad = ""
        dokad += miejsce_dokad
        self.dokad.delete(0.0, END)
        self.dokad.insert(0.0, dokad)

        przedmiot = ""
        przedmiot += przedmiot_szukaj
        self.przedmiot.delete(0.0, END)
        self.przedmiot.insert(0.0, przedmiot)

        efekt = ""
        efekt += str(magazyn.przemiesc(miejsce_skad, miejsce_dokad))
        self.efekt.delete(0.0, END)
        self.efekt.insert(0.0, efekt)


root = Tk()
root.title("Wózek widłowy")
root.geometry("500x300")
app = Application(root)
magazyn.wypisz(magazyn.miejsca)
root.mainloop()

