# UVP — rešeni izpiti 2023/24

Vsi trije izpitni roki predmeta **Uvod v programiranje** iz študijskega leta
2023/24, z rešitvami in razlagami. Skupaj **9 nalog po 3 podnaloge = 27 rešitev**.

Vsaka podnaloga ima:

1. **besedilo naloge** (dobesedno iz izpitne datoteke),
2. **rešitev**, ki jo lahko kopiraš,
3. **razlago** — ideja, zakaj deluje in kje se da pasti.

> ✅ **Vse rešitve so preverjene.** Vsaka je bila pognana skozi teste, ki so
> vgrajeni v izpitne datoteke Projekta Tomo, in vseh 27 podnalog je označenih
> kot »ima veljavno rešitev«. Koda v tem dokumentu je zajeta neposredno iz teh
> datotek, zato se z njimi ne more razhajati.

**Kazalo**

| Izpit | Naloga | Snov |
|---|---|---|
| [2324/1](#izpit-1-rok-202324) | [Urejanje z zlivanjem](#naloga-1--urejanje-z-zlivanjem) | rekurzija, deli in vladaj, seznami |
| | [Pesnik France: slovenska abeceda](#naloga-2--pesnik-france-slovenska-abeceda) | razredi, posebne metode, urejanje s ključem |
| | [Avtobusni prevozi](#naloga-3--avtobusni-prevozi) | datoteke, slovarji seznamov, množice |
| [2324/2](#izpit-2-rok-202324) | [Izštevanke](#naloga-1--izštevanke) | krožno štetje, modulo, brisanje iz seznama |
| | [Pesnik France: popravljanje kode](#naloga-2--pesnik-france-popravljanje-kode) | datoteke, obdelava vrstic, regularni izrazi |
| | [Kodiranje v bazi 64](#naloga-3--kodiranje-v-bazi-64) | slovarji, rezine fiksne dolžine, obrnjena preslikava |
| [2324/3](#izpit-3-rok-202324) | [Pesnik France: zlogi in ritem](#naloga-1--pesnik-france-zlogi-in-ritem) | nizi, sosedni znaki, vzorci |
| | [Pogosti znaki](#naloga-2--pogosti-znaki) | slovarji, gnezdeni nabori, rekurzija |
| | [Osebe](#naloga-3--osebe) | razredi, razčlenjevanje EMŠO, urejanje po dveh ključih |

Sorodni dokumenti v tem repozitoriju:

- [`uvod_v_programiranje_zapiski.md`](uvod_v_programiranje_zapiski.md) — teorija in pregled jezika,
- [`vaje_in_naloge.md`](vaje_in_naloge.md) — dodatne vaje po temah.

---

## Izpit 1. rok 2023/24
Prvi rok je klasična kombinacija: ena naloga o **rekurziji**, ena o
**razredih** in ena o **datotekah**. Ta razpored se v vseh treh rokih ponovi.

### Naloga 1 — Urejanje z zlivanjem
*Datoteka `2324_i1/01_urejanje_z_zlivanjem.py`*

Naloga te po korakih pripelje do algoritma *merge sort*. Podnaloge so odvisne
druga od druge: druga uporablja prvo, tretja drugo. Če ti prva ne uspe, jo
vseeno napiši po svoje — nadaljnji dve se ocenjujeta posebej.

#### a) `v_katerem_je_manjsi(sez1, sez2)`

Sestavite funkcijo `v_katerem_je_manjsi`, ki kot argumenta prejme dva
seznama ter vrne tistega v katerem je prvi element manjši (če sta prva elementa enaka, lahko vrne kateregakoli). Če je en od seznamov
prazen, naj funkcija vrne drugega. Predpostavite lahko, da oba seznama hkrati nista
prazna.

```python
>>> v_katerem_je_manjsi([1, 2, 3], [4, 5, 6])
[1, 2, 3]
>>> v_katerem_je_manjsi([1, 2], [])
[1, 2]
```

```python
def v_katerem_je_manjsi(sez1, sez2):
    if sez1 == []:
        return sez2
    if sez2 == []:
        return sez1
    if sez1[0]>sez2[0]:
        return sez2
    else:
        return sez1
```

**Ideja.** Funkcija je pomožno orodje za naslednji podnalogi: pove, iz katerega
seznama vzeti naslednji element. Vrstni red preverjanj ni poljuben — najprej
odpravimo prazna seznama, šele nato smemo pogledati `sez1[0]` in `sez2[0]`.

**Zakaj vrniti prav ta objekt.** Test preverja
`v_katerem_je_manjsi(a, b) is a`, torej z operatorjem `is` (identiteta), ne z
`==` (enakost vsebine). Zato je treba vrniti **prejeti seznam** in ne kopije:
`return sez1` je pravilno, `return sez1[:]` ali `return list(sez1)` bi padlo,
čeprav bi bila vsebina enaka.

**Pasti.**

- Če bi primerjavo `sez1[0] > sez2[0]` napisal pred preverjanjem praznosti, bi
  pri praznem seznamu dobil `IndexError`.
- Pri enakih prvih elementih naloga dovoli katerikoli seznam; ker je pogoj
  strogi `>`, funkcija v tem primeru vrne `sez1`.
- Funkcija primerja samo z `>`, zato deluje za vse primerljive elemente — tudi
  za nize (`["a", "b"]` proti `["c", "d"]`).

#### b) `zlij(a, b)`

Seznama `a` in `b` zlijemo tako, da ustvarimo nov seznam in ga napolnimo s ponavljem sledečega postopka.  Izberemo element iz tistega seznama, kjer je prvi element manjši, tj., če je prvi element v `a` manjši od prvega v `b` v nov seznam izberemo prvi element iz `a`, sicer pa iz `b`. Izbrani element nato dodamo v nov seznam in ga zavržemo iz seznama, iz katerega izvira. Postopek ponavljamo, dokler ne dodamo vseh elementov iz `a` in `b`.

Sestavite funkcijo `zlij`, ki zlije seznama, ki ju prejme kot argumenta.

```python
>>> zlij([1, 2, 3], [4, 5, 6])
[1, 2, 3, 4, 5, 6]
>>> zlij([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
>>> zlij([3], [2, 4, 6])
[2, 3, 4, 6]
```

```python
def zlij(a, b):
    # BAZNI PRIMER — vedno ga napiši prvega, še preden veš, kako gre korak.
    # Če je eden prazen, je rezultat kar drugi. Pokrije tudi primer,
    # ko sta prazna oba, ker je [] + [] == [].
    if a == [] or b == []:
        return a + b

    manjsi = v_katerem_je_manjsi(a, b)

    # Drugi seznam po izločanju: če je manjši ravno a, je večji b, sicer a.
    # `is` primerja identiteto (ali je to isti objekt), ne vsebine.
    vecji = b if manjsi is a else a

    # [manjsi[0]] — oglati oklepaji naredijo iz elementa seznam z enim elementom,
    # da ga lahko seštejemo z rezultatom rekurzivnega klica (seznam + seznam).
    # manjsi[1:] je isti seznam brez prvega elementa = MANJŠI problem.
    return [manjsi[0]] + zlij(manjsi[1:], vecji)
```

**Ideja (rekurzija).** Zlivanje dveh **že urejenih** seznamov: vzemi manjšo od
obeh glav, jo daj na začetek in rekurzivno zlij preostanek. Bazni primer je,
ko je eden prazen — takrat je rezultat kar drugi seznam.

**Trije drobci, ki jih je vredno prepoznati.**

- `a + b` v baznem primeru pokrije tudi možnost, da sta prazna oba (`[] + []`).
- `[manjsi[0]]` — glavo je treba oviti v seznam, ker `+` združuje seznam s
  seznamom, ne seznama z elementom.
- `manjsi is a` — spet identiteta. Če bi pisal `manjsi == a`, bi pri seznamih
  z enako vsebino (npr. `zlij([1], [1])`) dobil napačen »drugi« seznam.

**Alternativa z zanko** (brez rekurzije, hitrejša, ker ne dela rezin):

```python
def zlij(a, b):
    i = j = 0
    rezultat = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            rezultat.append(a[i])
            i += 1
        else:
            rezultat.append(b[j])
            j += 1
    return rezultat + a[i:] + b[j:]
```

**Zahtevnost.** Rekurzivna različica naredi za vsak element novo rezino
(`manjsi[1:]`), kar je O(n²) kopiranja; različica z indeksi je O(n). Na izpitu
to ni sporno, v praksi pa je razlika velika.

#### c) `uredi(sez)`

Postopek *urejanja* sprejme seznam elementov in vrne seznam, v katerem
so elementi originalnega seznama našteti po vrsti (v naraščajočem vrstnem redu). Eden
od pristopov za urejanje je *urejanje z zlivanjem*. Pri urejanju z zlivanjem vhodni
seznam razdelimo na pol, __rekurzivno__ uredimo polovici in ju nato zlijemo. Rekurzija se ustavi, ko najdemo seznam, ki ne more biti neurejen (namig: seznami katerih dolžin so vedno urejeni?).

Sestavite funkcijo `uredi`, ki sprejme seznam in ga uredi po postopku urejanja z zlivanjem, tj., ne uporablja vgrajenih metod za urejanje.

```python
>>> uredi([1, 3, 2, 5, 6, 7, 8, 4])
[1, 2, 3, 4, 5, 6, 7, 8]
```

```python
def uredi(sez):
    # BAZNI PRIMER: seznam dolžine 0 ali 1 je že urejen.
    # POZOR: pogoj mora biti <= 1, NE == [].
    # Pri seznamu z enim elementom je sredina = 0, torej sez[:0] == []
    # in sez[0:] == sez — rekurzija bi se spet vrtela v neskončnost.
    if len(sez) <= 1:
        return list(sez)

    # Razdeli na pol ...
    sredina = len(sez) // 2

    # ... rekurzivno uredi obe polovici in ju zlij s funkcijo iz 2. podnaloge.
    return zlij(uredi(sez[:sredina]), uredi(sez[sredina:]))
```

**Ideja (deli in vladaj).** Seznam razpolovimo, vsako polovico **rekurzivno**
uredimo in urejeni polovici zlijemo s funkcijo iz prejšnje podnaloge. To je
urejanje z zlivanjem (*merge sort*) in teče v času O(n log n).

**Bazni primer je ključen.** Mora biti `len(sez) <= 1`, ne `sez == []`. Pri
seznamu z enim elementom je `sredina = 1 // 2 = 0`, torej bi bila
`sez[:0] == []` in `sez[0:] == sez` — druga polovica bi bila cel seznam in
rekurzija se ne bi nikoli ustavila (`RecursionError`).

**Zakaj `list(sez)` in ne `sez`.** Vrnemo novo listo, da klicatelju ne vrnemo
istega objekta, ki bi ga lahko kdo kasneje spremenil. Za teste ni nujno, je pa
lepše.

**Preverjanje razumevanja.** Zaporedje klicev za `[3, 1, 2]`:
`uredi([3])` → `[3]`, `uredi([1, 2])` → `zlij([1], [2])` → `[1, 2]`,
na koncu `zlij([3], [1, 2])` → `[1, 2, 3]`.

### Naloga 2 — Pesnik France: slovenska abeceda
*Datoteka `2324_i1/02_pesnik_france.py`*

Naloga o razredih in posebnih metodah. Jedro je spoznanje, da Python nizov ne
zna urejati po slovenski abecedi, in da lahko to popravimo tako, da povemo,
kako se naši objekti primerjajo.

#### a) Razred `Beseda` (`__init__`, `__repr__`, `__str__`, `__getitem__`)

Definiraj razred Beseda, ki bo deloval podobno kot Pythonov niz, le da bo
prilagojen slovenski abecedi. Razred naj vsebuje naslednje metode:

- konstruktor `__init__(self, beseda)`, ki sprejme običajen Pythonov niz `beseda`
  in ga shrani v ustrezen atribut,
- metodo `__repr__(self)`, ki simulira klic konstruktorja (glej spodaj),
- metodo `__str__(self)`, ki vrne kar shranjeno besedo iz prve alineje,
- metodo `__getitem__(self, i)`, ki vrne i-ti znak besede. Z njeno pomočjo lahko
  dostopamo do posameznih znakov oz. rezin, kot smo že navajeni.

Primer:

```python
>>> a = Beseda('france')
>>> a
Beseda('france')
>>> str(a)
'france'
>>> (a[0], a[1:5], a[-1])
('f', 'ranc', 'e')
```

```python
# Slovenska abeceda po vrsti. Indeks črke v tem nizu je njena "vrednost" pri
# urejanju. Prav to Pythonu manjka: on ureja po kodah Unicode, kjer so č, š in ž
# šele ZA z — zato sorted("čšzž") vrne ['z', 'c', 's', 'z'] po napačnem vrstnem redu.
ABECEDA = 'abcčdefghijklmnoprsštuvzž'


def kljuc(niz):
    """Niz pretvori v seznam indeksov v slovenski abecedi: 'ce' -> [2, 4].

    Sezname Python primerja leksikografsko (element za elementom, prvi
    različni odloči), zato je primerjava dveh takih seznamov ravno
    primerjava po slovenski abecedi. To je isti prijem kot `key=` pri sorted.
    """
    # .find vrne -1, če znaka ni v abecedi (npr. presledek); tak znak se
    # uvrsti pred vse črke in ne sesuje programa — .index bi vrgel ValueError.
    return [ABECEDA.find(znak) for znak in niz]


class Beseda:

    def __init__(self, beseda):
        # Konstruktor samo shrani vrednost v atribut in NE VRAČA ničesar.
        self.beseda = beseda

    def __repr__(self):
        # __repr__ mora simulirati KLIC KONSTRUKTORJA:  Beseda('france')
        # !r pomeni "uporabi repr namesto str", torej z narekovaji okoli niza.
        return f'Beseda({self.beseda!r})'

    def __str__(self):
        # __str__ je človeški izpis: samo beseda, brez narekovajev.
        # __str__ in __repr__ NISTA isto — testi ju ločujejo.
        return self.beseda

    def __getitem__(self, i):
        # i je lahko število (a[0]) ali rezina (a[1:5]) — oboje zna že navaden
        # niz, zato delo preprosto prepustimo njemu.
        return self.beseda[i]
```

**Zakaj sploh razred.** Python nize ureja po kodah Unicode, kjer so `č`, `š` in
`ž` **za** črko `z`. Zato `sorted(['čas', 'dan'])` vrne napačen slovenski
vrstni red. Rešitev je preslikati vsak znak v njegov **indeks v slovenski
abecedi** in primerjati sezname števil — sezname Python primerja
leksikografsko (element za elementom, prvi različni odloči), kar je natanko
tisto, kar potrebujemo.

**Posebne (dunder) metode.**

| Metoda | Kdaj se pokliče | Kaj mora vrniti |
|---|---|---|
| `__init__` | ob `Beseda('france')` | nič (samo shrani v atribute) |
| `__repr__` | ob `a` v konzoli, ob `repr(a)` | niz, ki **simulira klic konstruktorja** |
| `__str__` | ob `print(a)`, `str(a)` | človeku prijazen izpis |
| `__getitem__` | ob `a[0]`, `a[1:5]` | element oz. rezino |

`__str__` in `__repr__` **nista isto** in testi ju ločujejo: prvi vrne
`'france'`, drugi `"Beseda('france')"`. Zapis `{self.beseda!r}` v f-nizu pomeni
»uporabi `repr`«, kar sam poskrbi za narekovaje.

**`__getitem__` in rezine.** Ko napišeš `a[1:5]`, Python metodi poda objekt
`slice(1, 5)`. Ker delo preprosto prepustimo shranjenemu nizu
(`return self.beseda[i]`), rezine delujejo same od sebe.

**`.find` namesto `.index`.** `.find` vrne `-1`, če znaka ni v abecedi (npr.
presledek ali vejica), `.index` pa bi sprožil `ValueError`. Znak z indeksom
`-1` se uvrsti pred vse črke, kar je za našo rabo povsem sprejemljivo.

#### b) `__lt__(self, other)` — primerjava po slovenski abecedi

V razred dodaj metodo `__lt__(self, other)`, ki vrne `True`,
če je `self` (leksikografsko glede na slovensko abecedo) manjši od `other`,
sicer pa vrne `False`.

```python
>>> a = Beseda("copat")
>>> b = Beseda("čevelj")
>>> a < b
True
>>> a < a
False
```

```python
# POZOR NA ZAMIK: ta metoda je zamaknjena za štiri presledke, ker je še
    # vedno del razreda Beseda iz 1. podnaloge. Vmesne vrstice z opisom naloge
    # Pythona ne motijo — komentarji in prazne vrstice ne zaključijo telesa
    # razreda. Če bi metodo napisal na levi rob, ne bi bila metoda.
    def __lt__(self, other):
        # Ko Python naleti na  a < b, pokliče a.__lt__(b).
        # Zaradi tega zna sorted() urejati kar objekte tipa Beseda.
        # str(other) pokliče __str__ in vrne navaden niz, tako metoda deluje
        # tudi, če je na desni strani navaden niz namesto Besede.
        return kljuc(self.beseda) < kljuc(str(other))
```

**Ideja.** Ko Python naleti na `a < b`, pokliče `a.__lt__(b)`. Ker naša metoda
primerja **seznama indeksov** namesto nizov, dobimo slovenski vrstni red. Stranski
učinek: `sorted` in `min`/`max` znajo od zdaj naprej urejati objekte `Beseda`.

**Pozor na zamik.** To je najpogostejša napaka pri tej nalogi. Metoda je
zamaknjena za štiri presledke, ker je še vedno del razreda iz prejšnje
podnaloge — vmesne vrstice z besedilom naloge Pythona ne motijo, saj komentarji
in prazne vrstice telesa razreda ne zaključijo. Če jo napišeš na levi rob,
postane navadna funkcija in `a < b` ne bo delovalo.

**`str(other)`.** S tem metoda deluje tudi, kadar je na desni strani navaden
niz (`Beseda('cas') < 'dan'`), ne le druga `Beseda`.

**Koliko metod je dovolj.** Za `sorted` zadošča `__lt__`. Če bi hotel še
`a > b`, `a == b` ali `a <= b`, bi dodal `__gt__`, `__eq__`, `__le__` — ali pa
uporabil dekorator `functools.total_ordering`, ki iz `__lt__` in `__eq__`
izpelje vse ostale.

#### c) `francetov_slovar(besede)`

Izven razreda `Beseda` definiraj funkcijo `francetov_slovar(besede)`, ki sprejme
seznam besed (Pythonovih nizov) in vrne seznam Pythonovih nizov,
urejen glede na slovensko abecedo.

```python
>>> francetov_slovar(['črta', 'cena', 'dok', 'uta', 'uš'])
['cena', 'črta', 'dok', 'uš', 'uta']
```

```python
def francetov_slovar(besede):
    # Ta funkcija je IZVEN razreda, torej na levem robu (tako zahteva naloga).
    #
    # Postopek v eni vrstici:
    #   1. vsak niz ovijemo v Beseda(...)          -> objekti, ki znajo <
    #   2. sorted(...) jih uredi z našim __lt__    -> slovenski vrstni red
    #   3. str(b) vsakega spet spremeni v niz      -> naloga hoče seznam NIZOV
    return [str(b) for b in sorted(Beseda(niz) for niz in besede)]
```

**Ideja (ovij — uredi — odvij).** Nize ovijemo v objekte, ki znajo `<`, jih
uredimo in razpakiramo nazaj v nize. Vzorec se v literaturi imenuje
*decorate–sort–undecorate*.

Razčlenjeno po korakih:

```python
def francetov_slovar(besede):
    objekti = [Beseda(niz) for niz in besede]   # 1. ovij
    urejeni = sorted(objekti)                   # 2. uredi (uporabi __lt__)
    return [str(b) for b in urejeni]            # 3. odvij nazaj v nize
```

**Ta funkcija je izven razreda**, torej na levem robu — tako zahteva naloga.

**Alternativa brez razreda.** Če bi imel na voljo samo funkcijo `kljuc`, bi bila
cela naloga ena vrstica:

```python
def francetov_slovar(besede):
    return sorted(besede, key=kljuc)
```

`key=` je pravzaprav isti prijem: `sorted` za vsak element enkrat izračuna
ključ in ureja po ključih. Razred je tu zato, ker ga zahteva besedilo naloge.

### Naloga 3 — Avtobusni prevozi
*Datoteka `2324_i1/03_avtobusni_prevozi.py`*

Tipična naloga z datotekami: preberi v podatkovno strukturo, izpiši v drugi
obliki, nato nad strukturo odgovori na vprašanje.

#### a) `linije(ime)` — branje datoteke v slovar seznamov

Sestavite funkcijo `linije`, ki sprejme ime vhodne datoteke in vrne slovar,
v katerem so ključi imena linij in vrednosti seznami pripadajočih postaj v
vrstnem redu, kot so napisane v vhodni datoteki.

```python
>>> linije('linije.txt')
{'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'],
 '1A': ['Park', 'Trg', 'Gledalisce'],
 '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']}
```

```python
def linije(ime):
    # Vzorec za VSE naloge z datotekami: preberi -> zgradi strukturo -> vrni.
    # Tu gradimo slovar seznamov: {'1': ['Sodisce', 'Knjiznica', ...], ...}
    rezultat = {}
    trenutna = None      # ime linije, ki jo trenutno polnimo
    with open(ime, encoding='utf-8') as f:
        for vrstica in f:
            # strip() VEDNO — sicer bi imena postaj imela na koncu '\n'
            # in primerjava z 'Park' ne bi držala.
            vrstica = vrstica.strip()
            if not vrstica:
                continue
            # Naloga pove ključ za razlikovanje: ime linije se začne s številko,
            # ime postaje s črko. To je edini način, da ločimo vrstici med sabo.
            if vrstica[0].isdigit():
                trenutna = vrstica
                rezultat[trenutna] = []      # nova linija -> prazen seznam postaj
            else:
                rezultat[trenutna].append(vrstica)
    return rezultat
```

**Vzorec za vse naloge z datotekami:** *preberi → zgradi strukturo → vrni*.
Tu gradimo slovar, kjer je ključ ime linije, vrednost pa seznam postaj.

**Kako ločimo vrstici med seboj.** Datoteka ne loči imen linij in postaj s
posebnim znakom, pove pa jih oblika: ime linije se začne s **številko**, ime
postaje s **črko**. Zato `vrstica[0].isdigit()`. Spremenljivka `trenutna` si
zapomni, v kateri seznam trenutno dodajamo — to je klasičen vzorec za
»razdelke« v datoteki.

**`strip()` vedno.** Vsaka vrstica iz datoteke se konča z `\n`. Brez `strip()`
bi bilo ime postaje `'Park\n'` in primerjava s `'Park'` ne bi držala, izpis pa
bi imel prazne vrstice.

**Zakaj `if not vrstica: continue`.** Prazne vrstice v datoteki sicer sprožijo
`IndexError` pri `vrstica[0]`.

#### b) `pregledno(slovar, izhodna)` — izpis v datoteko

Podatki v vhodni datoteki so nekoliko nepregledni. Sestavite funkcijo `pregledno`,
ki sprejme slovar enake oblike kot je rezultat prejšnje podnaloge in ime izhodne
datoteke, v katero pregledneje izpiše imena linij in postaj. Vsaka vrstica naj
predstavlja svojo linijo, ki se začne z imenom linije in dvopičjem, nato pa naj
bodo našteta postajališča, ločena s puščico. Zgleduj se po spodnjem primeru.

```
slovar = {'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'],
       '1A': ['Park', 'Trg', 'Gledalisce'],
       '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']}
```
Po klicu `pregledno(slovar, 'pregledno.txt')` dobimo datoteko `pregledno.txt`
z vsebino

```
1: Sodisce -> Knjiznica -> Trg -> Park
1A: Park -> Trg -> Gledalisce
2: Trgovina -> Muzej -> Sola -> Gledalisce
```

```python
def pregledno(slovar, izhodna):
    # Pisanje v datoteko: 'w' pomeni, da datoteko ustvarimo oz. prepišemo.
    with open(izhodna, 'w', encoding='utf-8') as f:
        for kljuc, postaje in slovar.items():
            # ' -> '.join(...) sestavi 'Trg -> Park -> Sola' in sam poskrbi,
            # da puščice NI pred prvo in za zadnjo postajo.
            # Format je prepisan iz primera v besedilu, znak za znakom:
            # dvopičje, presledek, postaje ločene s presledkom-puščico-presledkom.
            print(f'{kljuc}: ' + ' -> '.join(postaje), file=f)
    # Funkcija ničesar ne vrne — njen rezultat je datoteka.
```

**Ideja.** Vsaka linija dobi svojo vrstico oblike
`ime: postaja -> postaja -> postaja`.

**`' -> '.join(postaje)`** je pravo orodje: sam poskrbi, da puščice ni pred
prvo in za zadnjo postajo. Ročno sestavljanje z zanko in `+=` skoraj vedno
pusti odvečno puščico na koncu.

**Pisanje v datoteko.**

- `open(ime, 'w')` datoteko ustvari oz. **prepiše**; `'a'` bi dodajal na konec.
- `print(niz, file=f)` je najpreprostejši način pisanja, ker sam doda `\n`.
  Alternativa je `f.write(niz + '\n')` — pri `write` moraš prelom dodati sam.
- `with` poskrbi, da se datoteka zanesljivo zapre, tudi če vmes pride do napake.

**Funkcija ničesar ne vrne** — njen rezultat je datoteka. To je pogosto in
povsem pravilno; `return None` je implicitno.

#### c) `obstaja_povezava(slovar, zacetna, koncna)`

Sestavite funkcijo `obstaja_povezava`, ki sprejme slovar linij, začetno ter
končno postajo in vrne `True`, če obstaja povezava od začetne do končne postaje
z **največ enim** prestopom, sicer pa `False`. Če začetne ali končne postaje
ni v slovarju, naj funkcija vrne `None`.

```python
>>> obstaja_povezava(slovar, 'Trgovina', 'Trg')
True
>>> obstaja_povezava(slovar, 'Sodisce', 'Sola')
False
>>> obstaja_povezava(slovar, 'Trg', 'Aaaaaa')
None
```

```python
def obstaja_povezava(slovar, zacetna, koncna):
    # 1) NAJPREJ VALIDACIJA. Naloga zahteva None (ne False!), če katere od
    #    postaj sploh ni na nobeni liniji.
    vse = set()
    for postaje in slovar.values():
        vse |= set(postaje)          # |= je unija množic (dodaj vse elemente)
    if zacetna not in vse or koncna not in vse:
        return None

    # 2) Linije, na katerih leži začetna, in linije, na katerih leži končna.
    zacetne_linije = [p for p in slovar.values() if zacetna in p]
    koncne_linije = [p for p in slovar.values() if koncna in p]

    # 3) Dve možnosti za "največ en prestop":
    for a in zacetne_linije:
        # brez prestopa: obe postaji sta na isti liniji
        if koncna in a:
            return True
        for b in koncne_linije:
            # en prestop: liniji a in b imata vsaj eno skupno postajo,
            # na kateri lahko presedemo. & je presek množic.
            if set(a) & set(b):
                return True
    return False
```

**Najprej validacija.** Naloga zahteva `None` (in ne `False`), če katere od
postaj sploh ni na nobeni liniji. Zato najprej zberemo množico vseh postaj:
operator `|=` je unija množic, torej »dodaj vse elemente«.

`None` in `False` sta v Pythonu različni vrednosti; test to preverja, čeprav
sta oba »lažna« (`if not None` in `if not False` sta oba resnična).

**Dva primera za »največ en prestop«.**

1. **Brez prestopa** — obe postaji sta na isti liniji.
2. **En prestop** — obstajata liniji `a` (z začetno) in `b` (s končno), ki imata
   vsaj eno skupno postajo, na kateri presedemo. To je natanko neprazen presek
   `set(a) & set(b)`.

**Zakaj množice.** Presek in preverjanje pripadnosti sta na množici v povprečju
O(1), na seznamu pa O(n). Pri tako majhnih podatkih razlika ni pomembna, je pa
zapis z `&` bistveno krajši od dveh gnezdenih zank.

**Meja naloge.** Ta rešitev odgovarja na vprašanje o **največ enem** prestopu.
Če bi naloga spraševala po poljubnem številu prestopov, bi to bilo iskanje poti
v grafu (BFS) — bistveno daljša naloga.

---

## Izpit 2. rok 2023/24
Drugi rok: simulacija s seznami, obdelava besedila v datotekah (vključno z
regularnimi izrazi) in kodiranje s slovarjem.

### Naloga 1 — Izštevanke
*Datoteka `2324_i2/01_izstevanke.py`*

Naloga o krožnem štetju. Vse tri podnaloge stojijo na eni sami formuli —
`(i + n - 1) % len(seznam)` — zato se splača vzeti minuto in jo preveriti na
primeru iz besedila, preden pišeš naprej.

#### a) `izlocen(seznam, ime, n)`

Imena igralcev zapišimo v seznam v takem vrstnem redu, kot so postavljeni
v krogu. Predpostavimo lahko, da so imena igralcev paroma različna.
Sestavite funkcijo `izlocen`, ki sprejme seznam igralcev, ime igralca,
pri katerem začnemo, in število besed v izštevanki, vrne pa ime izločenega
igralca.

```python
>>> izlocen(['Andrej', 'Blaž', 'Cilka', 'Dunja'], 'Cilka', 4)
'Blaž'
```

```python
def izlocen(seznam, ime, n):
    # Igralci stojijo v KROGU, indeksi v seznamu pa se končajo — zato je
    # nujen % len(seznam), sicer pri i + n čez rob dobiš IndexError.
    #
    # Zakaj -1: igralec, pri katerem začnemo, je PRVA beseda izštevanke,
    # ne ničta. Preštej primer iz besedila:
    #     Cilka(1), Dunja(2), Andrej(3), Blaž(4)  ->  izpade Blaž
    # Cilka je na indeksu 2, Blaž na 1:  (2 + 4 - 1) % 4 == 1.
    i = seznam.index(ime)
    return seznam[(i + n - 1) % len(seznam)]
    # Opomba: NE uporabljamo .pop(), ker naloga zahteva samo, da ime vrnemo.
    # .pop() bi klicatelju spremenil (skrajšal) njegov seznam.
```

**Ideja.** Igralci stojijo v **krogu**, indeksi v seznamu pa se končajo — zato
je nujen `% len(seznam)`, sicer pri `i + n` čez rob dobiš `IndexError`.

**Od kod `- 1`.** Igralec, pri katerem začnemo, je **prva** beseda izštevanke,
ne ničta. Preštej primer iz besedila:

```
Cilka(1), Dunja(2), Andrej(3), Blaž(4)  ->  izpade Blaž
```

Cilka je na indeksu 2, Blaž na 1, izštevanka ima 4 besede:
`(2 + 4 - 1) % 4 == 5 % 4 == 1`. Brez `- 1` bi izpadel napačen igralec — to je
klasična napaka »off by one«.

**Funkcija ne spreminja seznama.** Naloga zahteva samo ime izločenega igralca.
Če bi uporabil `.pop()`, bi klicatelju skrajšal njegov seznam, kar bi se
maščevalo v naslednji podnalogi.

#### b) `zmagovalec(igralci, zacetni, izstevanke)`

Na voljo imamo več različnih izštevank. Vsakič uporabimo drugo, če nam jih zmanjka,
pa jih začnemo uporabljati še enkrat v istem vrstnem redu. Sestavite funkcijo
`zmagovalec`, ki sprejme seznam igralcev, ime igralca, pri katerem začnemo, in
seznam števil besed v izštevankah, ki jih bomo uporabili. Funkcija naj vrne
ime igralca, ki na koncu ostane edini v krogu.

```python
>>> zmagovalec(['Andrej', 'Blaž', 'Cilka', 'Dunja'], 'Cilka', [4, 3])
'Cilka'
```

```python
def zmagovalec(igralci, zacetni, izstevanke):
    # list(...) naredi KOPIJO: spodaj s .pop() brišemo igralce, in če bi brisali
    # po izvirnem seznamu, bi ga 3. podnaloga po prvem klicu dobila praznega.
    igralci = list(igralci)
    i = igralci.index(zacetni)
    k = 0                                   # katera izštevanka je na vrsti
    while len(igralci) > 1:
        # izstevanke[k % len(izstevanke)] — ko nam izštevank zmanjka, se
        # ciklično vrnemo na začetek. Isti prijem kot krožno gibanje po igralcih.
        n = izstevanke[k % len(izstevanke)]
        i = (i + n - 1) % len(igralci)      # ista formula kot v 1. podnalogi
        igralci.pop(i)
        # Po brisanju je na mestu i že NASLEDNJI igralec, torej i ostane.
        # Če pa je izpadel zadnji v seznamu, je i enak novi dolžini in bi
        # kazal izven seznama — modulo ga zavrti nazaj na 0.
        i %= len(igralci)
        k += 1
    return igralci[0]
```

**Ideja.** Ponavljamo izločanje, dokler ne ostane en sam igralec. Uporabimo
isto formulo kot prej, le da tokrat izločenega tudi zares odstranimo.

**Tri stvari, ki jih je treba narediti prav.**

1. **Kopija seznama.** `igralci = list(igralci)` — spodaj s `.pop()` brišemo, in
   če bi brisali po izvirnem seznamu, bi ga tretja podnaloga po prvem klicu
   dobila praznega. To je ena najbolj zoprnih napak, ker se pokaže šele
   drugje.
2. **Ciklične izštevanke.** `izstevanke[k % len(izstevanke)]` — ko nam
   izštevank zmanjka, se vrnemo na začetek. Isti prijem kot krožno gibanje po
   igralcih.
3. **Popravek indeksa po brisanju.** Po `.pop(i)` je na mestu `i` že
   **naslednji** igralec, zato `i` ostane. Če pa je izpadel zadnji v seznamu,
   je `i` enak novi dolžini in bi kazal izven seznama — zato `i %= len(igralci)`.

**Zakaj `while` in ne `for`.** Dolžina seznama se med izvajanjem spreminja;
`for` bi tekel po prvotnem številu elementov.

#### c) `pri_kom_zaceti(igralci, favorit, izstevanke)`

Zanima nas, pri katerem igralcu naj začnemo igro, da bo zmagal naš favorit.
Sestavite funkcijo `pri_kom_zaceti`, ki sprejme seznam igralcev, ime našega
favorita in seznam števil besed v izštevankah, ki jih bomo uporabili. Funkcija
naj vrne ime igralca, pri katerem moramo začeti igro, da bo zmagal naš favorit.

```python
>>> pri_kom_zaceti(['Andrej', 'Blaž', 'Cilka', 'Dunja'], 'Blaž', [2, 4])
'Cilka'
```

```python
def pri_kom_zaceti(igralci, favorit, izstevanke):
    # Groba sila je tu prava rešitev: igralcev je malo, možnih začetkov pa je
    # natanko toliko kot igralcev. Preizkusimo vse in vrnemo prvega, ki deluje.
    for igralec in igralci:
        if zmagovalec(igralci, igralec, izstevanke) == favorit:
            return igralec
    # Če favorit ne more zmagati pri nobenem začetku, funkcija vrne None.
    return None
```

**Ideja (groba sila).** Možnih začetkov je natanko toliko kot igralcev, torej
jih preprosto vse preizkusimo in vrnemo prvega, pri katerem zmaga favorit.

To je legitimna rešitev, ne bližnjica: prostor možnosti je majhen in vsak
poskus je poceni. Na izpitu je iskanje »pametne formule« tu izguba časa.

**Ponovna uporaba.** Funkcija ne pozna pravil izštevanja — vse prepusti
`zmagovalec`. Prav zato je bilo pomembno, da `zmagovalec` ne pokvari seznama,
ki ga dobi: tu ga kličemo v zanki znova in znova z istim seznamom.

**Robni primer.** Če favorit ne more zmagati pri nobenem začetku, zanka do
konca ne vrne ničesar in funkcija vrne `None`. Eksplicitni `return None` na
koncu ni nujen, je pa jasnejši.

### Naloga 2 — Pesnik France: popravljanje kode
*Datoteka `2324_i2/02_pesnik_france.py`*

Program, ki obdeluje program. Vse tri podnaloge berejo datoteko vrstico po
vrstico; razlikujejo se le po tem, kaj z vrstico naredijo.

#### a) `prestej_vrstice(datoteka)`

Za začetek Franceta zanima, kako dolge programe naj piše. Praznih vrstic
in vrstic, ki vsebujejo le komentarje, ne šteje. Napišite funkcijo
`prestej_vrstice(datoteka)`, ki prešteje število vrstic v datoteki.
Primer: če je vsebina datoteke `fibo.py` enaka

```
def f(n):
    # bazna primera
    if n <= 2:
        return 1  # fib(1) = fib(2) = 1
    else:
        # rekurzivni korak
        return f(n - 1) + f(n - 2)
```
naj funkcija vrne 5. Vsi komentarji se začnejo z znakom `#`.

```python
def prestej_vrstice(datoteka):
    st_vrstic = 0
    with open (datoteka, encoding='utf-8') as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue
            if vrstica[0] == '#':
                continue
            else:
                st_vrstic += 1
    return st_vrstic
```

**Ideja.** Preštejemo vrstice, ki niso prazne in niso samo komentar.

**Kaj natanko šteje.**

- `vrstica.strip()` odstrani presledke, tabulatorje in `\n` z obeh strani; če
  po tem ostane prazen niz, je bila vrstica prazna (ali je vsebovala le
  presledke) → ne šteje.
- Vrstica šteje kot komentar samo, če se `#` pojavi **na začetku** (po
  odstranitvi zamika). Komentar na koncu vrstice, npr.
  `return 1  # fibo(1) = 1`, je še vedno koda in šteje.

**Zakaj `strip()` pred preverjanjem `#`.** Komentarji so v kodi običajno
zamaknjeni; brez `strip()` bi `vrstica[0]` bil presledek in pogoj ne bi držal.

**Idiom.** `if not vrstica: continue` je krajši in bolj pythonovski od
`if vrstica == '': continue` — prazen niz je namreč »lažna« vrednost.

#### b) `odstrani_printe(slaba, popravljena)`

France ne razume dobro razlike med `print` in `return`.
Zapiši funkcijo `odstrani_printe(slaba, popravljena)`, ki v datoteki `slaba`
vse klice funkcije `print`, ki ne zapisujejo v datoteko,
nadomesti z ukazom `return` in popravljen program zapiše v datoteko `popravljena`.

```
# slaba                                       # popravljena
def podpis(datoteka):                         def podpis(datoteka):
    with open(datoteka, 'w') as f:                with open(datoteka, 'w') as f:
        print('France', 'Pesnik', file=f)             print('France', 'Pesnik', file=f)
    print(True)                                   return True
```

```python
def odstrani_printe(slaba, popravljena):
    with open(slaba, encoding='utf-8') as s:
        vrstice = s.readlines()

    with open(popravljena, 'w', encoding='utf-8') as p:
        for vrstica in vrstice:
            vrstica = vrstica.rstrip('\n')      # print() spodaj doda svojega
            gola = vrstica.strip()              # verzija brez zamika, za preverjanje

            if gola.startswith('print(') and gola.endswith(')') and 'file=' not in gola:
                # zamik moramo ohraniti, sicer razpade struktura programa
                zamik = vrstica[:len(vrstica) - len(vrstica.lstrip())]
                # vse med zunanjima oklepajema: 'print(' je 6 znakov, [-1] odreže ')'
                vsebina = gola[len('print('):-1]
                vrstica = zamik + 'return ' + vsebina

            print(vrstica, file=p)
```

**Ideja.** Vrstico po vrstico prepisujemo v novo datoteko; kjer prepoznamo
klic `print(...)`, ki ne piše v datoteko, ga zamenjamo z `return`.

**Trije pogoji, ki morajo držati hkrati.**

```python
gola.startswith('print(') and gola.endswith(')') and 'file=' not in gola
```

- prva dva poskrbita, da gre res za samostojen klic (in ne npr. za
  `x = print(...)` ali za vrstico, ki se nadaljuje),
- `'file=' not in gola` je izjema iz besedila naloge: `print(..., file=f)`
  piše v datoteko in ga pustimo pri miru.

**Zamik je treba ohraniti.** Če bi vrnili `'return ' + vsebina` brez zamika, bi
program razpadel — v Pythonu je zamik del sintakse. Zato izračunamo
`zamik = vrstica[:len(vrstica) - len(vrstica.lstrip())]`, kar je natanko
presledki na začetku vrstice.

**Izluščenje argumenta.** `gola[len('print('):-1]` vzame vse med zunanjima
oklepajema: `len('print(')` je 6 znakov na začetku, `-1` odreže zaklepaj.
Zapis `len('print(')` je boljši od trdo vpisane šestice — če se ime funkcije
spremeni, se izračun popravi sam.

**Omejitev.** Rešitev je namenoma preprosta obdelava besedila in ne razume
Pythona: klic, razpotegnjen čez dve vrstici, ali `print` znotraj niza bi jo
premotila. Za nalogo to zadošča.

#### c) `poenostavi(slaba, popravljena)`

France še ni odkril, da lahko npr. namesto `x = x + 2` napiše `x += 2`.
 Zapišite funkcijo `poenostavi(slaba, popravljena)`,
ki popravljeno vsebino Pythonovega programa iz datoteke `slaba`
(vpeljati mora vse možne okrajšave za seštevanje in odštevanje) zapiše v datoteko `popravljena`:

```
# slaba                          # popravljena
def f(vred):                     def f(vred):
    vred = vred + 3                  vred += 3
    vred = 2 + vred                  vred += 2
    return vred + 1                  return vred + 1
```
Privzameš lahko, da France sešteva/odšteva le naravna števila in so imena
spremenljivk iz malih angleških črk ter podčrtajev (npr. `novi_stevec`).

```python
import re

# Vrstica oblike "ime = X op Y", kjer sta X in Y bodisi ime spremenljivke
# bodisi število. Poimenovane skupine (?P<ime>...) omogočajo dostop prek m["ime"].
PRIREDITEV = re.compile(
    r"^(?P<zamik>\s*)(?P<ime>[a-z_]+)\s*=\s*"
    r"(?P<levo>[a-z_]+|\d+)\s*(?P<op>[-+])\s*(?P<desno>[a-z_]+|\d+)\s*$"
)


def okrajsaj(vrstica):
    """Vrne okrajšano vrstico, če je okrajšava možna, sicer nespremenjeno."""
    m = PRIREDITEV.match(vrstica)
    if m is None:
        return vrstica

    ime, op = m["ime"], m["op"]

    # x = x + 3  ->  x += 3     (spremenljivka je levi seštevanec)
    if op == "+" and m["levo"] == ime:
        return m["zamik"] + ime + " += " + m["desno"]

    # x = 3 + x  ->  x += 3     (seštevanje je komutativno, zato gre tudi obratno)
    if op == "+" and m["desno"] == ime:
        return m["zamik"] + ime + " += " + m["levo"]

    # x = x - 3  ->  x -= 3
    if op == "-" and m["levo"] == ime:
        return m["zamik"] + ime + " -= " + m["desno"]

    # x = 3 - x  NI x -= 3, ker odštevanje ni komutativno -> pustimo pri miru
    return vrstica


def poenostavi(slaba, popravljena):
    with open(slaba, encoding="utf-8") as s:
        vrstice = s.readlines()

    with open(popravljena, "w", encoding="utf-8") as p:
        for vrstica in vrstice:
            # rstrip("\n") odreže prelom, ki ga print spodaj doda sam
            print(okrajsaj(vrstica.rstrip("\n")), file=p)
```

**Ideja.** Iščemo vrstice oblike `ime = X op Y` in jih, kadar se da, skrajšamo
v `ime += Y` oz. `ime -= Y`.

**Zakaj regularni izraz.** Ročno razbijanje s `split(' = ')` in `split(' + ')`
je mogoče, a se hitro zaplete pri presledkih in predznakih. Vzorec z
**imenovanimi skupinami** je krajši in samodokumentiran:

```
^(?P<zamik>\s*)(?P<ime>[a-z_]+)\s*=\s*(?P<levo>[a-z_]+|\d+)\s*(?P<op>[-+])\s*(?P<desno>[a-z_]+|\d+)\s*$
```

| Del | Pomen |
|---|---|
| `^` … `$` | vzorec mora ujeti **celo** vrstico |
| `(?P<zamik>\s*)` | zamik na začetku, da ga lahko ohranimo |
| `[a-z_]+` | ime spremenljivke — naloga pravi: male črke in podčrtaji |
| `\d+` | naravno število |
| `(?P<op>[-+])` | znotraj oglatih oklepajev je `-` na koncu navaden znak |
| `\s*` | dovolimo poljubno število presledkov okoli `=` in operatorja |

Do skupin nato dostopamo z `m["ime"]`, `m["op"]` in tako naprej.

**Ključni premislek — katere okrajšave so sploh dovoljene.**

| Vrstica | Okrajšava | Zakaj |
|---|---|---|
| `x = x + 3` | `x += 3` | ✅ |
| `x = 3 + x` | `x += 3` | ✅ seštevanje je **komutativno** |
| `x = x - 3` | `x -= 3` | ✅ |
| `x = 3 - x` | — | ❌ odštevanje **ni** komutativno; `x -= 3` bi bilo nekaj drugega |

Zadnja vrstica je bistvo naloge: ravno zaradi nje ne moremo preprosto
zamenjati vseh vzorcev.

**Vrstice, ki se ne ujamejo** (npr. `return vred + 1` ali `def f(vred):`),
se prepišejo nespremenjene — zato je `okrajsaj` napisana kot funkcija, ki v
primeru neujemanja vrne vhod nedotaknjen.

### Naloga 3 — Kodiranje v bazi 64
*Datoteka `2324_i2/03_kodiranje_v_bazi_64.py`*

Kodirna tabela je v datoteki že podana — to je namig, da je naloga o **uporabi**
slovarja, ne o njegovem sestavljanju. Druga in tretja podnaloga sta natančno
obratni druga od druge.

#### a) `pravilna_koda(niz)`

Sestavite funkcijo `pravilna_koda`, ki preveri če je podani niz pravilno zakodiran
v bazi 64, tj., da vsebuje pravilne znake in da je morebiti ustrezno dopolnjen z `=`.

```python
>>> pravilna_koda('YmF6YTY0')
True
>>> pravilna_koda('YmF6YTY0===')
False
>>> pravilna_koda('--++')
False
```

```python
kodirna_tabela = {
    '000000': 'A', '010000': 'Q', '100000': 'g', '110000': 'w',
    '000001': 'B', '010001': 'R', '100001': 'h', '110001': 'x',
    '000010': 'C', '010010': 'S', '100010': 'i', '110010': 'y',
    '000011': 'D', '010011': 'T', '100011': 'j', '110011': 'z',
    '000100': 'E', '010100': 'U', '100100': 'k', '110100': '0',
    '000101': 'F', '010101': 'V', '100101': 'l', '110101': '1',
    '000110': 'G', '010110': 'W', '100110': 'm', '110110': '2',
    '000111': 'H', '010111': 'X', '100111': 'n', '110111': '3',
    '001000': 'I', '011000': 'Y', '101000': 'o', '111000': '4',
    '001001': 'J', '011001': 'Z', '101001': 'p', '111001': '5',
    '001010': 'K', '011010': 'a', '101010': 'q', '111010': '6',
    '001011': 'L', '011011': 'b', '101011': 'r', '111011': '7',
    '001100': 'M', '011100': 'c', '101100': 's', '111100': '8',
    '001101': 'N', '011101': 'd', '101101': 't', '111101': '9',
    '001110': 'O', '011110': 'e', '101110': 'u', '111110': '+',
    '001111': 'P', '011111': 'f', '101111': 'v', '111111': '/',
}


def pravilna_koda(niz):
    # Dovoljeni znaki so natanko VREDNOSTI kodirne tabele. Množica zato,
    # ker je preverjanje "z in mnozica" hitro in se lepo bere.
    dovoljeni = set(kodirna_tabela.values())

    # rstrip('=') odreže enačaje SAMO na koncu niza. Razlika med dolžinama
    # nam pove, koliko jih je bilo.
    telo = niz.rstrip('=')
    st_enacajev = len(niz) - len(telo)

    # Dopolnimo lahko z največ dvema paroma ničel, torej največ dva '='.
    if st_enacajev > 2:
        return False

    # V telesu ne sme biti nobenega nedovoljenega znaka. Ker '=' ni vrednost
    # v tabeli, to hkrati ujame primer 'YmF==6YQ', kjer je enačaj na sredini.
    for znak in telo:
        if znak not in dovoljeni:
            return False

    return True
```

**Ideja.** Niz je veljaven, če vsebuje samo dovoljene znake in ima na koncu
največ dva enačaja.

**Od kod nabor dovoljenih znakov.** To so natanko **vrednosti** kodirne tabele,
zato `set(kodirna_tabela.values())` — nabora ni treba prepisovati ročno.
Množica zato, ker je preverjanje `znak in mnozica` hitro in se lepo bere.

**`rstrip('=')`** odreže enačaje **samo na koncu** niza. Razlika med dolžinama
pove, koliko jih je bilo:

```python
telo = niz.rstrip('=')
st_enacajev = len(niz) - len(telo)
```

**Zakaj največ dva.** Blok je dolg 6 bitov; dopolnimo lahko z 2 ali 4 ničlami,
kar da en oz. dva enačaja. Trije enačaji (`'YmF6YTY0==='`) so torej neveljavni.

**Skriti primer, ki ga rešitev tudi ujame.** Enačaj sredi niza (`'YmF==6YQ'`)
`rstrip` ne odstrani, ostane v telesu — in ker `=` ni vrednost v kodirni
tabeli, ga zanka zavrne. Ni treba posebnega preverjanja.

#### b) `zakodiraj(bitni_zapis)`

Sestavite funkcijo `zakodiraj`, ki sprejme bitni zapis (kot niz) in ga zakodira v bazi 64.

```python
>>> zakodiraj('000000')
'A'
>>> zakodiraj('011000100110000101111010011000010011011000110100')
'YmF6YTY0'
>>> zakodiraj('01100010011000010111101001100001')
'YmF6YQ=='
```

```python
def zakodiraj(bitni_zapis):
    # Koliko ničel moramo dodati do dolžine, deljive s 6: 0, 2 ali 4.
    # Zunanji % 6 poskrbi, da pri že deljivi dolžini dobimo 0 in ne 6.
    dopolnitev = (6 - len(bitni_zapis) % 6) % 6
    bitni_zapis = bitni_zapis + '0' * dopolnitev

    # Rezanje na bloke fiksne dolžine: range s korakom 6 in rezina [i:i+6].
    rezultat = ''
    for i in range(0, len(bitni_zapis), 6):
        blok = bitni_zapis[i:i + 6]
        rezultat += kodirna_tabela[blok]

    # Za vsak dodan PAR ničel pripnemo en '=': 2 ničli -> '=', 4 ničle -> '=='.
    return rezultat + '=' * (dopolnitev // 2)
```

**Ideja.** Bite razrežemo na bloke po 6 in vsak blok po tabeli preslikamo v
znak. Če dolžina ni deljiva s 6, na konec dodamo ničle in to označimo z
enačaji.

**Izračun dopolnitve.**

```python
dopolnitev = (6 - len(bitni_zapis) % 6) % 6
```

Zunanji `% 6` je pomemben: pri dolžini, ki je že deljiva s 6, bi notranji del
dal 6 in bi po nepotrebnem dodali cel blok ničel. Ta »dvojni modulo« je pogost
prijem, kadar računaš »koliko manjka do naslednjega večkratnika«.

**Rezanje na bloke fiksne dolžine.**

```python
for i in range(0, len(bitni_zapis), 6):
    blok = bitni_zapis[i:i + 6]
```

`range` s korakom 6 in rezina `[i:i+6]` — vzorec, ki ga boš uporabil vsakič, ko
je treba zaporedje razdeliti na kose enake dolžine.

**Enačaji.** Za vsak dodan **par** ničel pripnemo en `=`, torej
`'=' * (dopolnitev // 2)`: 2 ničli → `'='`, 4 ničle → `'=='`.

#### c) `odkodiraj(koda)`

Sestavite funkcijo `odkodiraj`, ki sprejme niz zakodiran v bazi 64 in ga odkodira v bitni zapis (kot niz). Privzamete lahko, da je zakodirani niz veljaven.

```python
>>> odkodiraj('A')
'000000'
>>> odkodiraj('YmF6YTY0')
'011000100110000101111010011000010011011000110100'
>>> odkodiraj('YmF6YQ==')
'01100010011000010111101001100001'
```

```python
def odkodiraj(koda):
    # Obrnjen slovar: iz {biti: znak} naredimo {znak: biti}.
    # To je standarden prijem, kadar rabiš preslikavo v drugo smer.
    obratna_tabela = {znak: biti for biti, znak in kodirna_tabela.items()}

    telo = koda.rstrip('=')
    st_enacajev = len(koda) - len(telo)

    bitni_zapis = ''
    for znak in telo:
        bitni_zapis += obratna_tabela[znak]

    # Vsak '=' pomeni, da sta bili ob kodiranju dodani dve ničli — odrežemo ju.
    # POZOR na varovalko: brez nje bi pri st_enacajev == 0 pisalo
    # bitni_zapis[:-0], kar je [:0] in vrne PRAZEN niz.
    if st_enacajev > 0:
        bitni_zapis = bitni_zapis[:-2 * st_enacajev]

    return bitni_zapis
```

**Ideja.** Ravno obratno od kodiranja: vsak znak preslikamo nazaj v svojih 6
bitov, na koncu pa odstranimo ničle, ki so bile dodane pri kodiranju.

**Obrnjen slovar.**

```python
obratna_tabela = {znak: biti for biti, znak in kodirna_tabela.items()}
```

To je standarden prijem, kadar rabiš preslikavo v drugo smer. Deluje, ker so
vrednosti izvirnega slovarja različne — sicer bi se nekateri ključi povozili.

**Past, ki jo je treba poznati.**

```python
if st_enacajev > 0:
    bitni_zapis = bitni_zapis[:-2 * st_enacajev]
```

Brez varovalke `if` bi pri nič enačajih pisalo `bitni_zapis[:-0]`, kar je
`[:0]` in vrne **prazen niz**. Vsakič, ko v rezini nastopa izračunano
negativno število, se vprašaj, kaj se zgodi pri ničli.

**Kontrola.** `odkodiraj(zakodiraj(x)) == x` mora veljati za vsak bitni zapis —
dober način, da rešitev preizkusiš sam.

---

## Izpit 3. rok 2023/24
Tretji rok: obdelava nizov s pravili, gnezdena podatkovna struktura in razred
z razčlenjevanjem podatkov.

### Naloga 1 — Pesnik France: zlogi in ritem
*Datoteka `2324_i3/01_pesnik_france.py`*

Naloga o nizih, pri kateri je največ dela z **razumevanjem pravil**, ne s
programiranjem. Druga in tretja podnaloga si delita isto pomožno funkcijo, zato
se splača drugo rešiti temeljito.

#### a) `dolzine_kitic(pesem)`

Nekatere pesmi imajo predpisano število kitic in vrstic v njej.
Zapišite funkcijo `dolzine_kitic(pesem)`, ki vrne seznam dolžin kitic v
nizu `pesem`. Za vhoda

```
pesem1 = """Gnoj je zlato,    |    pesem2 = """Nina,
zlato je gnoj!                |    Nina,
                              |    Nina,
Ti si sova,                   |    ena in edina."""
jaz pa noj."""                |
```
velja, da je `dolzine_kitic(pesem1) == [2, 2]` in `dolzine_kitic(pesem2) == [4]`.

```python
def dolzine_kitic(pesem):
    seznam = []
    dolzina = 0
    for vrstica in pesem.split("\n"):
        if vrstica.strip() == "":
            # prazna vrstica konča kitico
            if dolzina > 0:
                seznam.append(dolzina)
            dolzina = 0
        else:
            dolzina += 1
    if dolzina > 0:
        seznam.append(dolzina)
    return seznam
```

**Ideja.** Sprehodimo se po **vrsticah** (ne po znakih!) in štejemo neprazne
vrstice. Prazna vrstica zaključi kitico: takrat števec shranimo in ga
ponastavimo.

**Trije obvezni deli tega vzorca (akumulator z izpiranjem).**

1. števec `dolzina`, ki ga med sprehodom povečujemo,
2. shranjevanje ob ločnici (`seznam.append(dolzina)`),
3. **izpiranje na koncu** — zadnja kitica se ne konča s prazno vrstico, zato jo
   je treba dodati po zanki. Brez tega bi `dolzine_kitic('a')` vrnil `[]`.

**Zakaj `if dolzina > 0`.** Pesem ima lahko več zaporednih praznih vrstic ali
prazne vrstice na začetku in koncu (`'\n\na\n\n\nb\nc\nd\n\n'`). Brez
tega pogoja bi v rezultat prišle kitice dolžine 0.

**`pesem.split("\n")`** razbije niz na vrstice. Pozor: za prazen niz vrne
`['']`, torej eno prazno vrstico — kar je ravno prav, saj rezultat ostane `[]`.

**Pogosta napaka.** Sprehod `for vrstica in pesem` gre po **znakih**, ne po
vrsticah, in pogoj `vrstica == '\n\n'` ni nikoli izpolnjen, ker en znak ne
more biti enak dvema.

#### b) `stevilo_zlogov(verz)`

Veliko pesmi ima predpisano število zlogov v verzu. Napiši funkcijo
`stevilo_zlogov(verz)`, ki vrne seznam števil zlogov po besedah v verzu.
Pri tem ignorirajte enočrkovne besede (npr. _v_, _k_, _s_).

Število zlogov v besedi dobimo tako, da preštejemo samoglasnike in
črke `r`, ki ne stojijo ob soglasniku:

```python
>>> stevilo_zlogov("Rdečo mašno maš v laseh")
[3, 2, 1, 2]
>>> stevilo_zlogov("Jaz sem hrast")
[1, 1, 1]
```

```python
SAMOGLASNIKI = "aeiouAEIOU"


def je_jedro(beseda, i):
    """Ali črka na mestu i v besedi tvori zlog?"""
    crka = beseda[i]
    if crka in SAMOGLASNIKI:
        return True
    if crka in "rR":
        prejsnja = beseda[i - 1] if i > 0 else "-"
        naslednja = beseda[i + 1] if i < len(beseda) - 1 else "-"
        return prejsnja not in SAMOGLASNIKI and naslednja not in SAMOGLASNIKI
    return False


def stevilo_zlogov(verz):
    seznam = []
    for beseda in verz.split():
        if len(beseda) == 1:
            continue
        zlogi = 0
        for i in range(len(beseda)):
            if je_jedro(beseda, i):
                zlogi += 1
        seznam.append(zlogi)
    return seznam
```

**Ideja.** Za vsako besedo preštejemo jedra zlogov: samoglasnike in tiste `r`,
ki tvorijo zlog sami (t. i. zlogotvorni `r`, kot v *vrt*, *smrt*, *šmrkelj*).

**Pozor — besedilo naloge je zavajajoče.** Naloga pravi »črke `r`, ki ne
stojijo ob soglasniku«, testi pa zahtevajo ravno nasprotno: `r` šteje, kadar
**ni ob samoglasniku**. Preveri sam na primerih:

| Beseda | Zlogi | Zakaj |
|---|---|---|
| `Rdečo` | 3 | `e`, `o` in `R` (sosed je `d`, ni samoglasnik) |
| `hrast` | 1 | samo `a`; `r` ima ob sebi `a` |
| `Park` | 1 | samo `a`; `r` ima ob sebi `a` |
| `pokr` | 2 | `o` in `r` (soseda sta `k` in konec besede) |

Kadar se besedilo in testi razhajata, veljajo **testi** — sledi primerom.

**Robovi besede.** Pri prvi in zadnji črki soseda ni. Za »ni samoglasnik«
uporabimo nadomestni znak `"-"`, **ne praznega niza**: `"" in "aeiou"` je
namreč `True` (prazen niz je podniz vsakega niza) in bi pravilo pokvaril.

**Enočrkovne besede.** Naloga jih izrecno izpušča (`v`, `k`, `s`), zato
`if len(beseda) == 1: continue`. Test `'a b c ... z'` mora vrniti `[]`.

**`verz.split()` brez argumenta** razbije po poljubnih belih znakih in pri
praznem nizu vrne `[]` (in ne `['']`) — zato robni primer ne potrebuje
posebne obravnave.

**Zakaj velike črke.** V `SAMOGLASNIKI` so tudi `AEIOU`, sicer bi
`'Aaaa'` dalo 3 namesto 4.

#### c) `ali_je_amfibrah(verz)`

Veliko pesmi ima predpisan tudi ritem, torej morajo biti poudarjeni zlogi
na pravih mestih. Ta'ke zlo'ge bo'mo pri' te'j nalo'gi ozna'čili z eno'jnim
narekova'jem ti'k za' naglaše'nim sa'mogla'snikom ozi'roma r'jem.

Zapišite funkcijo `ali_je_amfibrah(verz)`, ki vrne `True`, če je `verz`
zapisan v amfibrahu, in `False` sicer. Če poudarjene zloge označimo s `P`,
nepoudarjene pa z `N`, potem je verz v amfibrahu natanko tedaj, ko
mu pripada zaporedje zlogov `NPN NPN ... NPN`.

```python
>>> ali_je_ambfibrah("pole'tje")
True
>>> ali_je_amfibrah("V pole'tno nebo' poleti'jo sini'ce")
True
```
Predpostavite lahko, da verz vsebuje le črke, presledke in enojne narekovaje.
Beseda ima lahko več kot en poudarjen zlog.

```python
def zlogi_besede(beseda):
    """Za vsak zlog v besedi vrne True, če je poudarjen, in False sicer."""
    crke = ""
    poudarki = []
    for crka in beseda:
        if crka == "'":
            if poudarki:
                poudarki[-1] = True
        else:
            crke += crka
            poudarki.append(False)
    zlogi = []
    for i in range(len(crke)):
        if je_jedro(crke, i):
            zlogi.append(poudarki[i])
    return zlogi


def ali_je_amfibrah(verz):
    zlogi = []
    for beseda in verz.split():
        zlogi += zlogi_besede(beseda)
    if len(zlogi) == 0 or len(zlogi) % 3 != 0:
        return False
    for i in range(len(zlogi)):
        # poudarjeni so lahko le zlogi na mestih 1, 4, 7, ...
        if zlogi[i] != (i % 3 == 1):
            return False
    return True
```

**Ideja.** Verz razstavimo v **zaporedje zlogov čez cel verz** (meje besed niso
pomembne!) in preverimo, ali ustreza vzorcu `NPN NPN … NPN`.

**Dva pogoja.**

1. Število zlogov je deljivo s 3.
2. Poudarjeni so natanko zlogi na mestih 1, 4, 7, … — torej tisti, za katere
   velja `i % 3 == 1`.

Zapis `if zlogi[i] != (i % 3 == 1): return False` oboje preveri v eni vrstici:
desna stran je `True` natanko na mestih, kjer **mora** biti poudarek.

**Zakaj čez cel verz in ne po besedah.** Test
`ali_je_amfibrah("aa'aa a'aaa'a aa'a")` je `True`, čeprav nobena posamezna
beseda sama zase ni `NPN`. Ritem teče čez celotno vrstico.

**Narekovaji in sosedi.** Pri iskanju zlogotvornega `r` moramo gledati sosedne
**črke**, ne narekovajev. Zato funkcija `zlogi_besede` besedo najprej razstavi
na dvoje: niz samih črk in seznam podatkov, ali za posamezno črko stoji
narekovaj. Šele nad očiščenim nizom uporabimo isto funkcijo `je_jedro` kot v
prejšnji podnalogi.

**Ponovna uporaba se splača.** Če bi pravilo o zlogih pisal na novo, bi ga
moral tudi na novo razhroščiti. Tu je `je_jedro` že preverjena z 12 testi
prejšnje podnaloge.

### Naloga 2 — Pogosti znaki
*Datoteka `2324_i3/02_pogosti_znaki.py`*

Od štetja v slovar do rekurzije nad gnezdenimi nabori. Naloga je odličen
preizkus, ali ločiš nabor z enim elementom `(x, )` od navadnih oklepajev.

#### a) `pogostost(niz)`

Sestavite funkcijo `pogostost`, ki sprejme nek niz, ter vrne slovar, v katerem
so ključi znaki, ki se v nizu pojavljajo, pripadajoče vrednosti pa so števila
pojavitev teh znakov.

```python
>>> pogostost("abba")
{'a': 2, 'b': 2}
>>> pogostost("abeceda")
{'a': 2, 'b': 1, 'e': 2, 'c': 1, 'd': 1}
```

```python
def pogostost(niz):
    slovar = {}
    for znak in niz:
        # get(znak, 0) vrne dosedanje število pojavitev, ob prvi pojavitvi 0
        slovar[znak] = slovar.get(znak, 0) + 1
    return slovar
```

**Ideja.** Standardno štetje v slovar.

```python
slovar[znak] = slovar.get(znak, 0) + 1
```

`get(znak, 0)` vrne dosedanje število pojavitev ali `0`, kadar znaka še ni —
zato ni treba pisati `if znak not in slovar`.

**Enakovredni zapisi.**

```python
# s preverjanjem obstoja
if znak not in slovar:
    slovar[znak] = 0
slovar[znak] += 1

# s setdefault
slovar.setdefault(znak, 0)
slovar[znak] += 1

# s standardno knjižnico
from collections import Counter
slovar = Counter(niz)
```

**Robni primer je pokrit sam od sebe:** pri praznem nizu se zanka ne izvede in
funkcija vrne prazen slovar.

**Vrstni red ključev ni pomemben** — testi slovarje primerjajo po vsebini.

#### b) `gnezdi(slovar)`

Znake bomo po pogostosti gnezdili tako, da bom začeli z najredkejšim
znakom in ga vstavili v nabor, nato pa bomo znake dodajali po pogostosti od redkejših proti pogostim
tako, da bomo vzeli do sedaj ugnezdene znake in jih dodali v nov par.

**Primer:** Če obravnavamo sledeče znake s pogostostmi,

- `Z`: 1,
- `X`: 2,
- `O`: 3,
- `P`: 4,
- `A`: 10,

jih bomo ugnezdili v sledeče gnezdo:
`("A", ("P", ("O", ("X", ("Z", )))))`

Sestavite funkcijo `gnezdi`, ki sprejme slovar znakov in njihovih pogostosti,
ter znake gnezdi na zgornji način. Predpostavite lahko, da se pogostosti ne
ponavljajo ter, da je znak vsaj eden.

```python
def gnezdi(slovar):
    # znake uredimo po pogostosti: od najredkejšega proti najpogostejšemu
    # (slovar.get je funkcija, ki znaku priredi njegovo pogostost)
    znaki = sorted(slovar, key=slovar.get)

    # najredkejši znak je v najbolj notranjem naboru, ki ima en sam element
    gnezdo = (znaki[0], )

    # vsak naslednji (pogostejši) znak ovije dosedanje gnezdo v nov par
    for znak in znaki[1:]:
        gnezdo = (znak, gnezdo)
    return gnezdo
```

**Ideja.** Gnezdo gradimo **od znotraj navzven**: začnemo pri najredkejšem
znaku in vsak naslednji (pogostejši) znak ovije dosedanje gnezdo v nov par.

```python
znaki = sorted(slovar, key=slovar.get)   # od najredkejšega proti pogostemu
gnezdo = (znaki[0], )                    # najbolj notranji nabor
for znak in znaki[1:]:
    gnezdo = (znak, gnezdo)              # ovij
```

**`sorted(slovar, key=slovar.get)`.** Sprehod po slovarju da **ključe**;
`key=slovar.get` pove, naj se ureja po pripadajočih vrednostih. Zapis brez
oklepajev je pomemben — `slovar.get` je funkcija, `slovar.get()` bi bil njen
klic.

**Nabor z enim elementom se piše `(znak, )`** — z vejico! Brez nje je `(znak)`
samo znak v oklepajih, torej niz. To je najpogostejši vzrok, da ta naloga ne gre
skozi.

**Pogosta napaka.** Sestavljanje **niza**, ki je videti kot nabor
(`"('A',('P',))"`), izgleda pravilno pri izpisu, a testi primerjajo z resničnim
naborom in bodo padli. Enako velja za rešitev, ki gre po slovarju v vrstnem
redu vstavljanja in pogostosti sploh ne upošteva.

**Predpostavke naloge.** Pogostosti se ne ponavljajo (torej je vrstni red
enolično določen) in znak je vsaj eden (torej `znaki[0]` obstaja).

#### c) `indeks(gnezdo, znak)`

Indeks nekega znaka v danem gnezdu bomo poiskali tako, da bomo zabeležili kakšno zaporedje
indeksov moramo v gnezdu zahtevati, da bomo naleteli ravno na ta znak.

V gnezdu `("A", ("P", ("O", ("X", ("Z", )))))` imajo znaki sledeče indekse:

- `A`: `(0, )`,
- `P`: `(1, 0)`,
- `O`: `(1, 1, 0)`,
- `X`: `(1, 1, 1, 0)`,
- `Z`: `(1, 1, 1, 1, 0)`.

Če zapišemo drugače: `gnezdo[0]` je `A`, `gnezdo[1][0]` je `P`, `gnezdo[1][1][0]` je `O`, itd.

Sestavite funkcijo `indeks`, ki sprejme gnezdo in znak, ter vrne znakov indeks
v podanem gnezdu. Če znaka v gnezdu ni, naj funkcija vrne `None`.

```python
def indeks(gnezdo, znak):
    # prvi element gnezda je znak na tem nivoju
    if gnezdo[0] == znak:
        return (0, )

    # nabor dolžine 1 je najbolj notranje gnezdo, torej znaka ni več kje iskati
    if len(gnezdo) == 1:
        return None

    # sicer se rekurzivno spustimo v drugi element, ki je vgnezdeni nabor
    naprej = indeks(gnezdo[1], znak)
    if naprej is None:
        return None

    # do znaka smo prišli prek indeksa 1, zato ga dodamo pred dobljeno zaporedje
    return (1, ) + naprej
```

**Ideja (rekurzija po strukturi).** Gnezdo je bodisi `(znak, )` bodisi
`(znak, notranje_gnezdo)`. Zato so tudi primeri v funkciji trije:

1. `gnezdo[0] == znak` → našli smo ga, indeks je `(0, )`;
2. `len(gnezdo) == 1` → smo v najbolj notranjem gnezdu in znaka ni → `None`;
3. sicer se spustimo v `gnezdo[1]` in rezultatu **spredaj** dodamo `1`.

**Prenos `None` navzgor.** Če globlji klic vrne `None`, ga moramo vrniti
naprej — `(1, ) + None` bi sprožil `TypeError`. Zato:

```python
naprej = indeks(gnezdo[1], znak)
if naprej is None:
    return None
return (1, ) + naprej
```

To je splošen vzorec: **rezultat rekurzivnega klica vedno najprej preveri,
šele nato ga uporabi.**

**Zakaj se indeksi berejo tako.** `(1, 1, 0)` pomeni `gnezdo[1][1][0]` — dvakrat
se spustimo globlje, nato vzamemo znak. Zapis torej ni »koordinata«, ampak
**pot** do znaka.

**Različica z zanko** (za tiste, ki jim rekurzija ne leži):

```python
def indeks(gnezdo, znak):
    pot = []
    while True:
        if gnezdo[0] == znak:
            return tuple(pot + [0])
        if len(gnezdo) == 1:
            return None
        pot.append(1)
        gnezdo = gnezdo[1]
```

### Naloga 3 — Osebe
*Datoteka `2324_i3/03_osebe.py`*

Razred z razčlenjevanjem EMŠO, metoda, ki spreminja dva objekta hkrati, in
štetje z urejanjem po dveh kriterijih.

#### a) Razred `Oseba` — konstruktor in `__str__`

Centralni register prebivalstva je doživel hekerski napad, zato je treba
začeti z ničle. Definirajte razred `Oseba` s

 - konstruktorjem, ki sprejme nize `ime`, `priimek` in `emso`. Argumente naj
   shrani v istoimenske atribute. Dodatno naj iz EMŠA razbere spol in ga shrani v atribut `spol`
   (vrednost `"M"` oz. `"Ž"`).
 - metodo za lep prikaz osebe, ki npr. za osebo `Oseba("Miha", "Novak", "2506991500001")`
   vrne niz `"Miha Novak (M, 1991)"``

Primer:

```python
>>> miha = Oseba("Miha", "Novak", 2506991500001)
>>> print(miha)
Miha Novak (M, 1991)
```
Opomba: predpostavite lahko, da

 - so osebe žive,
 - se EMŠO začne z datumom rojstva (prva števka letnice je izpuščena),
   ki mu sledi število 500 (moški) ali 505 (ženske).

```python
class Oseba:
    def __init__(self, ime, priimek, emso):
        self.ime = ime
        self.priimek = priimek
        self.emso = str(emso)

        # EMŠO ima obliko DDMMLLL RRR XXX (13 števk):
        #   [0:2] dan, [2:4] mesec, [4:7] zadnje tri števke letnice,
        #   [7:10] 500 za moške in 505 za ženske, [10:13] zaporedna številka.
        self.spol = "M" if self.emso[7:10] == "500" else "Ž"

        # Prva števka letnice je izpuščena. Ker so osebe žive, pomeni
        # 900-999 letnice 1900-1999, 000-899 pa 2000-2899.
        zadnje = int(self.emso[4:7])
        self.letnica = 1000 + zadnje if zadnje >= 900 else 2000 + zadnje

    def __str__(self):
        # __str__ določa, kaj izpiše print(oseba) oz. vrne str(oseba)
        return f"{self.ime} {self.priimek} ({self.spol}, {self.letnica})"
```

**Razčlenitev EMŠO.** Trinajst števk ima ustaljen pomen; za nalogo rabimo tri
dele:

```
2 5 0 6 9 9 1 5 0 0 0 0 1
└─┬─┘ └┬┘ └─┬─┘ └─┬─┘ └─┬─┘
 dan mesec letnica  spol  zap. št.
[0:2] [2:4]  [4:7]  [7:10] [10:13]
```

- **Spol:** `emso[7:10]` je `"500"` za moške in `"505"` za ženske.
- **Letnica:** prva števka je izpuščena, ostanejo tri. Ker so osebe žive,
  pomeni 900–999 letnice 1900–1999, 000–899 pa 2000 in naprej:

```python
zadnje = int(self.emso[4:7])
self.letnica = 1000 + zadnje if zadnje >= 900 else 2000 + zadnje
```

Preveri na testih: `991` → 1991, `900` → 1900, `000` → 2000, `023` → 2023.

**Atribut, ki ga naloga ne zahteva izrecno.** `self.letnica` shranimo, ker ga
potrebujeta `__str__` **in** tretja podnaloga. Bolje enkrat izračunati v
konstruktorju kot dvakrat na različnih mestih.

**`str(emso)`.** Primer v besedilu podaja EMŠO kot število, testi pa kot niz.
S pretvorbo v niz delujeta oba načina, rezanje `[7:10]` pa je smiselno le na
nizu.

**`__str__` vrne niz — nikoli ne izpisuje.** Napaka, ki jo je lahko narediti:

```python
def __str__(self):
    print(f"{self.ime} ...")   # ❌ funkcija vrne None, izpis pride ob napačnem času
```

Pravilno je `return`; za izpis poskrbi klicatelj s `print(oseba)`.

#### b) `poroci(druga_oseba)`

Ljudje se v 21. stoletju poročajo na vse mogoče načine.
V razred `Oseba` dodajte metodo `poroci(druga_oseba)`,
ki spremeni priimka poročenih po naslednjih pravilih:

- Če se poročita moški in ženska, naj mož prevzame ženin priimek,
- Če se poročita moška, naj si priimka izmenjata,
- Če se poročita ženski, naj vsaka v svoj priimek na konec doda priimek druge.

```python
def poroci(self, druga_oseba):
        # dva moška: priimka zamenjata. Zaradi hkratnega prirejanja se
        # desna stran izračuna pred prirejanjem, zato tu ne rabimo pomožne
        # spremenljivke.
        if self.spol == "M" and druga_oseba.spol == "M":
            self.priimek, druga_oseba.priimek = druga_oseba.priimek, self.priimek

        # dve ženski: vsaka svojemu priimku doda priimek druge.
        # Tudi tu je hkratno prirejanje nujno, sicer bi drugi izraz
        # uporabil že spremenjeni self.priimek.
        elif self.spol == "Ž" and druga_oseba.spol == "Ž":
            self.priimek, druga_oseba.priimek = (
                self.priimek + " " + druga_oseba.priimek,
                druga_oseba.priimek + " " + self.priimek,
            )

        # mešan par: moški prevzame ženin priimek. Metodo lahko pokliče
        # katerakoli od obeh oseb, zato pokrijemo obe smeri.
        elif self.spol == "M":
            self.priimek = druga_oseba.priimek
        else:
            druga_oseba.priimek = self.priimek
```

**Ideja.** Trije primeri glede na spola. Metoda spreminja **oba** objekta —
tudi tistega, ki ga dobi kot argument.

| Para | Pravilo | Rezultat |
|---|---|---|
| moški + ženska | mož prevzame ženin priimek | oba `Kovač` |
| moški + moški | priimka se zamenjata | `Novak` ↔ `Kovač` |
| ženska + ženska | vsaka doda priimek druge | `Novak Kovač` in `Kovač Novak` |

**Hkratno prirejanje je nujno.** Pri zamenjavi in pri sestavljanju priimkov se
najprej v celoti izračuna desna stran, šele nato se priredi:

```python
self.priimek, druga.priimek = druga.priimek, self.priimek
```

Če bi pisal v dveh korakih, bi drugi korak že uporabil spremenjeno vrednost in
bi oba dobila isti priimek. To je isti razlog, zakaj `a, b = b, a` zamenja
vrednosti, `a = b; b = a` pa ne.

**Metodo lahko pokliče katerakoli od oseb.** Testi preverjajo `m.poroci(z)`
**in** `z.poroci(m)` in pričakujejo enak rezultat, zato mora mešani primer
pokrivati obe smeri:

```python
elif self.spol == "M":          # jaz sem moški -> prevzamem njen priimek
    self.priimek = druga_oseba.priimek
else:                            # jaz sem ženska -> on prevzame mojega
    druga_oseba.priimek = self.priimek
```

**Metoda ničesar ne vrne**, ker spreminja stanje objektov. To je razlika med
metodami tipa »ukaz« (spremenijo objekt) in »poizvedba« (vrnejo vrednost).

#### c) `najpogostejsa_imena(osebe, spol, obdobje=None)`

SURS zanima, katera so tri najpogostejša imena (po spolih) bodisi na splošno
bodisi med rojenimi določenem obdobju. Izven razreda `Oseba` definirajte
funkcijo `najpogostejsa_imena`, ki sprejme seznam oseb in spol
ter neobvezni argument obdobje, in vrne najpopularnejša tri imena za dani
spol v danem obdobju. Če obdobje ni podano, naj vrne najpopularnejša tri.

```python
>>> o1 = Oseba("Ana Maja", "Novak", "2506991505001")
>>> o2 = Oseba("Brina Maja", "Novak", "2506981505001")
>>> o3 = Oseba("Ana Marija", "Kovač", "2506951505001")
>>> najpogostejsa_imena([o1, o2, o3], "Ž")
["Ana", "Maja", "Brina"]
>>> najpogostejsa_imena([o1, o2, o3], "Ž", obdobje=(1981, 1991))
["Maja", "Ana", "Brina"]
```
Seznam naj bo padajoče urejen po številu pojavitev imena. Če se imeni
pojavita enako pogosto, naj bosta urejeni po abecedi. Obdobje je zaprti interval.

```python
def najpogostejsa_imena(osebe, spol, obdobje=None):
    pogostost = {}

    for oseba in osebe:
        if oseba.spol != spol:
            continue

        # obdobje je zaprti interval; če ni podano, upoštevamo vse letnice
        if obdobje is not None:
            od, do = obdobje
            if not (od <= oseba.letnica <= do):
                continue

        # ime je lahko sestavljeno ("Ana Maja"), zato ga razbijemo na dele
        # in vsakega štejemo posebej
        for del_imena in oseba.ime.split():
            pogostost[del_imena] = pogostost.get(del_imena, 0) + 1

    # Uredimo po dveh kriterijih hkrati: najprej padajoče po številu pojavitev,
    # ob izenačenju pa naraščajoče po abecedi. Ker sorted ureja naraščajoče,
    # padajoče urejanje po številu dosežemo z minusom pred številom.
    urejena = sorted(pogostost.items(), key=lambda par: (-par[1], par[0]))

    # iz parov (ime, pogostost) vzamemo le imena, in sicer prva tri
    return [ime for ime, _ in urejena[:3]]
```

**Ideja.** Filtriraj → preštej → uredi → odreži prve tri. Vsak korak je znan
vzorec, naloga je le v tem, da jih pravilno zložiš.

**Neobvezni argument.** `obdobje=None` pomeni, da ga klicatelj lahko izpusti.
Privzeta vrednost je `None` in **nikoli spremenljiv objekt** (`[]`, `{}`) —
tak privzetek se v Pythonu ustvari enkrat in si spremembe zapomni med klici.

```python
if obdobje is not None:
    od, do = obdobje
    if not (od <= oseba.letnica <= do):
        continue
```

Obdobje je **zaprti interval**, zato `<=` na obeh straneh. Veriženje
`od <= x <= do` je pythonovski zapis za `od <= x and x <= do`.

**Sestavljena imena.** `"Ana Maja"` šteje kot dve imeni, zato `oseba.ime.split()`
in štetje vsakega dela posebej.

**Urejanje po dveh kriterijih hkrati.**

```python
sorted(pogostost.items(), key=lambda par: (-par[1], par[0]))
```

`sorted` ureja naraščajoče in pri naborih primerja po komponentah: najprej
`-pogostost` (minus obrne vrstni red → **padajoče** po pojavitvah), ob
izenačenju pa `ime` (naraščajoče → **abecedno**). Ta trik z minusom deluje samo
za števila; za padajoče urejanje nizov bi potreboval `reverse=True` ali dva
zaporedna `sorted`.

**Zakaj `[:3]` in ne `[0:3]`.** Isto je; rezina brez začetka pomeni »od
začetka«. Če je imen manj kot tri, rezina vrne, kolikor jih je — brez napake.


---

## Kaj se na teh izpitih ponavlja

Vsi trije roki imajo isto zgradbo: **tri naloge po tri podnaloge**, pri čemer
so podnaloge znotraj naloge odvisne druga od druge (b uporablja a, c uporablja
b). Ocenjujejo pa se ločeno — če ti prva ne uspe, napiši svojo različico in
nadaljuj.

Snov, ki se pojavi na vsakem roku:

| Vzorec | Kje se pojavi | Ključni zapis |
|---|---|---|
| Štetje v slovar | `pogostost`, `najpogostejsa_imena`, `stevilo_besed` | `slovar[k] = slovar.get(k, 0) + 1` |
| Urejanje po ključu | `gnezdi`, `najpogostejsa_imena`, `francetov_slovar` | `sorted(x, key=...)`, `key=lambda p: (-p[1], p[0])` |
| Akumulator z izpiranjem | `dolzine_kitic`, `linije` | števec + `append` ob ločnici + `append` po zanki |
| Rekurzija po strukturi | `zlij`, `uredi`, `indeks` | bazni primer **najprej**, nato korak |
| Krožno gibanje | `izlocen`, `zmagovalec` | `% len(seznam)` |
| Branje datoteke | `linije`, `prestej_vrstice`, `odstrani_printe` | `with open(ime, encoding='utf-8')`, `strip()` |
| Pisanje datoteke | `pregledno`, `poenostavi` | `open(ime, 'w')`, `print(..., file=f)` |
| Posebne metode | `Beseda`, `Oseba` | `__init__`, `__str__`, `__repr__`, `__lt__`, `__getitem__` |
| Rezine fiksne dolžine | `zakodiraj` | `range(0, len(x), k)` in `x[i:i+k]` |
| Obrnjena preslikava | `odkodiraj` | `{v: k for k, v in slovar.items()}` |

## Napake, ki so v teh rešitvah dejansko nastale

Spodnje niso izmišljene — vse so bile v prvotnih oddajah teh izpitov.

1. **Sprehod po znakih namesto po vrsticah.** `for vrstica in pesem` gre po
   znakih. Za vrstice rabiš `pesem.split("\n")`.
2. **Primerjava enega znaka z več znaki.** `if znak == '\n\n'` in
   `if znak == 'bcdfg...'` nista nikoli resnična. Za drugo rabiš `in`.
3. **Vrnjen napačen tip.** `return dolzina, seznam` vrne nabor namesto seznama;
   sestavljanje niza `"('A',('P',))"` namesto pravega nabora.
4. **`niz.index(znak)` v zanki.** Vrne mesto **prve** pojavitve, ne trenutne.
   Če rabiš indeks med sprehodom, uporabi `enumerate` ali `range(len(...))`.
5. **Zadnji element se izgubi.** Če v zanki shranjuješ ob ločnici, moraš zadnjo
   skupino shraniti še po zanki.
6. **Kopija namesto istega objekta** (in obratno). Test z `is` zahteva prejeti
   objekt; funkcija, ki spreminja seznam, naj si prej naredi kopijo.
7. **Podnaloga, ki je ostala kopija prejšnje.** Ko rešitev prekopiraš kot
   izhodišče, jo je treba tudi predelati — sicer testi javijo napako pri
   podnalogi, za katero misliš, da je rešena.

## Kako preveriti rešitev

Izpitna datoteka ob zagonu rešitve **odda na strežnik Projekta Tomo** in šele
nato izpiše, katere podnaloge so veljavne. Med učenjem je to povsem v redu
(število poskusov ni omejeno), je pa dobro vedeti, da se zgodi.

Če hočeš samo lokalno preizkusiti posamezno funkcijo, jo pokliči v konzoli:

```python
>>> from importlib import reload
>>> stevilo_zlogov("Rdečo mašno maš v laseh")
[3, 2, 1, 2]
```

Primeri iz besedila naloge (vrstice z `>>>`) so prvi testi, ki jih je vredno
pognati — testi v datoteki jih skoraj vedno vsebujejo, dodajo pa še robne
primere: prazen niz, en sam element, izenačenja.
