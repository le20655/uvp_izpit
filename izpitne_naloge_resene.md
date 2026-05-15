# 🐍 Vzorčne izpitne naloge — Uvod v programiranje

> Zbirka rešenih nalog v slogu pisnih izpitov pri predmetu **Uvod v programiranje** (FMF / FRI, Matija Pretnar). Naloge so razvrščene od lažjih proti težjim in pokrivajo vse glavne teme: nize, sezname, slovarje, množice, datoteke, rekurzijo, razrede in generatorje.
>
> Vsaka naloga vsebuje besedilo, primere uporabe in rešitev s kratko razlago pristopa.

---

## Kazalo

1. [Najdaljša naraščajoča podveriga](#1-najdaljša-naraščajoča-podveriga) — _seznami, zanke_
2. [Cezarjeva šifra](#2-cezarjeva-šifra) — _nizi, ASCII, modularna aritmetika_
3. [Najpogostejše besede](#3-najpogostejše-besede) — _slovarji, regex, urejanje_
4. [Točke v območju](#4-točke-v-območju) — _množice, geometrija_
5. [Preverjanje EMŠO](#5-preverjanje-emšo) — _kontrolne števke_
6. [Sestavljanje zneska s kovanci](#6-sestavljanje-zneska-s-kovanci) — _dinamično programiranje_
7. [Branje datoteke z ocenami](#7-branje-datoteke-z-ocenami) — _datoteke, slovarji_
8. [Razred `Polinom`](#8-razred-polinom) — _razredi, posebne metode_
9. [Generator praštevil](#9-generator-praštevil) — _generatorji, `yield`_
10. [Pravilno gnezdeni oklepaji](#10-pravilno-gnezdeni-oklepaji) — _sklad_

---

## 1. Najdaljša naraščajoča podveriga

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

### 💡 Pristop

Drsimo skozi seznam in vzdržujemo dolžino **trenutne** naraščajoče podverige. Ko se ta prekine (`sez[i] <= sez[i-1]`), si shranimo maksimum in začnemo znova z dolžino 1.

### ✅ Rešitev

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

## 2. Cezarjeva šifra

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

### 💡 Pristop

Za vsak znak uporabimo `ord`/`chr`. Velike `A`-`Z` imajo kode 65–90, male `a`-`z` imajo 97–122. Premik delamo **po modulu 26**, da deluje tudi pri negativnih in velikih `k`.

### ✅ Rešitev

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

## 3. Najpogostejše besede

> 📚 **Teme:** slovarji, regularni izrazi, urejanje po dveh kriterijih

Sestavi funkcijo `najpogostejse(besedilo, n)`, ki vrne seznam `n` najpogosteje pojavljajočih se besed v besedilu, **urejen padajoče** po številu pojavitev. Pri **enakem** številu pojavitev naj bo prej tista, ki je **leksikografsko manjša**. Beseda je zaporedje črk. Ne razlikuj med velikimi in malimi črkami.

```python
>>> najpogostejse('Ena dva tri ena DVA ena', 2)
['ena', 'dva']
>>> najpogostejse('Pes maček pes maček miš', 3)
['maček', 'pes', 'miš']
```

### 💡 Pristop

1. Z regularnim izrazom izluščimo besede.
2. V slovar shranimo števec za vsako besedo (z `.get`).
3. Pare uredimo s ključem `(-pojavitve, beseda)` — minus za **padajoče** po pojavitvah, beseda za leksikografsko ureditev pri izenačenju.

### ✅ Rešitev

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

## 4. Točke v območju

> 📚 **Teme:** izpeljane množice, evklidska razdalja

Definirajmo razdaljo med točkama v ravnini kot evklidsko: $\sqrt{(dx)^2 + (dy)^2}$. Sestavi funkcijo `tocke_v_obmocju(tocke, sredisce, r)`, ki vrne **množico** vseh točk iz seznama `tocke`, ki ležijo **znotraj kroga** (vključno z mejo) s središčem `sredisce` in polmerom `r`.

```python
>>> sorted(tocke_v_obmocju([(0,0), (1,1), (3,4)], (0,0), 2))
[(0, 0), (1, 1)]
>>> sorted(tocke_v_obmocju([(0,0), (3,4), (6,8)], (0,0), 5))
[(0, 0), (3, 4)]
```

### 💡 Pristop

Izpeljana množica + Pitagorov izrek. **Kvadriramo**, da se izognemo `sqrt`-u (in s tem nenatančnostim s floati): primerjamo $dx^2 + dy^2 \leq r^2$.

### ✅ Rešitev

```python
def tocke_v_obmocju(tocke, sredisce, r):
    sx, sy = sredisce
    return {(x, y) for (x, y) in tocke if (x - sx) ** 2 + (y - sy) ** 2 <= r * r}
```

---

## 5. Preverjanje EMŠO

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

### 💡 Pristop

Najprej preverimo dolžino in da so vse znake števke (`str.isdigit`). Nato izračunamo kontrolno števko po formuli.

### ✅ Rešitev

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

## 6. Sestavljanje zneska s kovanci

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

### 💡 Pristop

Klasičen primer **dinamičnega programiranja**. Definiramo `dp[z]` = število načinov, da sestavimo znesek `z`. Za vsak kovanec posodobimo vse zneske od kovanca naprej. **Zunanja zanka po kovancih** (in ne po zneskih) zagotavlja, da ne štejemo iste kombinacije v različnih vrstnih redih.

### ✅ Rešitev

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

## 7. Branje datoteke z ocenami

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

### 💡 Pristop

1. Beremo po vrsticah z `with open(...)`.
2. Vsako vrstico `.strip()`-amo in razdelimo na 3 dele s `.split(';')`.
3. Za vsakega študenta zbiramo seznam ocen v slovar z `.setdefault(ime, []).append(ocena)`.
4. Na koncu izračunamo povprečja z izpeljanim slovarjem.

Napačne vrstice (premalo polj, ocena ni število) preprosto preskočimo s `continue`.

### ✅ Rešitev

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

## 8. Razred `Polinom`

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

### 💡 Pristop

- **Normalizacija:** v `__init__` odrežemo ničle z konca seznama, tako da je `Polinom([1, 2, 0])` po notranjosti enak `Polinom([1, 2])`.
- **Hornerjeva shema** za vrednotenje: $((a_n x + a_{n-1})x + \ldots)x + a_0$ — $n$ množenj namesto kvadratnega števila.
- **Seštevanje:** zlijemo koeficiente, manjkajoče tretiramo kot 0.

### ✅ Rešitev

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

## 9. Generator praštevil

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

### 💡 Pristop

Za vsako število `n` od 2 navzgor preverimo z deljenjem **samo z že najdenimi praštevili** do $\sqrt{n}$. Tako se izognemo testu z vsemi števili in delamo tako rekoč inkrementalno **Eratostenovo sito**.

Trik z `p * p > n` se izogne klicu `math.sqrt`.

### ✅ Rešitev

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

## 10. Pravilno gnezdeni oklepaji

> 📚 **Teme:** sklad, nizi

Sestavi funkcijo `pravilno_gnezdeni(niz)`, ki vrne `True` natanko, kadar so v nizu pravilno gnezdeni oklepaji `(`, `[`, `{` in njihovi zaklepaji. **Vse ostale znake ignorira.**

```python
>>> pravilno_gnezdeni('([]{()})')
True
>>> pravilno_gnezdeni('a(b[c]d)e{f}')
True
>>> pravilno_gnezdeni('([)]')
False
>>> pravilno_gnezdeni('(((')
False
>>> pravilno_gnezdeni('')
True
```

### 💡 Pristop

Klasičen vzorec s **skladom** (list, ki ga uporabljamo z `append`/`pop`):

- Uklepaje porivamo na sklad.
- Ob zaklepaju preverimo, da je vrh sklada ustrezen uklepaj, in ga `pop`-amo.
- Na koncu mora biti sklad **prazen** (vsi uklepaji so se zaprli).

### ✅ Rešitev

```python
def pravilno_gnezdeni(niz):
    sklad = []
    pari = {')': '(', ']': '[', '}': '{'}
    for znak in niz:
        if znak in '([{':
            sklad.append(znak)
        elif znak in ')]}':
            if not sklad or sklad.pop() != pari[znak]:
                return False
    return not sklad
```

> 💭 Pomembna sta dva razloga za `False` ob zaklepaju:
> 1. **Prazen sklad** — zaklepaj brez ujemajočega uklepaja: `)`.
> 2. **Vrh ni ujemajoč** — različen tip oklepaja: `([)]`.

---

## 🧪 Testna datoteka

Datoteko **[`izpitne_naloge_resene.py`](izpitne_naloge_resene.py)** lahko zaženeš in se izvedejo testi za vse rešitve:

```bash
python izpitne_naloge_resene.py
```

Vse rešitve so testirane in delujejo. ✅

---

## 📖 Predlagani naslednji koraki

Če ti je katera od tem še šibka, jih lahko vadiš tako:

- **Razredi:** dodaj `__mul__` v `Polinom` (množenje polinomov).
- **Generatorji:** napiši generator, ki vrača Pitagorske trojice.
- **Datoteke:** razširi nalogo 7, da izpisuje tudi povprečje **po predmetih**.
- **Rekurzija:** reši nalogo 6 še **rekurzivno** in primerjaj hitrost.
- **Sklad:** razširi nalogo 10, da podpre tudi `<` in `>` ali HTML značke.
