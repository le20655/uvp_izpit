# UVP – Izpitne naloge (po vzoru poskusnega izpita)

Zbirka **večdelnih izpitnih nalog** s polnimi rešitvami in razlagami.
Prve tri so iz `vaje_podobne_naloge.py` (vzorci *Sprehodi*, *GPS*, *Koda QR*),
ostalih šest je **novih**, a po težavnosti in obliki enakih – predvidevajo,
kaj bi še lahko zahtevali iz iste snovi (regex, OOP z operatorji, slovarji,
matrike, rekurzija nad gnezdenimi strukturami, generatorji/iteratorji).

Vse rešitve so testirane.

**Kazalo**

- [1. Kača na mreži](#1-kača-na-mreži-sprehodi) *(nizi, simulacija, razdalja)*
- [2. Senzor](#2-senzor-gps) *(datoteke, razčlenjevanje, analiza)*
- [3. Plošča](#3-plošča-koda-qr) *(razred, matrika, `__str__`)*
- [4. Ulomek](#4-ulomek-nova) *(razred, operatorji, Evklidov gcd)*
- [5. Dnevnik](#5-dnevnik-nova) *(regularni izrazi)*
- [6. Volitve](#6-volitve-nova) *(slovarji, štetje, urejanje)*
- [7. Minolovec](#7-minolovec-nova) *(matrike, sosedje, rekurzija)*
- [8. Gnezdeni seznami](#8-gnezdeni-seznami-nova) *(rekurzija nad strukturo)*
- [9. Tok podatkov](#9-tok-podatkov-nova) *(generatorji, iterator)*

Uvozi, ki jih naloge uporabljajo:

```python
import os
import re
import math

POT = os.path.join(os.path.dirname(__file__), "meritve.txt")
```

---

## 1. Kača na mreži (*Sprehodi*)

Kača se premika po ravnini s štirimi smermi korakov:
`S` (sever) `(x,y)→(x,y+1)`, `J` (jug) `(x,y)→(x,y-1)`,
`V` (vzhod) `(x,y)→(x+1,y)`, `Z` (zahod) `(x,y)→(x-1,y)`.
Pot je niz, npr. `'SSVVJ'`; vedno začnemo v izhodišču `(0,0)`.

### a) `pot(opis)` – končna točka poti; neveljavne znake ignoriraj.

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

### b) `strnjena_pot(opis)` – pred znakom smeri je lahko število ponovitev. Neveljaven znak zavrže trenutno nabrano število.

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

### c) `najblizja_izhodiscu(seznam)` – iz seznama strnjenih opisov vrne tistega, ki se konča najbliže izhodišču (ob izenačenju prvega).

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

## 2. Senzor (*GPS*)

Senzor v datoteko zapisuje meritve, vsako v svojo vrstico, polja ločena z
vejicami: `cas,temperatura,vlaga`. Primer `meritve.txt`:

```
0,20.0,50.0
60,22.5,48.0
120,21.0,55.0
180,24.0,52.0
240,19.5,60.0
```

### a) `preberi(ime)` – vrne seznam trojic realnih števil.

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

### b) `najtoplejsi(ime)` – čas (prvega) trenutka z najvišjo temperaturo.

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

### c) `analiza(ime)` – vrne `(trajanje, vzpon_temp, padec_temp)`, vse zaokroženo na 2 decimalki: trajanje = zadnji − prvi čas; vzpon = vsota vseh pozitivnih sprememb temperature; padec = vsota vseh padcev (kot pozitivno število).

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

## 3. Plošča (*Koda QR*)

Ploščo predstavimo kot matriko `n × m`.

### a) Konstruktor `Plosca(n, m)`: vsi elementi `None`, shranjeni v atribut `matrika`. Metoda `__str__`: `None`→`'.'`, `0`→`' '` (presledek), `1`→`'*'`; vrstice loči s prelomom.

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

### b) `postavi(vzorec, i, j)`: v matriko z levim zgornjim kotom `(i, j)` vpiše dani vzorec (manjšo matriko).

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

### c) `zapolni(seznam)`: nedoločene (`None`) elemente napolni po vrsticah od leve proti desni, od zgoraj navzdol; ko vrednosti zmanjka, polni z `0`.

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

## 4. Ulomek *(nova)*

Razred `Ulomek` predstavlja ulomek s števcem in imenovalcem. Vedno naj bo
**okrajšan**, predznak pa v števcu (imenovalec vedno pozitiven).

### a) `gcd(a, b)` – največji skupni delitelj, **rekurzivno** (Evklidov algoritem).

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

### b) Konstruktor + `__repr__` (oblike `"st/im"`). Ulomek naj se ob nastanku okrajša; imenovalec 0 sproži `ValueError`.

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

### c) Aritmetika in primerjava: `__add__`, `__mul__`, `__eq__`, `__lt__`.

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

## 5. Dnevnik *(nova)*

Iz besedila (npr. dnevniške vrstice) izluščamo podatke z **regularnimi izrazi**.

### a) `vsa_stevila(besedilo)` – seznam vseh celih števil (kot `int`).

```python
import re

def vsa_stevila(besedilo):
    return [int(x) for x in re.findall(r'\d+', besedilo)]
```

```python
>>> vsa_stevila("soba 12, 7 ljudi, kanal 3")
[12, 7, 3]
```

### b) `emaili(besedilo)` – seznam vseh e-poštnih naslovov.

```python
def emaili(besedilo):
    return re.findall(r'[\w.+-]+@[\w.-]+\.\w+', besedilo)
```

```python
>>> emaili("ana@fri.uni-lj.si in bor@gmail.com")
['ana@fri.uni-lj.si', 'bor@gmail.com']
```

### c) `datumi(besedilo)` – seznam trojic `(dan, mesec, leto)` za vse datume oblike `dd.mm.llll` (uporabi **imenovane skupine**).

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

## 6. Volitve *(nova)*

Glasovi so seznam imen kandidatov (vsak glas je eno ime).

### a) `prestej(glasovi)` – slovar `{kandidat: stevilo_glasov}`.

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

### b) `zmagovalec(glasovi)` – kandidat z največ glasovi; ob izenačenju abecedno prvi.

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

### c) `porazdelitev(glasovi)` – slovar `{kandidat: odstotek}` (na 2 decimalki).

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

## 7. Minolovec *(nova)*

Polje je matrika `0`/`1`, kjer `1` pomeni mino.

### a) `stevilo_min(mine)` – skupno število min.

```python
def stevilo_min(mine):
    return sum(sum(vrstica) for vrstica in mine)
```

```python
>>> stevilo_min([[0, 1, 0], [0, 0, 1]])
2
```

### b) `sosedje(mine)` – nova matrika: na mestu mine je `-1`, sicer število min med **8 sosedi**.

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

### c) `varne_celice(mine)` – seznam koordinat `(i, j)`, ki nimajo mine **in** nobenega soseda z mino (število sosedov je 0).

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

## 8. Gnezdeni seznami *(nova)*

Vrednost je bodisi celo število bodisi (poljubno globoko) gnezden seznam.
Vse tri naloge rešimo **rekurzivno**, robni primer je »ni seznam« (število).

### a) `globina(x)` – največja globina gnezdenja (število `0`, prazni seznam `1`).

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

### b) `vsota(x)` – vsota vseh števil, ne glede na gnezdenje.

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

### c) `splosci(x)` – seznam vseh števil v enem nivoju (flatten).

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

## 9. Tok podatkov *(nova)*

Vaja iz **generatorjev** in **iteratorskega protokola** (`__iter__`/`__next__`).

### a) `okna(seznam, k)` – generator, ki vrača zaporedna drsna okna dolžine `k` (kot terke).

```python
def okna(seznam, k):
    for i in range(len(seznam) - k + 1):
        yield tuple(seznam[i:i + k])
```

```python
>>> list(okna([1, 2, 3, 4], 2))
[(1, 2), (2, 3), (3, 4)]
```

### b) `tekoci_max(seznam)` – generator, ki vrača tekoči (do tega mesta) maksimum.

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

### c) Razred `Krozno(elementi, koraki)` – **iterator**, ki ciklično vrača elemente seznama, skupno `koraki`-krat.

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

## Povzetek pokritosti snovi

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
```

