import otwieracz, magazyn, szukacz
from tkinter import *

slownik_przedmiot = otwieracz.potnijPlik("przedmiot.txt")
slownik_polecenie = otwieracz.potnijPlik("czynnosci.txt")
slownik_magazyn = otwieracz.klucze(magazyn.miejsca)

okno = Tk()
okno.geometry("600x800")
okno.title("Widlak")

def wykonaj():
    rozkaz_pociete = polecenie_txt.get().split(" ")

    polecenie_szukaj = str(szukacz.przeszukujPolecenie(slownik_polecenie, rozkaz_pociete))
    przedmiot_szukaj = str(szukacz.przeszukujPolecenie(slownik_przedmiot, rozkaz_pociete))

    miejsce_skad = str(szukacz.przeszukujMiejsceSkad(slownik_magazyn, rozkaz_pociete, "z"))
    miejsce_dokad = str(szukacz.przeszukujMiejsceDokad(slownik_magazyn, rozkaz_pociete))

    stan_wozka = str(magazyn.stan_wozka())

    if stan_wozka == 1:
        magazyn.zmien_stan_wozka(przedmiot_szukaj)

    magazyn.wypisz(magazyn.miejsca)

    wozek = ""
    wozek += stan_wozka
    txt_wozek.delete(0.0, END)
    txt_wozek.insert(0.0, wozek)

    skad = ""
    skad += miejsce_skad
    txt_skad.delete(0.0, END)
    txt_skad.insert(0.0, skad)

    dokad = ""
    dokad += miejsce_dokad
    txt_dokad.delete(0.0, END)
    txt_dokad.insert(0.0, dokad)

    przedmiot = ""
    przedmiot += przedmiot_szukaj
    txt_przedmiot.delete(0.0, END)
    txt_przedmiot.insert(0.0, przedmiot)

    polecenie = ""
    polecenie += polecenie_szukaj
    txt_polecenie.delete(0.0, END)
    txt_polecenie.insert(0.0, polecenie)

    efekt = ""
    efekt += str(magazyn.przemiesc(miejsce_skad, miejsce_dokad))
    txt_efekt.delete(0.0, END)
    txt_efekt.insert(0.0, efekt)


lbl_pol = Label(okno, text = "Wpisz polecenie: ")
lbl_pol.place(x=5, y=20)
polecenie_txt = Entry(okno, width=30)
polecenie_txt.place(x=120, y=20)

btn_wyslij = Button(okno, text = "Wyslij",  command = wykonaj)
btn_wyslij.place(x=120, y=50)

lbl_wozek = Label(okno, text="Wózek: ")
lbl_wozek.place(x=5, y=80)
txt_wozek = Text(okno, width=30, height=1, wrap=WORD)
txt_wozek.place(x=120, y=80)

lbl_przedmiot = Label(okno, text="Przedmiot: ")
lbl_przedmiot.place(x=5, y=110)
txt_przedmiot = Text(okno, width=30, height=1, wrap=WORD)
txt_przedmiot.place(x=120, y=110)

lbl_czynnosc = Label(okno, text="Czynność: ")
lbl_czynnosc.place(x=5, y=140)
txt_polecenie = Text(okno, width=30, height=1, wrap=WORD)
txt_polecenie.place(x=120, y=140)

skad_lbl = Label(okno, text="Skąd: ")
skad_lbl.place(x=5, y=170)
txt_skad = Text(okno, width=30, height=1, wrap=WORD)
txt_skad.place(x=120, y=170)

lbl_dokad = Label(okno, text="Dokąd: ")
lbl_dokad.place(x=5, y=200)
txt_dokad = Text(okno, width=30, height=1, wrap=WORD)
txt_dokad.place(x=120, y=200)

lbl_efekt = Label(okno, text="Efekt: ")
lbl_efekt.place(x=5, y=230)
txt_efekt = Text(okno, width=30, height=2, wrap=WORD)
txt_efekt.place(x=120, y=230)

w = Canvas(okno, width=580, height=450, bg="yellow")
w.place(x=5, y=300)
for i in range(10, 560, 30):
    for j in range(10, 560, 30):
        w.create_rectangle(j, i, j+20, i+20, fill="grey")

okno.mainloop()


