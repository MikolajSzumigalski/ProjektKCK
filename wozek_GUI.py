import otwieracz, magazyn, szukacz
from tkinter import * #biblioteka ktora obsluguje GUI

slownik_przedmiot = otwieracz.potnijPlik("przedmiot.txt")
slownik_polecenie = otwieracz.potnijPlik("czynnosci.txt")
slownik_magazyn = otwieracz.klucze(magazyn.miejsca)

# szerokosc magazynu - 580px, wysokosc - 450px, 9 kolumn 4 rzedy
# i oraz j oznaczaja rozmiary miejsc w px, i - wysokosc, j - szerokosc
def rysuj_magazyn():
    i = 0
    for y in range(60, 420, 90):  # 360/90 = 4 rzedy: A B C D
        for x in range(20, 560, 60):  # 540/60 = 9 kolumn
            # dodac funkcje if, ktora przeleci po magazynie i tam gdzie bedzie pusto dac szary kwadrat,
            # a tam gdzie cos jest, da czerwony
            if magazyn.tab_miejsca[i] == 0:
                w.create_rectangle(x, y, x + 45, y + 65, fill="grey")
            else:
                w.create_rectangle(x, y, x + 45, y + 65, fill="red")
            i += 1

#inicjuje GUI
okno = Tk()
okno.geometry("600x800")
okno.title("Widlak")

w = Canvas(okno, width=580, height=450, bg="yellow")
w.place(x=5, y=300)

#wozek
w.create_rectangle(400, 400, 480, 480, fill="black")

rysuj_magazyn()

def wykonaj():

    rozkaz_pociete = polecenie_txt.get().split(" ")

    polecenie_szukaj = str(szukacz.przeszukujPolecenie(slownik_polecenie, rozkaz_pociete))
    przedmiot_szukaj = str(szukacz.przeszukujPolecenie(slownik_przedmiot, rozkaz_pociete))

    miejsce_skad = str(szukacz.przeszukujMiejsceSkad(slownik_magazyn, rozkaz_pociete, "z"))
    miejsce_dokad = str(szukacz.przeszukujMiejsceDokad(slownik_magazyn, rozkaz_pociete))

    stan_wozka = str(magazyn.stan_wozka())

    magazyn.zmien_stan_wozka(przedmiot_szukaj)

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
    magazyn.przemiesc(miejsce_skad, miejsce_dokad)
    # magazyn.wypisz(magazyn.miejsca)
    magazyn.miejsca_do_tablicy(magazyn.miejsca)
    rysuj_magazyn()
    print(magazyn.tab_miejsca)
    print(magazyn.stan_wozka())

lbl_pol = Label(okno, text = "Wpisz polecenie: ")
lbl_pol.place(x=5, y=20)
polecenie_txt = Entry(okno, width=30)
polecenie_txt.place(x=120, y=20)

btn_wyslij = Button(okno, text = "Wykonaj",  command = wykonaj)
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

okno.mainloop()
