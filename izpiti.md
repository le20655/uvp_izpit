# UVP — rešeni izpiti

Vsi izpitni roki predmeta **Uvod v programiranje**, ki so na voljo na Projektu
Tomo — od študijskega leta 2023/24 do 2025/26. Skupaj **devet izpitov, 27 nalog
in 81 podnalog**.

Vsaka podnaloga ima:

1. **besedilo naloge** (dobesedno iz izpitne datoteke),
2. **rešitev**, ki jo lahko kopiraš,
3. **razlago** — ideja, zakaj deluje in kje se da pasti.

> ✅ **Vse rešitve so preverjene.** Vsaka je bila pognana skozi teste, ki so
> vgrajeni v izpitne datoteke Projekta Tomo, in vseh 81 podnalog je označenih
> kot »ima veljavno rešitev«. Koda v tem dokumentu je zajeta neposredno iz teh
> datotek, zato se z njimi ne more razhajati.

## Kazalo

### Študijsko leto 2023/24

| Izpit | Naloga | Snov |
|---|---|---|
| [1. rok](#izpit-1-rok-202324) | [Urejanje z zlivanjem](#naloga-1--urejanje-z-zlivanjem) | rekurzija, deli in vladaj, seznami |
| | [Pesnik France: slovenska abeceda](#naloga-2--pesnik-france-slovenska-abeceda) | razredi, posebne metode, urejanje s ključem |
| | [Avtobusni prevozi](#naloga-3--avtobusni-prevozi) | datoteke, slovarji seznamov, množice |
| [2. rok](#izpit-2-rok-202324) | [Izštevanke](#naloga-1--izštevanke) | krožno štetje, modulo, brisanje iz seznama |
| | [Pesnik France: popravljanje kode](#naloga-2--pesnik-france-popravljanje-kode) | datoteke, obdelava vrstic, regularni izrazi |
| | [Kodiranje v bazi 64](#naloga-3--kodiranje-v-bazi-64) | slovarji, rezine fiksne dolžine, obrnjena preslikava |
| [3. rok](#izpit-3-rok-202324) | [Pesnik France: zlogi in ritem](#naloga-1--pesnik-france-zlogi-in-ritem) | nizi, sosedni znaki, vzorci |
| | [Pogosti znaki](#naloga-2--pogosti-znaki) | slovarji, gnezdeni nabori, rekurzija |
| | [Osebe](#naloga-3--osebe) | razredi, razčlenjevanje EMŠO, urejanje po dveh ključih |

### Študijsko leto 2024/25

| Izpit | Naloga | Snov |
|---|---|---|
| [1. rok](#izpit-1-rok-202425) | [Klepet](#naloga-1--klepet) | gnezdene strukture, množice, regularni izrazi |
| | [Zaredba na otoku Katan](#naloga-2--zaredba-na-otoku-katan) | razredi, slovar seznamov, `random` |
| | [Osmerosmerke](#naloga-3--osmerosmerke) | mreža, osem smeri, datoteke |
| [2. rok](#izpit-2-rok-202425) | [Prispevki za piknik](#naloga-1--prispevki-za-piknik) | gnezdeni slovarji, povprečja, plavajoča vejica |
| | [Dvigala](#naloga-2--dvigala) | razredi, privzeti argumenti, iskanje indeksa |
| | [Potapljanje ladjic](#naloga-3--potapljanje-ladjic) | matrike, koordinate, branje in pisanje datotek |
| [3. rok](#izpit-3-rok-202425) | [Analiza DNA](#naloga-1--analiza-dna) | nizi, validacija, `None` proti praznemu |
| | [Telefonski imenik](#naloga-2--telefonski-imenik) | razredi, `__repr__`/`__str__`, `isinstance` |
| | [Orientacijski tek](#naloga-3--orientacijski-tek) | filtriranje seznamov, časi, pisanje poročila |

### Študijsko leto 2025/26

| Izpit | Naloga | Snov |
|---|---|---|
| [1. rok](#izpit-1-rok-202526) | [Značke](#naloga-1--značke) | regularni izrazi, deleži, `None` proti 0 |
| | [Štetje](#naloga-2--štetje) | razred kot `Counter`, `__eq__`, unija in presek |
| | [Dostavljalec Miran](#naloga-3--dostavljalec-miran) | koordinate, razdalje, urejanje s ključem |
| [2. rok](#izpit-2-rok-202526) | [Vrhskala](#naloga-2--vrhskala) | razredi, simulacija gibanja, stanje |
| | [Razbitje](#naloga-3--razbitje) | rekurzija s sestopanjem, naštevanje vseh rešitev |
| | [Air Triglav](#naloga-4--air-triglav) | CSV, `zip`, slovar z naborom kot ključem |
| [Poskusni](#poskusni-izpit-202526) | [Sprehodi](#naloga-1--sprehodi) | razčlenjevanje niza, stanje med branjem |
| | [GPS](#naloga-2--gps) | datoteke, pretvorbe enot, zaporedne meritve |
| | [Koda QR](#naloga-3--koda-qr) | razred z matriko, polnjenje po vzorcu |

Sorodni dokumenti v tem repozitoriju:

- [`izpitni_prirocnik.md`](izpitni_prirocnik.md) — postopek reševanja in snov po tipih nalog,
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

## Izpit 1. rok 2024/25
Prvi rok 2024/25: delo z gnezdenimi strukturami in regularnimi izrazi, razred s
simulacijo ter mreža z osmimi smermi.

### Naloga 1 — Klepet
*Datoteka `2425_i1/01_klepet.py`*

Podatki so slovarji s seznami parov. Vse tri podnaloge se vrtijo okoli
istega sprehoda; razlikuje se le, kaj med njim zbiramo — množico, števce ali
ujemanja regularnega izraza.

#### a) `stisni(pogovor)`

Za potrebe arhiviranja bomo pogovor še nekoliko stisnili. Sestavite funkcijo
`stisni`, ki prejme pogovor kot zgoraj in ga vrne stisnjeno obliko:
trojico oblike `(naslov, stevilo_sodelujocih, stevilo_sporocil)`.

Primer uporabe:

```python
>>> stisni(pogovor1)
('Kam gremo jest?', 3, 3)
>>> stisni(pogovor2)
('Živjo svet', 1, 2)
```

```python
def stisni(pogovor):
    sporocila = pogovor["sporocila"]

    # množica avtorjev: vsak se v njej pojavi natanko enkrat, zato je
    # njena velikost ravno število sodelujočih
    sodelujoci = {avtor for avtor, besedilo in sporocila}

    return (pogovor["naslov"], len(sodelujoci), len(sporocila))
```

**Ideja.** Pogovor je slovar z dvema ključema: `naslov` in `sporocila`, kjer je
vsako sporočilo par `(avtor, besedilo)`. Naloga hoče trojico.

**Množica namesto štetja.** Število sodelujočih je število **različnih**
avtorjev. Namesto slovarja s števci zadošča množica — vsak avtor se vanjo
zapiše enkrat, ne glede na to, kolikokrat nastopi:

```python
sodelujoci = {avtor for avtor, besedilo in sporocila}
```

To je izpeljana množica (*set comprehension*); enako bi dosegel s
`set(avtor for avtor, besedilo in sporocila)`.

**Razstavljanje v zanki.** `for avtor, besedilo in sporocila` sproti razpakira
par. Če drugega dela ne rabiš, se pogosto piše `for avtor, _ in sporocila` —
podčrtaj je dogovor za »ta vrednost me ne zanima«.

**Rezultat mora biti nabor**, ne seznam: `return (a, b, c)`.

#### b) `klepetulja(pogovori)`

Sestavite funkcijo `klepetulja`, ki sprejme seznam pogovorov (opisanih kot zgoraj),
in vrne osebo, ki je v vseh vseh pogovorih poslala največ sporočil. Če je takih oseb več,
naj metoda vrne eno izmed njih.

Primer uporabe:

```python
>>> klepetulja([pogovor1, pogovor2])
'Aljaž'
>>> klepetulja([pogovor1, pogovor3])
'Tea'
```

```python
def klepetulja(pogovori):
    stevec = {}

    # seštevamo čez vse pogovore skupaj, ne po posameznem pogovoru
    for pogovor in pogovori:
        for avtor, besedilo in pogovor["sporocila"]:
            stevec[avtor] = stevec.get(avtor, 0) + 1

    # max po ključih slovarja, kjer je merilo pripadajoča vrednost;
    # ob izenačenju vrne prvega, kar naloga dovoli
    return max(stevec, key=stevec.get)
```

**Ideja.** Klasično štetje v slovar, le da tokrat čez **vse** pogovore skupaj —
zato je zanka dvojna: po pogovorih in znotraj vsakega po sporočilih.

```python
stevec[avtor] = stevec.get(avtor, 0) + 1
```

**Iskanje največjega ključa.**

```python
return max(stevec, key=stevec.get)
```

Sprehod po slovarju da **ključe**, `key=stevec.get` pa pove, naj se primerja po
pripadajočih vrednostih. Ob izenačenju `max` vrne prvega, kar naloga izrecno
dovoli.

**Pogosta zmeda.** `max(stevec)` brez `key` bi vrnil abecedno največje ime,
`max(stevec.values())` pa največje **število** namesto imena. Pravilna
kombinacija je ta zgoraj.

#### c) `custvencki(pogovori)`

Opazimo, da so pri izvozu podatkov vsi čustvenčki postali besedilo oblike `:custvencek:`; v zgornjih primerih opazimo `:thumbsup:` in `:cry:`.
Za definicijo čustvenčka bomo zahtevali, da se začne in konča z `:` vmes pa so lahko le male črke angleške abecede.
Sestavite funkcijo `custvencki`, sprejme seznam pogovorov in vrne **množico** vseh čustvenčkov, ki se v pogovorih pojavijo.

Primer uporabe:

```python
>>> custvencki([pogovor1, pogovor2])
{':thumbsup:', ':cry:'}
>>> custvencki([pogovor3])
set()
```

```python
import re

# ':' + vsaj ena mala angleška črka + ':'
CUSTVENCEK = re.compile(r":[a-z]+:")


def custvencki(pogovori):
    najdeni = set()
    for pogovor in pogovori:
        for avtor, besedilo in pogovor["sporocila"]:
            # findall vrne seznam vseh ujemanj; z |= ga zlijemo v množico
            najdeni |= set(CUSTVENCEK.findall(besedilo))
    return najdeni
```

**Ideja.** Čustvenček je vzorec `:beseda:`, kjer so vmes le male angleške črke.
To je natanko delo za regularni izraz:

```python
CUSTVENCEK = re.compile(r":[a-z]+:")
```

| Del | Pomen |
|---|---|
| `:` | dobesedno dvopičje |
| `[a-z]+` | ena ali več malih angleških črk (`+` pomeni »vsaj ena«) |
| `:` | zaključno dvopičje |

`+` je pomemben: z `*` bi se ujelo tudi golo `::`.

**Zakaj `re.compile` zunaj funkcije.** Vzorec se prevede enkrat, ne ob vsakem
klicu. Za izpit je enakovredno tudi `re.findall(r":[a-z]+:", besedilo)`.

**Zlivanje množic.** `najdeni |= set(...)` je krajši zapis za
`najdeni = najdeni | set(...)`, torej unijo. Enako dela `najdeni.update(...)`.

**Robni primer.** Če čustvenčkov ni, funkcija vrne prazno množico `set()` —
in ne `{}`, kar je prazen **slovar**.

### Naloga 2 — Zaredba na otoku Katan
*Datoteka `2425_i1/02_zareditev_na_otoku_katan.py`*

Naloga o razredih, v kateri je največ vredna pravilna izbira podatkovne
strukture: slovar seznamov, ki metu kock priredi dobrine.

#### a) `roka_usode(vsota=None)`

Sestavite funkcijo `roka_usode`, ki simulira vsoto pik pri metu dveh (pravičnih) 6-stranih
kock. Za naključna števila uporabite funkcijo `randint` v knjižnici `random`.
Funkcija naj ima tudi pomožni argument `vsota`. Če je argument podan, kar določi vsoto, ki
jo funkcija vrne.

Primer uporabe:

```python
>>> roka_usode()
7
>>> roka_usode(vsota=12)
12
```
_Pozor:_ če argumetna `vsota` ne podamo, mora biti rezultat naključen.

```python
from random import randint


def roka_usode(vsota=None):
    # neobvezni argument: če ga klicatelj poda, ga preprosto vrnemo,
    # sicer vržemo dve kocki. Privzeta vrednost je None in ne npr. 0,
    # ker je 0 sicer veljavno število, ki bi ga kdo lahko podal.
    if vsota is not None:
        return vsota
    return randint(1, 6) + randint(1, 6)
```

**Ideja.** Funkcija ima neobvezni argument: če je podan, ga vrne, sicer vrže
dve kocki.

```python
from random import randint

def roka_usode(vsota=None):
    if vsota is not None:
        return vsota
    return randint(1, 6) + randint(1, 6)
```

**Zakaj privzeta vrednost `None` in ne `0`.** Ker je 0 lahko veljaven podatek;
`None` pa pomeni »ni bilo podano«. Iz istega razloga primerjamo z `is not None`
in ne z `if vsota:` — slednje bi pri `vsota=0` napačno metalo kocki.

**Dvakrat `randint(1, 6)`, ne `randint(2, 12)`.** Vsota dveh kock ni enakomerno
porazdeljena: 7 je šestkrat verjetnejša od 2. Simulirati je treba metanje, ne
rezultata.

`randint(a, b)` vključuje **obe** meji — drugače kot `range(a, b)`.

#### b) Razred `Naseljenec` — konstruktor in izpis

Sestavite razred `Naseljenec`, ki bo predstavljal zarejenega naseljenca.
Konstruktor naj prejme ime naseljenca, ki ga shrani v atribut `ime`, poleg tega
pa naj pripravi še atributa `dobrine`, ki začne kot prazen seznam, in `rop`, ki
začne kot prazen slovar. Dodajte še ustrezni metodi `__str__` in `__repr__` (pravilnosti ene izmed njiju Tomo ne preverja).

```python
class Naseljenec:
    def __init__(self, ime):
        self.ime = ime
        self.dobrine = []   # kar je naseljenec doslej nabral
        self.rop = {}       # vsota pik -> seznam dobrin, ki jih tedaj oropa

    def __repr__(self):
        # repr simulira klic konstruktorja; !r poskrbi za narekovaje okoli imena
        return f"Naseljenec({self.ime!r})"

    def __str__(self):
        return f"Naseljenec {self.ime} z dobrinami {self.dobrine}"
```

**Ideja.** Konstruktor poleg imena pripravi tudi dve prazni zbirki, ki ju
napolnita metodi iz naslednje podnaloge:

- `dobrine` — seznam, ker se dobrine lahko ponavljajo in nas zanima vrstni red,
- `rop` — slovar, ker iščemo po metu kocke: `vsota -> seznam dobrin`.

**Izbira strukture je bistvo naloge.** Če bi bil `rop` seznam, bi moral ob
vsakem metu preiskati vse zapise; slovar da odgovor neposredno.

**`__repr__` proti `__str__`.**

```python
def __repr__(self):
    return f"Naseljenec({self.ime!r})"     # simulira klic konstruktorja
```

`!r` v f-nizu pokliče `repr` na vrednosti, zato se okoli imena izpišejo
narekovaji — `Naseljenec('Ana')` in ne `Naseljenec(Ana)`. Naloga pravi, da
pravilnosti ene od obeh metod Tomo ne preverja, a je dobra navada napisati
obe: `__repr__` za razvijalca, `__str__` za uporabnika.

#### c) Metodi `ropa` in `usoda`

Razredu dodajte še metodo `ropa`, ki doda novo surovino za ropanje.
Metoda naj kot argumenta sprejme število med 1 in 12 ter niz, ki opisuje,
katero dobrino bo naseljenec oropal, če usoda z metom kock
določi to število. Posodobite atribut `rop` tako, da bo pod ključem podane vsote števila pik
shranjen seznam dobrin, ki jih naseljenec ob tem metu usode oropa.

Poleg tega dodajte še metodo `usoda`, ki sprejme število med 1 in 12, ter na podlagi vrednosti v atributu `rop` v
naseljenčeve dobrine (tj. v atribut `dobrine`) doda tiste dobrine, ki jih s tem metom usode oropa. Metoda
naj tudi vrne seznam novo pridobljenih surovin.

Primer uporabe:

```python
>>> ana = Naseljenec('Ana')
>>> ana.ropa(6, 'ovca')
>>> ana.ropa(6, 'kamen')
>>> ana.ropa(8, 'pšenica')
>>> ana.ropa(11, 'glina')
>>> ana.dobrine
[]
>>> ana.usoda(6)
['ovca', 'kamen']
>>> ana.dobrine
['ovca', 'kamen']
>>> ana.usoda(8)
['pšenica']
>>> ana.dobrine
['ovca', 'kamen', 'pšenica']
>>> ana.usoda(4)
[]
>>> ana.dobrine
['ovca', 'kamen', 'pšenica']
```

```python
def ropa(self, vsota, dobrina):
        # setdefault vrne obstoječi seznam ali pa najprej vstavi praznega —
        # tako lahko takoj kličemo .append()
        self.rop.setdefault(vsota, []).append(dobrina)

    def usoda(self, vsota):
        # get z privzetim [] pokrije mete, za katere naseljenec nima ropa
        nove = self.rop.get(vsota, [])

        # extend doda elemente enega seznama v drugega (append bi dodal
        # cel seznam kot en element)
        self.dobrine.extend(nove)

        # vrnemo kopijo, da klicatelj s spreminjanjem rezultata ne bi
        # posegel v self.rop
        return list(nove)
```

**`ropa` — dodajanje v slovar seznamov.**

```python
self.rop.setdefault(vsota, []).append(dobrina)
```

`setdefault(kljuc, [])` vrne obstoječi seznam ali pa najprej vstavi praznega in
vrne tega — zato lahko takoj kličemo `.append()`. Brez njega bi pisali:

```python
if vsota not in self.rop:
    self.rop[vsota] = []
self.rop[vsota].append(dobrina)
```

**`usoda` — `extend` proti `append`.**

```python
self.dobrine.extend(nove)     # doda ELEMENTE seznama
self.dobrine.append(nove)     # ❌ doda cel seznam kot en element
```

Po `append` bi bilo `dobrine` enako `[['ovca', 'kamen']]` namesto
`['ovca', 'kamen']`.

**Zakaj vrnemo kopijo.** `self.rop.get(vsota, [])` vrne **isti** seznam, kot je
shranjen v slovarju. Če bi ga vrnili neposredno, bi ga klicatelj lahko
spremenil in s tem tiho pokvaril stanje objekta. `return list(nove)` naredi
kopijo.

**`get` s privzeto vrednostjo** poskrbi za mete, za katere naseljenec nima
ničesar — takrat vrne prazen seznam in `dobrine` ostanejo nespremenjene.

### Naloga 3 — Osmerosmerke
*Datoteka `2425_i1/03_osmerosmerke.py`*

Šolski primer stopnjevanja: preveri eno mesto, nato preišči vsa mesta, nato
uporabi vse skupaj na podatkih iz datoteke.

#### a) `preveri_besedo(mreza, beseda, zacetek, smer)`

Sestavi funkcijo `preveri_besedo(mreza, beseda, zacetek, smer)`, ki preveri,
ali se v mreži `mreza` nahaja beseda `beseda` z začetkom v polju `zacetek`,
ki je podano s parom koordinat (vrstica, stolpec), ter gledano v smeri `smer`,
ki je podana z enim od osmih smernih vektorjev (-1, -1), (-1, 0), (-1, 1),
(0, -1), (0, 1), (1, -1), (1, 0), (1, 1).

```python
>>> mreza = ['atene',
             'otrop',
             'oeisl',
             'blmoa']
>>> preveri_besedo(mreza, 'bern', (3, 0), (-1, 1))
True
>>> preveri_besedo(mreza, 'plaz', (1, 4), (1, 0))
False
```

```python
def preveri_besedo(mreza, beseda, zacetek, smer):
    i, j = zacetek
    di, dj = smer

    for znak in beseda:
        # preverjanje robov mora biti PRED branjem mreza[i][j], sicer
        # negativni indeks tiho prebere znak z drugega konca vrstice
        if not (0 <= i < len(mreza) and 0 <= j < len(mreza[i])):
            return False
        if mreza[i][j] != znak:
            return False

        # korak v podano smer
        i += di
        j += dj

    return True
```

**Ideja.** Od začetnega polja korakamo v podano smer in primerjamo črko za
črko. Smer je par `(di, dj)`, kar korak zapiše kot `i += di`, `j += dj` — brez
osmih ločenih primerov.

**Vrstni red preverjanj je kritičen.**

```python
if not (0 <= i < len(mreza) and 0 <= j < len(mreza[i])):
    return False
if mreza[i][j] != znak:
    return False
```

Robove je treba preveriti **pred** branjem. Python namreč negativnih indeksov
ne zavrne — `mreza[0][-1]` tiho vrne zadnji znak prve vrstice. Beseda, ki
»pade« čez levi rob, bi se torej lahko lažno ujela z znaki na desni strani.

**Veriženje primerjav.** `0 <= i < len(mreza)` je krajši zapis za
`0 <= i and i < len(mreza)`.

**Zakaj `len(mreza[i])` in ne `len(mreza[0])`.** Ker preverjamo dolžino tiste
vrstice, v katero dejansko gledamo. Pri pravokotni mreži je vseeno, pri
nepravilni pa ne.

#### b) `poisci_besedo(mreza, beseda)`

Sestavi funkcijo `poisci_besedo(mreza, beseda)`, ki v mreži `mreza` poišče
besedo `beseda`. Vrne naj polje, kjer se beseda prične, in smer, v katero
je beseda zapisana. Če iskane besede ne najde, naj vrne `None`.

```python
>>> poisci_besedo(mreza, 'bern')
((3, 0), (-1, 1))
>>> poisci_besedo(mreza, 'plaz')
None
```

```python
# vseh osem smeri: vse kombinacije premikov -1, 0, 1 razen stanja (0, 0)
SMERI = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def poisci_besedo(mreza, beseda):
    # groba sila: vsako polje kot možen začetek, vsaka od osmih smeri
    for i in range(len(mreza)):
        for j in range(len(mreza[i])):
            for smer in SMERI:
                if preveri_besedo(mreza, beseda, (i, j), smer):
                    return ((i, j), smer)
    return None
```

**Ideja.** Groba sila: vsako polje kot možen začetek, vsaka od osmih smeri.
Ker je delo že opravljeno v prejšnji podnalogi, je koda kratka:

```python
for i in range(len(mreza)):
    for j in range(len(mreza[i])):
        for smer in SMERI:
            if preveri_besedo(mreza, beseda, (i, j), smer):
                return ((i, j), smer)
return None
```

**Osem smeri.** To so vse kombinacije premikov −1, 0, 1, razen `(0, 0)`:

```python
SMERI = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]
```

Zapisane v obliki kvadratka se lažje preveri, da nobena ne manjka. Isto bi
dobil z izpeljanim seznamom:
`[(di, dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0)]`.

**`return` sredi trojne zanke** je najbolj pregleden način, da vse tri zanke
prekineš hkrati — `break` bi prekinil le najbolj notranjo.

**Zakaj je pomembno, da najdemo prvo.** Naslednja podnaloga na najdenem mestu
črta besedo. Če bi našli drugo pojavitev, bi bil končni ostanek črk drugačen.

#### c) `osmerosmerka(dat_mreza, dat_besede)`

Osmerosmerke si običajno pripravimo na datotekah, in sicer ločeno mrežo ter
besede, ki jih iščemo. Sestavi funkcijo `osmerosmerka(dat_mreza, dat_besede)`,
ki iz datoteke z imenom `dat_mreza` prebere mrežo, iz datoteke z imenom
`dat_besede` pa besede ter reši dobljeno osmerosmerko. Predpostaviš lahko,
da se vse besede res nahajajo v mreži. Funkcija naj vrne niz, sestavljen
iz neprečrtanih črk v mreži, brano po vrsticah.

Če imamo datoteko z imenom `'mreza.txt'` z vsebino

```
atene
otrop
oeisl
blmoa
```
in datoteko z imenom `'besede.txt'` z vsebino

```
alpe
atene
bern
porto
rim
```
potem dobimo:

```python
>>> osmerosmerka('mreza.txt', 'besede.txt')
'oslo'
```

```python
def preberi_vrstice(ime):
    """Vrne seznam nepraznih vrstic datoteke, brez prelomov."""
    with open(ime, encoding="utf-8") as f:
        return [vrstica.strip() for vrstica in f if vrstica.strip()]


def osmerosmerka(dat_mreza, dat_besede):
    mreza = preberi_vrstice(dat_mreza)
    besede = preberi_vrstice(dat_besede)

    # koordinate vseh prečrtanih črk; množica, ker se besede lahko križajo
    # in bi isto polje sicer prečrtali večkrat
    prectrtane = set()

    for beseda in besede:
        najdba = poisci_besedo(mreza, beseda)
        if najdba is None:
            continue
        (i, j), (di, dj) = najdba
        # ponovimo toliko korakov, kolikor je črk v besedi
        for znak in beseda:
            prectrtane.add((i, j))
            i += di
            j += dj

    # neprečrtane črke po vrsticah od leve proti desni
    ostanek = ""
    for i in range(len(mreza)):
        for j in range(len(mreza[i])):
            if (i, j) not in prectrtane:
                ostanek += mreza[i][j]
    return ostanek
```

**Ideja.** Preberi obe datoteki, vsako besedo poišči in si zapomni **koordinate**
prečrtanih črk, na koncu pa preberi, kar je ostalo.

**Zakaj množica koordinat.** Besede se v osmerosmerki križajo, isto polje je
lahko prečrtano večkrat. Množica poskrbi, da to ni problem, hkrati pa je
preverjanje `(i, j) not in prectrtane` hitro.

**Alternativa, ki je slabša:** prepisovati črke v mreži s presledki. Mreža je
seznam **nizov**, nizi pa so nespremenljivi — `mreza[i][j] = ' '` sproži
`TypeError`. Moral bi jih pretvoriti v sezname znakov.

**Ponovno prehodimo besedo.** Iz najdbe dobimo le začetek in smer, zato moramo
za črtanje ponoviti korake:

```python
(i, j), (di, dj) = najdba
for znak in beseda:
    prectrtane.add((i, j))
    i += di
    j += dj
```

Zanka `for znak in beseda` tu služi le kot števec — teče tolikokrat, kolikor je
črk. Enakovredno bi bilo `for _ in range(len(beseda))`.

**Branje datoteke z izpeljanim seznamom:**

```python
[vrstica.strip() for vrstica in f if vrstica.strip()]
```

`strip()` odreže prelome, pogoj `if` pa izpusti prazne vrstice (npr. zadnjo).

---

## Izpit 2. rok 2024/25
Drugi rok 2024/25: gnezdeni slovarji z računanjem, razred s privzetimi
vrednostmi in dvodimenzionalna plošča z branjem ter pisanjem datotek.

### Naloga 1 — Prispevki za piknik
*Datoteka `2425_i2/01_prispevki_za_piknik.py`*

Tri podnaloge, ki se nadgrajujejo: seštej po jedeh, seštej po osebah, primerjaj
s pravičnim deležem. Tretja podnaloga naravnost kliče prvo in drugo.

#### a) `zbrano(prispevki)`

Prijatelje zanima, koliko enot posameznih jedi in pijač so zbrali. Sestavi
funkcijo `zbrano(prispevki)`, ki sprejme slovar prispevkov udeležencev piknika
in vrne slovar, ki za vsako jed ali pijačo pove, koliko enot so zbrali.

Primer za slovar `prispevki`:

```python
>>> zbrano(prispevki)
{
    "radler": 10,
    "lepinja": 9,
    "čevapčiči": 4,
    "perutničke": 4,
    "kajmak": 3
}
```

```python
def zbrano(prispevki):
    skupaj = {}
    # prispevki so gnezden slovar: oseba -> {jed: kolicina}
    for oseba, dobrine in prispevki.items():
        for jed, kolicina in dobrine.items():
            skupaj[jed] = skupaj.get(jed, 0) + kolicina
    return skupaj
```

**Ideja.** `prispevki` je **gnezden slovar**: `oseba -> {jed: kolicina}`. Za
seštevanje po jedeh gremo v dveh zankah in seštevamo v nov slovar.

```python
for oseba, dobrine in prispevki.items():
    for jed, kolicina in dobrine.items():
        skupaj[jed] = skupaj.get(jed, 0) + kolicina
```

**`.items()` da pare ključ-vrednost.** Brez njega bi sprehod dal samo ključe:
`for oseba in prispevki` da imena, ne pa njihovih prispevkov.

**Robni primeri pridejo zastonj.** Prazen slovar → zanka se ne izvede → `{}`.
Oseba brez prispevkov (`{"Cene": {}}`) → notranja zanka se ne izvede → prav
tako `{}`. Posebnih primerov ni treba pisati.

#### b) `prispevki_oseb(prispevki, cene)`

Prijatelje zanima, koliko je posameznik prispeval k uspehu piknika. V slovarju
so zbrali okvirne cene posameznih jedi in pijač.

Primer slovarja s cenami:

```
cene = {"radler": 1.20, "kajmak": 3.30, "lepinja": 0.70, "perutničke": 5.50, "čevapčiči": 5.30}
```
Sestavi funkcijo `prispevki_oseb(prispevki, cene)`, ki sprejme slovarja prispevkov
in cen ter vrne slovar, ki imenom oseb pripiše skupno ceno njihovih prispevkov.

```python
>>> prispevki_oseb(prispevki, cene)
{
    "Alenka": 10.2,
    "Bojan": 16.5,
    "Cene": 0,
    "Dani": 24.9,
    "Erik": 19.8,
    "Francka": 0
}
```

```python
def prispevki_oseb(prispevki, cene):
    vrednosti = {}
    for oseba, dobrine in prispevki.items():
        vsota = 0
        for jed, kolicina in dobrine.items():
            vsota += kolicina * cene[jed]
        # osebo zabeležimo tudi, če ni prinesla ničesar (vsota ostane 0)
        vrednosti[oseba] = vsota
    return vrednosti
```

**Ideja.** Za vsako osebo seštej `kolicina * cena` čez vse njene prispevke.

**Ključna razlika glede na prejšnjo podnalogo:** rezultat ima **vedno vse
osebe**, tudi tiste s praznim prispevkom — te dobijo 0. Zato vsoto začnemo pri
0 in jo zapišemo v slovar ne glede na to, ali se je kaj prištelo.

**Cena se bere iz drugega slovarja:** `cene[jed]`. Če bi kakšna jed manjkala,
bi to bil `KeyError`; naloga zagotavlja, da so vse cene znane, zato `get` ni
potreben.

**Plavajoča vejica.** `1.2 * 3` v Pythonu ni natanko `3.6`, ampak
`3.6000000000000005`. Testi to upoštevajo (primerjajo zaokroženo), zato tu
zaokroževanje ni nujno — je pa nujno v naslednji podnalogi, kjer rezultat
primerjamo z 0.

#### c) `dolzniki(prispevki, cene)`

Da bodo pikniki v prihodnje bolj pravični, so se odločili, da preverijo dolg
vsakega udeleženca. Zanima jih, koliko je prispevek posameznika manjši od pravičnega
deleža. Če je, na primer, 5 prijateljev skupaj prineslo za 50 evrov hrane in pijače in
je Bojan prinesel le kajmak za 3.3 evre, potem njegov dolg znaša 6.7 evra.

Sestavi funkcijo `dolzniki(prispevki, cene)`, ki za dana slovarja prispevkov in cen
vrne slovar, ki za vsakega udeleženca zabeleži njegov dolg. Slovar naj ne vsebuje udeležencev,
ki ničesar ne dolgujejo.

Primer:

```python
>>> dolzniki(prispevki, cene)
{
    "Alenka": 1.7,
    "Cene": 11.9,
    "Francka": 12.9
}
```

```python
def dolzniki(prispevki, cene):
    if not prispevki:
        return {}

    # ponovna uporaba prejšnje podnaloge
    vrednosti = prispevki_oseb(prispevki, cene)

    # pravični delež = skupna vrednost, deljena s številom udeležencev
    pravicni_delez = sum(vrednosti.values()) / len(vrednosti)

    dolgovi = {}
    for oseba, prispeval in vrednosti.items():
        # zaokrožitev odpravi ostanke plavajoče vejice (npr. 1.7000000000000011),
        # hkrati pa poskrbi, da natanko pravičen prispevek da 0.0 in ne 1e-16
        dolg = round(pravicni_delez - prispeval, 6)
        if dolg > 0:
            dolgovi[oseba] = dolg
    return dolgovi
```

**Ideja.** Pravični delež je skupna vrednost, deljena s številom udeležencev.
Kdor je prispeval manj, dolguje razliko.

```python
vrednosti = prispevki_oseb(prispevki, cene)          # ponovna uporaba
pravicni_delez = sum(vrednosti.values()) / len(vrednosti)
```

**Ponovna uporaba prejšnje podnaloge** je tu pravi prijem — vrednosti so že
izračunane, druge poti do njih ni treba pisati.

**Zaokrožitev ni kozmetika, ampak nujna.**

```python
dolg = round(pravicni_delez - prispeval, 6)
if dolg > 0:
    dolgovi[oseba] = dolg
```

Kdor je prispeval natanko pravični delež, bi zaradi plavajoče vejice lahko
dobil dolg velikosti `1e-16`, kar je `> 0`, in bi se po nepotrebnem znašel v
rezultatu. Zaokrožitev to odpravi.

**Naloga zahteva, da dolžnikov brez dolga v slovarju ni** — torej ne
`dolgovi[oseba] = 0`, ampak osebo preprosto izpustimo. Enako velja za tiste,
ki so prispevali več od deleža (negativen »dolg«).

**Deljenje z nič.** Pri praznem slovarju bi `len(vrednosti)` bil 0. Zato na
začetku `if not prispevki: return {}`.

### Naloga 2 — Dvigala
*Datoteka `2425_i2/02_dvigala.py`*

Kratka naloga z dvema klasičnima pastema: spremenljiva privzeta vrednost
argumenta in iskanje **indeksa** namesto elementa.

#### a) Razred `Dvigalo` — konstruktor in `__repr__`

Sestavite razred `Dvigalo`, ki opisuje trenutno stanje dvigala. Konstruktor
naj za parametra prejme trenuten položaj dvigala in seznam postankov, ter
ju uporabi za nastavitev atributov `nadstropje` in `postanki`. Privzeti
vrednosti parametrov nastavite tako, da bomo dobili mirujoče dvigalo v pritličju.

Sestavite še metodo `__repr__`, ki vrne znakovni opis dvigala kot je prikazano
v spodnjem primeru.

```python
>>> dvigalo = Dvigalo(3, [1, 5, 0, 4])
>>> dvigalo.nadstropje
3
>>> dvigalo.postanki
[1, 5, 0, 4]
>>> repr(dvigalo)
'Dvigalo(3, [1, 5, 0, 4])'
```

```python
class Dvigalo:
    def __init__(self, nadstropje=0, postanki=None):
        self.nadstropje = nadstropje

        # Privzeta vrednost NE sme biti [] — privzetki se ustvarijo enkrat ob
        # definiciji funkcije, zato bi si vsa dvigala delila isti seznam in bi
        # postanek, dodan enemu, videla vsa.
        self.postanki = [] if postanki is None else postanki

    def __repr__(self):
        return f"Dvigalo({self.nadstropje}, {self.postanki})"
```

**Past s privzeto vrednostjo.** Naloga hoče, da `Dvigalo()` da mirujoče dvigalo
v pritličju. Zapis

```python
def __init__(self, nadstropje=0, postanki=[]):     # ❌
```

je ena najbolj znanih pasti v Pythonu: privzeta vrednost se ustvari **enkrat**,
ob definiciji funkcije, in si jo delijo vsi objekti. Postanek, dodan enemu
dvigalu, bi videla vsa. Test to izrecno preverja:

```python
d1 = Dvigalo(1); d2 = Dvigalo(2)
d1.postanki.append(0)
# d2.postanki mora ostati []
```

Pravilno je:

```python
def __init__(self, nadstropje=0, postanki=None):
    self.postanki = [] if postanki is None else postanki
```

**Pravilo:** privzeta vrednost naj bo vedno nespremenljiva (`None`, število,
niz, nabor). Spremenljive (`[]`, `{}`, `set()`) nikoli.

**`__repr__`** vrne `Dvigalo(3, [1, 5, 0, 4])`. Seznam se v f-nizu izpiše sam
od sebe v pravi obliki, zato dodatnega dela ni.

#### b) `razdalja(nadstropje)`

Razredu `Dvigalo` dodajte metodo `razdalja`, ki izračuna in vrne razdaljo
dvigala do danega nadstropja. Če dvigalo miruje, je razdalja enaka absolutni
vrednosti razlike med trenutnim položajem in danim nadstropjem, sicer pa
razdaljo dobimo kot vsoto razdalj od trenutnega položaja preko vseh postankov
do danega nadstropja.

```python
>>> dvigalo.razdalja(2)
17
```

```python
def razdalja(self, nadstropje):
        # Pot dvigala: trenutni položaj, vsi postanki po vrsti, nato cilj.
        # Če je seznam postankov prazen, ostane [polozaj, cilj] in formula
        # sama od sebe da |polozaj - cilj| — posebnega primera ne rabimo.
        pot = [self.nadstropje] + self.postanki + [nadstropje]

        skupaj = 0
        for i in range(len(pot) - 1):
            skupaj += abs(pot[i + 1] - pot[i])
        return skupaj
```

**Ideja.** Pot dvigala je zaporedje točk: trenutni položaj, vsi postanki po
vrsti, na koncu ciljno nadstropje. Razdalja je vsota absolutnih razlik med
zaporednimi točkami.

```python
pot = [self.nadstropje] + self.postanki + [nadstropje]
skupaj = 0
for i in range(len(pot) - 1):
    skupaj += abs(pot[i + 1] - pot[i])
```

**Posebnega primera za mirujoče dvigalo ni treba pisati.** Če je seznam
postankov prazen, ostane `pot = [polozaj, cilj]`, zanka teče enkrat in formula
da `|polozaj − cilj|` — natanko to, kar zahteva naloga. Splošna formula, ki
robni primer požre sama, je vedno boljša od dveh ločenih vej.

**Sestavljanje seznama z `+`** ustvari nov seznam in ne spremeni `self.postanki`.
Če bi pisal `self.postanki.append(nadstropje)`, bi cilj trajno dodal med
postanke — in vsak nadaljnji klic bi vrnil drugačen rezultat.

**Sosednji pari z `zip`.** Enakovredna, bolj idiomatska različica:

```python
skupaj = sum(abs(b - a) for a, b in zip(pot, pot[1:]))
```

#### c) `klic(nadstropje, dvigala)`

Sestavite še funkcijo `klic(nadstropje, dvigala)`, ki v seznamu dvigal
poišče in vrne indeks tistega dvigala, ki je najbližje danemu nadstropju.
Če je najbližjih dvigal več, naj vrne indeks prvega takšnega iz seznama.
Predpostaviš lahko, da je v seznamu vsaj eno dvigalo.

```python
>>> klic(3, [dvigalo, Dvigalo()])
1
```

```python
def klic(nadstropje, dvigala):
    # min po indeksih, kjer je merilo razdalja pripadajočega dvigala.
    # Ob izenačenju min vrne prvega, kar naloga zahteva.
    return min(range(len(dvigala)), key=lambda i: dvigala[i].razdalja(nadstropje))
```

**Ideja.** Iščemo **indeks** najbližjega dvigala, ne dvigala samega.

```python
return min(range(len(dvigala)), key=lambda i: dvigala[i].razdalja(nadstropje))
```

`min` teče po indeksih `0, 1, 2, …`, merilo pa je razdalja pripadajočega
dvigala. Ob izenačenju `min` (in `max`) vrne **prvega** — natanko to naloga
zahteva.

**Enakovredna različica z zanko**, če ti `lambda` ne leži:

```python
def klic(nadstropje, dvigala):
    najblizje = 0
    for i in range(1, len(dvigala)):
        if dvigala[i].razdalja(nadstropje) < dvigala[najblizje].razdalja(nadstropje):
            najblizje = i
    return najblizje
```

Pozor na **strogi** `<`: z `<=` bi ob izenačenju obdržal zadnjega namesto
prvega.

**Pogosta napaka:** `min(dvigala, key=...)` vrne objekt dvigala, ne indeksa.
Kadar naloga hoče mesto v seznamu, mora `min`/`max` teči po `range(len(...))`.

### Naloga 3 — Potapljanje ladjic
*Datoteka `2425_i2/03_potapljanje_ladjic.py`*

Matrike, koordinate od 1 in dve datoteki. Podnaloge so verižne: druga riše, kar
prebere prva, tretja pa strelja po plošči, ki jo sestavi prva.

#### a) `preberi_ladjice(vhodna, dimenzija)`

Postavitev ladjic bosta v datoteko zapisala tako, da bosta v vsako vrstico
zapisala informacije o eni ladjici na sledeč način:

```
vrstica,stolpec,smer,dolzina
```
`vrstica` in `stolpec` določata začetni koordinati, `smer` določa ali je
ladjica od teh koordinat postavljena v desno (znak `'>'`) ali navzdol (znak `'v'`). `dolzina`
določa dolžino ladjice, tj., koliko koordinat v podani smeri zaseda. Predpostavite lahko, da se ladjice ne prekrivajo.

Sestavite funkcijo `preberi_ladjice(vhodna, dimenzija)`, ki iz vhodne datoteke prebere
pozicije ladjic in jih predstavi na igralni plošči velikosti `dimenzija`x`dimenzija`.
Katerkoli ladjico, ki ni v celoti na igralni plošči (tj. vsaj ena ladjičina koordinata pade čez rob),
spustite.

Igralno ploščo predstavite s tabelo na sledeč način: če je na dani koordinati ladjica
naj bo na tem mestu znak lojtra `'#'`, sicer pa naj bo na tej koordinati presledek `' '`.

```python
def preberi_ladjice(vhodna, dimenzija):
    # prazna plošča; vsako vrstico ustvarimo posebej, sicer bi bile vse
    # vrstice isti seznam ([[' '] * n] * n je past!)
    plosca = [[" "] * dimenzija for i in range(dimenzija)]

    with open(vhodna, encoding="utf-8") as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue

            v, s, smer, dolzina = vrstica.split(",")
            v, s, dolzina = int(v), int(s), int(dolzina)

            # koordinate, ki jih ladjica zaseda (koordinate so oštevilčene od 1)
            polja = []
            for k in range(dolzina):
                if smer == ">":
                    polja.append((v, s + k))
                else:
                    polja.append((v + k, s))

            # ladjico narišemo le, če je CELA na plošči
            if all(1 <= i <= dimenzija and 1 <= j <= dimenzija for i, j in polja):
                for i, j in polja:
                    plosca[i - 1][j - 1] = "#"

    return plosca
```

**Ideja.** Za vsako vrstico datoteke izračunaj polja, ki jih ladjica zaseda, in
jih vpiši — a le, če je ladjica **cela** na plošči.

**Prazna matrika brez pasti.**

```python
plosca = [[" "] * dimenzija for i in range(dimenzija)]
```

Zapis `[[" "] * dimenzija] * dimenzija` bi naredil `dimenzija` sklicev na
**isto** vrstico: sprememba enega polja bi se pojavila v vseh vrsticah. To je
ista past kot pri privzetih vrednostih — spremenljiv objekt, deljen med več
mesti.

**Najprej zberi, nato nariši.**

```python
polja = [...]                       # koordinate ladjice
if all(1 <= i <= dimenzija and 1 <= j <= dimenzija for i, j in polja):
    for i, j in polja:
        plosca[i - 1][j - 1] = "#"
```

Če bi risal sproti in šele nato opazil, da ladjica gleda čez rob, bi moral že
narisana polja brisati. Dvokoračni postopek se temu izogne.

**`all` z generatorjem** vrne `True`, če pogoj velja za vse elemente — in se
ustavi pri prvem, ki ga ne izpolni.

**Koordinate v datoteki se štejejo od 1**, indeksi v Pythonu pa od 0. Zato
`plosca[i - 1][j - 1]`. Ta zamik je najpogostejši vir napak pri tej nalogi;
splača se ga narediti na enem samem mestu.

#### b) `vizualiziraj(plosca, izhodna)`

Za lepšo vizalno predstavitev bomo igralno ploščo predstavili na preprostejši način. To bomo storili tako, da vsebino plošče strnemo v niz,
okoli pa dodamo še rob. Na primer, ploščo

```
[[' ', ' ', '#', '#', ' '],
 [' ', '#', ' ', ' ', '#'],
 [' ', '#', ' ', ' ', '#'],
 [' ', '#', ' ', ' ', '#'],
 [' ', ' ', ' ', ' ', '#']]
```
bomo vizualizirali kot:

```
/-----\
|  ## |
| #  #|
| #  #|
| #  #|
|    #|
\-----/
```
Sestavite funkcijo `vizualiziraj(plosca, izhodna)`, ki sprejme opis plošče kot zgoraj in
v datoteko `izhodna` zapiše vizualizirano igralno ploščo. Predpostavite lahko, da je igralna
plošča kvadratna.

```python
def vizualiziraj(plosca, izhodna):
    n = len(plosca)
    with open(izhodna, "w", encoding="utf-8") as f:
        # zgornji rob; niz "-" ponovimo n-krat
        print("/" + "-" * n + "\\", file=f)

        for vrstica in plosca:
            # "".join spoji seznam znakov v niz
            print("|" + "".join(vrstica) + "|", file=f)

        print("\\" + "-" * n + "/", file=f)
```

**Ideja.** Okvir okoli matrike: zgornja vrstica, vsebina z navpičnicama ob
straneh, spodnja vrstica.

```python
print("/" + "-" * n + "\\", file=f)
for vrstica in plosca:
    print("|" + "".join(vrstica) + "|", file=f)
print("\\" + "-" * n + "/", file=f)
```

**Množenje niza** `"-" * n` je najkrajši način za ponovljen znak.

**Poševnica nazaj v nizu.** `"\\"` je **en** znak `\`. Ubežni znak `\` ima
poseben pomen (npr. `\n` je prelom vrstice), zato ga je treba podvojiti. Če
želiš izpisati vrstico z več poševnicami, je pogosto lažje uporabiti surovi
niz: `r"\"`.

**`"".join(vrstica)`** spoji seznam znakov v niz. Vsota z `+=` v zanki bi
delovala, a je pri dolgih nizih počasnejša, ker vsakič ustvari nov niz.

**Dolžina roba je `n`**, torej toliko, kolikor je stolpcev — ne `n + 2`. Če se
okvir ne poravna, je skoraj vedno kriva ta številka.

#### c) `streljaj(streli, plosca, dimenzija)`

Na podoben način kot sta zabeležila postavitev ladjic bosta Ana in Žiga zabeležila še strele, tj., v vsako vrstico (druge)
datoteke bosta zabeležila koordinate strelov, ločene z vejico. Na primer, strela
na koordinati `(3, 5)` in `(2, 1)` bosta v datoteko zapisala kot:

```
3,5
2,1
```
Sestavite funkcijo `streljaj(streli, plosca, dimenzija)`, ki iz vhodne datoteke
`streli` prebere strele, iz datoteke `plosca` in števila `dimenzija` pa postavitev ladjic (kot zgoraj).
Funkcija naj spet vrne igralno ploščo kot prej, ki pa jo streli spremenijo na sledeč način:
če je strel zadel eno od ladjic na to mesto postavimo `'X'`, če pa je zadel prazno polje
na to mesto zapišemo `'.'`. Strele, ki so izven igralne plošče, preskočite.

```python
def streljaj(streli, plosca, dimenzija):
    # argument plosca je IME DATOTEKE s postavitvijo ladjic
    tabla = preberi_ladjice(plosca, dimenzija)

    with open(streli, encoding="utf-8") as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue

            v, s = [int(x) for x in vrstica.split(",")]

            # streli izven plošče se preskočijo
            if not (1 <= v <= dimenzija and 1 <= s <= dimenzija):
                continue

            if tabla[v - 1][s - 1] == "#":
                tabla[v - 1][s - 1] = "X"   # zadetek
            else:
                tabla[v - 1][s - 1] = "."   # zgrešeno

    return tabla
```

**Pozor na imena argumentov.** `plosca` tu ni matrika, ampak **ime datoteke** z
ladjicami. Prvo, kar funkcija naredi, je klic prejšnje podnaloge:

```python
tabla = preberi_ladjice(plosca, dimenzija)
```

**Ideja.** Za vsak strel pogledamo, kaj je na tem mestu: če je `#`, je zadetek
(`X`), sicer zgrešeno (`.`).

```python
if tabla[v - 1][s - 1] == "#":
    tabla[v - 1][s - 1] = "X"
else:
    tabla[v - 1][s - 1] = "."
```

**Streli izven plošče se preskočijo**, ne prekinejo branja — zato `continue` in
ne `break`.

**Branje parov iz vrstice:**

```python
v, s = [int(x) for x in vrstica.split(",")]
```

Razstavljanje na levi strani zahteva, da ima seznam natanko dva elementa; pri
napačno oblikovani vrstici bi to sprožilo `ValueError`. Naloga jamči obliko,
zato je tak zapis v redu.

**Vrstni red je pomemben:** najprej se postavijo ladjice, šele nato streljamo.
Če bi obrnil, bi ladjica prekrila zadetek.

---

## Izpit 3. rok 2024/25
Tretji rok 2024/25: nizi s pravili veljavnosti, razreda z validacijo vhoda ter
zaporedja s časi.

### Naloga 1 — Analiza DNA
*Datoteka `2425_i3/01_analiza_dna.py`*

Naloga o nizih, kjer je v vsaki podnalogi treba ločiti med »ni rezultata«
(`None`) in »rezultat je prazen« (`""` oz. `[]`).

#### a) `komplement(dna)`

*Komplement* zaporedja DNA je zaporedje DNA, ki ga dobimo tako, da vsak nukleotid
zamenjamo z njegovim veznim nukleotidom (vežeta se `A` in `T` ter `G` in `C`).
Na primer, komplement zaporedja `ATGGCTA` je `TACCGAT`.

Sestavite funkcijo `komplement(dna)`, ki sestavi in vrne komplement danega
zaporedja DNA. Če vhodni niz ne določa zaporedja DNA, naj funkcija vrne `None`.

```python
>>> komplement('ATGGCTA')
'TACCGAT'
>>> komplement('ATGgCTA')
None
```

```python
# vezni pari nukleotidov; slovar hkrati določa, kateri znaki so sploh veljavni
VEZI = {"A": "T", "T": "A", "G": "C", "C": "G"}


def komplement(dna):
    rezultat = ""
    for nukleotid in dna:
        if nukleotid not in VEZI:
            return None       # niz ni zaporedje DNA
        rezultat += VEZI[nukleotid]
    return rezultat
```

**Ideja.** Slovar `{"A": "T", "T": "A", "G": "C", "C": "G"}` hkrati opravi dve
nalogi: pove zamenjavo in določa, kateri znaki so sploh veljavni.

```python
for nukleotid in dna:
    if nukleotid not in VEZI:
        return None
    rezultat += VEZI[nukleotid]
```

**Predčasni `return None`** je pomemben: takoj ko naletimo na neveljaven znak,
je odgovor znan in nadaljnje delo je odveč. Test `komplement('ATGgCTA')` cilja
prav na to — mala črka `g` ni veljavna, čeprav je »skoraj« pravilna.

**Prazen niz** vrne prazen niz: zanka se ne izvede, `rezultat` ostane `""`.
Robni primer je pokrit sam od sebe.

**Krajša različica** za tiste, ki jim ustreza:

```python
if not all(z in VEZI for z in dna):
    return None
return "".join(VEZI[z] for z in dna)
```

#### b) `bralni_okvir(dna, indeks)`

*Bralni okvir* je ena od treh možnosti branja zaporedja DNA v obliki
neprekrivajočih se kodonov, odvisno od tega, ali začnemo brati pri prvem,
drugem ali tretjem nukleotidu. Pri zaporedju `ATGGCTA` imamo tako tri
bralne okvirje: `ATG GCT`, `TGG CTA` in `GGC`.

Sestavite funkcijo `bralni_okvir(dna, indeks)`, ki sprejme zaporedje DNA (niz)
in vrne seznam kodonov (seznam nizov) bralnega okvirja, ki se začne na mestu
z danim indeksom. Če vhodni niz ne določa zaporedja DNA, naj funkcija vrne `None`.

```python
>>> bralni_okvir('ATGGCTA', 1)
['TGG', 'CTA']
>>> bralni_okvir('xTGATTCA', 2)
None
```

```python
def je_dna(dna):
    """Ali so vsi znaki veljavni nukleotidi? Prazen niz je veljaven."""
    return all(znak in VEZI for znak in dna)


def bralni_okvir(dna, indeks):
    # veljavnost preverimo na CELEM zaporedju, ne šele od indeksa naprej
    if not je_dna(dna):
        return None

    ostanek = dna[indeks:]

    kodoni = []
    # korak 3; zadnji, nepopolni kodon (dolžine 1 ali 2) izpustimo
    for i in range(0, len(ostanek) - 2, 3):
        kodoni.append(ostanek[i:i + 3])
    return kodoni
```

**Ideja.** Odrežemo začetek do danega indeksa in ostanek razrežemo na trojke.

**Veljavnost preverimo na celem nizu**, ne šele od indeksa naprej. Test
`bralni_okvir('ATG123', 2)` mora vrniti `None`, čeprav bi bil ostanek `'G123'`
prav tako neveljaven — pomembno pa je, da bi pri drugačnih podatkih (npr.
`'xTGATTCA'` z indeksom 2) izrez skril neveljaven znak na začetku.

**Rezanje na kose fiksne dolžine:**

```python
for i in range(0, len(ostanek) - 2, 3):
    kodoni.append(ostanek[i:i + 3])
```

**Zakaj `- 2` in ne `len(ostanek)`.** Zadnji, nepopoln kodon je treba izpustiti.
Pri dolžini 7 gre `range(0, 5, 3)` čez 0 in 3, torej dve popolni trojki, znak na
mestu 6 pa ostane zunaj. Če bi pisal `range(0, len(ostanek), 3)`, bi dobil še
`ostanek[6:9]`, kar je niz dolžine 1.

**Robni primeri.** `bralni_okvir('ATG', 1)` da `[]` (ostaneta le dva znaka), kar
ni isto kot `None` — prazen seznam pomeni »veljaven DNA, a noben cel kodon«.

#### c) `najdaljsi_gen(okvir)`

V DNA zaporedju se gen začne z začetnim kodonom `ATG` in konča pri prvem
stop kodonu, ki sledi začetnemu kodonu. Stop kodoni so `TAA`, `TAG` in `TGA`.

Sestavite funkcijo `najdaljsi_gen(okvir)`, ki za dani bralni okvir
(seznam kodonov) vrne najdaljši gen (seznam kodonov). Če v bralnem okvirju
ni nobenega gena, naj funkcija vrne `None`. Če je najdaljših genov več,
naj funkcija vrne prvega izmed njih.

```python
>>> najdaljsi_gen(['ATG', 'TAA', 'ATG', 'CCC', 'TAA'])
['ATG', 'CCC', 'TAA']
>>> najdaljsi_gen(['ATG', 'CCC'])
None
```
Namig: Zanko predčasno končamo z ukazom `break`.

```python
STOP_KODONI = ("TAA", "TAG", "TGA")


def najdaljsi_gen(okvir):
    najdaljsi = None

    for i in range(len(okvir)):
        if okvir[i] != "ATG":
            continue

        # od začetnega kodona naprej iščemo PRVI stop kodon
        for j in range(i + 1, len(okvir)):
            if okvir[j] in STOP_KODONI:
                gen = okvir[i:j + 1]
                # strogi > poskrbi, da ob izenačenju obdržimo prvega
                if najdaljsi is None or len(gen) > len(najdaljsi):
                    najdaljsi = gen
                break     # nadaljnji stop kodoni tega gena ne zadevajo

    return najdaljsi
```

**Ideja.** Za vsak `ATG` poišči **prvi** stop kodon za njim; to je kandidat.
Med kandidati vrni najdaljšega.

```python
for i in range(len(okvir)):
    if okvir[i] != "ATG":
        continue
    for j in range(i + 1, len(okvir)):
        if okvir[j] in STOP_KODONI:
            gen = okvir[i:j + 1]
            if najdaljsi is None or len(gen) > len(najdaljsi):
                najdaljsi = gen
            break
```

**`break` je bistven** (namig ga izrecno omenja): gen se konča pri **prvem**
stop kodonu. Brez njega bi za isti `ATG` našli tudi daljše »gene«, ki segajo
čez prvi stop.

**`continue` proti gnezdenju.** Zapis »če to ni začetni kodon, pojdi naprej«
prihrani en nivo zamika in se lepše bere kot `if okvir[i] == "ATG":` z vsem
ostalim znotraj.

**Strogi `>` pri primerjavi dolžin** poskrbi, da ob izenačenju obdržimo prvega
najdenega — točno to zahteva naloga.

**Rezina `okvir[i:j + 1]`** vključuje stop kodon; `+ 1` je nujen, ker je zgornja
meja rezine izključujoča.

**Zakaj `None` in ne `[]`.** Prazen seznam bi pomenil »gen brez kodonov«;
`None` pomeni »gena ni«. Testi ju ločujejo.

### Naloga 2 — Telefonski imenik
*Datoteka `2425_i3/02_telefonski_imenik.py`*

Dva razreda, ki sodelujeta. Del kode je podan; dopolniti je treba predstavitvi
osebe ter metodi imenika, ki preverjata veljavnost vhoda.

#### a) Razred `Oseba` — `__repr__` in `__str__`

Razredu `Oseba` dodajte ustrezni metodi `__repr__` in `__str__`. Oseba se predstavi kot `Ime Priimek`, če nima vzdevka, ter kot `Ime "Vzdevek" Priimek`, če ga ima.

```python
class Oseba:
    def __init__(self, ime, priimek, vzdevek=None):
        self.ime = ime
        self.priimek = priimek
        self.vzdevek = vzdevek

    def __eq__(self, other):
        return (self.ime, self.priimek, self.vzdevek) == (other.ime, other.priimek, other.vzdevek)

    def __repr__(self):
        # simulira klic konstruktorja, vključno z imenovanim argumentom
        return f"Oseba({self.ime!r}, {self.priimek!r}, vzdevek={self.vzdevek!r})"

    def __str__(self):
        if self.vzdevek is None:
            return f"{self.ime} {self.priimek}"
        # vzdevek gre v dvojne narekovaje med ime in priimek
        return f'{self.ime} "{self.vzdevek}" {self.priimek}'
```

**Dve različni predstavitvi.**

| Metoda | Namen | Rezultat |
|---|---|---|
| `__repr__` | za razvijalca; simulira klic konstruktorja | `Oseba('Janez', 'Kranjski', vzdevek=None)` |
| `__str__` | za uporabnika | `Janez "Đoni" Kranjski` |

```python
def __repr__(self):
    return f"Oseba({self.ime!r}, {self.priimek!r}, vzdevek={self.vzdevek!r})"
```

`!r` je nujen pri vseh treh: pri nizih doda narekovaje, pri `None` pa izpiše
`None` brez njih — natanko tako, kot bi napisal klic v kodi.

**Narekovaji v nizu.** Ker mora izpis vsebovati znak `"`, niz ovijemo v
enojne narekovaje:

```python
return f'{self.ime} "{self.vzdevek}" {self.priimek}'
```

Alternativa je ubežni znak `f"... \"{self.vzdevek}\" ..."`, kar je manj berljivo.

**Ločevanje primerov.** `if self.vzdevek is None` — spet `is None` in ne
`if not self.vzdevek`, saj bi slednje kot »brez vzdevka« obravnavalo tudi
prazen niz.

#### b) `Imenik.dodaj(stevilka, oseba)`

Razredu `Imenik` dodajte metodo `dodaj`, ki kot argumenta prejme telefonsko številko (predstavljeno kot niz) in osebo, ter si pod podano številko shrani podano osebo. Metoda naj preveri, da je telefonska številka veljavna, tj., vsebuje lahko le števke, z izjemo prvega znaka, ki je lahko znak `+`. Metoda naj preveri še, da je podana oseba res objekt razreda `Oseba`; tu si lahko pomagate z vgrajeno funkcijo `isinstance`. Če številka ali oseba nista veljavni, naj metoda ne naredi ničesar.

```python
class Imenik:
    def __init__(self):
        self.imenik = {}

    def dodaj(self, stevilka, oseba):
        # samo objekti razreda Oseba (isinstance zna tudi za dedovanje)
        if not isinstance(oseba, Oseba):
            return

        # dovoljena je vodilna +, vse ostalo morajo biti števke
        telo = stevilka[1:] if stevilka.startswith("+") else stevilka
        if not telo.isdigit():
            return

        self.imenik[stevilka] = oseba
```

**Ideja.** Metoda je v celoti sestavljena iz dveh preverjanj; če katero pade,
ne naredi ničesar (`return` brez vrednosti).

**Preverjanje tipa.**

```python
if not isinstance(oseba, Oseba):
    return
```

`isinstance` je pravilnejši od `type(oseba) == Oseba`, ker sprejme tudi objekte
podrazredov.

**Preverjanje številke.** Dovoljena je vodilna `+`, vse ostalo morajo biti
števke:

```python
telo = stevilka[1:] if stevilka.startswith("+") else stevilka
if not telo.isdigit():
    return
```

Trik je v tem, da morebitno **prvo** plusko odrežemo in preverimo le preostanek.
S tem samodejno pade `"65+4321"` (plus na sredini) in `"++777777"` (druga plus
ostane v telesu). Prazen niz `""` prav tako pade, ker `"".isdigit()` je `False`.

**Zgodnji izhod (*guard clause*).** Namesto gnezdenja

```python
if isinstance(...):
    if telo.isdigit():
        self.imenik[stevilka] = oseba
```

je bolj pregledno najprej odpraviti vse neveljavne primere in šele na koncu
narediti pravo delo.

#### c) `Imenik.klice(stevilka)`

Razredu `Imenik` dodajte še metodo `klice`, ki sprejme telefonsko številko in
preveri ali kliče znana številka, tj., vrne niz oblike `Kliče: Ime "Vzdevek" Priimek`,
če oseba je v imeniku, sicer pa naj vrne niz oblike `Kliče: neznana številka`.
Opis osebe naj metoda dobi neposredno iz razreda `Oseba`.

Primer:

```python
>>> i = Imenik()
>>> i.dodaj('+123456', Oseba('Ana', 'Celjska', vzdevek='Kraljica'))
>>> i.klice('+123456')
'Kliče: Ana "Kraljica" Celjska'
>>> i.klice('654321')
'Kliče: neznana številka'
```

```python
def klice(self, stevilka):
        if stevilka in self.imenik:
            # f-niz pokliče __str__ osebe, zato je opis en sam, na enem mestu
            return f"Kliče: {self.imenik[stevilka]}"
        return "Kliče: neznana številka"
```

**Ideja.**

```python
if stevilka in self.imenik:
    return f"Kliče: {self.imenik[stevilka]}"
return "Kliče: neznana številka"
```

**»Opis osebe naj metoda dobi neposredno iz razreda `Oseba`«** — to je zahteva
naloge in jo izpolni f-niz: vstavljanje objekta v f-niz pokliče njegov
`__str__`. Če bi opis sestavljal tu (`f"{o.ime} {o.priimek}"`), bi isto pravilo
pisal na dveh mestih; ko bi se oblika spremenila, bi eno pozabil popraviti.

**Preverjanje `in` na slovarju** gleda **ključe**, ne vrednosti, in je hitro
(v povprečju O(1)).

**Enakovreden zapis z `get`:**

```python
oseba = self.imenik.get(stevilka)
if oseba is None:
    return "Kliče: neznana številka"
return f"Kliče: {oseba}"
```

Ta se izogne dvojnemu iskanju po slovarju (`in`, nato `[...]`), kar je pri
velikih slovarjih boljša navada.

### Naloga 3 — Orientacijski tek
*Datoteka `2425_i3/03_orientacijski_tek.py`*

Najlepša naloga tega roka: če pravo idejo najdeš pri prvi podnalogi, sta drugi
dve skoraj samodejni.

#### a) `je_veljaven(tek, proga)`

Tekmovalčev tek je veljaven, če je podano veljavno zaporedje točk:

* začne se s točko `START` in konča s točko `CILJ`,
* vsebuje vse točke, ki spadajo v tekmovalčevo progo,
* vse točke, ki spadajo v tekmovalčevo progo nastopajo v pravilnem zaporedju.
(npr. če je določeno zaporedje točk na progi `ABE`, sta `AEB` in `AEBE` neveljavni zaporedji)

Morebitne točke, ki niso del trase se ignorirajo in ne vplivajo na veljavnost teka.

Napiši funkcijo `je_veljaven(tek, proga)`, ki sprejme podatke o teku ter zaporedje točk
na progi in preveri, če je tekmovalčev tek veljaven.

Primeri:

```python
>>> je_veljaven([("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)], proga1)
True
>>> je_veljaven([("START", 0), ("A", 5), ("B", 6), ("C", 9), ("E", 10), ("CILJ", 11)], proga1)
True
>>> je_veljaven([("START", 0), ("E", 3), ("A", 5), ("B", 6), ("CILJ", 11)], proga1)
False
>>> je_veljaven([("START", 0), ("A", 5), ("B", 6), ("CILJ", 11)], proga1)
False
```

```python
def je_veljaven(tek, proga):
    # obdržimo le točke, ki so na progi — ostale naloga izrecno ignorira
    obiskane = [tocka for tocka, cas in tek if tocka in proga]

    # zaporedje mora biti natanko enako progi: to hkrati preveri, da so
    # vse točke obiskane, v pravem vrstnem redu in brez ponovitev
    return obiskane == proga
```

**Ideja, ki nalogo skrči na eno vrstico.** Iz teka pobrišemo vse točke, ki niso
na progi, in preverimo, ali je preostanek **natanko enak** progi:

```python
obiskane = [tocka for tocka, cas in tek if tocka in proga]
return obiskane == proga
```

**Zakaj to zajame vse tri zahteve naloge hkrati:**

| Zahteva | Kako jo pokrije primerjava seznamov |
|---|---|
| začne s START, konča s CILJ | prvi in zadnji element se morata ujemati |
| vsebuje vse točke proge | seznama morata biti enako dolga |
| točke v pravem zaporedju | seznama se primerjata po vrsti |
| ponovitve niso dovoljene (`AEBE`) | podvojena točka podaljša seznam |

Poskus reševanja z ločenimi preverjanji (»ali vsebuje vse«, »ali je START prvi«
…) je bistveno daljši in skoraj vedno spregleda kakšen primer.

**Izpeljani seznam s pogojem** je tu naravno orodje: `[x for x in ... if ...]`.

**Točke izven proge ne škodujejo**, ker jih filter odstrani — natanko to
zahteva besedilo (»morebitne točke, ki niso del trase, se ignorirajo«).

#### b) `zmagovalec(tekmovalci, proga)`

Napiši funkcijo `zmagovalec(tekmovalci, proga)`, ki poišče indeks zmagovalca
v seznamu tekov vseh tekmovalcev v kategoriji. Zmagovalec je tekmovalec, ki je
uspešno našel vse kontrolne točke svoje proge v najkrajšem času od svojega
začetka (čas na točki `START`).

Za tabelo:

```
tekmovalci = [
    [("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)],
    [("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)],
    [("START", 4), ("A", 9), ("B", 10), ("E", 14), ("CILJ", 16)],
    [("START", 6), ("B", 11), ("E", 12), ("CILJ", 14)],
    [("START", 8), ("A", 13), ("G", 17), ("B", 19), ("E", 23), ("CILJ", 27)],
]
```
in progo `proga1` iz primera, je zmagovalec tekmovalec z zaporedno
številko 1, ki je s progo opravil v 9 minutah.
Tekmovalec s številko 3 je sicer na cilj prišel hitreje, a je zgrešil točko "A",
zato njegov tek ni veljaven.

```python
def cas_teka(tek, proga):
    """Čas od točke START do točke CILJ za veljaven tek."""
    tocke = [(tocka, cas) for tocka, cas in tek if tocka in proga]
    return tocke[-1][1] - tocke[0][1]


def zmagovalec(tekmovalci, proga):
    najboljsi = None
    najkrajsi = None

    for i in range(len(tekmovalci)):
        if not je_veljaven(tekmovalci[i], proga):
            continue          # neveljavni teki ne tekmujejo

        cas = cas_teka(tekmovalci[i], proga)
        if najkrajsi is None or cas < najkrajsi:
            najkrajsi = cas
            najboljsi = i     # strogi < obdrži prvega ob izenačenju

    return najboljsi
```

**Ideja.** Med veljavnimi teki poišči najkrajši čas in vrni **indeks**.

```python
for i in range(len(tekmovalci)):
    if not je_veljaven(tekmovalci[i], proga):
        continue
    cas = cas_teka(tekmovalci[i], proga)
    if najkrajsi is None or cas < najkrajsi:
        najkrajsi = cas
        najboljsi = i
```

**Čas ni čas na cilju.** Meri se od tekmovalčevega **lastnega** starta:

```python
tocke = [(tocka, cas) for tocka, cas in tek if tocka in proga]
return tocke[-1][1] - tocke[0][1]
```

Tekmovalci startajo ob različnih urah, zato bi primerjanje absolutnih časov na
cilju dalo napačnega zmagovalca. V testnih podatkih je to past: tekmovalec,
ki pride na cilj prvi, ni zmagovalec.

**Zakaj filtriranje tudi tu.** Če bi vzel kar `tek[0]` in `tek[-1]`, bi te
lahko premotila dodatna točka pred STARTom ali za CILJem. Ker je tek veljaven,
je prva točka po filtriranju zagotovo START in zadnja CILJ.

**Neveljavni teki preprosto preskočimo** s `continue` — vrstica manj kot
gnezden `if`.

**`None` kot »še nič ni najdeno«** deluje tudi, kadar je najmanjši čas 0 —
`if not najkrajsi` bi se tu zmotil.

#### c) `izpisi(tek, proga, datoteka)`

Napiši funkcijo `izpisi(tek, proga, datoteka)`, ki v datoteko zapiše poročilo
tekmovalčevega teka. Vsaka vrstica naj vsebuje oznako kontrolne točke, čas
od začetka tekmovalčevega teka ter čas od predhodne kontrolne točke, kot kaže
primer. Če tekmovalčev tek ni veljaven, naj se v datoteko
zapiše le niz `DQ` (disqualified).

Za tek `[("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)]` in progo
`proga1`, naj bo datoteka:

```
START:    0    0
A:    2    2
B:    4    2
E:    5    1
CILJ:    9    4
```
Posamezne vrednosti v vrstici naj bodo med seboj ločene s 4 presledki.

```python
def izpisi(tek, proga, datoteka):
    with open(datoteka, "w", encoding="utf-8") as f:
        if not je_veljaven(tek, proga):
            print("DQ", file=f)
            return

        # čas na točki START je izhodišče za vse ostale čase
        zacetek = None
        for tocka, cas in tek:
            if tocka == proga[0]:
                zacetek = cas
                break

        prejsnji = zacetek
        # izpišemo VSE točke teka, tudi tiste, ki niso na progi
        for tocka, cas in tek:
            print(f"{tocka}:    {cas - zacetek}    {cas - prejsnji}", file=f)
            prejsnji = cas
```

**Ideja.** Če tek ni veljaven, v datoteko gre samo `DQ`; sicer za vsako točko
izpišemo ime, čas od starta in čas od prejšnje točke.

**Dve različni razliki.**

```python
print(f"{tocka}:    {cas - zacetek}    {cas - prejsnji}", file=f)
prejsnji = cas
```

- `cas - zacetek` je **kumulativni** čas — vedno glede na START,
- `cas - prejsnji` je **medčas** — glede na prejšnjo vrstico.

`prejsnji` na začetku nastavimo na `zacetek`, da prva vrstica da `0    0`.

**Izpišejo se vse točke teka**, tudi tiste, ki niso na progi. Test s točko `G`
to izrecno preverja — filtriranje iz prve podnaloge tu torej ne velja.

**Zgodnji `return` po `DQ`** je pomemben: brez njega bi se za `DQ` izpisale še
vrstice s časi.

**Ločilo so štirje presledki**, zapisani kar v f-niz. Če bi jih bilo treba
poravnati v stolpce, bi uporabil `{vrednost:>6}`, a naloga tega ne zahteva —
in izmišljena poravnava bi test podrla.

---

## Izpit 1. rok 2025/26
Prvi rok 2025/26: regularni izrazi in deleži, razred v vlogi lastnega
`Counterja` ter geometrija na mreži z branjem in pisanjem datotek.

### Naloga 1 — Značke
*Datoteka `2526_i1/01_znacke.py`*

Vsaka podnaloga stoji na prejšnji. Če prvo (regularni izraz) dobro premisliš,
sta drugi dve kratki.

#### a) `znacke(vsebina)`

Sestavite funkcijo `znacke`, ki sprejme vsebino objave in vrne množico značk, ki se v njej pojavijo.

Primer uporabe:

```python
>>> znacke("pozdravljen svet #hello #world")
{'#hello', '#world'}
>>> znacke("samo # ni značka")
{}
```

```python
import re

# '#' in za njim vsaj en znak, ki ni presledek in ni nova lojtra —
# zato "###" ne da nobene značke, "#a#b" pa dve
ZNACKA = re.compile(r"#[^\s#]+")


def znacke(vsebina):
    return set(ZNACKA.findall(vsebina))
```

**Ideja.** Značka je `#`, ki mu sledi vsaj en znak, ki ni presledek in ni nova
lojtra:

```python
ZNACKA = re.compile(r"#[^\s#]+")
```

| Del | Pomen |
|---|---|
| `#` | dobesedna lojtra |
| `[^...]` | **negirani** razred: katerikoli znak, ki ni našteti |
| `\s` | poljuben presledni znak (presledek, tabulator, prelom) |
| `+` | vsaj eden |

**Zakaj mora biti `#` v negiranem razredu.** Test `znacke("#a#b#c")` pričakuje
tri značke. Brez `#` med izključenimi bi vzorec požrešno ujel `#a#b#c` kot eno
samo značko.

**Zakaj `+` in ne `*`.** Test `znacke("###")` mora dati prazno množico; z `*`
bi se `#` ujel sam s sabo (nič znakov za njim je tudi ujemanje).

**Rezultat je množica**, zato se ponovitve (`"#a #b #c #b"`) same odpravijo.

**Brez regularnih izrazov** bi šlo tudi z razbitjem po `#`, a je precej bolj
zapleteno — in prav zaradi primerov, kot je `"#a#b#c"`, se hitro zalomi.

#### b) `delez_objav_z_znackami(objave, oseba)`

Sestavite funkcijo `delez_objav_z_znackami`, ki sprejme seznam objav in osebo ter vrne delež (med 0.0 in 1.0) objav te osebe, ki vsebujejo vsaj eno značko. Če oseba ni objavila ničesar, naj funkcija vrne `None`.

Primer uporabe:

```python
>>> delez_objav_z_znackami(objave, "Ana")
0.5
>>> delez_objav_z_znackami(objave, "Bojan")
1.0
```

```python
def delez_objav_z_znackami(objave, oseba):
    vseh = 0
    z_znackami = 0

    for avtor, vsebina in objave:
        if avtor != oseba:
            continue
        vseh += 1
        if znacke(vsebina):     # neprazna množica je "resnična"
            z_znackami += 1

    if vseh == 0:
        return None             # oseba ni objavila ničesar
    return z_znackami / vseh
```

**Ideja.** Dva števca: koliko objav ima ta oseba in koliko jih vsebuje značko.

```python
if znacke(vsebina):     # neprazna množica je "resnična"
    z_znackami += 1
```

**Prazne zbirke so lažne.** V Pythonu so `set()`, `[]`, `{}`, `""` in `0` vsi
»lažni«, zato ni treba pisati `if len(znacke(vsebina)) > 0`. Ta lastnost je tu
ravno prav uporabna.

**Deljenje z nič.** Če oseba ni objavila ničesar, je `vseh == 0` in deljenje bi
sprožilo `ZeroDivisionError`. Naloga zahteva `None` — zato preverjanje **pred**
deljenjem.

**`None` proti `0`.** Sta različna odgovora: `0.0` pomeni »objavljala je, a
brez značk«, `None` pa »ni objavljala«. Testi ju ločujejo.

**Deljenje z `/`** vrne realno število (`1/2` je `0.5`); `//` bi vrnil `0`.

#### c) `najbolj_znackast(objave)`

Sestavi funkcijo `najbolj_znackast`, ki sprejme seznam objav in vrne osebo z največjim deležem objav, ki vsebujejo značke. Če je takih oseb več, naj funkcija vrne eno izmed njih.

Primer uporabe:

```python
>>> najbolj_znackast(objave)
'Bojan'
```

```python
def najbolj_znackast(objave):
    najboljsi = None
    najvecji_delez = None

    for avtor, vsebina in objave:
        # isto osebo bi sicer obravnavali večkrat, a rezultat je vsakič enak
        delez = delez_objav_z_znackami(objave, avtor)
        if najvecji_delez is None or delez > najvecji_delez:
            najvecji_delez = delez
            najboljsi = avtor

    return najboljsi
```

**Ideja.** Za vsakega avtorja izračunaj delež s prejšnjo podnalogo in obdrži
največjega.

```python
for avtor, vsebina in objave:
    delez = delez_objav_z_znackami(objave, avtor)
    if najvecji_delez is None or delez > najvecji_delez:
        najvecji_delez = delez
        najboljsi = avtor
```

**Isto osebo obravnavamo večkrat** — enkrat za vsako njeno objavo — a rezultat
je vsakič enak, zato to na pravilnost ne vpliva. Ceno plačamo v hitrosti: pri
`n` objavah je to `n` klicev, od katerih vsak spet pregleda vseh `n` objav
(O(n²)). Pri izpitnih velikostih to ni problem; če bi bilo, bi avtorje najprej
zbral v množico:

```python
for avtor in {avtor for avtor, vsebina in objave}:
    ...
```

**Ponovna uporaba prejšnje podnaloge** je tu pravilna odločitev — pravilo za
delež je zapisano na enem mestu.

**Strogi `>`** obdrži prvega ob izenačenju; naloga dovoli katerokoli od
najboljših oseb, a je določen odgovor lažje preveriti.

### Naloga 2 — Štetje
*Datoteka `2526_i1/02_stetje.py`*

Sestavljamo poenostavljeno različico razreda `collections.Counter`. Naloga
lepo pokaže, kaj vse mora znati razred, da se obnaša kot vgrajen tip.

#### a) Razred `Stevec` — konstruktor in `koliko`

Sestavite razred `Stevec` in mu dodajte konstruktor, ki sprejme seznam
elementov in jih nato prešteje, informacijo pa zabeleži v slovar, kjer
so ključi elementi, vrednosti pa števila njihovih ponovitev. Ta slovar naj konstruktor
zabeleži v atribut `stevilo`. Originalnega seznama ne shranite.

Razredu dodajte še metodo `koliko`, ki sprejme element in vrne število njegovih
pojavitev. Če elementa ni bilo v seznamu, naj metoda vrne 0.

Primer uporabe:

```python
>>> s = Stevec([1, 2, 3, 4, 5, 1, 2, 3])
>>> s.koliko(3)
2
>>> s.koliko(5)
1
>>> s.koliko('a')
0
```

```python
class Stevec:
    def __init__(self, elementi):
        # originalnega seznama namenoma ne shranimo — zabeležimo samo števila
        self.stevilo = {}
        for element in elementi:
            self.stevilo[element] = self.stevilo.get(element, 0) + 1

    def koliko(self, element):
        # get s privzeto 0 poskrbi za elemente, ki jih v seznamu ni bilo
        return self.stevilo.get(element, 0)
```

**Ideja.** Konstruktor prešteje elemente in si zapomni **samo števce**:

```python
self.stevilo = {}
for element in elementi:
    self.stevilo[element] = self.stevilo.get(element, 0) + 1
```

**»Originalnega seznama ne shranite«** je izrecna zahteva naloge in ni
muhavost: iz slovarja števcev se da vse potrebno izračunati, seznam pa bi
zasedal prostor in omogočal, da bi se stanje razšlo (npr. po `dodaj`).

**`koliko` s privzeto vrednostjo.**

```python
return self.stevilo.get(element, 0)
```

`self.stevilo[element]` bi pri neznanem elementu sprožil `KeyError`. Naloga
zahteva 0, kar je natanko drugi argument `get`.

**Ključi so lahko karkoli nespremenljivega** — števila, nizi, nabori. Test
`Stevec([1, 2, 3]).koliko('a')` meša tipe in mora vrniti 0, ne napake; slovar
to zmore brez posebne obravnave.

#### b) `__eq__` in `dodaj`

Razredu dodajte ustrezno metodo za preverjanje enakosti. Števca sta enaka
natanko tedaj, ko vsebujeta enako število pojavitev enakih elementov.

Razredu dodajte še metodo `dodaj`, ki sprejme poljubni element in poveča
število njegovih pojavitev za 1.

Primer uporabe:

```python
>>> t = Stevec([5, 4, 3, 3, 2, 2, 1])
>>> s == t
False
>>> t.dodaj(1)
>>> s == t
True
```

```python
def __eq__(self, other):
        # dva slovarja sta enaka, če imata iste ključe z istimi vrednostmi —
        # vrstni red ključev ni pomemben
        return self.stevilo == other.stevilo

    def dodaj(self, element):
        self.stevilo[element] = self.stevilo.get(element, 0) + 1
```

**Primerjava je primerjava slovarjev.**

```python
def __eq__(self, other):
    return self.stevilo == other.stevilo
```

Dva slovarja sta enaka, če imata iste ključe z istimi vrednostmi; **vrstni red
ključev ni pomemben**. Zato ni treba ničesar urejati ali ročno primerjati.

**Kaj `__eq__` sploh omogoči.** Brez nje bi `s == t` primerjal identiteto
objektov in bi bil vedno `False` (razen za isti objekt). Z njo delujeta `==` in
`!=`, pa tudi `in` na seznamu števcev.

**Opomba za naprej:** ko razredu dodaš `__eq__`, Python izklopi privzeti
`__hash__` in objekti niso več uporabni kot ključi slovarja ali elementi
množice. Za to nalogo to ni pomembno, sicer bi dodal še `__hash__`.

**`dodaj` je ista vrstica kot v konstruktorju:**

```python
self.stevilo[element] = self.stevilo.get(element, 0) + 1
```

Deluje tudi za elemente, ki jih prej ni bilo — takrat začne pri 0.

#### c) `unija` in `presek`

Razredu dodajte metodo, ki izračuna unijo dveh števcev. Unijo izračunamo
tako, da ima novi števec elemente obeh števcev z vsoto ponovitev elementa
obeh števcev.

Razredu dodajte še metodo, ki izračuna presek števcev. Presek izračunamo
tako, da ima novi števec le elemente, ki se pojavijo v obeh števcih,
število njihovih pojavitev pa je manjše izmed števil pojavitev v števcih.

Primer uporabe:

```python
>>> u = Stevec(['a', 'b', 'c', 'a', 'a'])
>>> v = s.unija(u)
>>> v.koliko(5)
1
>>> v.koliko('a')
3
>>> z = s.presek(u)
>>> z.koliko('a')
0
>>> z.koliko(1)
0
```

```python
def unija(self, drugi):
        nov = Stevec([])        # prazen števec, ki ga nato napolnimo
        for element, koliko in self.stevilo.items():
            nov.stevilo[element] = koliko
        for element, koliko in drugi.stevilo.items():
            # elemente, ki so v obeh, seštejemo
            nov.stevilo[element] = nov.koliko(element) + koliko
        return nov

    def presek(self, drugi):
        nov = Stevec([])
        for element, koliko in self.stevilo.items():
            if element in drugi.stevilo:
                # obdržimo manjše od obeh števil pojavitev
                nov.stevilo[element] = min(koliko, drugi.stevilo[element])
        return nov
```

**Obe metodi vrneta nov števec** in ne spreminjata obstoječih. To je enako
obnašanje kot pri `a + b` ali `a & b` — operacije, ki računajo, ne smejo
tiho spreminjati operandov.

**Unija — seštevanje.**

```python
nov = Stevec([])                    # prazen števec, ki ga napolnimo
for element, koliko in self.stevilo.items():
    nov.stevilo[element] = koliko
for element, koliko in drugi.stevilo.items():
    nov.stevilo[element] = nov.koliko(element) + koliko
```

Druga zanka uporabi `nov.koliko`, ki za elemente, ki so le v `drugi`, vrne 0 —
zato ni treba posebej ločiti primerov »je v obeh« in »je le v enem«.

**Presek — minimum.**

```python
for element, koliko in self.stevilo.items():
    if element in drugi.stevilo:
        nov.stevilo[element] = min(koliko, drugi.stevilo[element])
```

Pri preseku je zanka **ena sama**: element, ki ga ni v `self`, v presek tako ali
tako ne spada.

**`Stevec([])` kot prazen začetek** je čist način, da nov objekt nastane po
pravilih razreda; ročno postavljanje `nov.stevilo = {}` bi delalo isto, a bi
obšlo konstruktor.

**Primerjava z množicami.** Unija in presek se pri števcih obnašata drugače kot
pri množicah: unija sešteje (ne vzame največjega), presek pa vzame najmanjše
število pojavitev. Enako počne `collections.Counter` z operatorjema `+` in `&`.

### Naloga 3 — Dostavljalec Miran
*Datoteka `2526_i1/03_dostavljalec_miran.py`*

Koordinate, razdalje in urejanje. Rdeča nit je, da korena skoraj nikoli ne
rabimo — razen takrat, ko razdaljo izpisujemo.

#### a) `poisci_stranke(vhodna)`

Žal so zaradi pomanjkanja denarja v trgovini morali odpustiti uslužbenca,
ki je iz zemljevida prepisoval koordinate, tako da mora Miran te točke
poiskati sam. Seveda vas prosi, da to storite namesto njega. Sestavite funkcijo
`poisci_stranke(vhodna)`, ki sprejme ime vhodne datoteke z opisom zemljevida,
in vrne množico lokacij strank. Na zemljevidu je z znakom `#` določen položaj
stranke, znak `.` pa določa prazen prostor. Koordinate posamezne stranke so
indeksi vrstice in stolpca. Če imamo vhodno datoteko `zemljevid.txt` z vsebino:

```
...#....
.#.....#
........
........
.#......
```
potem dobimo:

```python
>>> poisci_stranke("zemljevid.txt")
{(0, 3), (1, 1), (1, 7), (4, 1)}
```

```python
def poisci_stranke(vhodna):
    stranke = set()
    with open(vhodna, encoding="utf-8") as f:
        # enumerate da hkrati indeks vrstice in njeno vsebino
        for i, vrstica in enumerate(f):
            vrstica = vrstica.rstrip("\n")
            for j, znak in enumerate(vrstica):
                if znak == "#":
                    stranke.add((i, j))
    return stranke
```

**Ideja.** Preberi zemljevid vrstico za vrstico in si zapomni koordinate vseh
`#`.

```python
for i, vrstica in enumerate(f):
    for j, znak in enumerate(vrstica.rstrip("\n")):
        if znak == "#":
            stranke.add((i, j))
```

**`enumerate` da hkrati indeks in vrednost** — pri branju datoteke torej
številko vrstice, pri sprehodu po nizu pa številko stolpca. Alternativa s
`range(len(...))` je daljša in bolj podvržena napakam.

**`rstrip("\n")` in ne `strip()`.** Odrezati je treba samo prelom vrstice.
Navadni `strip()` bi odstranil tudi presledke na začetku — in če bi zemljevid
za prazna polja uporabljal presledke namesto pik, bi se vsi stolpci zamaknili.
Tu so prazna polja pike, a je navada pomembna.

**Rezultat je množica parov.** Nabori so nespremenljivi in jih zato lahko damo
v množico; s seznami `[i, j]` to ne bi šlo (`TypeError: unhashable type`).

**Vrstni red se izgubi**, kar je v redu — naloga zahteva množico, in naslednja
podnaloga koordinate tako ali tako uredi po razdalji.

#### b) `najblizja_stranka(centrala, stranke)`

Miran je plačan glede na število strank, ki jim dostavi naročeno blago,
zato ga zanima, katera stranka mu je najbližja. Sestavite funkcijo
`najblizja_stranka(centrala, stranke)`, ki sprejme točko `centrala`, kjer
se nahaja skladišče spletne trgovine, in seznam točk `stranke`, kjer se
nahajajo stranke. Vsaka točka je predstavljena s parom koordinat. Funkcija
naj vrne točko iz seznama, ki je najbližja centrali glede na zračno razdaljo.
Če ni nobene stranke, naj funkcija vrne `None`. Če je najbližjih več točk,
naj funkcija vrne prvo izmed njih. Nalogo rešite brez spreminjanja vhodnega
ali ustvarjanja novih seznamov.

```python
>>> najblizja_stranka((1, 1), [(2, 4), (1, 4), (4, 9)])
(1, 4)
>>> najblizja_stranka((2, 8), [])
None
```

```python
def razdalja(a, b):
    """Kvadrat zračne razdalje med točkama.

    Korena ne računamo: če je kvadrat razdalje manjši, je manjša tudi
    razdalja sama. Tako se izognemo nenatančnostim plavajoče vejice.
    """
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def najblizja_stranka(centrala, stranke):
    najblizja = None
    najmanjsa = None

    # navadna zanka: seznama ne spreminjamo in ne ustvarjamo novega
    for stranka in stranke:
        d = razdalja(centrala, stranka)
        if najmanjsa is None or d < najmanjsa:
            najmanjsa = d
            najblizja = stranka     # strogi < obdrži prvo ob izenačenju

    return najblizja
```

**Ideja.** Preprost sprehod z zapomnjenjem najboljšega doslej.

```python
for stranka in stranke:
    d = razdalja(centrala, stranka)
    if najmanjsa is None or d < najmanjsa:
        najmanjsa = d
        najblizja = stranka
```

**Naloga izrecno prepove `sorted` in nove sezname** (»brez spreminjanja
vhodnega ali ustvarjanja novih seznamov«), zato je ročna zanka edina pot.
`min(stranke, key=...)` bi sicer deloval in ne bi ustvaril seznama, a ročna
različica bolje pokaže, kaj se dogaja.

**Korena ni treba računati.**

```python
def razdalja(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
```

Če je kvadrat razdalje manjši, je manjša tudi razdalja — koren je naraščajoča
funkcija. S tem se izognemo nenatančnostim plavajoče vejice in pridobimo na
hitrosti. Koren potrebujemo šele, ko razdaljo **izpisujemo** (naslednja
podnaloga).

**Prazen seznam** da `None`, ker se zanka ne izvede in začetna vrednost ostane.

**Strogi `<`** obdrži prvo od enako oddaljenih strank, kot zahteva naloga.

#### c) `uredi_stranke(centrala, vhodna, izhodna)`

Miran vas prosi, da mu sestavite vrstni red obiskovanja strank. Vrstni red je
seznam vseh točk, urejen glede na oddaljenost od centrale. Sestavite funkcijo
`uredi_stranke(centrala, vhodna, izhodna)`, ki sprejme lokacijo centrale,
ime vhodne datoteke, ki je take oblike kot v zgornjem primeru, in ime izhodne
datoteke, kamor naj funkcija zapiše v vsako vrstico najprej koordinate centrale,
potem puščico z razdaljo na dve decimalki (`"==d.dd==>"`) in na koncu še ciljno točko.
Funkcija naj vrne urejen seznam lokacij strank. Predpostavite lahko, da so vse
stranke različno oddaljene od centrale.

```python
>>> uredi_stranke((4, 5), "zemljevid.txt", "izhod.txt")
[(1, 7), (4, 1), (0, 3), (1, 1)]
```
Pri tem v datoteki `izhod.txt` dobimo še:

```
(4, 5) ==3.61==> (1, 7)
(4, 5) ==4.00==> (4, 1)
(4, 5) ==4.47==> (0, 3)
(4, 5) ==5.00==> (1, 1)
```

```python
import math


def uredi_stranke(centrala, vhodna, izhodna):
    stranke = poisci_stranke(vhodna)

    # sorted sprejme tudi množico in vrne seznam;
    # kot ključ uporabimo kvadrat razdalje, ki ureja enako kot razdalja sama
    urejene = sorted(stranke, key=lambda stranka: razdalja(centrala, stranka))

    with open(izhodna, "w", encoding="utf-8") as f:
        for stranka in urejene:
            # tu koren res potrebujemo, ker razdaljo izpisujemo
            d = math.sqrt(razdalja(centrala, stranka))
            # :.2f zaokroži na dve decimalki in doda morebitne ničle (4 -> 4.00)
            print(f"{centrala} =={d:.2f}==> {stranka}", file=f)

    return urejene
```

**Ideja.** Preberi stranke, uredi po razdalji, izpiši vrstice in vrni urejen
seznam. Funkcija torej hkrati piše v datoteko **in** vrača vrednost — testi
preverjajo oboje.

**Urejanje s ključem.**

```python
urejene = sorted(stranke, key=lambda stranka: razdalja(centrala, stranka))
```

`sorted` sprejme tudi množico in vedno vrne **seznam**. Kot ključ spet uporabimo
kvadrat razdalje — ureja enako kot razdalja sama.

**Zdaj koren potrebujemo**, ker razdaljo izpisujemo:

```python
d = math.sqrt(razdalja(centrala, stranka))
print(f"{centrala} =={d:.2f}==> {stranka}", file=f)
```

**Oblikovanje števila.** `{d:.2f}` zaokroži na dve decimalki **in** doda
ničle, kjer manjkajo: 4 se izpiše kot `4.00`. Navadni `round(4, 2)` bi dal `4`
in izpis bi bil `==4==>`.

**Nabor se izpiše sam.** `f"{centrala}"` da `(4, 5)` — z oklepajema in vejico,
natanko kot zahteva pričakovani izpis. Ročno sestavljanje
`f"({centrala[0]}, {centrala[1]})"` ni potrebno.

**Predpostavka naloge**, da so vse stranke različno oddaljene, pomeni, da nam
ni treba določati vrstnega reda med enako oddaljenimi.

---

## Izpit 2. rok 2025/26
Drugi rok 2025/26: razred s simulacijo gibanja, rekurzivno razbijanje nizov ter
branje tabele iz datoteke CSV.

### Naloga 2 — Vrhskala
*Datoteka `2526_i2/02_vrhskala.py`*

Simulacija gibanja po pravilih, ki se med potjo spremenijo. Ključ je, da
`premik` pravilno ločuje tri stanja: konec poti, korakanje v začetni smeri in
korakanje proti zahodu.

#### a) Razred `Izvidnica` — konstruktor in `premik`

Sestavite razred `Izvidnica`, katerega konstruktor sprejme in zabeleži začetni koordinati `x` in `y`, smer premikanja `smer`, ter število korakov `st_korakov`.

Razredu dodajte še metodo `premik`, ki izvede premik za en korak, po sledečih pravilih:

- pot izvidnice poteka v smeri premikanja, ki je ena izmed severa (`S`, navzgor), vzhoda (`V`, desno) ali juga (`J`, navzdol) za podano število korakov,
- ko izvidnica opravi podano število korakov, pot nadaljuje tako, da se obrne proti zahodu (`Z`, levo) in premike izvaja le še v tej smeri,
- čim izvidnica pride na koordinate, ki so nad previsom (tj., imajo $x \leq 0$) se njena pot zaključi.

Vsak premik, ki ga izvidnica naredi, je dolg natanko eno enoto v smeri, izbrani na način opisan zgoraj.

Primer poti izvidnice, ki začne na koordinatah $(3, 4)$ in nadaljuje v smeri juga za dva koraka je:

$$ (3, 4) \rightarrow (3, 3) \rightarrow (3, 2) \rightarrow (2, 2) \rightarrow (1, 2) \rightarrow (0, 2) $$

```python
>>> i = Izvidnica(3, 4, 'J', 2)
>>> (i.x, i.y)
(3, 4)
>>> i.premik()
>>> (i.x, i.y)
(3, 3)
>>> i.premik()
>>> (i.x, i.y)
(3, 2)
>>> i.premik()
>>> (i.x, i.y)
(2, 2)
```

```python
import random

# Spodnjo funkcijo boste potrebovali pri drugi podnalogi.
def ima_zanimivost(x, y):
    random.seed(int(6 * x + 7 * y))
    return random.randint(1, 6) + random.randint(1, 6) >= 10


# premiki v posamezni smeri: (sprememba x, sprememba y)
PREMIKI = {"S": (0, 1), "J": (0, -1), "V": (1, 0), "Z": (-1, 0)}


class Izvidnica:

    def __init__(self, x, y, smer, st_korakov):
        self.x = x
        self.y = y
        self.smer = smer
        self.st_korakov = st_korakov
        self.zanimivosti = set()    # potrebujemo jo šele v 2. podnalogi

    def premik(self):
        # nad previsom je poti konec — izvidnica obstane
        if self.x <= 0:
            return

        if self.st_korakov > 0:
            # še korakamo v začetni smeri
            dx, dy = PREMIKI[self.smer]
            self.st_korakov -= 1
        else:
            # korakov je zmanjkalo: od tu naprej samo še proti zahodu
            dx, dy = PREMIKI["Z"]

        self.x += dx
        self.y += dy
```

**Ideja.** Namesto štirih vej za štiri smeri uporabimo slovar premikov:

```python
PREMIKI = {"S": (0, 1), "J": (0, -1), "V": (1, 0), "Z": (-1, 0)}
```

Korak je nato vedno enak: `self.x += dx`, `self.y += dy`. Ta prijem se splača
povsod, kjer nastopajo smeri — tudi pri osmerosmerkah in sprehodih.

**Trije primeri v pravem vrstnem redu.**

```python
if self.x <= 0:          # 1. konec poti: nad previsom se ne premakne več
    return
if self.st_korakov > 0:  # 2. še korakamo v začetni smeri
    dx, dy = PREMIKI[self.smer]
    self.st_korakov -= 1
else:                    # 3. korakov je zmanjkalo -> samo še proti zahodu
    dx, dy = PREMIKI["Z"]
```

Vrstni red ni poljuben: preverjanje konca mora biti prvo, sicer bi izvidnica
z `x = 0` naredila še en korak. Test `Izvidnica(-1, 0, 'J', 5)` cilja prav na
to — po klicu `premik()` mora ostati na mestu.

**`st_korakov` je števec, ki ga trošimo.** Zmanjšujemo ga le, kadar se res
premaknemo v začetni smeri; ko pade na 0, se vedenje trajno spremeni.

**Atribut za naslednjo podnalogo.** V konstruktor smo dodali še
`self.zanimivosti = set()`. Atribute, ki jih rabijo poznejše metode, je
najbolje pripraviti v konstruktorju — tako je objekt vedno v veljavnem stanju.

#### b) `preisci` in `do_sedaj`

Po poti izvidnice se morda nahajajo zanimivosti, zato izvidnica preišče okolico vsakih koordinat, ki jih obišče.
Razredu dodajte metodo `preisci`, ki s pomočjo vnaprej podane metode `ima_zanimivost`,
preveri ali se na trenutnih koordinatah nahaja zanimivost; če se, si metoda to zabeleži. Metoda `preisci` naj ne vrača ničesar.

Zanimivost se na nekih koordinatah `(x, y)` nahaja natanko takrat, ko funkcija `ima_zanimivost` pri argumentih `x` in `y` vrne `True`.

Razredu še dodajte metodo `do_sedaj`, ki vrne **množico** koordinat do sedaj odkritih zanimivosti.

```python
>>> i = Izvidnica(3, 2, 'J', 2)
>>> i.preisci()
>>> i.do_sedaj()
set()
>>> j = Izvidnica(1, 3, 'S', 7)
>>> j.preisci()
>>> j.do_sedaj()
{(1, 3)}
```

```python
def preisci(self):
        # metoda ničesar ne vrne, le zabeleži najdbo
        if ima_zanimivost(self.x, self.y):
            self.zanimivosti.add((self.x, self.y))

    def do_sedaj(self):
        return self.zanimivosti
```

**Ideja.** Podana funkcija `ima_zanimivost(x, y)` pove, ali je na danih
koordinatah kaj zanimivega; metoda si najdbo le zapiše.

```python
def preisci(self):
    if ima_zanimivost(self.x, self.y):
        self.zanimivosti.add((self.x, self.y))

def do_sedaj(self):
    return self.zanimivosti
```

**Metoda, ki ne vrača ničesar.** Naloga izrecno pravi, da `preisci` ne vrača
nič — je **ukaz**, ki spremeni stanje objekta. `do_sedaj` je nasprotno
**poizvedba**: ničesar ne spremeni, le vrne. Ločevanje obojega je dobra
navada, ker se metode lažje testirajo in kombinirajo.

**Zakaj množica.** Izvidnica lahko isto polje obišče večkrat (npr. na poti nazaj
proti zahodu); množica poskrbi, da je zanimivost zabeležena enkrat.

**`ima_zanimivost` je deterministična.** Uporablja `random.seed(...)`, kar
generator naključnih števil vsakič postavi v isto stanje — za iste koordinate
torej vedno vrne isto. Zato so testi ponovljivi, čeprav je videti naključno.

**Klic je `ima_zanimivost(...)`, ne `self.ima_zanimivost(...)`** — gre za
navadno funkcijo na nivoju datoteke, ne za metodo razreda.

#### c) `preiskovanje(izvidnice)`

Sedaj bi radi simulirali preiskovanje vseh izvidnic, ki jih vasica Vrhskala razpošlje v pragozd. Sestavite **funkcijo** `preiskovanje`, ki sprejme seznam začetnih koordinat, smeri in števil korakov izvidnic vasice Vrhskala in simulira preiskovanje pragozda pod vasico.
Preiskovanje poteka tako, da vsake koordinate izvidnica preišče, nato pa se prestavi na naslednje koordinate.

Funkcija `preiskovanje` naj vrne seznam izvidnic, po trenutku ko vse zaključijo s preiskovanjem.

```python
>>> i1, i2 = preiskovanje([(3, 2, 'J', 2), (1, 3, 'S', 18)])
>>> (i1.x, i1.y)
(0, 0)
>>> (i2.x, i2.y)
(0, 20)
>>> i1.do_sedaj()
set()
>>> i2.do_sedaj()
{(1, 3), (1, 16)}
```

```python
def preiskovanje(izvidnice):
    vse = [Izvidnica(x, y, smer, koraki) for x, y, smer, koraki in izvidnice]

    for izvidnica in vse:
        # vsake koordinate najprej preišče, nato se premakne;
        # ko pride nad previs (x <= 0), je njene poti konec
        while izvidnica.x > 0:
            izvidnica.preisci()
            izvidnica.premik()

    return vse
```

**Ideja.** Iz opisov ustvari objekte, vsakega poženi do konca poti in vrni
seznam objektov.

```python
vse = [Izvidnica(x, y, smer, koraki) for x, y, smer, koraki in izvidnice]

for izvidnica in vse:
    while izvidnica.x > 0:
        izvidnica.preisci()
        izvidnica.premik()
```

**Vrstni red v zanki je pomemben:** najprej preišči trenutne koordinate, šele
nato se premakni. Obratni vrstni red bi izpustil začetno točko — in prav ta je
v testih pogosto tista z zanimivostjo.

**Razstavljanje v izpeljanem seznamu.** `for x, y, smer, koraki in izvidnice`
razpakira vsako četverko v štiri spremenljivke, ki jih podamo konstruktorju.

**Pogoj zanke `while izvidnica.x > 0`** je isti, kot ga uporablja `premik` za
konec poti. Ko izvidnica pride nad previs, se zanka ustavi — brez tega bi se
vrtela v neskončnost, saj `premik` takrat ničesar več ne spremeni.

**Funkcija vrne objekte, ne koordinat**, ker klicatelj potrebuje tudi njihove
najdbe (`do_sedaj`).

### Naloga 3 — Razbitje
*Datoteka `2526_i2/03_razbitje.py`*

Učbeniški primer rekurzije s sestopanjem. Tretja podnaloga je ista rekurzija
kot druga, le da namesto odgovora »da/ne« zbira vse možnosti.

#### a) `se_zacne(n, s)`

Sestavite funkcijo `se_zacne`, ki sprejme niz `n` ter seznam nizov `s`. Funkcija naj vrne
seznam natanko tistih nizov iz `s`, ki so na začetku niza `n`.

Primer uporabe:

```python
>>> se_zacne('potokrog', ['pot', 'o', 'potok', 'krog', 'rog'])
['pot', 'potok']
>>> se_zacne('catsanddogs', ['cat', 'cats', 'and', 'sand', 'dogs'])
['cat', 'cats']
```

```python
def se_zacne(n, s):
    seznam = []
    for niz in s:
        # startswith preveri cel predpono, ne le prve črke
        if n.startswith(niz):
            seznam.append(niz)
    return seznam
```

**Ideja.** Iščemo tiste nize iz `s`, ki so **predpone** niza `n`:

```python
if n.startswith(niz):
    seznam.append(niz)
```

**Pogosta napaka** je primerjava samo prvih znakov (`n[0] == niz[0]`). Tak
pogoj bi pri `se_zacne('potokrog', ['pot', 'potok', 'plaz'])` vrnil tudi
`'plaz'`. `startswith` primerja celotno predpono.

**Enakovredno brez metode:** `n[:len(niz)] == niz`. Rezina je varna tudi, kadar
je `niz` daljši od `n` — takrat vrne krajši niz in primerjava pade.

**Vrstni red rezultata** je vrstni red seznama `s`, ne po dolžini — ker gremo
po `s` in dodajamo sproti. Testi to preverjajo (`['pot', 'potok']`).

**Prazen niz v `s`** bi bil predpona vsakega niza in bi v naslednjih dveh
podnalogah povzročil neskončno rekurzijo. Naloga takih podatkov ne predvideva.

#### b) `se_razbije(n, s)`

Sestavite funkcijo `se_razbije`, ki sprejme niz `n` in seznami nizov `s`, kot zgoraj.
Funkcija naj izračuna, ali je možno niz `n` natanko razbiti na podnize iz `s`. Podnizi
iz `s` se lahko v razbitju `n` pojavijo v kateremkoli vrstnem redu, lahko pa se tudi ponavljajo.

**Primer:** Niz `potokrog` lahko razbijemo s `['pot', 'o', 'potok', 'krog', 'rog']`, npr., na `pot` `o` `krog` ali `potok` `rog`. Če pa imamo na voljo le `['o', 'potok', 'krog']`, niza ne moremo razbiti, saj bi po `potok`, ki je edini možni začetek razbitja, ostal niz `rog`, ki pa ga z nizi, ki so na voljo, ne moremo razbiti.

**Namig:** Uporabite rekurzijo.

Primer uporabe:

```python
>>> se_razbije('potokrog', ['pot', 'o', 'potok', 'krog', 'rog'])
True
>>> se_razbije('potokrog', ['o', 'potok', 'krog'])
False
>>> se_razbije('catsanddogs', ['cat', 'cats', 'and', 'sand', 'dogs'])
True
>>> se_razbije('abba', ['a', 'bb'])
True
```

```python
def se_razbije(n, s):
    # BAZNI PRIMER: prazen niz je vedno razbit (na nič delov)
    if n == "":
        return True

    for zacetek in se_zacne(n, s):
        # odrežemo predpono in vprašamo isto vprašanje za krajši niz
        if se_razbije(n[len(zacetek):], s):
            return True

    return False
```

**Ideja (rekurzija).** Niz je razbiten, če se začne s katerim od danih nizov
**in** je razbiten tudi preostanek.

```python
if n == "":
    return True                       # bazni primer

for zacetek in se_zacne(n, s):
    if se_razbije(n[len(zacetek):], s):
        return True
return False
```

**Zakaj je prazen niz `True`.** Razbit je na nič delov — to je veljavno
razbitje. Ta bazni primer je motor celotne rekurzije: vsaka uspešna veja se
konča prav tu.

**Zakaj ne zadošča požrešnost.** Mamljivo bi bilo vzeti najdaljšo možno
predpono in nadaljevati. Besedilo naloge to izrecno spodbije: pri `potokrog` je
`potok` daljša predpona, a `rog` je nato treba znati razbiti — pri seznamu
`['o', 'potok', 'krog']` se zatakne, čeprav bi krajša izbira drugje uspela.
Zato je treba **preizkusiti vse** predpone in obupati šele, ko nobena ne izide.

**Rezina `n[len(zacetek):]`** odreže ravno toliko znakov, kolikor jih ima
predpona — problem se zmanjša in rekurzija se zagotovo konča.

**Vzorec »preizkusi vse možnosti in vrni True ob prvem uspehu«** je klasično
sestopanje (*backtracking*) in se pojavi v mnogih izpitnih nalogah.

#### c) `razbitja(n, s)`

Sestavite funkcijo `razbitja`, ki sprejme argumente kot zgoraj, vrne pa množico
vseh razbitji niza `n` na podnize iz seznama `s`. Vsakro razbitje bomo zabeležili
kot nabor nizov iz `s`.

Primer uporabe:

```python
>>> razbitja('potokrog', ['pot', 'o', 'potok', 'krog', 'rog'])
{('pot', 'o', 'krog'), ('potok', 'rog')}
>>> razbitja('potokrog', ['o', 'potok', 'krog'])
set()
>>> razbitja('catsanddogs', ['cat', 'cats', 'and', 'sand', 'dogs'])
{('cats', 'and', 'dogs'), ('cat', 'sand', 'dogs')}
>>> razbitja('abba', ['a', 'bb'])
{('a', 'bb', 'a')}
```

```python
def razbitja(n, s):
    # BAZNI PRIMER: prazen niz ima natanko eno razbitje — prazen nabor.
    # Pozor: to ni set(), ampak množica z enim (praznim) naborom.
    if n == "":
        return {()}

    vsa = set()
    for zacetek in se_zacne(n, s):
        # vsakemu razbitju preostanka spredaj dodamo trenutno predpono
        for razbitje in razbitja(n[len(zacetek):], s):
            vsa.add((zacetek, ) + razbitje)
    return vsa
```

**Ideja.** Ista rekurzija kot prej, le da namesto »ali obstaja« zbiramo **vsa**
razbitja.

```python
if n == "":
    return {()}          # ena sama možnost: prazen nabor

vsa = set()
for zacetek in se_zacne(n, s):
    for razbitje in razbitja(n[len(zacetek):], s):
        vsa.add((zacetek, ) + razbitje)
return vsa
```

**Najpomembnejša podrobnost je bazni primer.** `{()}` je množica z **enim**
elementom, praznim naborom — in ne `set()`, ki je prazna množica. Razlika je
usodna: prazna množica bi pomenila »ni nobenega razbitja«, notranja zanka se ne
bi izvedla in funkcija bi vedno vrnila `set()`.

| Zapis | Pomen |
|---|---|
| `set()` | ni razbitij (niza ni mogoče razbiti) |
| `{()}` | natanko eno razbitje, in sicer prazno |

**Sestavljanje nabora.** `(zacetek, ) + razbitje` doda predpono na začetek
obstoječega nabora. Vejica v `(zacetek, )` je nujna — brez nje bi bili to
navadni oklepaji in `+` bi poskusil sešteti niz z naborom.

**Zakaj nabori in ne seznami.** Elementi množice morajo biti nespremenljivi;
seznamov v množico ni mogoče dati.

**Prejšnja podnaloga postane enovrstična:** `se_razbije(n, s)` je pravzaprav
`razbitja(n, s) != set()`. Ločeni sta zato, ker je iskanje enega razbitja
lahko bistveno hitrejše od naštevanja vseh.

### Naloga 4 — Air Triglav
*Datoteka `2526_i2/04_air_triglav.py`*

Tabela v datoteki CSV, kjer je treba imena stolpcev povezati z vrednostmi v
vrsticah. Podnaloge so verižne: prva prebere glavo, druga celo tabelo, tretja
iz nje izlušči poročilo.

#### a) `destinacije(niz)`

Napiši funkcijo `destinacije(niz)`, ki dobi niz z imeni krajev, kot so zapisani v prvi vrstici datoteke
in vrne seznam z imeni destinacij, na katere letijo letala družbe Air Triglav.
Destinacije naj se v seznamu pojavijo v enakem vrstnem redu kot v vhodnem nizu.

Za zgornjo datoteko `potovanja.txt` funkcija vrne:

```python
>>> destinacije("-,Ljubljana,London,Lizbona\n")
["Ljubljana", "London", "Lizbona"]
```

```python
def destinacije(niz):
    resitev = []
    for kraj in niz.strip().split(","):
        kraj = kraj.strip()
        # prvo polje je oznaka "-", morebitna prazna polja preskočimo
        if kraj and kraj != "-":
            resitev.append(kraj)
    return resitev
```

**Ideja.** Prva vrstica datoteke je glava tabele: oznaka `-` in nato imena
krajev, ločena z vejicami.

```python
for kraj in niz.strip().split(","):
    kraj = kraj.strip()
    if kraj and kraj != "-":
        resitev.append(kraj)
```

**Dvojni `strip`.** Prvi odstrani prelom vrstice na koncu, drugi pa morebitne
presledke okoli posameznih imen. Brez prvega bi bila zadnja destinacija
`"Lizbona\n"` in vse nadaljnje primerjave bi tiho odpovedale.

**`if kraj and ...`** poskrbi za prazna polja (npr. odvečna vejica na koncu
vrstice). Prazen niz je »lažen«, zato je zapis krajši od `if kraj != ""`.

**Vrstni red se ohrani**, ker gradimo seznam v vrstnem redu razbitja — to je
pomembno, saj druga podnaloga stolpce tabele povezuje z imeni prav po zaporedju.

#### b) `preberi_podatke(ime_datoteke)`

Napiši funkcijo `destinacije(ime_datoteke)`, ki iz datoteke prebere podatke
o potovanjih in seznam krajev ter slovar s podatki o številu potnikov (vrednost) za vsak
par izhodišča in destinacije (ključ).

Za zgornjo datoteko `potovanja.txt` funkcija vrne:

```python
>>> preberi_podatke("potovanja.txt")
{("Ljubljana", "London"): 3, ("Ljubljana", "Lizbona"): 3,
 ("London", "Ljubljana"): 2, ("London", "Lizbona"): 5,
 ("Lizbona", "Ljubljana"): 1, ("Lizbona", "London"): 1}
```

```python
def preberi_podatke(ime_datoteke):
    potovanja = {}
    kraji = None

    with open(ime_datoteke, encoding="utf-8") as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue

            if kraji is None:
                # prva vrstica so imena destinacij (stolpci tabele)
                kraji = destinacije(vrstica)
                continue

            polja = vrstica.split(",")
            izhodisce = polja[0].strip()

            # zip poveže stolpce z vrednostmi in se ustavi pri krajšem
            # od obeh — s tem poskrbi tudi za morebitno odvečno vejico
            for cilj, vrednost in zip(kraji, polja[1:]):
                vrednost = vrednost.strip()
                # prazno polje je diagonala (kraj sam s sabo);
                # pozor: "0" NI prazno in mora ostati
                if vrednost == "":
                    continue
                potovanja[(izhodisce, cilj)] = int(vrednost)

    return potovanja
```

**Ideja.** Datoteka je matrika: prva vrstica so imena stolpcev (cilji), prvi
stolpec vsake nadaljnje vrstice pa izhodišče. Rezultat je slovar
`(izhodišče, cilj) -> potniki`.

**Prva vrstica je posebna.** Namesto zastavice `stikalo` uporabimo kar
`kraji is None`:

```python
if kraji is None:
    kraji = destinacije(vrstica)
    continue
```

Spremenljivka torej hkrati hrani podatek in pove, ali smo glavo že prebrali.

**`zip` poveže stolpce z vrednostmi.**

```python
for cilj, vrednost in zip(kraji, polja[1:]):
```

`polja[1:]` izpusti prvo polje (izhodišče). `zip` se ustavi pri krajšem od obeh
zaporedij, kar tiho reši težavo z odvečno vejico na koncu nekaterih vrstic —
brez ročnega štetja stolpcev.

**Prazno polje ni nič.**

```python
if vrednost == "":
    continue
```

Prazna polja so na diagonali (kraj sam s sabo). Pomembno: preverjamo `== ""`
in **ne** `if not vrednost` — slednje bi izpustilo tudi veljavno vrednost
`"0"`, ki v testnih podatkih res nastopa (`Berlin → Pariz: 0`).

**Zakaj nabor kot ključ.** Slovar potrebuje nespremenljiv ključ; par
`(izhodisce, cilj)` je naraven način, da povezavo opišemo z enim ključem
namesto z gnezdenim slovarjem.

#### c) `porocilo(potovanja, kraj)`

Napiši funkcijo `porocilo(potovanja, kraj)`, ki sprejme slovar potovanj,
kot ga vrne funkcija `preberi_podatke`, ter v datoteko zapiše poročilo o potovanjih
na destinaciji. Datoteka naj bo poimenovana z imenom kraja in končnico `txt`.
V datoteko se zapiše ime kraja, skupno število prihodov, skupno število odhodov
in saldo.

V zgornjem datoteke je Ljubljano zapustilo 6 potnikov, pripotovali pa so 3.
Ker so odšli trije več kot prišli, je saldo enak -3.

Če funkcijo pokličemo kot `porocilo(potovanja, "Ljubljana")`, kjer je `potovanja`
slovar iz primera v prejšnji podnalogi, naj funkcija ustvari datoteko `"Ljubljana.txt"`
z vsebino:

```
Ljubljana
============
Prihodi: 3
Odhodi: 6
------------
Saldo: -3
```
Opomba: vrstici z znaki `-` in `=` imata po 12 znakov.

```python
def porocilo(potovanja, kraj):
    prihodi = 0
    odhodi = 0

    # ključ je par (izhodišče, cilj), vrednost pa število potnikov
    for (izhodisce, cilj), potniki in potovanja.items():
        if cilj == kraj:
            prihodi += potniki
        if izhodisce == kraj:
            odhodi += potniki

    with open(f"{kraj}.txt", "w", encoding="utf-8") as f:
        print(kraj, file=f)
        print("=" * 12, file=f)
        print(f"Prihodi: {prihodi}", file=f)
        print(f"Odhodi: {odhodi}", file=f)
        print("-" * 12, file=f)
        print(f"Saldo: {prihodi - odhodi}", file=f)
```

**Ideja.** Iz slovarja povezav seštej vse prihode in vse odhode za dani kraj.

```python
for (izhodisce, cilj), potniki in potovanja.items():
    if cilj == kraj:
        prihodi += potniki
    if izhodisce == kraj:
        odhodi += potniki
```

**Razstavljanje ključa v zanki.** `for (izhodisce, cilj), potniki in
slovar.items()` razpakira nabor-ključ in vrednost v enem koraku. Brez tega bi
pisal `for kljuc in potovanja: kljuc[0] ...`, kar se slabše bere.

**Dva ločena `if`, ne `elif`.** Kraj je lahko hkrati izhodišče ene in cilj
druge povezave; z `elif` bi drugega preskočili.

**Ime datoteke sestavi funkcija sama:** `f"{kraj}.txt"`. Način `open(..., "x")`
bi zahteval, da datoteka še ne obstaja, in bi ob ponovnem klicu sprožil napako —
zato `"w"`, ki jo ustvari ali prepiše.

**Robova sta natanko 12 znakov**, kar zapišemo kot `"=" * 12` in `"-" * 12`.
Ročno preštevanje enačajev je nepotrebno mesto za napako.

**`print(..., file=f)`** sam doda prelom vrstice; z `f.write` bi ga moral
dodajati sam.

**Saldo je `prihodi - odhodi`** in je lahko negativen — f-niz predznak izpiše
sam.

---

## Poskusni izpit 2025/26
Poskusni izpit: sprehodi po pravilih, obdelava izmerjenih podatkov in razred z
matriko. Po zgradbi je enak pravim rokom, zato je najboljša vaja pred izpitom.

### Naloga 1 — Sprehodi
*Datoteka `2526_poskusni/01_sprehodi.py`*

Razčlenjevanje niza znak za znakom. Druga podnaloga doda števila pred koraki,
kar je klasična naloga o »stanju med branjem«.

#### a) `sprehod(opis)`

Sestavite funkcijo `sprehod(opis)`, ki za sprehod `opis` izračuna in vrne
točko, v kateri se sprehod konča. Znakov, ki ne opisujejo veljavnih korakov,
naj funkcija ne upošteva. Primer:

```python
>>> sprehod('-gg-dg--dlddd')
(12, -2)
```

```python
# posamezni koraki: znak -> (sprememba x, sprememba y)
KORAKI = {"-": (1, 0), "g": (1, 1), "d": (1, -1)}


def sprehod(opis):
    x = 0
    y = 0
    for znak in opis:
        if znak in KORAKI:      # neveljavne znake preprosto preskočimo
            dx, dy = KORAKI[znak]
            x += dx
            y += dy
    return (x, y)
```

**Ideja.** Vsak veljaven znak je korak; neveljavne preskočimo. Namesto treh
`if` stavkov uporabimo slovar korakov:

```python
KORAKI = {"-": (1, 0), "g": (1, 1), "d": (1, -1)}

for znak in opis:
    if znak in KORAKI:
        dx, dy = KORAKI[znak]
        x += dx
        y += dy
```

**Preverjanje `if znak in KORAKI` hkrati odpravi neveljavne znake** — pogoja
za `'l'` ali `'@'` ni treba pisati posebej. Slovar tako opravlja dve nalogi:
določa premike in definira, kaj je veljavno.

**Vsi trije koraki gredo v desno** (`x += 1`), razlikujejo se le po višini. To
je smiselno: sprehod napreduje v času, `y` pa je nadmorska višina.

**Rezultat je nabor** `(x, y)`.

**Slovarski pristop se izplača v naslednji podnalogi**, kjer isti `KORAKI`
uporabimo znova — brez podvajanja pravil.

#### b) `strnjen_sprehod(opis)`

Sprehod lahko opišemo krajše, če več zaporednih enakih znakov (več korakov
v isto smer) nadomestimo s številom korakom in opisom koraka. Sprehod
`'-gggggd-dddddddddddd-'` bi krajše opisali z nizom `'-5gd-12d-'`. Sestavite
funkcijo `strnjen_sprehod(opis)`, ki za sprehod `opis` izračuna in vrne točko,
v kateri se sprehod konča. Na primer:

```python
>>> strnjen_sprehod('-7@5gd-12d-')
(21, -8)
>>> strnjen_sprehod('1000g1000-1000d')
(3000, 0)
```

```python
def strnjen_sprehod(opis):
    x = 0
    y = 0
    stevilo = 0     # doslej prebrano število ponovitev

    for znak in opis:
        if znak.isdigit():
            # večmestno število sestavljamo števko po števko
            stevilo = stevilo * 10 + int(znak)
        elif znak in KORAKI:
            # brez števila pred korakom gre za en sam korak
            ponovitve = stevilo if stevilo > 0 else 1
            dx, dy = KORAKI[znak]
            x += dx * ponovitve
            y += dy * ponovitve
            stevilo = 0
        else:
            # neveljaven znak zavrže doslej nabrano število
            stevilo = 0

    return (x, y)
```

**Ideja.** Pred korakom lahko stoji število ponovitev. Števke sestavljamo v
število, dokler ne naletimo na znak koraka.

```python
if znak.isdigit():
    stevilo = stevilo * 10 + int(znak)
elif znak in KORAKI:
    ponovitve = stevilo if stevilo > 0 else 1
    dx, dy = KORAKI[znak]
    x += dx * ponovitve
    y += dy * ponovitve
    stevilo = 0
else:
    stevilo = 0
```

**Sestavljanje večmestnega števila.** `stevilo * 10 + int(znak)` je standardni
prijem: `1`, nato `1*10+2 = 12`. Zbiranje števk v niz in klic `int` na koncu bi
prav tako delovalo, a je tole krajše.

**Brez števila je en korak.** `'-gd'` pomeni po en korak vsake vrste, zato
`ponovitve = stevilo if stevilo > 0 else 1`.

**Neveljaven znak zavrže nabrano število.** Test `'-7@5gd-12d-'` cilja prav na
to: `7` se ob `@` zavrže, veljavna je šele `5` pred `g`. Zato ima veja `else`
pomembno nalogo — brez nje bi se `7` in `5` zlili v `75`.

**Ničesar ni treba izpisati na koncu.** Če se opis konča s številom brez
koraka (npr. `'gg12'`), se to število preprosto ne uporabi — kar je pravilno,
saj brez smeri koraka ni.

**Preverjanje na velikih številih.** `'1000g1000-1000d'` da `(3000, 0)`; če
tvoja rešitev dela z zanko po posameznih korakih, bo počasna, a še vedno
pravilna. Množenje je hitrejše in enostavnejše.

#### c) `najdaljsi_strnjen_sprehod(seznam)`

Sestavite funkcijo `najdaljsi_strnjen_sprehod(seznam)`, ki v danem seznamu
strnjenih opisov sprehodov poišče in vrne tistega, ki se konča čimdlje od
izhodišča. Če je takih sprehodov več, naj vrne prvega med njimi. Predpostavite
lahko, da bo `seznam` neprazen. Primer:

```python
>>> l = ['gdgd--', '-gg-dg--dlddd', '----6---', '-dd-gd--glggg']
>>> najdaljsi_strnjen_sprehod(l)
'-gg-dg--dlddd'
```

```python
def najdaljsi_strnjen_sprehod(seznam):
    najboljsi = None
    najvecja = None

    for opis in seznam:
        x, y = strnjen_sprehod(opis)
        # primerjamo kvadrate razdalj — korena ni treba računati
        oddaljenost = x ** 2 + y ** 2
        if najvecja is None or oddaljenost > najvecja:
            najvecja = oddaljenost
            najboljsi = opis        # strogi > obdrži prvega ob izenačenju

    return najboljsi
```

**Ideja.** Za vsak opis izračunaj končno točko in obdrži tistega, ki je
najdlje od izhodišča.

```python
x, y = strnjen_sprehod(opis)
oddaljenost = x ** 2 + y ** 2
if najvecja is None or oddaljenost > najvecja:
    ...
```

**Korena spet ne rabimo.** Primerjava kvadratov razdalj da isti vrstni red kot
primerjava razdalj, brez `math.sqrt` in brez zaokroževalnih napak.

**Funkcija vrne opis (niz), ne točke.** Lahek spodrsljaj je vrniti `(x, y)`
namesto niza, iz katerega je izračunan.

**Izenačenja so tu resnična.** V testnem seznamu sta dva sprehoda enako
oddaljena od izhodišča (oba pri kvadratu razdalje 148), zato strogi `>`ni
kozmetika — z `>=` bi funkcija vrnila napačnega.

**Ponovna uporaba `strnjen_sprehod`** je bistvena: opisi so v strnjeni obliki,
zato bi klic `sprehod` (iz prve podnaloge) števila ponovitev obravnaval kot
neveljavne znake in dal napačne rezultate.

### Naloga 2 — GPS
*Datoteka `2526_poskusni/02_gps.py`*

Datoteke, pretvorbe enot in analiza zaporednih meritev. Največ napak nastane
pri pretvorbi stopinj v metre — ta korak preveri na roko.

#### a) `preberi(datoteka)`

Sestavite funkcijo `preberi`, ki prebere podatke iz datoteke z danim imenom
ter jih vrne v obliki seznama četverk realnih števil.

```python
>>> preberi("podatki.txt")
[(2762.4, 15.119413, 46.336617, 338.3379), (3254.2, 15.115366, 46.33926, 347.26877),
(3505.27, 15.112539, 46.33839, 365.7277), (3845.9, 15.113494, 46.340103, 381.00534),
(4214.5, 15.115937, 46.34285, 397.64374), (4924.32, 15.12341, 46.344727, 376.80148),
(5872.8, 15.135635, 46.343216, 380.04355), (6919.7, 15.141463, 46.33902, 352.5718),
(7975.7, 15.132955, 46.335052, 337.85965), (9128.91, 15.124098, 46.334476, 342.77164),
(10153.3, 15.119547, 46.3368, 348.18036)]
```

```python
def preberi(datoteka):
    seznam = []
    with open(datoteka, encoding="utf-8") as d:
        for vrstica in d:
            vrstica = vrstica.strip()
            if not vrstica:
                continue
            # naloga zahteva ČETVERKE REALNIH ŠTEVIL, ne seznamov nizov
            seznam.append(tuple(float(x) for x in vrstica.split(",")))
    return seznam
```

**Ideja.** Vsaka vrstica je četverka realnih števil, ločenih z vejico.

```python
seznam.append(tuple(float(x) for x in vrstica.split(",")))
```

**Naloga zahteva števila, ne nizov.** `vrstica.split(",")` da seznam **nizov**;
brez `float` bi kasnejše računanje odpovedalo — `"338.3379" - "347.26877"` je
`TypeError`, `"3" + "4"` pa bi bil `"34"` namesto 7. To je pogosta napaka pri
branju datotek.

**Naloga zahteva nabore, ne seznamov.** `tuple(...)` okoli generatorja to
uredi. Testi tipa ne preverjajo strogo, a se je vredno držati besedila.

**`float` sprejme tudi presledke okoli števila**, zato dodatni `strip` pri
posameznih poljih ni potreben — je pa potreben `strip` na celi vrstici, da
odrežemo prelom.

**Preskok praznih vrstic** (`if not vrstica: continue`) prepreči `ValueError`
pri zadnji, prazni vrstici datoteke.

#### b) `razdalja(a, b)`

Sestavite funkcijo `razdalja`, ki izračuna zračno razdaljo v metrih
med dvema izmerjenima točkama. Točki sta podani kot trojica realnih števil
(zemljepisna dolžina, zemljepisna širina, nadmorska višina). Ne pozabite
pretvoriti zemljepisnih dolžin in širin iz stopinj v metre. Ena minuta
zemljepisne dolžine meri 1291 metrov, ena minuta zemljepisne širine pa
1852 metrov. Izračunano razdaljo zaokrožite na dve decimalni mesti.

```python
>>> razdalja((15.119413, 46.336617, 338.3379), (15.12341, 46.344727, 376.80148))
953.66
```

```python
# ena stopinja ima 60 minut, ena minuta pa toliko metrov:
METROV_NA_MINUTO_DOLZINE = 1291
METROV_NA_MINUTO_SIRINE = 1852


def razdalja(a, b):
    # stopinje -> minute (x 60) -> metri (x metrov na minuto)
    dolzina = abs(a[0] - b[0]) * 60 * METROV_NA_MINUTO_DOLZINE
    sirina = abs(a[1] - b[1]) * 60 * METROV_NA_MINUTO_SIRINE
    visina = abs(a[2] - b[2])

    # Pitagorov izrek v treh razsežnostih
    return round((dolzina ** 2 + sirina ** 2 + visina ** 2) ** 0.5, 2)
```

**Bistvo naloge so enote.** Koordinati sta v **stopinjah**, razdalja pa mora
biti v **metrih**. Ena stopinja ima 60 minut, ena minuta pa toliko metrov, kot
pove naloga:

```python
dolzina = abs(a[0] - b[0]) * 60 * 1291
sirina = abs(a[1] - b[1]) * 60 * 1852
visina = abs(a[2] - b[2])
```

**Pogosta napaka je deljenje s 60 namesto množenja.** Razmisli o smeri
pretvorbe: stopinja je **več** kot minuta, torej je razlika v minutah **večja**
številka — množimo. Kdor deli, dobi razdalje reda velikosti pol metra namesto
skoraj kilometra, kar je takoj očitno, če rezultat pogledaš.

**Višina je že v metrih** in se ne pretvarja.

**Pitagorov izrek v treh razsežnostih:**

```python
return round((dolzina ** 2 + sirina ** 2 + visina ** 2) ** 0.5, 2)
```

`** 0.5` je koren; enakovredno je `math.sqrt(...)`.

**Zaokroževanje je del naloge**, ne kozmetika — testi primerjajo z `953.66`.
`round(x, 2)` zaokroži na dve decimalki.

**Zakaj `abs`.** Pri kvadriranju predznak sicer izgine, tako da bi delovalo tudi
brez — `abs` pa jasno pove namero in obvaruje pred napako, če bi kdo kvadrat
zamenjal z absolutno vrednostjo.

#### c) `analiza(datoteka)`

Sestavite funkcijo `analiza` ki analizira prehojeno pot. Podatke o poti naj
prebere iz datoteke z danim imenom, vrne pa naj čas, ki ga je Janez porabil
za to pot, skupno prehojeno razdaljo, skupno višino vzpona in skupno višino
spusta. Vse vrednosti naj na koncu zaokroži na dve decimalni mesti.

```python
>>> analiza("podatki.txt")
(7390.9, 5380.14, 72.87, 63.03)
```

```python
def analiza(datoteka):
    meritve = preberi(datoteka)

    cas = meritve[-1][0] - meritve[0][0]
    pot = 0
    vzpon = 0
    spust = 0

    for i in range(len(meritve) - 1):
        # prvi element meritve je čas, ostali trije so koordinate
        prejsnja = meritve[i][1:]
        naslednja = meritve[i + 1][1:]

        pot += razdalja(prejsnja, naslednja)

        # razlika višin: pozitivna je vzpon, negativna spust
        razlika = naslednja[2] - prejsnja[2]
        if razlika > 0:
            vzpon += razlika
        else:
            spust -= razlika

    return (round(cas, 2), round(pot, 2), round(vzpon, 2), round(spust, 2))
```

**Ideja.** En sam sprehod čez zaporedne pare meritev, med katerim seštevamo
tri različne stvari.

```python
for i in range(len(meritve) - 1):
    prejsnja = meritve[i][1:]
    naslednja = meritve[i + 1][1:]
    pot += razdalja(prejsnja, naslednja)
    razlika = naslednja[2] - prejsnja[2]
    if razlika > 0:
        vzpon += razlika
    else:
        spust -= razlika
```

**Rezina `meritve[i][1:]`** odreže čas in pusti trojico
(dolžina, širina, višina) — natanko obliko, ki jo pričakuje `razdalja`. To je
lep primer, kako dobro izbrani vmesniki med funkcijami prihranijo delo.

**`range(len(...) - 1)`**, ker vsak korak potrebuje **par** zaporednih meritev;
zadnja nima naslednika.

**Spust seštevamo kot pozitivno število.** `spust -= razlika` pri negativni
razliki prišteva — enakovredno bi bilo `spust += abs(razlika)`.

**Čas je razlika prve in zadnje meritve**, ne vsota medčasov — čeprav v tem
primeru pride enako, je prvo neposredno.

**Zakaj štiri ločene zaokrožitve na koncu.** Vmes računamo z nezaokroženimi
vrednostmi in zaokrožimo šele rezultat, da se napake ne kopičijo.

**Rezultat je četverka** — funkcija torej vrne štiri vrednosti hkrati, kar
klicatelj razpakira z `cas, pot, vzpon, spust = analiza(...)`.

### Naloga 3 — Koda QR
*Datoteka `2526_poskusni/03_koda_qr.py`*

Razred z matriko. Tretja podnaloga je najzahtevnejša na celem izpitu: polnjenje
po stolpcih izmenično navzgor in navzdol, ob tem pa preskakovanje že
določenih polj.

#### a) Razred `KodaQR` — konstruktor in `__str__`

Definirajte razred `KodaQR`, katerega konstruktor bo pripravil matriko
velikosti $n \times m$, kjer sta $n$ in $m$ parametra. Vsi elementi te
matrike naj bodo enaki `None`, kar bo pomenilo, da ustrezna vrednost
v kodi QR še ni določena. Pripravljeno matriko naj konstruktor zapiše v
atribut `matrika`.

```python
>>> qr = KodaQR(3, 4)
>>> qr.matrika
[[None, None, None, None], [None, None, None, None], [None, None, None, None]]
```
Sestavite tudi metodo `__str__`, ki vrne predstavitev kode QR z nizom.
Vrednost `None` naj bo predstavljena s piko, ničla s presledkom, enka pa
z znakom `'#'`. Vse vrstice razen zadnje naj bodo zaključene z znakom
za skok v novo vrsto.

```python
>>> print(qr)
....
....
....
```

```python
class KodaQR:
    def __init__(self, n, m):
        # None pomeni "vrednost še ni določena"
        # Vsako vrstico ustvarimo posebej — [[None] * m] * n bi naredil
        # n sklicev na ISTI seznam.
        self.matrika = [[None] * m for i in range(n)]

    def __str__(self):
        znaki = {None: ".", 0: " ", 1: "#"}
        vrstice = []
        for vrstica in self.matrika:
            vrstice.append("".join(znaki[element] for element in vrstica))
        # join postavi prelom MED vrstice, zato zadnja ni zaključena z njim
        return "\n".join(vrstice)
```

**Ustvarjanje matrike brez pasti.**

```python
self.matrika = [[None] * m for i in range(n)]
```

Zapis `[[None] * m] * n` bi ustvaril `n` sklicev na **isti** seznam — sprememba
enega polja bi se pokazala v vseh vrsticah. Izpeljani seznam ustvari vsako
vrstico posebej. To je najpogostejša napaka pri delu z matrikami.

**Notranji `[None] * m` je varen**, ker je `None` nespremenljiv in ga tako ali
tako vedno zamenjamo, nikoli spreminjamo.

**Preslikava vrednosti v znake s slovarjem:**

```python
znaki = {None: ".", 0: " ", 1: "#"}
```

Slovar je krajši in preglednejši od treh `if`-ov — in `None` je povsem
veljaven ključ.

**`"\n".join(vrstice)` postavi prelom MED vrstice**, zato zadnja ni zaključena
z njim. Naloga to izrecno zahteva (»vse vrstice razen zadnje«). Če bi v zanki
pisal `niz += vrstica + "\n"`, bi imel odvečen prelom na koncu.

**`__str__` mora vrniti niz** in ne izpisovati. Za izpis poskrbi `print(qr)`,
ki `__str__` pokliče sam.

#### b) `vzorec(vzorec, vrstica, stolpec)`

Fiksni elementi v kodi QR nastopajo kot manjše podmatrike posebnih vzorcev.
Razredu `KodaQR` dodajte metodo `vzorec`, ki za parametre dobi manjšo matriko
z vzorcem ter položaj vzorca v kodi QR, podan z indeksom vrstice in indeksom
stolpca, kjer je levi zgornji element vzorca. Metoda naj v kodo QR na dano
mesto zapiše dani vzorec, vrne pa naj ne ničesar.

```python
>>> qr.vzorec([[0, 1], [1, 0]], 1, 1)
>>> qr.matrika
[[None, None, None, None], [None, 0, 1, None], [None, 1, 0, None]]
>>> print(qr)
....
. #.
.# .
```

```python
def vzorec(self, vzorec, vrstica, stolpec):
        # i, j sta indeksa znotraj vzorca, zamik pa ju prestavi v kodo QR
        for i in range(len(vzorec)):
            for j in range(len(vzorec[i])):
                self.matrika[vrstica + i][stolpec + j] = vzorec[i][j]
        # metoda ničesar ne vrne
```

**Ideja.** Manjšo matriko prepišemo v veliko, z zamikom.

```python
for i in range(len(vzorec)):
    for j in range(len(vzorec[i])):
        self.matrika[vrstica + i][stolpec + j] = vzorec[i][j]
```

**Dva para indeksov.** `i, j` sta indeksa **znotraj vzorca**, `vrstica + i` in
`stolpec + j` pa mesto v kodi QR. Zamenjava enega para z drugim je klasična
napaka; pomaga, če ju poimenuješ različno (npr. `i, j` proti `v, s`).

**Zanki gresta po vzorcu, ne po kodi QR.** Velikost vzorca je tista, ki določa,
koliko polj prepišemo.

**`len(vzorec[i])` in ne `len(vzorec[0])`** — dosledno, čeprav so vzorci
pravokotni.

**Metoda ničesar ne vrne.** Testi to izrecno preverjajo (`rezultat` mora biti
`None`). Funkcija brez `return` vrne `None` sama od sebe; pisati `return None`
ni potrebno, a tudi ne škodi.

**Robov ne preverjamo**, ker naloga jamči, da vzorec pade v matriko. Če ne bi,
bi prevelik indeks sprožil `IndexError` — negativni pa bi tiho pisal na
napačno mesto.

#### c) `napolni(podatki)`

Podatke, ki jih želimo zapisati v kodo QR, pripravimo v obliki seznama
ničel in enic. Elemente tega seznama po vrsti zapišemo v kodo QR, pri čemer
začnemo v zadnjem stolpcu spodaj in gremo do vrha, nato po predzadnjem stolpcu
od vrha navzdol, ter nadaljujemo izmenično gor in dol, dokler ne napolnimo
cele matrike. Seveda pri tem spreminjamo samo tiste elemente matrike, ki
imajo od prej še nedoločeno vrednost. Opomba: pravi postopek za zapis
podatkov v kodo QR je malo bolj zapleten, saj se namesto po enem stolpcu
premikamo po dveh naenkrat, enega pa je treba v celoti preskočiti.

Sestavite metodo `napolni`, ki v kodo QR z že vpisanimi fiksnimi vzorci
prepiše elemente danega seznama na način, kot je bil opisan v prejšnem
odstavku. Če nam elementov v seznamu zmanjka, naj preostanek kode QR
napolni z ničlami. Metoda naj ne vrača ničesar.

```python
>>> qr.napolni([1, 1, 1, 0, 1, 0, 1, 1])
>>> qr.matrika
[[0, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1]]
>>> print(qr)
 # #
# ##
## #
```

```python
def napolni(self, podatki):
        n = len(self.matrika)
        m = len(self.matrika[0])

        naslednji = 0       # indeks naslednjega še neporabljenega podatka
        navzgor = True      # v zadnjem stolpcu gremo od spodaj navzgor

        # stolpce obiskujemo od zadnjega proti prvemu
        for j in range(m - 1, -1, -1):
            vrstice = range(n - 1, -1, -1) if navzgor else range(n)

            for i in vrstice:
                # fiksnih vzorcev ne povozimo
                if self.matrika[i][j] is None:
                    if naslednji < len(podatki):
                        self.matrika[i][j] = podatki[naslednji]
                        naslednji += 1
                    else:
                        self.matrika[i][j] = 0   # podatkov je zmanjkalo

            navzgor = not navzgor   # naslednji stolpec v nasprotni smeri
```

**Ideja.** Po stolpcih od zadnjega proti prvemu, izmenično navzgor in navzdol,
polnimo le polja, ki so še `None`.

```python
navzgor = True
for j in range(m - 1, -1, -1):
    vrstice = range(n - 1, -1, -1) if navzgor else range(n)
    for i in vrstice:
        if self.matrika[i][j] is None:
            if naslednji < len(podatki):
                self.matrika[i][j] = podatki[naslednji]
                naslednji += 1
            else:
                self.matrika[i][j] = 0
    navzgor = not navzgor
```

**Vzorec »kača« (*boustrophedon*).** Smer obračamo s
`navzgor = not navzgor`, sam obrat pa je le izbira med dvema `range`-oma. To je
bistveno preglednejše od računanja indeksov s formulami.

**`range(m - 1, -1, -1)`** teče od `m-1` do 0. Tretji argument je korak, drugi
pa je izključujoč — zato `-1` in ne `0`, sicer bi ničti stolpec izpadel.

**Trije primeri za vsako polje:**

1. polje ni `None` → fiksni vzorec, ne diramo ga;
2. polje je `None` in podatki še so → vpišemo naslednjega;
3. polje je `None`, podatkov ni več → vpišemo 0.

**`is None` in ne `== None`.** Pri `None` se vedno uporablja `is`; z `==` bi
razred, ki povozi `__eq__`, lahko dal presenetljiv odgovor. Tu bi delovalo, a
je navada pomembna — pri vrednosti `0` je razlika usodna, saj je `0 == None`
sicer `False`, `if not polje` pa bi ničlo napačno štel za prazno.

**Lastni števec `naslednji`** je preprostejši od brisanja iz seznama
(`podatki.pop(0)`), ki bi vhodni seznam spremenil in bil počasnejši.


---

## Kaj se na teh izpitih ponavlja

Vseh devet rokov ima isto zgradbo: **tri naloge po tri podnaloge**, pri čemer
so podnaloge znotraj naloge odvisne druga od druge (b uporablja a, c uporablja
b). Ocenjujejo pa se ločeno — če ti prva ne uspe, napiši svojo različico in
nadaljuj.

Vsak rok ima praviloma po eno nalogo iz vsake od treh skupin: **obdelava
podatkovnih struktur**, **razred** in **datoteke**. Če ti katera od teh treh ne
leži, se ji na izpitu ne boš mogel izogniti.

### Vzorci, ki se pojavijo skoraj na vsakem roku

| Vzorec | Kje se pojavi | Ključni zapis |
|---|---|---|
| Štetje v slovar | `pogostost`, `klepetulja`, `zbrano`, `Stevec` | `slovar[k] = slovar.get(k, 0) + 1` |
| Urejanje po ključu | `gnezdi`, `najpogostejsa_imena`, `uredi_stranke` | `sorted(x, key=...)`, `key=lambda p: (-p[1], p[0])` |
| Iskanje najboljšega z zanko | `klepetulja`, `zmagovalec`, `najblizja_stranka` | `if najboljsi is None or novo > najboljsi:` |
| Iskanje **indeksa** namesto elementa | `klic`, `zmagovalec` | `min(range(len(x)), key=lambda i: ...)` |
| Akumulator z izpiranjem | `dolzine_kitic`, `linije` | števec + `append` ob ločnici + `append` po zanki |
| Rekurzija po strukturi | `zlij`, `uredi`, `indeks`, `se_razbije`, `razbitja` | bazni primer **najprej**, nato korak |
| Sestopanje (preizkusi vse) | `se_razbije`, `razbitja`, `pri_kom_zaceti` | zanka čez možnosti + rekurzivni klic |
| Slovar smeri | `Izvidnica`, `sprehod`, `osmerosmerke` | `PREMIKI = {"S": (0, 1), ...}` |
| Krožno gibanje | `izlocen`, `zmagovalec` (izštevanke) | `% len(seznam)` |
| Kvadrat razdalje namesto korena | `najblizja_stranka`, `najdaljsi_strnjen_sprehod` | `dx ** 2 + dy ** 2` |
| Branje datoteke | `linije`, `preberi_ladjice`, `preberi_podatke` | `with open(ime, encoding='utf-8')`, `strip()` |
| Pisanje datoteke | `pregledno`, `vizualiziraj`, `porocilo` | `open(ime, 'w')`, `print(..., file=f)` |
| Matrika brez pasti | `preberi_ladjice`, `KodaQR` | `[[x] * m for i in range(n)]` |
| Posebne metode | `Beseda`, `Oseba`, `Dvigalo`, `Stevec`, `KodaQR` | `__init__`, `__str__`, `__repr__`, `__lt__`, `__eq__` |
| Regularni izrazi | `custvencki`, `znacke`, `poenostavi` | `re.findall(r"...", niz)` |

### Odločitve, ki se ponavljajo

- **`None` proti prazni vrednosti.** `None` pomeni »odgovora ni«, `[]`/`""`/`0`
  pa »odgovor je prazen«. Testi ju vedno ločujejo — glej `bralni_okvir`,
  `delez_objav_z_znackami`, `obstaja_povezava`, `najdaljsi_gen`.
- **Strogi `<` oz. `>` pri iskanju najboljšega**, kadar naloga zahteva
  »prvega med enakimi«.
- **Nabor proti seznamu.** Kadar naloga govori o paru ali trojici, se
  pričakuje nabor — in nabor z enim elementom se piše `(x, )`.
- **Kopija proti istemu objektu.** Funkcija, ki seznam spreminja, naj si najprej
  naredi kopijo; funkcija, ki naj vrne prejeti objekt, pa ne sme vrniti kopije.

## Napake, ki so v teh rešitvah dejansko nastale

Spodnje niso izmišljene — vse so bile v prvotnih oddajah teh izpitov.

1. **Sprehod po znakih namesto po vrsticah.** `for vrstica in pesem` gre po
   znakih. Za vrstice rabiš `pesem.split("\n")`.
2. **Primerjava enega znaka z več znaki.** `if znak == '\n\n'` in
   `if znak == 'bcdfg...'` nista nikoli resnična. Za drugo rabiš `in`.
3. **Vrnjen napačen tip.** `return dolzina, seznam` vrne nabor namesto seznama;
   sestavljanje niza `"('A',('P',))"` namesto pravega nabora; seznam nizov
   namesto seznama števil pri branju datoteke.
4. **`niz.index(znak)` v zanki.** Vrne mesto **prve** pojavitve, ne trenutne.
   Če rabiš indeks med sprehodom, uporabi `enumerate` ali `range(len(...))`.
5. **Zadnji element se izgubi.** Če v zanki shranjuješ ob ločnici, moraš zadnjo
   skupino shraniti še po zanki.
6. **Primerjanje le prvega znaka namesto cele predpone.** `n[0] == niz[0]`
   namesto `n.startswith(niz)`.
7. **Napačna smer pretvorbe enot.** Deljenje s 60 namesto množenja pri
   pretvorbi stopinj v minute — rezultat je za faktor 3600 premajhen.
8. **Kopija namesto istega objekta** (in obratno). Test z `is` zahteva prejeti
   objekt; funkcija, ki spreminja seznam, naj si prej naredi kopijo.
9. **Podnaloga, ki je ostala kopija prejšnje.** Ko rešitev prekopiraš kot
   izhodišče, jo je treba tudi predelati — sicer testi javijo napako pri
   podnalogi, za katero misliš, da je rešena.

## Kako preveriti rešitev

Izpitna datoteka ob zagonu rešitve **odda na strežnik Projekta Tomo** in šele
nato izpiše, katere podnaloge so veljavne. Med učenjem je to povsem v redu
(število poskusov ni omejeno), je pa dobro vedeti, da se zgodi.

Posamezno funkcijo lahko preizkusiš brez oddaje kar v konzoli:

```python
>>> stevilo_zlogov("Rdečo mašno maš v laseh")
[3, 2, 1, 2]
```

Primeri iz besedila naloge (vrstice z `>>>`) so prvi testi, ki jih je vredno
pognati — testi v datoteki jih skoraj vedno vsebujejo, dodajo pa še robne
primere: prazen niz, en sam element, izenačenja, vrednost izven mej.

### Kako brati testno kodo

Na dnu vsake izpitne datoteke je razdelek s testi. Splača se ga prebrati
**pred** pisanjem rešitve — pogosto pove več kot besedilo naloge:

- `Check.equal('izraz', pricakovano)` — najpogostejši; pokaže natančno obliko
  rezultata (nabor proti seznamu, `None` proti `0`).
- `Check.run([ukazi], {'spremenljivka': vrednost})` — preveri stanje po
  zaporedju ukazov; tipično za razrede.
- `Check.in_file(ime, vsebina)` in `Check.out_file(ime, vsebina)` — ustvarita
  vhodno datoteko oz. primerjata izhodno, vrstico za vrstico.

Kadar se besedilo naloge in testi razhajata, **veljajo testi**. V tem naboru
izpitov se to zgodi vsaj dvakrat (pravilo za zlogotvorni `r` v 3. roku 2023/24
in primer v besedilu 3. podnaloge pri Vrhskali).
