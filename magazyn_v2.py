# magazyn jako slownik z kluczami 4x9
miejsca = {'a1': "b", 'a2': 0, 'a3': "b", 'a4': 0, 'a5': 0, 'a6': 0, 'a7': 0, 'a8': 0, 'a9': 0,
            'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'b5': "b", 'b6': 0, 'b7': 0, 'b8': 0, 'b9': 0,
            'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'c7': 0, 'c8': 0, 'c9': 0,
            'd1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0, 'd6': 0, 'd7': 0, 'd8': 0, 'd9': 0}

# wózek widłowy
wozek = {'x': 0, 'y': 0, 'wolny' : 1}

#jezeli wozek jest wolny
def stan_wozka():
    if wozek['wolny'] == 1:
        return 1
    else:
        return 0

#to wrzuc na niego przedmiot
def zmien_stan_wozka(przedmiot):
    wozek['zajety'] = przedmiot

def zmien_miejsce_wozka(x, y):
    wozek['x'] = x
    wozek['y'] = y

def polozenie_wozka():
    return wozek['x'], wozek['y']


def czy_wolne(miejsca, miejsce):
    for m in miejsca:
        if m[miejsce] != "b":
            wolne = True
        else:
            wolne = False
    return wolne

def wypisz(stan_magazynu):
    for key in sorted(stan_magazynu):
        print("%s: %s" % (key, stan_magazynu[key]))


def przemiesc(skad, cel=None):
    if (miejsca[(skad)] == "b"): #jesli na wskazanym miejscu jest przedmiot to przenosi go na miejsce podane w poleceniu
        miejsca[(cel)] = "b"
        miejsca[(skad)] = 0
        if cel==None:
            return ("Przedmiot na wózku")
        else:
            return ("Przeniesiono z ", skad, " na ", cel)
    else:
        return ("Brak wskazanego przedmiotu na podanym miejscu")
