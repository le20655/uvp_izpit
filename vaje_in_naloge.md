# UVP — vaje in dodatne naloge

Zbirka rešenih vaj in vzorčnih nalog za predmet **Uvod v programiranje**.
Dokument je nastal z združitvijo treh prejšnjih datotek tega repozitorija —
`vaje.md`, `izpitne_naloge_resene.md` in `Resene_naloge.md` — pri čemer je
odstranjena edina podvojena naloga (*pravilno gnezdeni oklepaji*, ki je bila
v dveh datotekah). Izvirne različice so dosegljive v zgodovini repozitorija.

> ⚠️ **Razlika glede na `izpiti_2324.md`:** tam so **pravi izpiti** in rešitve,
> preverjene z vgrajenimi testi Projekta Tomo. Naloge v tem dokumentu so
> **vaje in vzorčne naloge**; rešitve so pregledane, niso pa preverjene z
> uradnimi testi, ker ti zanje ne obstajajo.

**Kazalo**

- [Del A — Vaje po temah](#del-a--vaje-po-temah) — 13 tem, vsaka z dvema različicama naloge
- [Del B — Vzorčne izpitne naloge](#del-b--vzorčne-izpitne-naloge) — 9 samostojnih nalog
- [Del C — Večdelne naloge v obliki izpita](#del-c--večdelne-naloge-v-obliki-izpita) — 9 nalog s po tremi podnalogami

Naloge uporabljajo naslednje uvoze:

```python
import os
import re
import math
import string
```

---

## Del A — Vaje po temah

*Vir: `vaje.md`. Vse naloge iz `vaje_1.py` in `vaje_2.py`, urejene po 13 temah.
Za vsako temo sta dve različici naloge, polna rešitev, razlaga in — kjer je
smiseln — alternativni pristop.*

### 1. Rekurzija nad števkami

#### vaje_1 — `najvecja_stevka(n)`

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

#### vaje_2 — `vsota_stevk(n)`

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

### 2. Rekurzija nad nizi

#### vaje_1 — `razteg(niz)`

> Vrne nov niz, v katerem je vsak znak podvojen. Rekurzivno.

```python
def razteg(niz):
    if niz == "":              # robni primer: prazen niz
        return ""
    return niz[0] * 2 + razteg(niz[1:])
```

**Razlaga** — prvi znak podvojimo (`niz[0] * 2`) in pripnemo razteg preostanka (`niz[1:]`). `"abc"` → `"aa" + "bb" + "cc"`.

#### vaje_2 — `obrni(niz)`

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

### 3. Nizi in štetje

#### vaje_1 — `besede_dolzine(stavek, k)`

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

#### vaje_2 — `besede_z_zacetnico(stavek, c)`

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

### 4. Seznami (izpeljani seznam)

#### vaje_1 — `vsote_sosednjih(seznam)`

> i-ti element rezultata je vsota i-tega in (i+1)-tega elementa. Rezultat je za 1 krajši.

```python
def vsote_sosednjih(seznam):
    return [seznam[i] + seznam[i + 1] for i in range(len(seznam) - 1)]
```

#### vaje_2 — `razlike_sosednjih(seznam)`

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

### 5. Matrike

#### vaje_1 — `je_simetricna(M)`

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

#### vaje_2 — `je_zgornje_trikotna(M)`

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

### 6. Gnezdeni slovarji

#### vaje_1 — `povprecja(zapisi)`

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

#### vaje_2 — `vsote_po_kategorijah(zapisi)`

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

### 7. Množice

#### vaje_1 — `skupni_prijatelji(graf, a, b)`

> `graf` je `oseba -> množica prijateljev`. Vrni **urejen** seznam oseb, ki so prijatelji oboje, `a` in `b`.

```python
def skupni_prijatelji(graf, a, b):
    return sorted(graf[a] & graf[b])
```

**Razlaga** — »prijatelj obeh« = **presek** množic (`&`). `sorted(...)` ga pretvori v urejen seznam.

#### vaje_2 — `samo_pri_prvem(graf, a, b)`

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

### 8. Razred z operatorji

#### vaje_1 — `Vektor`

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

#### vaje_2 — `Kompleksno`

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

### 9. Razred in urejanje

#### vaje_1 — `Knjiga` + `uredi_knjige`

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

#### vaje_2 — `Izdelek` + `uredi_izdelke`

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

### 10. Generator – neskončno zaporedje

#### vaje_1 — `fibonacci()`

> Neskončen generator Fibonaccijevih števil: `0, 1, 1, 2, 3, 5, 8, ...`

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

**Razlaga** — `yield` vrne trenutno vrednost in **zamrzne** stanje do naslednjega `next()`. `a, b = b, a + b` je hkratno prirejanje (desna stran se izračuna iz starih vrednosti).

#### vaje_2 — `trikotniska()`

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

### 11. Generator – zlivanje

#### vaje_1 — `izmenicno(a, b)`

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

#### vaje_2 — `zlij_urejeno(a, b)`

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

### 12. Sklad

#### vaje_1 — `pravilno_gnezdeni(niz)`

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

#### vaje_2 — `odstrani_pare(niz)`

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

### 13. Datoteke

> Obe nalogi delata z datoteko `besedilo.txt` v isti mapi (pot v `POT`).

#### vaje_1 — `stevilo_besed(ime)` in `najdaljsa_vrstica(ime)`

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

#### vaje_2 — `stevilo_vrstic(ime)` in `pojavitve(ime, beseda)`

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

### Hitri povzetek vzorcev

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

---

## Del B — Vzorčne izpitne naloge

*Vir: `izpitne_naloge_resene.md`. Samostojne naloge v slogu pisnih izpitov,
razvrščene od lažjih proti težjim. Deseta naloga izvirnika (pravilno gnezdeni
oklepaji) je izpuščena — ista naloga je že v [Del A, tema 12](#12-sklad).*

### 1. Najdaljša naraščajoča podveriga

> 📚 **Teme:** seznami, zanke, sledenje stanju

Sestavi funkcijo `najdaljsa_narascajoca(sez)`, ki sprejme seznam števil in vrne **dolžino** najdaljšega zaporedja zaporednih elementov, ki je **strogo naraščajoče**.

```python
>>> najdaljsa_narascajoca([1, 2, 3, 1, 2])
3
>>> najdaljsa_narascajoca([5, 4, 3, 2, 1])
1
>>> najdaljsa_narascajoca([1, 2, 2, 3, 4])
3
>>> najdaljsa_narascajoca([])
0
```

#### 💡 Pristop

Drsimo skozi seznam in vzdržujemo dolžino **trenutne** naraščajoče podverige. Ko se ta prekine (`sez[i] <= sez[i-1]`), si shranimo maksimum in začnemo znova z dolžino 1.

#### ✅ Rešitev

```python
def najdaljsa_narascajoca(sez):
    if not sez:
        return 0
    najboljsa = trenutna = 1
    for i in range(1, len(sez)):
        if sez[i] > sez[i - 1]:
            trenutna += 1
        else:
            trenutna = 1
        if trenutna > najboljsa:
            najboljsa = trenutna
    return najboljsa
```

---

### 2. Cezarjeva šifra

> 📚 **Teme:** nizi, `ord`/`chr`, modularna aritmetika

Cezarjeva šifra premakne vsako črko za `k` mest v abecedi (samo angleška abeceda). Velike črke ostanejo velike, male male, ostali znaki ostanejo nespremenjeni.

Sestavi funkcijo `cezar(niz, k)`.

```python
>>> cezar('ABC', 1)
'BCD'
>>> cezar('xyz', 3)
'abc'
>>> cezar('Hello, World!', 13)
'Uryyb, Jbeyq!'
>>> cezar('Uryyb, Jbeyq!', -13)
'Hello, World!'
```

#### 💡 Pristop

Za vsak znak uporabimo `ord`/`chr`. Velike `A`-`Z` imajo kode 65–90, male `a`-`z` imajo 97–122. Premik delamo **po modulu 26**, da deluje tudi pri negativnih in velikih `k`.

#### ✅ Rešitev

```python
def cezar(niz, k):
    rezultat = []
    for znak in niz:
        if 'A' <= znak <= 'Z':
            rezultat.append(chr((ord(znak) - ord('A') + k) % 26 + ord('A')))
        elif 'a' <= znak <= 'z':
            rezultat.append(chr((ord(znak) - ord('a') + k) % 26 + ord('a')))
        else:
            rezultat.append(znak)
    return ''.join(rezultat)
```

---

### 3. Najpogostejše besede

> 📚 **Teme:** slovarji, regularni izrazi, urejanje po dveh kriterijih

Sestavi funkcijo `najpogostejse(besedilo, n)`, ki vrne seznam `n` najpogosteje pojavljajočih se besed v besedilu, **urejen padajoče** po številu pojavitev. Pri **enakem** številu pojavitev naj bo prej tista, ki je **leksikografsko manjša**. Beseda je zaporedje črk. Ne razlikuj med velikimi in malimi črkami.

```python
>>> najpogostejse('Ena dva tri ena DVA ena', 2)
['ena', 'dva']
>>> najpogostejse('Pes maček pes maček miš', 3)
['maček', 'pes', 'miš']
```

#### 💡 Pristop

1. Z regularnim izrazom izluščimo besede.
2. V slovar shranimo števec za vsako besedo (z `.get`).
3. Pare uredimo s ključem `(-pojavitve, beseda)` — minus za **padajoče** po pojavitvah, beseda za leksikografsko ureditev pri izenačenju.

#### ✅ Rešitev

```python
import re

def najpogostejse(besedilo, n):
    # [^\W\d_]+ ujame samo črke (vključno s šumniki), brez števk in podčrtaja
    besede = re.findall(r"[^\W\d_]+", besedilo.lower(), flags=re.UNICODE)
    stevec = {}
    for b in besede:
        stevec[b] = stevec.get(b, 0) + 1
    urejene = sorted(stevec.items(), key=lambda par: (-par[1], par[0]))
    return [par[0] for par in urejene[:n]]
```

> 💭 Z `collections.Counter` bi bilo še krajše:
> ```python
> from collections import Counter
> stevec = Counter(besede)
> ```

---

### 4. Točke v območju

> 📚 **Teme:** izpeljane množice, evklidska razdalja

Definirajmo razdaljo med točkama v ravnini kot evklidsko: $\sqrt{(dx)^2 + (dy)^2}$. Sestavi funkcijo `tocke_v_obmocju(tocke, sredisce, r)`, ki vrne **množico** vseh točk iz seznama `tocke`, ki ležijo **znotraj kroga** (vključno z mejo) s središčem `sredisce` in polmerom `r`.

```python
>>> sorted(tocke_v_obmocju([(0,0), (1,1), (3,4)], (0,0), 2))
[(0, 0), (1, 1)]
>>> sorted(tocke_v_obmocju([(0,0), (3,4), (6,8)], (0,0), 5))
[(0, 0), (3, 4)]
```

#### 💡 Pristop

Izpeljana množica + Pitagorov izrek. **Kvadriramo**, da se izognemo `sqrt`-u (in s tem nenatančnostim s floati): primerjamo $dx^2 + dy^2 \leq r^2$.

#### ✅ Rešitev

```python
def tocke_v_obmocju(tocke, sredisce, r):
    sx, sy = sredisce
    return {(x, y) for (x, y) in tocke if (x - sx) ** 2 + (y - sy) ** 2 <= r * r}
```

---

### 5. Preverjanje EMŠO

> 📚 **Teme:** kontrolne števke, modularna aritmetika, validacija vhoda

EMŠO ima 13 števk $d_1 \ldots d_{13}$. Kontrolna števka $d_{13}$ se izračuna takole:

1. Uteži za $d_1 \ldots d_{12}$ so `7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2`.
2. Izračunaj $S = \sum_{i=1}^{12} d_i \cdot \text{utež}_i$.
3. $r = S \bmod 11$.
4. Če je $r = 0$, je $d_{13} = 0$; če je $r = 1$, EMŠO **ni veljaven**; sicer je $d_{13} = 11 - r$.

Sestavi funkcijo `veljaven_emso(niz)`, ki vrne `True` natanko, kadar je niz dolg 13 in zadošča zgornjemu pravilu.

```python
>>> veljaven_emso('0101006500006')
True
>>> veljaven_emso('0101006500007')
False
>>> veljaven_emso('123')
False
>>> veljaven_emso('010100650000a')
False
```

#### 💡 Pristop

Najprej preverimo dolžino in da so vse znake števke (`str.isdigit`). Nato izračunamo kontrolno števko po formuli.

#### ✅ Rešitev

```python
def veljaven_emso(niz):
    if len(niz) != 13 or not niz.isdigit():
        return False
    utezi = [7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    vsota = sum(int(niz[i]) * utezi[i] for i in range(12))
    r = vsota % 11
    if r == 0:
        kontrolna = 0
    elif r == 1:
        return False
    else:
        kontrolna = 11 - r
    return int(niz[12]) == kontrolna
```

---

### 6. Sestavljanje zneska s kovanci

> 📚 **Teme:** dinamično programiranje, "coin change"

Imamo nabor kovancev (npr. `[1, 2, 5, 10, 20, 50]`) in znesek. Sestavi funkcijo `nacini(znesek, kovanci)`, ki vrne, na koliko **različnih** načinov lahko sestavimo znesek z neomejeno količino vsakega tipa kovanca. **Vrstni red kovancev v skupini ni pomemben** — `[1, 2, 2]` in `[2, 1, 2]` sta isto.

```python
>>> nacini(5, [1, 2, 5])
4
>>> nacini(0, [1, 2, 5])
1
>>> nacini(3, [2])
0
>>> nacini(10, [1, 5, 10])
4
```

#### 💡 Pristop

Klasičen primer **dinamičnega programiranja**. Definiramo `dp[z]` = število načinov, da sestavimo znesek `z`. Za vsak kovanec posodobimo vse zneske od kovanca naprej. **Zunanja zanka po kovancih** (in ne po zneskih) zagotavlja, da ne štejemo iste kombinacije v različnih vrstnih redih.

#### ✅ Rešitev

```python
def nacini(znesek, kovanci):
    dp = [0] * (znesek + 1)
    dp[0] = 1  # prazen znesek lahko sestavimo na 1 način
    for k in kovanci:
        for z in range(k, znesek + 1):
            dp[z] += dp[z - k]
    return dp[znesek]
```

> 💭 Za `znesek = 5, kovanci = [1, 2, 5]` so štirje načini:
> `5×1`, `1+1+1+2`, `1+2+2`, `5`.

---

### 7. Branje datoteke z ocenami

> 📚 **Teme:** delo z datotekami, `setdefault`, robustno parsiranje

Datoteka `ocene.txt` vsebuje vrstice oblike:

```
ime_studenta;predmet;ocena
```

kjer je ocena celo število med 5 in 10. Sestavi funkcijo `povprecja_studentov(ime_datoteke)`, ki vrne slovar, katerega ključi so imena študentov, vrednosti pa povprečje vseh njihovih ocen (zaokroženo na **2 decimalki**). Prazne vrstice in vrstice z napačnim formatom ignoriraj.

**Primer vsebine:**

```
Ana;Analiza;10
Bine;Analiza;7
Ana;Algebra;9
Bine;Algebra;8
```

**Rezultat:** `{'Ana': 9.5, 'Bine': 7.5}`

#### 💡 Pristop

1. Beremo po vrsticah z `with open(...)`.
2. Vsako vrstico `.strip()`-amo in razdelimo na 3 dele s `.split(';')`.
3. Za vsakega študenta zbiramo seznam ocen v slovar z `.setdefault(ime, []).append(ocena)`.
4. Na koncu izračunamo povprečja z izpeljanim slovarjem.

Napačne vrstice (premalo polj, ocena ni število) preprosto preskočimo s `continue`.

#### ✅ Rešitev

```python
def povprecja_studentov(ime_datoteke):
    ocene = {}
    with open(ime_datoteke, encoding='UTF-8') as dat:
        for vrstica in dat:
            deli = vrstica.strip().split(';')
            if len(deli) != 3:
                continue
            ime, _, ocena_niz = deli
            try:
                ocena = int(ocena_niz)
            except ValueError:
                continue
            ocene.setdefault(ime, []).append(ocena)
    return {ime: round(sum(o) / len(o), 2) for ime, o in ocene.items()}
```

---

### 8. Razred `Polinom`

> 📚 **Teme:** razredi, posebne metode (`__init__`, `__call__`, `__add__`, `__eq__`, `__repr__`)

Sestavi razred `Polinom`, ki predstavlja polinom z realnimi koeficienti. Polinom inicializiramo s seznamom koeficientov **od najnižje stopnje navzgor**. Tako je `Polinom([1, 2, 3])` polinom $3x^2 + 2x + 1$.

Implementiraj:

| Metoda | Pomen |
|--------|-------|
| `__init__(self, koeficienti)` | shrani koeficiente in odstrani odvečne ničle z višje stopnje |
| `stopnja(self)` | vrne stopnjo polinoma (`-1` za ničelni polinom) |
| `__call__(self, x)` | izračuna $p(x)$ (uporabi Hornerjevo shemo) |
| `__add__(self, drugi)` | sešteje dva polinoma in vrne nov `Polinom` |
| `__eq__(self, drugi)` | primerja po koeficientih |
| `__repr__(self)` | npr. `'Polinom([1, 2, 3])'` |

```python
>>> p = Polinom([1, 2, 3])
>>> p.stopnja()
2
>>> p(2)
17
>>> q = Polinom([0, 1])
>>> (p + q).koeficienti
[1, 3, 3]
>>> Polinom([0, 0, 0]).stopnja()
-1
```

#### 💡 Pristop

- **Normalizacija:** v `__init__` odrežemo ničle z konca seznama, tako da je `Polinom([1, 2, 0])` po notranjosti enak `Polinom([1, 2])`.
- **Hornerjeva shema** za vrednotenje: $((a_n x + a_{n-1})x + \ldots)x + a_0$ — $n$ množenj namesto kvadratnega števila.
- **Seštevanje:** zlijemo koeficiente, manjkajoče tretiramo kot 0.

#### ✅ Rešitev

```python
class Polinom:
    def __init__(self, koeficienti):
        # Odstrani odvečne ničle z višjih stopenj
        kof = list(koeficienti)
        while kof and kof[-1] == 0:
            kof.pop()
        self.koeficienti = kof

    def stopnja(self):
        # Ničelni polinom ima stopnjo -1 (po dogovoru).
        return len(self.koeficienti) - 1

    def __call__(self, x):
        # Hornerjeva shema
        rezultat = 0
        for k in reversed(self.koeficienti):
            rezultat = rezultat * x + k
        return rezultat

    def __add__(self, drugi):
        dolzina = max(len(self.koeficienti), len(drugi.koeficienti))
        novi = []
        for i in range(dolzina):
            a = self.koeficienti[i] if i < len(self.koeficienti) else 0
            b = drugi.koeficienti[i] if i < len(drugi.koeficienti) else 0
            novi.append(a + b)
        return Polinom(novi)

    def __eq__(self, drugi):
        return self.koeficienti == drugi.koeficienti

    def __repr__(self):
        return f'Polinom({self.koeficienti})'
```

---

### 9. Generator praštevil

> 📚 **Teme:** generatorji, `yield`, inkrementalno sito

Sestavi **generator** `prastevila()`, ki rodi vsa praštevila po vrsti (`2, 3, 5, 7, 11, ...`). Generator je neskončen.

Nato napiši še:
- `prvih_n_prastevil(n)` — vrne seznam prvih `n` praštevil,
- `pod(meja)` — vrne seznam vseh praštevil, **strogo manjših** od `meja`.

```python
>>> prvih_n_prastevil(5)
[2, 3, 5, 7, 11]
>>> pod(20)
[2, 3, 5, 7, 11, 13, 17, 19]
```

#### 💡 Pristop

Za vsako število `n` od 2 navzgor preverimo z deljenjem **samo z že najdenimi praštevili** do $\sqrt{n}$. Tako se izognemo testu z vsemi števili in delamo tako rekoč inkrementalno **Eratostenovo sito**.

Trik z `p * p > n` se izogne klicu `math.sqrt`.

#### ✅ Rešitev

```python
def prastevila():
    najdena = []
    n = 2
    while True:
        je_prastevilo = True
        for p in najdena:
            if p * p > n:
                break
            if n % p == 0:
                je_prastevilo = False
                break
        if je_prastevilo:
            najdena.append(n)
            yield n
        n += 1


def prvih_n_prastevil(n):
    gen = prastevila()
    return [next(gen) for _ in range(n)]


def pod(meja):
    rezultat = []
    for p in prastevila():
        if p >= meja:
            return rezultat
        rezultat.append(p)
```

> 💭 Pri `pod` izkoriščamo, da je generator **leniven** — zanka se ustavi takoj, ko praštevilo prvič preseže mejo. Brez generatorja bi morali vnaprej določiti zgornjo mejo.

---

---

## Del C — Večdelne naloge v obliki izpita

*Vir: `Resene_naloge.md`. Naloge s po treh podnalogah, kot na pravem izpitu.
Prve tri so po vzoru poskusnega izpita 2526 (Sprehodi, GPS, Koda QR) — ko bodo
ti izpiti rešeni in preverjeni s Tomovimi testi, bodo prešli v `izpiti_2324.md`
oz. njegovo nadaljevanje.*

### 1. Kača na mreži (*Sprehodi*)

Kača se premika po ravnini s štirimi smermi korakov:
`S` (sever) `(x,y)→(x,y+1)`, `J` (jug) `(x,y)→(x,y-1)`,
`V` (vzhod) `(x,y)→(x+1,y)`, `Z` (zahod) `(x,y)→(x-1,y)`.
Pot je niz, npr. `'SSVVJ'`; vedno začnemo v izhodišču `(0,0)`.

#### a) `pot(opis)` – končna točka poti; neveljavne znake ignoriraj.

```python
def pot(opis):
    x = y = 0
    for a in opis:
        if a == 'S': y += 1
        if a == 'J': y -= 1
        if a == 'V': x += 1
        if a == 'Z': x -= 1
    return (x, y)
```

```python
>>> pot('SSVVJ?VV')
(4, 1)
```

#### b) `strnjena_pot(opis)` – pred znakom smeri je lahko število ponovitev. Neveljaven znak zavrže trenutno nabrano število.

```python
def strnjena_pot(opis):
    x = y = 0
    num = 0          # nabrano število
    smer = None      # še neizvedena smer

    def premakni(s, k):
        nonlocal x, y
        if s == 'S': y += k
        elif s == 'J': y -= k
        elif s == 'V': x += k
        elif s == 'Z': x -= k

    for a in opis:
        if a.isdigit():
            if smer is not None:                 # nova skupina → izvedi prejšnjo smer
                premakni(smer, num if num > 0 else 1)
                smer, num = None, 0
            num = num * 10 + int(a)
        elif a in 'SJVZ':
            if smer is not None:
                premakni(smer, num if num > 0 else 1)
                num = 0
            smer = a                             # smer zadržimo (lahko jo zavrže neveljaven znak)
        else:
            num = 0                              # neveljaven znak zavrže število

    if smer is not None:
        premakni(smer, num if num > 0 else 1)
    return (x, y)
```

```python
>>> strnjena_pot('3S2V')      # 3× sever, 2× vzhod
(2, 3)
>>> strnjena_pot('10V5Z')
(5, 0)
>>> strnjena_pot('2S@3V')     # '@' pobriše število 2 pred S
(3, 1)
```

**Razlaga** – korak izvedemo **z zamikom**: ko preberemo smer, je ne izvedemo takoj, ampak jo skupaj z njenim številom zadržimo. Premik naredimo šele ob naslednjem številu/smeri/koncu niza. Tako lahko neveljaven znak izniči število, **preden** je uporabljeno (zato `'2S@3V'` da `(3,1)`).

#### c) `najblizja_izhodiscu(seznam)` – iz seznama strnjenih opisov vrne tistega, ki se konča najbliže izhodišču (ob izenačenju prvega).

```python
def najblizja_izhodiscu(seznam):
    najblizja = seznam[0]
    x, y = strnjena_pot(seznam[0])
    min_d = x ** 2 + y ** 2
    for opis in seznam[1:]:
        x, y = strnjena_pot(opis)
        d = x ** 2 + y ** 2
        if d < min_d:
            min_d = d
            najblizja = opis
    return najblizja
```

```python
>>> najblizja_izhodiscu(['3S2V', '1S1J', 'V'])
'1S1J'
```

**Razlaga** – razdaljo do izhodišča merimo z `x² + y²`. **Kvadrata korena ni treba računati** – za primerjanje, kateri je bližje, zadošča kvadrat razdalje (manjši kvadrat = manjša razdalja). Strogi `<` ohrani prvega ob izenačenju.

---

### 2. Senzor (*GPS*)

Senzor v datoteko zapisuje meritve, vsako v svojo vrstico, polja ločena z
vejicami: `cas,temperatura,vlaga`. Primer `meritve.txt`:

```
0,20.0,50.0
60,22.5,48.0
120,21.0,55.0
180,24.0,52.0
240,19.5,60.0
```

#### a) `preberi(ime)` – vrne seznam trojic realnih števil.

```python
def preberi(ime):
    rez = []
    with open(ime, encoding="utf-8") as d:
        for vrstica in d:
            vrstica = vrstica.strip()
            if vrstica:
                rez.append(tuple(float(x) for x in vrstica.split(",")))
    return rez
```

```python
>>> preberi("meritve.txt")[0]
(0.0, 20.0, 50.0)
```

#### b) `najtoplejsi(ime)` – čas (prvega) trenutka z najvišjo temperaturo.

```python
def najtoplejsi(ime):
    meritve = preberi(ime)
    najcas, najtemp = meritve[0][0], meritve[0][1]
    for cas, temp, vlaga in meritve:
        if temp > najtemp:
            najtemp = temp
            najcas = cas
    return najcas
```

```python
>>> najtoplejsi("meritve.txt")
180.0
```

**Alternativa s `max` in `key`:**

```python
def najtoplejsi(ime):
    return max(preberi(ime), key=lambda m: m[1])[0]
```

> `max(..., key=lambda m: m[1])` poišče meritev z največjo temperaturo; `[0]` vzame njen čas. Ob izenačenju `max` vrne **prvega**, kar ustreza zahtevi.

#### c) `analiza(ime)` – vrne `(trajanje, vzpon_temp, padec_temp)`, vse zaokroženo na 2 decimalki: trajanje = zadnji − prvi čas; vzpon = vsota vseh pozitivnih sprememb temperature; padec = vsota vseh padcev (kot pozitivno število).

```python
def analiza(ime):
    meritve = preberi(ime)
    trajanje = meritve[-1][0] - meritve[0][0]
    vzpon = padec = 0
    for prej, zdaj in zip(meritve, meritve[1:]):
        razlika = zdaj[1] - prej[1]          # sprememba temperature
        if razlika > 0:
            vzpon += razlika
        else:
            padec += -razlika                # padec kot pozitivno število
    return (round(trajanje, 2), round(vzpon, 2), round(padec, 2))
```

```python
>>> analiza("meritve.txt")
(240.0, 5.5, 6.0)
```

**Razlaga** – `zip(meritve, meritve[1:])` parno združi vsako meritev z naslednjo, da gledamo **zaporedne razlike**. Vsoto pozitivnih in (negiranih) negativnih sprememb ločimo z `if razlika > 0`.

---

### 3. Plošča (*Koda QR*)

Ploščo predstavimo kot matriko `n × m`.

#### a) Konstruktor `Plosca(n, m)`: vsi elementi `None`, shranjeni v atribut `matrika`. Metoda `__str__`: `None`→`'.'`, `0`→`' '` (presledek), `1`→`'*'`; vrstice loči s prelomom.

```python
class Plosca:
    def __init__(self, n, m):
        self.matrika = [[None] * m for _ in range(n)]

    def __str__(self):
        vrstice = []
        for vrstica in self.matrika:
            niz = ""
            for el in vrstica:
                if el is None:
                    niz += "."
                elif el == 0:
                    niz += " "
                else:
                    niz += "*"
            vrstice.append(niz)
        return "\n".join(vrstice)
```

```python
>>> p = Plosca(2, 3)
>>> p.matrika
[[None, None, None], [None, None, None]]
```

> ⚠️ **Past:** `[[None] * m] * n` ustvari `n` **sklicev na isto vrstico** – sprememba enega elementa spremeni cel stolpec. Zato uporabimo `[[None] * m for _ in range(n)]` (vsaka vrstica svoja).

#### b) `postavi(vzorec, i, j)`: v matriko z levim zgornjim kotom `(i, j)` vpiše dani vzorec (manjšo matriko).

```python
    def postavi(self, vzorec, i, j):
        for di in range(len(vzorec)):
            for dj in range(len(vzorec[di])):
                self.matrika[i + di][j + dj] = vzorec[di][dj]
```

```python
>>> p.postavi([[1, 0]], 0, 1)
>>> p.matrika
[[None, 1, 0], [None, None, None]]
```

#### c) `zapolni(seznam)`: nedoločene (`None`) elemente napolni po vrsticah od leve proti desni, od zgoraj navzdol; ko vrednosti zmanjka, polni z `0`.

```python
    def zapolni(self, seznam):
        k = 0
        for vr in range(len(self.matrika)):
            for st in range(len(self.matrika[vr])):
                if self.matrika[vr][st] is None:
                    if k < len(seznam):
                        self.matrika[vr][st] = seznam[k]
                        k += 1
                    else:
                        self.matrika[vr][st] = 0
```

```python
>>> p.zapolni([1, 1, 0, 1])
>>> p.matrika
[[1, 1, 0], [1, 0, 1]]
>>> print(p)
**
* *
```

**Razlaga** – števec `k` kaže na naslednjo neporabljeno vrednost iz seznama. Polnimo **le** mesta z `None` (že postavljen vzorec ostane). Ko `k` doseže `len(seznam)`, preostanek zapolnimo z `0`.

---

### 4. Ulomek *(nova)*

Razred `Ulomek` predstavlja ulomek s števcem in imenovalcem. Vedno naj bo
**okrajšan**, predznak pa v števcu (imenovalec vedno pozitiven).

#### a) `gcd(a, b)` – največji skupni delitelj, **rekurzivno** (Evklidov algoritem).

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

```python
>>> gcd(12, 8)
4
```

**Razlaga** – Evklid: `gcd(a, b) = gcd(b, a % b)`, dokler `b` ni 0. `gcd(12,8)→gcd(8,4)→gcd(4,0)→4`.

#### b) Konstruktor + `__repr__` (oblike `"st/im"`). Ulomek naj se ob nastanku okrajša; imenovalec 0 sproži `ValueError`.

```python
class Ulomek:
    def __init__(self, st, im):
        if im == 0:
            raise ValueError("imenovalec ne sme biti 0")
        if im < 0:                      # predznak vedno v števcu
            st, im = -st, -im
        d = gcd(abs(st), im)
        self.st = st // d
        self.im = im // d

    def __repr__(self):
        return f"{self.st}/{self.im}"
```

```python
>>> Ulomek(2, 4)
1/2
>>> Ulomek(3, -4)
-3/4
```

**Razlaga** – okrajšamo z deljenjem obeh delov z `gcd`. Predznak normaliziramo: če je imenovalec negativen, obrnemo predznak obema, da je `-3/4` namesto `3/-4`. `raise ValueError(...)` zavrne neveljaven ulomek (snov: izjeme).

#### c) Aritmetika in primerjava: `__add__`, `__mul__`, `__eq__`, `__lt__`.

```python
    def __add__(self, other):
        return Ulomek(self.st * other.im + other.st * self.im,
                      self.im * other.im)

    def __mul__(self, other):
        return Ulomek(self.st * other.st, self.im * other.im)

    def __eq__(self, other):
        return self.st == other.st and self.im == other.im

    def __lt__(self, other):
        return self.st * other.im < other.st * self.im
```

```python
>>> Ulomek(1, 2) + Ulomek(1, 3)
5/6
>>> Ulomek(2, 3) * Ulomek(3, 4)
1/2
>>> Ulomek(1, 2) == Ulomek(2, 4)
True
>>> Ulomek(1, 3) < Ulomek(1, 2)
True
```

**Razlaga**
- **Seštevanje:** `a/b + c/d = (a·d + c·b) / (b·d)`; rezultat se v konstruktorju samodejno okrajša.
- **Množenje:** `a/b · c/d = (a·c)/(b·d)`.
- **Enakost** je preprosta, ker sta oba ulomka že okrajšana (`1/2 == 2/4`, ker se `2/4` okrajša na `1/2`).
- **Primerjava** brez deljenja: `a/b < c/d` ⇔ `a·d < c·b` (velja, ker so imenovalci pozitivni – sicer bi se neenakost obrnila).

---

### 5. Dnevnik *(nova)*

Iz besedila (npr. dnevniške vrstice) izluščamo podatke z **regularnimi izrazi**.

#### a) `vsa_stevila(besedilo)` – seznam vseh celih števil (kot `int`).

```python
import re

def vsa_stevila(besedilo):
    return [int(x) for x in re.findall(r'\d+', besedilo)]
```

```python
>>> vsa_stevila("soba 12, 7 ljudi, kanal 3")
[12, 7, 3]
```

#### b) `emaili(besedilo)` – seznam vseh e-poštnih naslovov.

```python
def emaili(besedilo):
    return re.findall(r'[\w.+-]+@[\w.-]+\.\w+', besedilo)
```

```python
>>> emaili("ana@fri.uni-lj.si in bor@gmail.com")
['ana@fri.uni-lj.si', 'bor@gmail.com']
```

#### c) `datumi(besedilo)` – seznam trojic `(dan, mesec, leto)` za vse datume oblike `dd.mm.llll` (uporabi **imenovane skupine**).

```python
def datumi(besedilo):
    rez = []
    for m in re.finditer(r'(?P<d>\d{1,2})\.(?P<m>\d{1,2})\.(?P<l>\d{4})', besedilo):
        rez.append((int(m['d']), int(m['m']), int(m['l'])))
    return rez
```

```python
>>> datumi("Sestanek 12.03.2024 in 1.1.2025")
[(12, 3, 2024), (1, 1, 2025)]
```

**Razlaga**
- `\d+` = eno ali več števk; `re.findall` vrne **vse** ujemajoče se podnize.
- E-pošta: `[\w.+-]+` (uporabniško ime) `@` `[\w.-]+` (domena) `\.\w+` (končnica). `\w` so črke, števke in `_`.
- `(?P<ime>...)` je **imenovana skupina**; do nje dostopamo z `m['ime']` (ali `m.group('ime')`). `re.finditer` vrne objekte `Match` (za razliko od `findall`, ki vrne nize).

> Razširitve te snovi: `re.search` (prvo ujemanje), `re.sub` (zamenjava), kvantifikatorji `* + ? {m,n}`, razredi `[...]`, sidri `^ $`.

---

### 6. Volitve *(nova)*

Glasovi so seznam imen kandidatov (vsak glas je eno ime).

#### a) `prestej(glasovi)` – slovar `{kandidat: stevilo_glasov}`.

```python
def prestej(glasovi):
    rez = {}
    for g in glasovi:
        rez[g] = rez.get(g, 0) + 1
    return rez
```

```python
>>> prestej(["ana", "bor", "ana", "cene", "bor", "ana"])
{'ana': 3, 'bor': 2, 'cene': 1}
```

**Alternativa:** `from collections import Counter; dict(Counter(glasovi))`.

#### b) `zmagovalec(glasovi)` – kandidat z največ glasovi; ob izenačenju abecedno prvi.

```python
def zmagovalec(glasovi):
    st = prestej(glasovi)
    najvec = max(st.values())
    return sorted(k for k, v in st.items() if v == najvec)[0]
```

```python
>>> zmagovalec(["ana", "bor", "ana", "cene", "bor", "ana"])
'ana'
>>> zmagovalec(["a", "b", "a", "b"])     # izenačenje → abecedno prvi
'a'
```

**Razlaga** – najprej poiščemo največje **število** glasov (`max(st.values())`), nato med vsemi kandidati s tem številom vzamemo abecedno prvega (`sorted(...)[0]`). Naivni `max(st, key=st.get)` bi pri izenačenju vrnil naključnega (odvisno od vrstnega reda), zato eksplicitno razbijemo izenačenje.

#### c) `porazdelitev(glasovi)` – slovar `{kandidat: odstotek}` (na 2 decimalki).

```python
def porazdelitev(glasovi):
    st = prestej(glasovi)
    n = len(glasovi)
    return {k: round(100 * v / n, 2) for k, v in st.items()}
```

```python
>>> porazdelitev(["ana", "bor", "ana", "cene", "bor", "ana"])
{'ana': 50.0, 'bor': 33.33, 'cene': 16.67}
```

**Razlaga** – slovarska izpeljava (*dict comprehension*) preslika vsako število glasov v odstotek `100 · v / n`, zaokrožen na 2 decimalki.

---

### 7. Minolovec *(nova)*

Polje je matrika `0`/`1`, kjer `1` pomeni mino.

#### a) `stevilo_min(mine)` – skupno število min.

```python
def stevilo_min(mine):
    return sum(sum(vrstica) for vrstica in mine)
```

```python
>>> stevilo_min([[0, 1, 0], [0, 0, 1]])
2
```

#### b) `sosedje(mine)` – nova matrika: na mestu mine je `-1`, sicer število min med **8 sosedi**.

```python
def sosedje(mine):
    n, m = len(mine), len(mine[0])
    rez = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mine[i][j] == 1:
                rez[i][j] = -1
            else:
                c = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if (di, dj) != (0, 0):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m and mine[ni][nj] == 1:
                                c += 1
                rez[i][j] = c
    return rez
```

```python
>>> sosedje([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
[[1, 1, 1], [1, -1, 1], [1, 1, 1]]
>>> sosedje([[1, 0], [0, 0]])
[[-1, 1], [1, 1]]
```

**Razlaga**
- 8 sosedov dobimo z dvema zankama `di, dj ∈ {-1, 0, 1}`, pri čemer **izpustimo** `(0,0)` (to je celica sama).
- **Preverjanje robov** `0 <= ni < n and 0 <= nj < m` prepreči, da bi pogledali izven matrike (sicer `IndexError` ali napačno ovijanje z negativnim indeksom).

#### c) `varne_celice(mine)` – seznam koordinat `(i, j)`, ki nimajo mine **in** nobenega soseda z mino (število sosedov je 0).

```python
def varne_celice(mine):
    s = sosedje(mine)
    return [(i, j)
            for i in range(len(s))
            for j in range(len(s[0]))
            if s[i][j] == 0]
```

```python
>>> varne_celice([[1, 0, 0], [0, 0, 0]])
[(0, 2), (1, 2)]
```

**Razlaga** – ponovno uporabimo `sosedje`; celica je varna, če je njena vrednost natanko `0` (`-1` so mine, `>0` mejijo na mino).

> Sorodne matrične naloge iste snovi: transponiranje `list(zip(*M))`, rotacija matrike, korak Igre življenja – vse temeljijo na enaki shemi sprehoda po sosedih.

---

### 8. Gnezdeni seznami *(nova)*

Vrednost je bodisi celo število bodisi (poljubno globoko) gnezden seznam.
Vse tri naloge rešimo **rekurzivno**, robni primer je »ni seznam« (število).

#### a) `globina(x)` – največja globina gnezdenja (število `0`, prazni seznam `1`).

```python
def globina(x):
    if not isinstance(x, list):
        return 0
    if not x:                       # prazen seznam
        return 1
    return 1 + max(globina(e) for e in x)
```

```python
>>> globina(7)
0
>>> globina([1, [2, [3]]])
3
```

#### b) `vsota(x)` – vsota vseh števil, ne glede na gnezdenje.

```python
def vsota(x):
    if isinstance(x, list):
        return sum(vsota(e) for e in x)
    return x                        # robni primer: število je samo svoja vsota
```

```python
>>> vsota([1, [2, [3, 4]], 5])
15
```

#### c) `splosci(x)` – seznam vseh števil v enem nivoju (flatten).

```python
def splosci(x):
    if not isinstance(x, list):
        return [x]
    rez = []
    for e in x:
        rez.extend(splosci(e))      # razširi z elementi podseznama
    return rez
```

```python
>>> splosci([1, [2, [3]], 4])
[1, 2, 3, 4]
```

**Razlaga**
- `isinstance(x, list)` loči seznam od števila – to je **ključ** rekurzije nad heterogeno strukturo.
- Pri `vsota` in `globina` se rekurzija razveja na vsak element seznama (`for e in x`).
- Pri `splosci` uporabimo `.extend(...)` (ne `.append`), da podseznam **razgrnemo** v posamezne elemente, ne dodamo kot vgnezdeni seznam.

---

### 9. Tok podatkov *(nova)*

Vaja iz **generatorjev** in **iteratorskega protokola** (`__iter__`/`__next__`).

#### a) `okna(seznam, k)` – generator, ki vrača zaporedna drsna okna dolžine `k` (kot terke).

```python
def okna(seznam, k):
    for i in range(len(seznam) - k + 1):
        yield tuple(seznam[i:i + k])
```

```python
>>> list(okna([1, 2, 3, 4], 2))
[(1, 2), (2, 3), (3, 4)]
```

#### b) `tekoci_max(seznam)` – generator, ki vrača tekoči (do tega mesta) maksimum.

```python
def tekoci_max(seznam):
    najv = None
    for x in seznam:
        if najv is None or x > najv:
            najv = x
        yield najv
```

```python
>>> list(tekoci_max([3, 1, 4, 1, 5]))
[3, 3, 4, 4, 5]
```

**Razlaga** – `yield` sproti oddaja vrednosti; stanje (`najv`) se ohranja med klici. Generator je »len« – vrednosti ustvarja na zahtevo, brez vmesnega seznama.

#### c) Razred `Krozno(elementi, koraki)` – **iterator**, ki ciklično vrača elemente seznama, skupno `koraki`-krat.

```python
class Krozno:
    def __init__(self, elementi, koraki):
        self.elementi = elementi
        self.koraki = koraki
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.koraki:
            raise StopIteration
        el = self.elementi[self.i % len(self.elementi)]
        self.i += 1
        return el
```

```python
>>> list(Krozno(["a", "b"], 5))
['a', 'b', 'a', 'b', 'a']
```

**Razlaga (iteratorski protokol)**
- `__iter__` vrne sam iterator (`return self`), zato objekt deluje v `for` zanki in v `list(...)`.
- `__next__` vrne naslednji element ali sproži **`StopIteration`**, ko je konec – to je signal, da se iteracija ustavi.
- Ciklični dostop dosežemo z `self.i % len(self.elementi)` (indeks se »ovije« nazaj na začetek).
- Generator (`a`, `b`) je krajši način za isti protokol – Python iz `yield` samodejno naredi iterator s `__iter__`/`__next__`.

---

### Povzetek pokritosti snovi

| Naloga | Snov |
|--------|------|
| 1 Kača | nizi, znak-po-znak razčlenjevanje, simulacija, `nonlocal`, razdalja brez korena |
| 2 Senzor | datoteke (`with open`), `split`, terke, `zip` za sosednje, `max(key=...)` |
| 3 Plošča | razred, 2D-matrika, `__str__`, past `[[..]*m]*n` |
| 4 Ulomek | razred + operatorji, Evklidov `gcd` (rekurzija), izjeme (`ValueError`) |
| 5 Dnevnik | regex: `findall`/`finditer`, imenovane skupine, vzorci `\d \w` |
| 6 Volitve | slovarji, `get`-štetje / `Counter`, `max`, razbijanje izenačenja, dict comprehension |
| 7 Minolovec | matrike, 8 sosedov, preverjanje robov, ponovna uporaba funkcije |
| 8 Gnezdeni | rekurzija nad strukturo, `isinstance`, `extend` vs `append` |
| 9 Tok | generatorji (`yield`), iterator (`__iter__`/`__next__`/`StopIteration`) |
