# UVP – Zbornik rešenih vaj (vaje_1 + vaje_2)

Vse naloge iz `vaje_1.py` in `vaje_2.py`, urejene po **13 temah**.
Za vsako temo: naloga, **polna rešitev**, razlaga in **alternativni pristop**, kjer je smiseln.

**Kazalo**

1. [Rekurzija nad števkami](#1-rekurzija-nad-števkami)
2. [Rekurzija nad nizi](#2-rekurzija-nad-nizi)
3. [Nizi in štetje](#3-nizi-in-štetje)
4. [Seznami (izpeljani seznam)](#4-seznami-izpeljani-seznam)
5. [Matrike](#5-matrike)
6. [Gnezdeni slovarji](#6-gnezdeni-slovarji)
7. [Množice](#7-množice)
8. [Razred z operatorji](#8-razred-z-operatorji)
9. [Razred in urejanje](#9-razred-in-urejanje)
10. [Generator – neskončno zaporedje](#10-generator--neskončno-zaporedje)
11. [Generator – zlivanje](#11-generator--zlivanje)
12. [Sklad](#12-sklad)
13. [Datoteke](#13-datoteke)

Na začetku datotek so potrebni uvozi:

```python
import os
import math
import string

POT = os.path.join(os.path.dirname(__file__), "besedilo.txt")
```

---

## 1. Rekurzija nad števkami

### vaje_1 — `najvecja_stevka(n)`

> Za nenegativno celo število `n` vrne njegovo največjo števko. Reši **rekurzivno** (brez pretvorbe v niz, brez zanke).

```python
def najvecja_stevka(n):
    if n < 10:                 # robni primer: enomestno število
        return n
    return max(n % 10, najvecja_stevka(n // 10))
```

**Razlaga**
- Robni primer ustavi rekurzijo: če `n < 10`, ima eno samo števko → vrni `n`.
- Sicer število razbijemo: zadnja števka `n % 10`, preostanek `n // 10`. Vrnemo večjo med zadnjo števko in največjo števko preostanka.
- `najvecja_stevka(28193)` → `max(3, max(9, max(1, max(8, 2)))) = 9`.

### vaje_2 — `vsota_stevk(n)`

> Vrne vsoto vseh števk števila `n`. Rekurzivno, brez niza in zanke.

```python
def vsota_stevk(n):
    if n < 10:
        return n
    return n % 10 + vsota_stevk(n // 10)
```

**Razlaga** — ista shema, le `max(...)` zamenja `+`: zadnjo števko **prištejemo** vsoti števk preostanka. `vsota_stevk(123)` → `3 + 2 + 1 = 6`.

**Alternativa (z zanko – če rekurzija ni zahtevana)**

```python
def vsota_stevk(n):
    vsota = 0
    while n > 0:
        vsota += n % 10
        n //= 10
    return vsota
```

> ⚠️ Pretvorba v niz (`sum(int(c) for c in str(n))`) da pravilen rezultat, a **krši** zahtevo »brez niza« — na izpitu izgubiš točke. Dvoje ključnih orodij za števke je vedno `n % 10` (zadnja števka) in `n // 10` (preostanek).

---

## 2. Rekurzija nad nizi

### vaje_1 — `razteg(niz)`

> Vrne nov niz, v katerem je vsak znak podvojen. Rekurzivno.

```python
def razteg(niz):
    if niz == "":              # robni primer: prazen niz
        return ""
    return niz[0] * 2 + razteg(niz[1:])
```

**Razlaga** — prvi znak podvojimo (`niz[0] * 2`) in pripnemo razteg preostanka (`niz[1:]`). `"abc"` → `"aa" + "bb" + "cc"`.

### vaje_2 — `obrni(niz)`

> Vrne niz v obratnem vrstnem redu. Rekurzivno.

```python
def obrni(niz):
    if niz == "":
        return ""
    return obrni(niz[1:]) + niz[0]   # obrni preostanek, prvi znak na KONEC
```

**Razlaga** — obrnemo preostanek in **na konec** pripnemo prvi znak. `obrni("abc")` = `obrni("bc") + "a"` = `"cb" + "a"` = `"cba"`.

**Alternativi**

```python
# simetrična rekurzija: zadnji znak naprej, obrni preostanek
def obrni(niz):
    if niz == "":
        return ""
    return niz[-1] + obrni(niz[:-1])

# brez rekurzije: rezina z negativnim korakom
def obrni(niz):
    return niz[::-1]
```

> Vsaka rekurzija nad nizom potrebuje robni primer `niz == ""`, sicer se kliče v neskončnost (in poči na praznem nizu).

---

## 3. Nizi in štetje

### vaje_1 — `besede_dolzine(stavek, k)`

> Vrne seznam besed iz stavka, ki imajo natanko `k` znakov (v enakem vrstnem redu).

```python
def besede_dolzine(stavek, k):
    resitev = []
    for beseda in stavek.split():
        if len(beseda) == k:
            resitev.append(beseda)
    return resitev
```

**Alternativa (izpeljani seznam)**

```python
def besede_dolzine(stavek, k):
    return [b for b in stavek.split() if len(b) == k]
```

### vaje_2 — `besede_z_zacetnico(stavek, c)`

> Vrne seznam besed, ki se začnejo s črko `c` (ne loči med malimi/velikimi črkami).

```python
def besede_z_zacetnico(stavek, c):
    return [b for b in stavek.split() if b[:1].lower() == c.lower()]
```

**Razlaga**
- `stavek.split()` **brez argumenta** razbije po poljubnih belih znakih in pri praznem nizu vrne `[]` (ne `['']`). Zato je robusten od `split(' ')`.
- `b[:1]` je varen »prvi znak«: za prazno besedo vrne `""` namesto napake `IndexError` (ki bi jo dal `b[0]`).
- `.lower()` na obeh straneh → neobčutljivost na velikost črk.

**Alternativa (navadna zanka)**

```python
def besede_z_zacetnico(stavek, c):
    resitev = []
    for b in stavek.split():
        if b[:1].lower() == c.lower():
            resitev.append(b)
    return resitev
```

> Pogosta past: `"".split(' ')` vrne `['']`, nato `b[0]` poči. `split()` brez argumenta se temu izogne.

---

## 4. Seznami (izpeljani seznam)

### vaje_1 — `vsote_sosednjih(seznam)`

> i-ti element rezultata je vsota i-tega in (i+1)-tega elementa. Rezultat je za 1 krajši.

```python
def vsote_sosednjih(seznam):
    return [seznam[i] + seznam[i + 1] for i in range(len(seznam) - 1)]
```

### vaje_2 — `razlike_sosednjih(seznam)`

> i-ti element je `seznam[i+1] - seznam[i]`. Pri 0 ali 1 elementu vrni `[]`.

```python
def razlike_sosednjih(seznam):
    return [seznam[i + 1] - seznam[i] for i in range(len(seznam) - 1)]
```

**Razlaga**
- Gremo do `len(seznam) - 1`, ker zadnji element nima soseda na desni.
- Pri ≤1 elementu je `range(...)` prazen → rezultat `[]` (robni primer samodejno pokrit).
- ⚠️ Pazi na **vrstni red odštevanja**: naloga zahteva `seznam[i+1] - seznam[i]`. Obratno (`seznam[i] - seznam[i+1]`) da nasprotne predznake.

**Alternativi**

```python
# navadna zanka
def razlike_sosednjih(seznam):
    rez = []
    for i in range(len(seznam) - 1):
        rez.append(seznam[i + 1] - seznam[i])
    return rez

# zip s premaknjeno kopijo (zelo idiomatsko za "sosednje pare")
def razlike_sosednjih(seznam):
    return [b - a for a, b in zip(seznam, seznam[1:])]
```

> `zip(seznam, seznam[1:])` parno združi vsak element z naslednjim — pogost trik za delo s sosednjimi elementi.

---

## 5. Matrike

### vaje_1 — `je_simetricna(M)`

> Vrne `True`, če velja `M[i][j] == M[j][i]` za vse `i, j`.

```python
def je_simetricna(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != M[j][i]:
                return False
    return True
```

**Razlaga** — brž ko najdemo en neujemajoč par, vrnemo `False`; sicer na koncu `True`. Brez končnega `return True` bi funkcija vrnila `None`.

### vaje_2 — `je_zgornje_trikotna(M)`

> Vrne `True`, če so vsi elementi **pod** glavno diagonalo enaki 0 (`M[i][j] == 0` za vse `i > j`).

```python
def je_zgornje_trikotna(M):
    for i in range(len(M)):
        for j in range(i):          # samo stolpci LEVO od diagonale (j < i)
            if M[i][j] != 0:
                return False
    return True
```

**Razlaga** — pod diagonalo so mesta z `j < i`. `range(i)` da prav te stolpce, zato ni treba dodatnega pogoja `if i > j`.

**Alternativi**

```python
# z eksplicitnim pogojem (pregled cele matrike)
def je_zgornje_trikotna(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i > j and M[i][j] != 0:
                return False
    return True

# z all() in generatorjem
def je_zgornje_trikotna(M):
    return all(M[i][j] == 0
               for i in range(len(M))
               for j in range(i))
```

> `all(...)` vrne `True`, če je pogoj izpolnjen za vse elemente; prazna matrika ali `[[7]]` dasta `True` (ni elementov pod diagonalo).

---

## 6. Gnezdeni slovarji

### vaje_1 — `povprecja(zapisi)`

> `zapisi` je seznam trojic `(student, predmet, ocena)`. Vrni `{student: povprecna_ocena}` (zaokroženo na 2 decimalki).

```python
def povprecja(zapisi):
    zbir = {}                                   # student -> seznam ocen
    for student, predmet, ocena in zapisi:
        if student not in zbir:
            zbir[student] = []
        zbir[student].append(ocena)

    rezultat = {}                               # student -> povprečje
    for student, ocene in zbir.items():
        rezultat[student] = round(sum(ocene) / len(ocene), 2)
    return rezultat
```

**Razlaga (dva koraka)** — najprej **zberi** vse ocene v sezname, **šele nato** izračunaj povprečje (`sum / len`). Povprečja ne moremo računati sproti, ker takrat še ne poznamo vseh ocen.

### vaje_2 — `vsote_po_kategorijah(zapisi)`

> `zapisi` je seznam parov `(kategorija, znesek)`. Vrni `{kategorija: vsota_zneskov}` (zaokroženo na 2 decimalki).

```python
def vsote_po_kategorijah(zapisi):
    vsote = {}
    for kategorija, znesek in zapisi:
        vsote[kategorija] = vsote.get(kategorija, 0) + znesek
    for kategorija in vsote:
        vsote[kategorija] = round(vsote[kategorija], 2)
    return vsote
```

**Razlaga**
- Pri **vsoti** (za razliko od povprečja) lahko seštevamo **sproti**, ker za vsoto ne rabimo poznati vseh vrednosti vnaprej.
- `vsote.get(kategorija, 0)` vrne dosedanjo vsoto ali `0` ob prvem pojavu → ni potrebe po `if kategorija not in ...`.
- ⚠️ Tu **ne** deli z `len(...)` — to bi bilo povprečje.

**Alternativa (dvostopenjska, kot pri povprečjih)**

```python
def vsote_po_kategorijah(zapisi):
    zbir = {}
    for kategorija, znesek in zapisi:
        if kategorija not in zbir:
            zbir[kategorija] = []
        zbir[kategorija].append(znesek)
    return {k: round(sum(v), 2) for k, v in zbir.items()}
```

> Vzorec `slovar.get(kljuc, privzeto)` je standardni trik za štetje/seštevanje brez ročnega preverjanja obstoja ključa. (Še krajše z `collections.defaultdict(int)` ali `Counter`.)

---

## 7. Množice

### vaje_1 — `skupni_prijatelji(graf, a, b)`

> `graf` je `oseba -> množica prijateljev`. Vrni **urejen** seznam oseb, ki so prijatelji oboje, `a` in `b`.

```python
def skupni_prijatelji(graf, a, b):
    return sorted(graf[a] & graf[b])
```

**Razlaga** — »prijatelj obeh« = **presek** množic (`&`). `sorted(...)` ga pretvori v urejen seznam.

### vaje_2 — `samo_pri_prvem(graf, a, b)`

> Vrni **urejen** seznam prijateljev osebe `a`, ki **niso** prijatelji osebe `b`.

```python
def samo_pri_prvem(graf, a, b):
    return sorted(graf[a] - graf[b])
```

**Razlaga** — »pri `a`, ne pri `b`« = **razlika** množic (`-`). Prazna razlika → `sorted` da `[]`.

**Pregled operacij z množicami (alternativni zapisi)**

| Operacija | Operator | Metoda |
|-----------|----------|--------|
| presek | `a & b` | `a.intersection(b)` |
| razlika | `a - b` | `a.difference(b)` |
| unija | `a \| b` | `a.union(b)` |
| simetrična razlika | `a ^ b` | `a.symmetric_difference(b)` |

```python
# z metodo namesto operatorja (enakovredno)
def samo_pri_prvem(graf, a, b):
    return sorted(graf[a].difference(graf[b]))
```

---

## 8. Razred z operatorji

### vaje_1 — `Vektor`

> 2D vektor s komponentama `x`, `y`. Implementiraj `__init__`, `__repr__`, `__eq__`, `__add__`, `__sub__`, `__mul__` (s skalarjem), `dolzina`.

```python
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, skalar):                    # množenje s ŠTEVILOM
        return Vektor(self.x * skalar, self.y * skalar)

    def dolzina(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
```

### vaje_2 — `Kompleksno`

> Kompleksno število z `re`, `im`. Enako kot Vektor, le `__mul__` je **množenje kompleksnih števil**: `(a+bi)(c+di) = (ac − bd) + (ad + bc)i`.

```python
class Kompleksno:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __repr__(self):
        return f"Kompleksno({self.re}, {self.im})"

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __add__(self, other):
        return Kompleksno(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Kompleksno(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Kompleksno(self.re * other.re - self.im * other.im,
                          self.re * other.im + self.im * other.re)

    def dolzina(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)
```

**Razlaga (dunder metode)**
- Posebne metode z dvojnimi podčrtaji povedo Pythonu, kaj naredi `+`, `-`, `*`, `==`, kako se objekt izpiše (`__repr__`).
- `__add__`, `__sub__`, `__mul__` vedno **vrnejo nov objekt** in ne spreminjajo obstoječih.
- Razlika med nalogama: pri `Vektor` je `*` množenje s **skalarjem** (število), pri `Kompleksno` množenje **dveh objektov** po formuli.

**Alternativa / razširitev**

```python
    def __abs__(self):           # omogoči abs(k) namesto k.dolzina()
        return math.sqrt(self.re ** 2 + self.im ** 2)
```

> Z `__abs__` bi delovalo `abs(Kompleksno(3, 4)) == 5.0` — Python ima za vsako vgrajeno operacijo svojo dunder metodo.

---

## 9. Razred in urejanje

### vaje_1 — `Knjiga` + `uredi_knjige`

> Atributi `naslov`, `leto`, `strani`. `__lt__`: manjša je knjiga z manjšim **letom**; pri istem letu z manj **stranmi**. `uredi_knjige` vrne nov urejen seznam.

```python
class Knjiga:
    def __init__(self, naslov, leto, strani):
        self.naslov = naslov
        self.leto = leto
        self.strani = strani

    def __repr__(self):
        return f"Knjiga({self.naslov}, {self.leto}, {self.strani})"

    def __lt__(self, other):
        if self.leto != other.leto:        # primarno merilo: leto
            return self.leto < other.leto
        return self.strani < other.strani  # pri istem letu: strani


def uredi_knjige(knjige):
    return sorted(knjige)
```

### vaje_2 — `Izdelek` + `uredi_izdelke`

> Atributi `ime`, `cena`, `kolicina`. `__lt__`: manjša **cena**; pri enaki ceni manjša **kolicina**.

```python
class Izdelek:
    def __init__(self, ime, cena, kolicina):
        self.ime = ime
        self.cena = cena
        self.kolicina = kolicina

    def __repr__(self):
        return f"Izdelek({self.ime}, {self.cena}, {self.kolicina})"

    def __lt__(self, other):
        if self.cena != other.cena:              # primarno: cena
            return self.cena < other.cena
        return self.kolicina < other.kolicina    # pri enaki ceni: kolicina


def uredi_izdelke(izdelki):
    return sorted(izdelki)
```

**Razlaga** — `__lt__` (operator `<`) vgradi vrstni red v razred; `sorted` se interno opira nanj, zato ne rabi `key`. `sorted` vrne **nov** seznam (za razliko od `.sort()`, ki spreminja na mestu).

**Alternativa — urejanje s `key` (brez `__lt__`)**

Namesto `__lt__` lahko vrstni red določiš pri klicu `sorted` z ** key funkcijo**, ki vrne **terko**. Python primerja terke po elementih (najprej cena, ob izenačenju kolicina):

```python
def uredi_izdelke(izdelki):
    return sorted(izdelki, key=lambda iz: (iz.cena, iz.kolicina))
```

Druge variante:

```python
from operator import attrgetter
sorted(izdelki, key=attrgetter("cena", "kolicina"))   # enako, brez lambde

sorted(izdelki, key=lambda iz: (iz.cena, -iz.kolicina))  # cena ↑, kolicina ↓

izdelki.sort(key=lambda iz: (iz.cena, iz.kolicina))   # na mestu (NE vrne novega)
```

> **Kdaj kaj:** `__lt__` uporabi, ko želiš, da objekti znajo `<`, `min`, `max`, `sorted` povsod. `key` je bolj prožen za enkratno/poljubno urejanje. Za to nalogo navodilo zahteva `__lt__`, a obe rešitvi sta pravilni. Za »nov seznam« vedno `sorted`, ne `.sort()`.

---

## 10. Generator – neskončno zaporedje

### vaje_1 — `fibonacci()`

> Neskončen generator Fibonaccijevih števil: `0, 1, 1, 2, 3, 5, 8, ...`

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

**Razlaga** — `yield` vrne trenutno vrednost in **zamrzne** stanje do naslednjega `next()`. `a, b = b, a + b` je hkratno prirejanje (desna stran se izračuna iz starih vrednosti).

### vaje_2 — `trikotniska()`

> Neskončen generator trikotniških števil: `0, 1, 3, 6, 10, 15, ...` (k-to število je `0+1+...+k`).

```python
def trikotniska():
    vsota = 0
    k = 1
    while True:
        yield vsota
        vsota += k
        k += 1
```

**Razlaga** — vsakič vrnemo trenutno vsoto, nato prištejemo naslednje celo število `k`.

**Uporaba (oba sta neskončna!)**

```python
g = trikotniska()
[next(g) for _ in range(6)]      # [0, 1, 3, 6, 10, 15]
```

> ⚠️ Ker sta neskončna, ju **nikoli** ne kliči z `list(trikotniska())` (zacikljalo bi se). Uporabi `next(g)` ali omeji z `range`.

**Alternativa — formula brez akumulacije**

```python
def trikotniska():
    k = 0
    while True:
        yield k * (k + 1) // 2   # zaprta formula za k-to trikotniško število
        k += 1
```

---

## 11. Generator – zlivanje

### vaje_1 — `izmenicno(a, b)`

> Generator izmenično vrača elemente: prvi iz `a`, prvi iz `b`, drugi iz `a`, ... Ko se eno izčrpa, vrne preostanek drugega.

```python
def izmenicno(a, b):
    a = list(a)
    b = list(b)
    for i in range(max(len(a), len(b))):
        if i < len(a):
            yield a[i]
        if i < len(b):
            yield b[i]
```

**Razlaga** — gremo do dolžine daljšega zaporedja; za vsak indeks vrnemo `a[i]` in nato `b[i]`, vsakega le, če ta indeks obstaja.

### vaje_2 — `zlij_urejeno(a, b)`

> `a` in `b` sta že naraščajoče urejena. Generator vrača vse elemente v naraščajočem vrstnem redu (zlivanje).

```python
def zlij_urejeno(a, b):
    a = list(a)
    b = list(b)
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            yield a[i]
            i += 1
        else:
            yield b[j]
            j += 1
    while i < len(a):               # preostanek a
        yield a[i]
        i += 1
    while j < len(b):               # preostanek b
        yield b[j]
        j += 1
```

**Razlaga** — dva kazalca `i`, `j`; vsakič vrnemo **manjšega** med `a[i]` in `b[j]` ter premaknemo njegov kazalec. Ko se eno zaporedje izčrpa, vrnemo preostanek drugega. `<=` ohrani stabilnost (pri enakosti gre `a` pred `b`).

> To je korak »merge« iz urejanja z zlivanjem (merge sort).

---

## 12. Sklad

### vaje_1 — `pravilno_gnezdeni(niz)`

> Niz vsebuje `()`, `[]`, `{}` in druge znake (te ignoriraj). Vrni `True`, če so oklepaji pravilno gnezdeni in zaprti.

```python
def pravilno_gnezdeni(niz):
    pari = {')': '(', ']': '[', '}': '{'}      # ZAPIRAJOČI -> ODPIRAJOČI
    sklad = []
    for znak in niz:
        if znak in '([{':
            sklad.append(znak)                 # odpiramo: na sklad
        elif znak in ')]}':
            if not sklad or sklad.pop() != pari[znak]:
                return False                   # nič odprtega ali napačen par
    return len(sklad) == 0                      # na koncu mora biti prazen
```

**Razlaga** — odpirajoče damo na sklad; zapirajoči se mora ujemati z **zadnjim** odprtim (`sklad.pop()`). Slovar `pari` slika zapirajoči → odpirajoči (zato `pari[znak]` deluje pri zapirajočem). Na koncu mora biti sklad prazen.

### vaje_2 — `odstrani_pare(niz)`

> Ponavljajoče odstranjuj **dva enaka sosednja** znaka, dokler je mogoče. Vrni končni niz.

```python
def odstrani_pare(niz):
    sklad = []
    for znak in niz:
        if sklad and sklad[-1] == znak:     # enak vrhu -> par se odstrani
            sklad.pop()
        else:
            sklad.append(znak)
    return "".join(sklad)
```

**Razlaga** — znak primerjamo z vrhom sklada (`sklad[-1]`). Če sta enaka, tvorita par → `pop()` (oba izgineta). Sicer znak damo na sklad. Tako se »ujamejo« tudi pari, ki nastanejo po odstranitvi: `"abbac"` → `bb` izgine → `aa` izgine → ostane `"c"`.

> Sklad je seznam, kjer dodajamo/jemljemo **le na koncu**: `.append()` in `.pop()`. `sklad[-1]` je vrh (zadnji element).

---

## 13. Datoteke

> Obe nalogi delata z datoteko `besedilo.txt` v isti mapi (pot v `POT`).

### vaje_1 — `stevilo_besed(ime)` in `najdaljsa_vrstica(ime)`

```python
def stevilo_besed(ime):
    slovar = {}
    with open(ime, encoding="utf-8") as d:
        for vrstica in d:
            for beseda in vrstica.lower().split():
                beseda = beseda.strip(string.punctuation)   # odstrani ločila z robov
                if beseda:                                   # preskoči prazne
                    slovar[beseda] = slovar.get(beseda, 0) + 1
    return slovar


def najdaljsa_vrstica(ime):
    najdaljsa = ""
    with open(ime, encoding="utf-8") as d:
        for vrstica in d:
            vrstica = vrstica.rstrip("\n")
            if len(vrstica) > len(najdaljsa):
                najdaljsa = vrstica
    return najdaljsa
```

**Razlaga**
- `with open(...) as d` varno odpre datoteko (sama se zapre); beremo vrstico za vrstico.
- `vrstica.lower().split()` normalizira velikost črk in razbije po belih znakih.
- `string.punctuation` je vnaprej pripravljen niz vseh ločil; `.strip(string.punctuation)` jih odreže z **obeh robov** besede.
- `slovar.get(beseda, 0) + 1` je standardni trik za štetje.
- Strogi `>` v `najdaljsa_vrstica` poskrbi, da pri enaki dolžini obdržimo **prvo** najdaljšo.

### vaje_2 — `stevilo_vrstic(ime)` in `pojavitve(ime, beseda)`

```python
def stevilo_vrstic(ime):
    stevec = 0
    with open(ime, encoding="utf-8") as d:
        for vrstica in d:
            if vrstica.strip():             # preskoči prazne vrstice
                stevec += 1
    return stevec


def pojavitve(ime, beseda):
    iskana = beseda.lower()
    stevec = 0
    with open(ime, encoding="utf-8") as d:
        for vrstica in d:
            for b in vrstica.lower().split():
                if b.strip(string.punctuation) == iskana:
                    stevec += 1
    return stevec
```

**Razlaga**
- `stevilo_vrstic`: `vrstica.strip()` je »resničen«, če vrstica vsebuje kak nepresledni znak → tako ločimo prazne vrstice.
- `pojavitve`: vsako besedo normaliziramo (`lower`) in z `.strip(string.punctuation)` odrežemo ločila z robov, da `'"dober'`, `'mesto,'`, `'skrita.)'` ujamemo pravilno.

**Alternativa — `pojavitve` prek `stevilo_besed`**

Če imaš že `stevilo_besed`, je `pojavitve` le branje iz tega slovarja:

```python
def pojavitve(ime, beseda):
    return stevilo_besed(ime).get(beseda.lower(), 0)
```

> ⚠️ Vedno odpiraj z `encoding="utf-8"` (zaradi šumnikov) in uporabi `with`, da se datoteka zanesljivo zapre.

---

## Hitri povzetek vzorcev

| Tema | Ključni prijem |
|------|----------------|
| Rekurzija (števke) | robni primer `n < 10`; `n % 10`, `n // 10` |
| Rekurzija (nizi) | robni primer `niz == ""`; `niz[0]` + rekurzija na `niz[1:]` |
| Štetje besed | `stavek.split()` (brez argumenta!), izpeljani seznam |
| Sosednji elementi | `range(len(seznam) - 1)` ali `zip(seznam, seznam[1:])` |
| Matrike | dvojna zanka po `i`, `j`; `range(i)` za pod diagonalo |
| Slovarji-zbiranje | `slovar.get(k, 0) + ...`; vsota sproti, povprečje v 2 korakih |
| Množice | presek `&`, razlika `-`, nato `sorted(...)` |
| Razred + operatorji | dunder metode vrnejo **nov** objekt |
| Razred + urejanje | `__lt__` (dvonivojska primerjava) ali `key=lambda` s terko |
| Generatorji | `yield`; neskončne omeji z `next`/`range`, NE `list(...)` |
| Sklad | seznam + `.append()` / `.pop()`; vrh je `sklad[-1]` |
| Datoteke | `with open(ime, encoding="utf-8")`; `.strip(string.punctuation)` |
