# 🐍 Uvod v programiranje
> Vir: [matija.pretnar.info/uvod-v-programiranje](https://matija.pretnar.info/uvod-v-programiranje/00-uvod.html)

---

## Kazalo

1. [Python 2 vs Python 3 & osnove](#1-python-2-vs-python-3--osnove)
2. [Aritmetične operacije in osnovne funkcije](#2-aritmetične-operacije-in-osnovne-funkcije)
3. [Uvažanje iz knjižnic](#3-uvažanje-iz-knjižnic)
4. [Spremenljivke](#4-spremenljivke)
5. [Definicije funkcij in stavek return](#5-definicije-funkcij-in-stavek-return)
6. [Logične vrednosti in pogojni stavek](#6-logične-vrednosti-in-pogojni-stavek)
7. [Vrste napak](#7-vrste-napak)
8. [Rekurzija](#8-rekurzija)
9. [Nizi](#9-nizi)
10. [Zanke](#10-zanke)
11. [Seznami & nabori](#11-seznami--nabori)
12. [Slovarji & množice](#12-slovarji--množice)
13. [Razredi](#13-razredi)
14. [Iteratorji, generatorji in iterabilni objekti](#14-iteratorji-generatorji-in-iterabilni-objekti)
15. [Datoteke](#15-datoteke)
16. [Regularni izrazi](#16-regularni-izrazi)
17. [Koristne vgrajene funkcije — hiter pregled](#17-koristne-vgrajene-funkcije--hiter-pregled)
18. [Časovna zahtevnost — kratek pregled](#17½-časovna-zahtevnost--kratek-pregled)
19. [Algoritemski vzorci](#18-algoritemski-vzorci)
20. [Pretvorbe baz](#19-pretvorbe-baz-binarno-šestnajstiško-)

---

## 1. Python 2 vs Python 3 & osnove

- **Vedno** uporabljaj Python 3 (Python 2 je uradno ugasnil 1. januarja 2020).
- Pri zagonu preveri: v terminalu mora pisati `Python 3.x.x`, ne `Python 2.x.x`.
- Datoteke shranjuješ s končnico `.py`.
- Interaktivna konzola: poziv `>>>`.
- Komentarji: `# to je komentar` — Python jih ignorira.
- **PEP 8** — standard za berljivo kodo:
  - Na vsaki strani operatorja en presledek: `a = 3 + 3`
  - Za ločilom (`,`) presledek, pred njim ne: `max(3, 6)`
  - Spremenljivke z malimi črkami, besede ločene z `_`: `ime_spremenljivke`
  - Zamik teles (funkcij, pogojnih stavkov, zank): **4 presledki**

---

## 2. Aritmetične operacije in osnovne funkcije

| Operator | Pomen | Primer | Rezultat |
|----------|-------|--------|----------|
| `+` | seštevanje | `3 + 2` | `5` |
| `-` | odštevanje | `3 - 2` | `1` |
| `*` | množenje | `3 * 2` | `6` |
| `**` | potenciranje | `3 ** 2` | `9` |
| `/` | deljenje (vrne float) | `7 / 2` | `3.5` |
| `//` | celoštevilsko deljenje | `7 // 2` | `3` |
| `%` | ostanek pri deljenju | `7 % 2` | `1` |

**Prioriteta (od največje):** `**` → `*`, `/`, `//`, `%` → `+`, `-`

Za spremembo vrstnega reda: **oklepaji** `(1 + 2) * 3`

### Vgrajene funkcije

```python
max(3, 6)        # 6
min(3, 6)        # 3
abs(-5)          # 5
len("beseda")    # 6
str(42)          # '42'
int("42")        # 42
float("3.14")    # 3.14
round(3.7)       # 4
sum([1, 2, 3])   # 6
```

### Števila s plavajočo vejico

`1.22e-16` pomeni `1.22 × 10⁻¹⁶`. Računalnik dela z **aproximacijami** realnih števil.

```python
# Bodi previden:
import math
math.sin(math.pi)   # vrne ~1.22e-16, ne točno 0
```

### Operatorji za skrajšano posodabljanje

```python
x += 2    # x = x + 2
x -= 2    # x = x - 2
x *= 2    # x = x * 2
x //= 2   # x = x // 2
x **= 2   # x = x ** 2
x %= 2    # x = x % 2
```

### `divmod` — celoštevilsko deljenje in ostanek hkrati

```python
divmod(17, 5)    # (3, 2)   ker je 17 = 3*5 + 2
divmod(7, 2)     # (3, 1)
```

Uporabno pri pretvorbah enot in delu z bazami:

```python
# Sekunde -> ure, minute, sekunde:
def cas(sek):
    ure, sek = divmod(sek, 3600)
    minute, sek = divmod(sek, 60)
    return ure, minute, sek

cas(3725)   # (1, 2, 5)  -> 1h 2min 5s

# Število -> seznam števk v dani bazi:
def stevke(n, baza=10):
    rez = []
    while n > 0:
        n, r = divmod(n, baza)
        rez.append(r)
    return rez[::-1]
```

---

## 3. Uvažanje iz knjižnic

```python
# 1. način: uvozi knjižnico, nato dostopaj z math.xxx
import math
math.sqrt(2)
math.sin(math.pi / 4)
math.log(100, 10)     # log base 10
math.floor(3.7)       # 3
math.ceil(3.2)        # 4
math.factorial(5)     # 120

# 2. način: uvozi samo to, kar potrebuješ
from math import sqrt, sin, pi, e

# 3. način (odsvetovan): uvozi vse
from math import *
```

```python
import random
random.uniform(0, 1)      # naključno float med 0 in 1
random.randint(1, 6)      # naključno int med 1 in 6 (vključno)
random.choice([1, 2, 3])  # naključni element seznama
random.shuffle(seznam)    # premešaj seznam na mestu
```

```python
import os          # delo z datotečnim sistemom
import json        # zapis/branje JSON
import re          # regularni izrazi
```

---

## 4. Spremenljivke

```python
# Prireditveni stavek
a = 3 + 3       # a = 6 (ne vrne vrednosti v konzoli)

# Več spremenljivk hkrati
a, b = 10, 15   # a = 10, b = 15

# Hkratna zamenjava vrednosti
a, b = b, a     # swap!

# Povozimo vrednost — ostale spremenljivke ostanejo
a = 10
b = a + 3       # b = 13
a = 25          # b ostane 13
```

**Pravila za imena:**
- Opisna, z malimi črkami: `stevilo_uciteljev`
- Ne začnejo s številko
- Brez presledkov (namesto tega `_`)

### `==` vs `is`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b    # True  — enaki vrednosti
a is b    # False — različna objekta v pomnilniku
a is c    # True  — c kaže na ISTI objekt kot a
```

- `==` primerja **vrednosti**
- `is` primerja **identiteto** (ali gre za isti objekt v pomnilniku)

> `is` uporabljamo le za primerjavo z `None`: `if x is None:`

---

## 5. Definicije funkcij in stavek return

```python
def ime_funkcije(argument1, argument2):
    """Dokumentacijski niz — opiše, kaj funkcija počne."""
    # telo funkcije (zamaknjeno za 4 presledke)
    rezultat = argument1 + argument2
    return rezultat
```

```python
# Primer: Heronova formula
import math

def ploscina_trikotnika(a, b, c):
    """Vrne ploščino trikotnika z danimi stranicami."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

ploscina_trikotnika(4, 13, 15)   # 24.0
```

### Privzeti argumenti (keyword arguments)

```python
def koren(x, n=2):
    return x ** (1 / n)

koren(64)        # 8.0  (n=2 privzeto)
koren(64, n=3)   # ~4.0
```

> ⚠️ Okoli `=` pri privzetih argumentih **ne pišemo presledkov**: `def f(x, n=2):`

> ⚠️ **Privzeti argument nikoli ne sme biti spremenljiv objekt** (seznam, slovar, množica)!
> Python ustvari privzeto vrednost **enkrat** ob definiciji funkcije — ne ob vsakem klicu.
> ```python
> # SLABO — seznam si "zapomni" vsebino iz prejšnjega klica:
> def dodaj(x, sez=[]):
>     sez.append(x)
>     return sez
>
> dodaj(1)   # [1]
> dodaj(2)   # [1, 2]  ← ni [2]!
>
> # PRAVILNO — privzeto None, ustvari nov seznam znotraj funkcije:
> def dodaj(x, sez=None):
>     if sez is None:
>         sez = []
>     sez.append(x)
>     return sez
> ```

### Stavek return

- `return` takoj konča izvajanje funkcije.
- Funkcija brez `return` vrne `None`.
- Pogosta napaka: `TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'` → manjka `return`!

```python
def f(x):
    return x ** 2   # ustavi se tukaj
    return 1000     # ta vrstica se nikoli ne izvede
```

### Lokalne vs globalne spremenljivke

```python
def f(x):
    y = 3 * x   # y je lokalna — zunaj funkcije ne obstaja
    return y

y = 10          # to je globalna y
f(4)            # vrne 12, globalne y ne spremeni
y               # še vedno 10
```

### `*args` in `**kwargs` — poljubno število argumentov

```python
# *args zbira pozicijske argumente v nabor:
def vsota(*stevila):
    rez = 0
    for x in stevila:
        rez += x
    return rez

vsota(1, 2, 3)        # 6
vsota(1, 2, 3, 4, 5)  # 15

# **kwargs zbira poimenovane argumente v slovar:
def opisi(**lastnosti):
    for kljuc, vrednost in lastnosti.items():
        print(f"{kljuc}: {vrednost}")

opisi(ime="Ana", starost=22, smer="UVP")

# Kombinacija (vrstni red: pozicijski, *args, privzeti, **kwargs):
def f(a, b, *args, c=10, **kwargs):
    ...
```

Operator `*` (ali `**`) lahko uporabimo tudi pri **klicu** funkcije, da razpakiramo seznam (ali slovar) v argumente:

```python
sez = [3, 1, 4]
max(*sez)            # = max(3, 1, 4) = 4

slovar = {'sep': '-', 'end': '!\n'}
print('a', 'b', 'c', **slovar)   # 'a-b-c!'
```

### Funkcije so prvorazredni objekti

V Pythonu lahko funkcije:
- shranimo v spremenljivko,
- damo kot argument drugi funkciji,
- vrnemo iz funkcije,
- shranimo v sezname/slovarje.

```python
def kvadrat(x): return x * x
def kub(x): return x ** 3

f = kvadrat            # f zdaj kaže na funkcijo
f(5)                   # 25

operacije = [kvadrat, kub, abs]
[f(3) for f in operacije]   # [9, 27, 3]

# To je razlog, da deluje key= pri sorted/min/max:
besede = ['hruška', 'jabolko', 'češnja']
sorted(besede, key=len)         # ['hruška', 'češnja', 'jabolko']
sorted(besede, key=str.lower)
max([(1, 'a'), (3, 'b'), (2, 'c')], key=lambda par: par[0])   # (3, 'b')
```

**Lambda izrazi** so anonimne funkcije za enkratno uporabo:

```python
kvadrat = lambda x: x * x       # ekvivalentno def kvadrat(x): return x*x
sorted([-3, 1, -2], key=lambda x: abs(x))   # [1, -2, -3]
```

---

## 6. Logične vrednosti in pogojni stavek

### Logične vrednosti

```python
True    # resnica
False   # neresnica
```

### Primerjalni operatorji

```python
a == b    # enakost
a != b    # neenakost
a < b     # manjši
a > b     # večji
a <= b    # manjši ali enak
a >= b    # večji ali enak
```

### Logični operatorji

```python
True and False    # False
True or False     # True
not True          # False

# Kombinacije
3 < 5 or 10 > 20     # True
x > 0 and x < 10    # True, če je 0 < x < 10
```

### Tabele resničnosti

```
A      B      | A and B | A or B | not A | A→B
False  False  |  False  |  False |  True | True
False  True   |  False  |  True  |  True | True
True   False  |  False  |  True  |  False| False
True   True   |  True   |  True  |  False| True
```

Pogosto potrebne sestavljene operacije:

| Operacija | Definicija v Pythonu |
|-----------|----------------------|
| implikacija (A→B) | `not a or b` |
| ekvivalenca (A↔B) | `(not a or b) and (not b or a)` |
| XOR | `(a and not b) or (not a and b)` |
| NAND | `not (a and b)` |

**NAND je univerzalen** — z njim lahko izrazimo vse ostale:
```python
def nand(a, b): return not (a and b)

# not a  ≡  nand(a, a)
# a and b  ≡  nand(nand(a, b), nand(a, b))
# a or b  ≡  nand(nand(a, a), nand(b, b))
```

**Kratki stik (short-circuit):** Python preneha vrednotiti takoj, ko je rezultat znan.
- `or` se ustavi pri prvem `True`
- `and` se ustavi pri prvem `False`

```python
# Koristno: varno preverjanje brez IndexError
sez and sez[0]          # ne vrže napake, če je sez prazen
x != 0 and y / x > 2   # ne deli z nič, če je x == 0
```

### Pogojni stavek if / elif / else

```python
if pogoj1:
    # izvede se, če pogoj1 velja
elif pogoj2:
    # izvede se, če pogoj1 ne velja, a velja pogoj2
elif pogoj3:
    # ...
else:
    # izvede se, če noben pogoj ne velja
```

```python
# Primer:
def predznak(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1
```

### Pogojni izraz (ternary)

```python
def absolutna_vrednost(x):
    return x if x >= 0 else -x
```

### Resnične in lažne vrednosti (truthy / falsy)

Python ima poleg `True`/`False` še **resnično vrednost vsakega objekta**. V `if`, `while`, `and`, `or` in `not` se objekti samodejno pretvorijo v logično vrednost.

**Lažne (falsy) vrednosti:**

```python
bool(False)      # False
bool(None)       # False
bool(0)          # False
bool(0.0)        # False
bool('')         # False  (prazen niz)
bool([])         # False  (prazen seznam)
bool({})         # False  (prazen slovar)
bool(set())      # False  (prazna množica)
bool(())         # False  (prazen nabor)
```

**Vse ostalo je truthy** — vsak neprazen niz/seznam/slovar, vsako neničelno število.

```python
# Idiomatični načini:
if sez:                 # "če seznam ni prazen"
    ...

if not slovar:          # "če je slovar prazen"
    ...

# Privzete vrednosti z `or`:
ime = vneseno_ime or 'Anonimno'   # če je vneseno_ime '', vzemi 'Anonimno'

# Pozor: `or` vrne en operand, ne obvezno True/False:
0 or 'a'    # 'a'
'a' or 'b'  # 'a'
[] or [1]   # [1]
```

---

## 7. Vrste napak

### 1. Sintaktične napake (SyntaxError)
Python odkrije **pred izvajanjem**. Program sploh ne začne teči.

```python
max(2; 4)     # SyntaxError: invalid syntax (vejico, ne podpičje!)
max(2, 4))    # SyntaxError: unmatched ')'
```

### 2. Napake ob izvajanju (RuntimeError)
Koda je sintaktično pravilna, a Python ne more izvesti ukaza.

```python
1 / 0         # ZeroDivisionError
mix(2, 4)     # NameError: name 'mix' is not defined
int("abc")    # ValueError
```

> Ključna informacija je v **zadnji vrstici** sporočila o napaki!

### 3. Vsebinske napake (logične napake)
Najhujše — Python ne javi napake, a odgovor je **napačen**.

```python
# Hotelimo koren, a Python to razume drugače:
((2-5)**2 + (3-7)**2) ** 1/2    # NAPAČNO: (... ** 1) / 2
((2-5)**2 + (3-7)**2) ** (1/2)  # PRAVILNO
```

**Preprečevanje:** berljiva koda, opisna imena, presledki okoli operatorjev, sproti testiramo.

### Lovljenje napak — `try/except`

Včasih napake **pričakujemo** in jih hočemo obravnavati namesto, da program propade.

```python
try:
    n = int(input("Vnesi število: "))
except ValueError:
    print("To ni veljavno število!")
    n = 0
```

Polna oblika:

```python
try:
    # poskusi nekaj nevarnega
    rez = a / b
except ZeroDivisionError:
    # izvede se SAMO ob tej napaki
    print("Deljenje z nič!")
except (ValueError, TypeError) as e:
    # lahko ujamemo več napak hkrati in pridobimo objekt napake
    print(f"Druga napaka: {e}")
else:
    # izvede se, če NI bilo napake
    print(f"Rezultat: {rez}")
finally:
    # izvede se VEDNO (uporabno za zapiranje datotek/povezav)
    print("Konec.")
```

### Sprožanje napak — `raise`

```python
def deli(a, b):
    if b == 0:
        raise ValueError("Drugi argument ne sme biti 0.")
    return a / b
```

### Stavek `assert`

Trditev, da nekaj velja. Če ne velja, sproži `AssertionError`. Uporaben za sanity checks med razvojem.

```python
def koren(x):
    assert x >= 0, f"Pričakoval nenegativno število, dobil {x}."
    return x ** 0.5
```

### Pomembne standardne izjeme

| Izjema | Kdaj se zgodi |
|--------|---------------|
| `ValueError` | `int("abc")`, `math.sqrt(-1)` — napačna vrednost prave vrste |
| `TypeError` | `'a' + 1`, `len(5)` — operacija nad napačnim tipom |
| `ZeroDivisionError` | deljenje z nič |
| `IndexError` | `sez[100]` — indeks zunaj območja |
| `KeyError` | `slovar['ni_v_njem']` — ključ ne obstaja |
| `NameError` | uporaba spremenljivke/funkcije, ki ni definirana |
| `AttributeError` | `niz.napacna_metoda()` |
| `FileNotFoundError` | `open('ne_obstaja.txt')` |
| `StopIteration` | `next()` na praznem iteratorju |
| `RecursionError` | preglobok rekurzivni klic |

---

## 8. Rekurzija

Funkcija, ki **kliče samo sebe**. Vedno potrebuje:
1. **Osnovni primer** (base case) — kdaj se ustavi
2. **Rekurzivni korak** — klic s "manjšim" problemom

```python
# Fakulteta: n! = n * (n-1)!
def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n - 1)

fakulteta(5)   # 120
```

```python
# Fibonaccijevo zaporedje (učinkovita različica)
def splosni_fibonacci(n, a=0, b=1):
    """Vrne n-ti člen zaporedja a, b, a+b, a+2b, ..."""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return splosni_fibonacci(n - 1, b, a + b)

splosni_fibonacci(10)      # 55
splosni_fibonacci(10, 0, 10)  # 550
```

### Evklidov algoritem (NSD)

```python
def gcd(m, n):
    """Vrne največji skupni delitelj m in n."""
    return m if n == 0 else gcd(n, m % n)

gcd(456, 123)   # 3
```

> ⚠️ Python ima omejitev globine rekurzije (~1000 klicev). Za globoke rekurzije raje zanke.

### Bisekcija (iskanje z razpolovljanjem)

```python
def bisekcija(f, a, b, eps=1e-10):
    """Poišče ničlo funkcije f na intervalu [a, b]."""
    while b - a > eps:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2
```

### Binarno iskanje v urejenem seznamu (deli in vladaj)

```python
def binarno_iskanje(sez, x):
    """Vrne indeks elementa x v urejenem seznamu sez, ali -1, če ga ni."""
    levo, desno = 0, len(sez) - 1
    while levo <= desno:
        sredina = (levo + desno) // 2
        if sez[sredina] == x:
            return sredina
        elif sez[sredina] < x:
            levo = sredina + 1
        else:
            desno = sredina - 1
    return -1

# Rekurzivna različica:
def binarno_rek(sez, x, levo=0, desno=None):
    if desno is None:
        desno = len(sez) - 1
    if levo > desno:
        return -1
    sredina = (levo + desno) // 2
    if sez[sredina] == x:
        return sredina
    elif sez[sredina] < x:
        return binarno_rek(sez, x, sredina + 1, desno)
    else:
        return binarno_rek(sez, x, levo, sredina - 1)
```

Iskanje v seznamu z `n` elementi vzame `O(log n)` korakov — pri milijonu elementov **20 korakov** namesto milijon.

### Pozor: naivni Fibonacci je eksponenten

```python
# SLABA verzija — O(2^n) klicev, fib(40) traja sekundo, fib(50) minute:
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# DOBRA verzija — O(n), z akumulatorjema:
def fib(n, a=0, b=1):
    if n == 0:
        return a
    return fib(n - 1, b, a + b)
```

Razlog: naivna različica izračuna isto vrednost **ponovno in ponovno**. Pri vsakem rekurzivnem branjenju se veji navzdol kot dvojiško drevo.

---

## 9. Nizi

### Osnovne operacije

```python
'zala' + 'gasper'    # 'zalagasper'  (stikanje)
'tro' + 4 * 'lo'     # 'trololololo' (množenje)
len('lokomotiva')    # 10

'gram' in 'programiranje'      # True (podniz)
'liter' not in 'programiranje' # True

'abak' <= 'abeceda'  # True (leksikografska primerjava)
```

### Indeksi in rezine

```python
niz = 'REKURZIJA'
#      0 1 2 3 4 5 6 7 8   (pozitivni indeksi)
#     -9-8-7-6-5-4-3-2-1   (negativni indeksi)

niz[0]      # 'R'  (prvi znak)
niz[-1]     # 'A'  (zadnji znak)
niz[3]      # 'U'

niz[2:6]    # 'KURZ'  (od indeksa 2 do 5, brez 6)
niz[:6]     # 'REKURZ' (od začetka do 5)
niz[2:]     # 'KURZIJA' (od indeksa 2 do konca)
niz[1:8:2]  # 'EUZJ'   (vsak 2. znak)
niz[::-1]   # 'AJIZRUKER' (obrnjeno)
```

### Zapisi nizov

```python
'enojni narekovaji'
"dvojni narekovaji"
'''trojni enojni (lahko čez več vrstic)'''
"""trojni dvojni (za docstringe)"""

Enojni (`'`) in dvojni (`"`) narekovaji v Pythonu so funkcionalno **popolnoma enaki** — izbira je stvar osebne preference.

Koristno je vedeti:
- Če niz vsebuje apostrof, ga lažje zapišeš z dvojnimi: `"it's fine"`
- Če niz vsebuje narekovaj, ga lažje zapišeš z enojnimi: `'rekel je "živjo"'`
- Trojni narekovaji (`"""` ali `'''`) omogočajo večvrstične nize

PEP 8 ne predpisuje enega ali drugega, samo priporoča, da si pri projektu dosleden.

# Ubežni znaki:
'\n'   # nova vrstica
'\t'   # tabulator
'\\'   # poševnica \
'\''   # enojni narekovaj
'\"'   # dvojni narekovaj

# Surovi niz (raw string) — \ nima posebnega pomena:
r'\n se ne pretvori v novo vrstico'
```

### Vgrajene metode na nizih

```python
s = 'Otorinolaringolog'

s.lower()           # 'otorinolaringolog'
s.upper()           # 'OTORINOLARINGOLOG'
s.title()           # 'Otorinolaringolog' (velika začetnica vsake besede)
s.capitalize()      # 'Otorinolaringolog' (prva črka velika)
s.swapcase()        # zamenjaj male/velike

s.count('o')        # 4 (prešteje pojavitve)
s.count('o', 2)     # začne šteti pri indeksu 2
s.index('ring')     # 8 (indeks prve pojavitve, napaka če ni)
s.find('ring')      # 8 (enako kot index, a vrne -1 če ni)

s.replace('o', '0')           # zamenjaj vse
s.replace('o', '0', 2)        # zamenjaj le prvi 2

s.strip()           # odstrani bele znake z robov
s.strip('Og')       # odstrani znake 'O' in 'g' z robov
s.lstrip()          # samo levi rob
s.rstrip()          # samo desni rob

s.split()           # ['Otorinolaringolog'] — razdeli po belem prostoru
'a,b,c'.split(',')  # ['a', 'b', 'c']
','.join(['a','b']) # 'a,b'

s.startswith('Oto') # True
s.endswith('log')   # True

s.isdigit()         # True, če so samo števke
s.isalpha()         # True, če so samo črke
s.islower()         # True, če so samo male črke
s.isupper()         # True, če so samo velike črke
s.isalnum()         # True, če so črke ali števke
s.isspace()         # True, če so samo beli znaki
```

### `partition` in `rpartition`

Razdelita niz na **tri dele**: del pred prvo (oz. zadnjo) pojavitvijo ločila, ločilo samo, in del za njim. Vrneta nabor dolžine 3 tudi, če ločila ni.

```python
'janez@kranjsko.si'.partition('@')
# ('janez', '@', 'kranjsko.si')

'a=b=c'.partition('=')    # ('a', '=', 'b=c')   prvo
'a=b=c'.rpartition('=')   # ('a=b', '=', 'c')   zadnje

'brez_locila'.partition('@')
# ('brez_locila', '', '')
```

Pogosto bolj priročno od `.split()`, ko nas zanima točno **eno** ločilo.

### f-nizi (formatted strings)

```python
kdo = 'Janez'
starost = 25
f'{kdo} je star {starost} let.'    # 'Janez je star 25 let.'

a, b = 22, 7
f'{a}/{b} = {a/b:.5}'              # '22/7 = 3.1429'  (5 signifikantnih mest)
f'{a/b:.2f}'                       # '3.14'  (2 decimalni mesti)
f'{1/3:.2%}'                       # '33.33%'  (procenti)
f'{"NASLOV":*^30}'                 # '************NASLOV************'
```

### print in input

```python
print('Pozdravljen!')               # izpiše v konzolo
print('a =', a, 'b =', b)          # izpiše več vrednosti
print('konec', end='')              # brez nove vrstice na koncu
print('x', 'y', sep='-')           # 'x-y'

ime = input('Vnesi ime: ')          # prebere niz s konzole
starost = int(input('Vnesi starost: '))  # pretvori v int
```

---

## 10. Zanke

### Zanka while

```python
while pogoj:
    # stavki se ponavljajo, dokler velja pogoj
```

```python
n = 12
while n < 1000:
    n *= 2
    print(n)
# Izpiše: 24, 48, 96, ..., 1536
```

```python
# Primer: celoštevilski logaritem
def celostevilski_logaritem(n, k):
    """Vrne stopnjo največje potence k, ki deli n."""
    stopnja = 0
    while n % k == 0:
        n //= k
        stopnja += 1
    return stopnja

celostevilski_logaritem(81, 3)   # 4
```

### Zanka for

```python
for spremenljivka in vrednosti:
    # stavki za vsako vrednost
```

```python
# Sprehod čez niz
for znak in 'abc':
    print(znak)     # a, b, c

# Sprehod čez range
for x in range(5):           # 0, 1, 2, 3, 4
    print(x)

for x in range(5, 10):       # 5, 6, 7, 8, 9
    print(x)

for x in range(5, 10, 2):   # 5, 7, 9
    print(x)

for x in range(10, 0, -1):  # 10, 9, ..., 1
    print(x)
```

```python
# Primer: fakulteta z zanko for
def fakulteta(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt
```

### Stavki break, continue in pass

```python
# break — prekine zanko
for n in range(10):
    if n == 5:
        break       # ustavi zanko pri 5
    print(n)

# continue — preskoči preostanek tega obhoda
for n in range(10):
    if n % 2 == 0:
        continue    # preskoči sode
    print(n)        # izpiše samo lihe: 1, 3, 5, 7, 9

# pass — ne naredi ničesar (placeholder)
for n in range(10):
    if n == 5:
        pass        # nič se ne zgodi
    print(n)
```

### Metoda Monte-Carlo (ocena π)

```python
import random

def oceni_pi(n):
    v_krogu = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            v_krogu += 1
    return 4 * v_krogu / n

oceni_pi(100000)   # ~3.14...
```

---

## 11. Seznami & nabori

### Osnove seznamov

```python
sez = [10, 20, 30, 40, 50]   # seznam
prazen = []                   # prazen seznam
gnezedn = [[1, 2], [3, 4]]   # gnezdeni seznam

# Iste operacije kot na nizih:
[1, 2] + [3, 4]       # [1, 2, 3, 4]  (stikanje)
3 * [0]               # [0, 0, 0]     (množenje)
len([1, 2, 3])        # 3
5 in [1, 2, 5]        # True
[1,2] < [1,3]         # True (leksikografsko)

# Indeksi in rezine (enako kot nizi):
sez[0]      # 10
sez[-1]     # 50
sez[1:3]    # [20, 30]
sez[::2]    # [10, 30, 50]
```

```python
# Gnezdeni indeksi:
mat = [[1, 0, 0], [0, -1, 2], [3, 1, 5]]
mat[1][-1]   # 2
```

### Spreminjanje seznamov

```python
sez = [10, 20, 30]
sez[1] = 40           # [10, 40, 30]
sez[1:3] = [0, 0, 0]  # nadomesti rezino
del sez[1]            # izbriše element
del sez[2:4]          # izbriše rezino
```

> ⚠️ **Pozor na aliase!** Seznami so spremenljivi in se "delijo":
```python
a = [1, 1, 1]
b = a           # b kaže na ISTI seznam
a[1] = 2        # b se prav tako spremeni!
b               # [1, 2, 1]

# Rešitev — naredi kopijo:
b = a[:]        # ali: b = list(a)
```

### Plitka vs globoka kopija

Pri **gnezdenih** seznamih `a[:]` ne zadošča — skopira le zunanji seznam, notranji ostanejo skupni:

```python
a = [[1, 2], [3, 4]]
b = a[:]          # plitka kopija
b[0].append(99)
a                 # [[1, 2, 99], [3, 4]]   ← spremenil se je tudi a!

# Rešitev: globoka kopija
import copy
b = copy.deepcopy(a)
b[0].append(99)
a                 # [[1, 2], [3, 4]]       ← nedotaknjeno
```

| Operacija | Kopira zunanji? | Kopira notranje? |
|-----------|:---:|:---:|
| `b = a` | ne (samo alias) | ne |
| `b = a[:]` ali `list(a)` | da | ne |
| `copy.deepcopy(a)` | da | da |

### Vgrajene metode na seznamih

```python
sez = [10, 20, 30]

sez.append(40)          # [10, 20, 30, 40]  — doda na konec
sez.extend([40, 50])    # [10, 20, 30, 40, 50]  — doda več (= +=)
sez.insert(1, 0)        # [10, 0, 20, 30]  — vstavi pred indeks 1
sez.remove(20)          # odstrani prvo pojavitev 20
sez.pop()               # odstrani in vrne zadnji element
sez.pop(1)              # odstrani in vrne element na indeksu 1
sez.clear()             # [] — pobriše vse

sez.index(20)           # vrne indeks prve pojavitve 20
sez.count(20)           # prešteje pojavitve 20

sez.sort()              # uredi na mestu (naraščajoče)
sez.sort(reverse=True)  # uredi padajoče
sez.sort(key=len)       # uredi po dolžini (za nize ipd.)
sorted(sez)             # vrne nov urejen seznam, original ne_spremi
sez.reverse()           # obrne na mestu
sez[::-1]               # vrne novo obrnjeno rezino
```

### Izpeljani seznami

```python
# Osnovna oblika:
[izraz for var in vrednosti]

# S pogojem:
[izraz for var in vrednosti if pogoj]

# Primeri:
[2 * n for n in range(1, 10)]
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

[n**2 for n in range(10) if n % 2 == 0]
# [0, 4, 16, 36, 64]

[int(c) for c in str(3141592)]
# [3, 1, 4, 1, 5, 9, 2]

# Gnezdeni izpeljani seznam (identična matrika):
def identicna_matrika(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Dve zanki v enem:
[(i, j) for i in range(3) for j in range(i, 3)]
```

### Koristne funkcije za sezname

```python
sum([1, 2, 3])           # 6
max([1, 2, 3])           # 3
min([1, 2, 3])           # 1
sorted([3, 1, 2])        # [1, 2, 3]
reversed([1, 2, 3])      # iterator (obrnjeno)
list(range(5))           # [0, 1, 2, 3, 4]

# enumerate — hkrati indeks in vrednost:
for i, x in enumerate(['a', 'b', 'c']):
    print(i, x)
# 0 a, 1 b, 2 c

# zip — spoji več seznamov:
for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)
# 1 a, 2 b, 3 c

# Skalarni produkt:
def skalarni_produkt(v1, v2):
    return sum([x1 * x2 for x1, x2 in zip(v1, v2)])
```

### Nabori (tuple)

```python
t = (1, 2, 3)       # nabor
t = (1,)            # nabor z enim elementom (vejica obvezna!)
t = ()              # prazen nabor

# Enake operacije kot seznami, razen...
t[0] = 5            # TypeError! Nabori so NEspremenljivi.

# Razstavljanje:
datum = (25, 6, 1991)
dan, mesec, leto = datum

# Hkratna zamenjava spremenljivk je v resnici nabor:
a, b = b, a         # = (b, a)
```

**Kdaj seznam, kdaj nabor?**
- **Seznam** `[...]`: homogena zbirka (vsi elementi z enakim pomenom), poljubno dolžina.
- **Nabor** `(...)`: heterogena zbirka (elementi z različnimi pomeni, npr. datum, koordinata), fiksna dolžina.

---

## 12. Slovarji & množice

### Slovarji

```python
# Ustvarjanje:
s = {'a': 1, 'b': 5, 'c': 10}
prazen = {}

# Dostop:
s['a']          # 1
s['d']          # KeyError! Ključ ne obstaja.
s.get('d')      # None — ne javi napake
s.get('d', 0)   # 0 — privzeta vrednost

# Dodajanje / posodabljanje:
s['d'] = 20     # doda nov par ali posodobi obstoječi

# Brisanje:
del s['a']
s.pop('b')      # vrne vrednost in jo odstrani
s.popitem()     # odstrani in vrne naključni par
```

```python
# Zanke:
for kljuc in s:              # sprehod po ključih
    print(kljuc)

for v in s.values():         # sprehod po vrednostih
    print(v)

for k, v in s.items():       # sprehod po parih
    print(k, '->', v)
```

```python
# Izpeljani slovarji:
{i: 2**i for i in range(10)}
# {0: 1, 1: 2, 2: 4, ...}

{k: v for k, v in s.items() if v > 3}
# samo pari, kjer je vrednost > 3
```

```python
# Štetje pojavitev:
def prestej_pojavitve(niz):
    pojavitve = {}
    for znak in niz:
        pojavitve[znak] = pojavitve.get(znak, 0) + 1
    return pojavitve

prestej_pojavitve('abrakadabra')
# {'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}
```

> ⚠️ Ključi morajo biti **nespremenljivi** (nizi, števila, nabori — ne pa seznami!).
> Zanka vrača ključe v vrstnem redu dodajanja (Python 3.7+).

### `setdefault` — krajša pot za "če ni, dodaj"

```python
# Klasično grupiranje v seznam vrednosti:
skupine = {}
for ime, mesto in [('Ana', 'LJ'), ('Bine', 'MB'), ('Cene', 'LJ')]:
    skupine.setdefault(mesto, []).append(ime)
# skupine = {'LJ': ['Ana', 'Cene'], 'MB': ['Bine']}
```

`setdefault(k, privzeto)` vrne `s[k]`, če obstaja, sicer ga nastavi na `privzeto` in vrne tega.

### `collections.Counter` in `collections.defaultdict`

Knjižnica `collections` ponuja **pripravljena** orodja za pogoste vzorce.

**`Counter`** je slovar za štetje pojavitev:

```python
from collections import Counter

c = Counter('abrakadabra')
# Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})

c.most_common(2)        # [('a', 5), ('b', 2)]   ← top 2
c['a']                  # 5
c['z']                  # 0  (manjkajoči ne sprožijo KeyError!)

# Lahko ga uporabimo tudi nad seznamom:
Counter(['jabolko', 'hruška', 'jabolko'])
# Counter({'jabolko': 2, 'hruška': 1})

# Counter podpira aritmetiko:
Counter('aab') + Counter('abc')   # Counter({'a': 3, 'b': 2, 'c': 1})
```

**`defaultdict`** je slovar s **privzeto vrednostjo** za neobstoječe ključe:

```python
from collections import defaultdict

skupine = defaultdict(list)   # privzeta vrednost = prazen seznam
for ime, mesto in [('Ana', 'LJ'), ('Bine', 'MB'), ('Cene', 'LJ')]:
    skupine[mesto].append(ime)
# defaultdict(<class 'list'>, {'LJ': ['Ana', 'Cene'], 'MB': ['Bine']})

# defaultdict(int) za štetje:
stevec = defaultdict(int)
for znak in 'abrakadabra':
    stevec[znak] += 1
# defaultdict(<class 'int'>, {'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
```

### Množice

```python
mn = {1, 2, 3, 4}     # množica
prazna = set()         # prazen set (ne {} — to je slovar!)

# Vsak element se pojavi ENKRAT, vrstni red je nepredvidljiv.

# Operacije:
{1,2,3} | {3,4,5}    # {1,2,3,4,5}  unija
{1,2,3} & {3,4,5}    # {3}          presek
{1,2,3} - {3,4,5}    # {1,2}        razlika
3 in {1,2,3}          # True
len({1,2,2,3})        # 3  (duplikati se ignorirajo)

# Metode:
mn.add(5)             # doda element
mn.update([6, 7])     # doda več elementov
mn.remove(5)          # odstrani (napaka, če ni)
mn.discard(5)         # odstrani (brez napake, če ni)
mn.pop()              # odstrani in vrne naključni element

mn |= {8, 9}          # unija na mestu
mn &= {1, 2}          # presek na mestu
mn -= {1}             # razlika na mestu
```

```python
# Izpeljane množice:
{f(x) for x in a}
{abs(x) for x in {1, -3, 2, -5}}   # {1, 2, 3, 5}
```

**Razlika med seznam in množico:**
- **Seznam**: urejen, dovoljuje duplikate, `in` je počasen (O(n))
- **Množica**: neurejen, brez duplikatov, `in` je hiter (O(1))

---

## 13. Razredi

```python
class ImeRazreda:
    """Dokumentacijski niz razreda."""

    def __init__(self, arg1, arg2):
        """Inicializacijska metoda — kliče se ob ustvaritvi objekta."""
        self.atribut1 = arg1    # self.xxx so atributi objekta
        self.atribut2 = arg2

    def metoda(self, x):
        """Navadna metoda — prvi argument je vedno self."""
        return self.atribut1 + x

# Ustvarjanje objekta:
obj = ImeRazreda(10, 20)

# Dostop do atributov in metod:
obj.atribut1       # 10
obj.metoda(5)      # 15
```

### Posebne metode

```python
class AritmeticnoZaporedje:
    def __init__(self, a, d):
        self.a = a    # začetni člen
        self.d = d    # razlika

    def __repr__(self):
        """Izpis v konzoli — za razvijalce."""
        return f"AritmeticnoZaporedje({self.a}, {self.d})"

    def __str__(self):
        """Izpis z print() — za uporabnike."""
        return f"{self.a}, {self.a+self.d}, {self.a+2*self.d}, ..."

    def __getitem__(self, i):
        """Podpre z [i] dostop."""
        return self.a + i * self.d

    def __contains__(self, x):
        """Podpre operator in."""
        return (x - self.a) % self.d == 0

    def __add__(self, other):
        """Podpre operator +."""
        return AritmeticnoZaporedje(self.a + other.a, self.d + other.d)

    def __eq__(self, other):
        """Podpre operator ==."""
        return self.a == other.a and self.d == other.d

    def __len__(self):
        """Podpre len()."""
        return ...

    def __lt__(self, other):
        """Podpre operator <. Podobno: __le__, __gt__, __ge__."""
        return ...
```

| Posebna metoda | Kdaj se pokliče |
|---|---|
| `__init__(self, ...)` | ob `ImeRazreda(...)` |
| `__repr__(self)` | ob izpisu v konzoli |
| `__str__(self)` | ob `print(obj)` |
| `__add__(self, other)` | ob `obj1 + obj2` |
| `__sub__(self, other)` | ob `obj1 - obj2` |
| `__mul__(self, other)` | ob `obj1 * obj2` |
| `__eq__(self, other)` | ob `obj1 == obj2` |
| `__lt__(self, other)` | ob `obj1 < obj2` |
| `__getitem__(self, i)` | ob `obj[i]` |
| `__contains__(self, x)` | ob `x in obj` |
| `__len__(self)` | ob `len(obj)` |
| `__iter__(self)` | ob zanki `for x in obj` |
| `__next__(self)` | ob klicu `next(obj)` |

### Razširjena tabela posebnih metod

| Operator / uporaba | Posebna metoda |
|---|---|
| `obj + other` | `__add__` |
| `obj - other` | `__sub__` |
| `obj * other` | `__mul__` |
| `obj / other` | `__truediv__` |
| `obj // other` | `__floordiv__` |
| `obj % other` | `__mod__` |
| `obj ** other` | `__pow__` |
| `-obj` (unarni minus) | `__neg__` |
| `abs(obj)` | `__abs__` |
| `obj[i]` (branje) | `__getitem__` |
| `obj[i] = x` (pisanje) | `__setitem__` |
| `del obj[i]` | `__delitem__` |
| `obj(x, y)` (objekt kot funkcija!) | `__call__` |
| `bool(obj)`, `if obj:` | `__bool__` |
| `hash(obj)` | `__hash__` |
| `with obj:` | `__enter__`, `__exit__` |

### Razredne spremenljivke in metode

Atribut, ki ga pripisujemo razredu (ne posamičnemu objektu), je **razredna spremenljivka** — deljen je med vsemi objekti razreda.

```python
class Zival:
    # Razredna spremenljivka:
    stevilo_ustvarjenih = 0

    def __init__(self, ime):
        self.ime = ime    # atribut OBJEKTA
        Zival.stevilo_ustvarjenih += 1

a = Zival("Maček")
b = Zival("Pes")
Zival.stevilo_ustvarjenih    # 2
a.stevilo_ustvarjenih        # 2  (do razredne spremenljivke dostopa tudi objekt)
```

> ⚠️ Razredna spremenljivka **nikoli** ne sme biti spremenljiv objekt (seznam, slovar, množica). Enako kot pri privzetih argumentih bi se delila med vsemi objekti razreda in povzročila težko izsledljive napake.

### `__hash__` — za uporabo objektov v množicah in kot ključev slovarja

Če definiraš `__eq__`, je nujno definirati tudi `__hash__`, sicer postane objekt **nedoločljiv** (`unhashable`) in ga ni mogoče dati v množico ali uporabiti kot ključ.

```python
class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Pravilo: enaka objekta morata vrniti enak hash.
        # Najlažje: hash nabora atributov, ki sodelujejo v __eq__.
        return hash((self.x, self.y))

mn = {Tocka(1, 2), Tocka(3, 4), Tocka(1, 2)}
len(mn)   # 2 — duplikat se ujema z enim od prejšnjih
```

### `__bool__` — kdaj je objekt "truthy"

Pove Pythonu, ali je objekt v `if`, `while` ali z `bool()` resničen ali lažen. Brez te metode je vsak objekt po privzetku `True`.

```python
class Vrec:
    def __init__(self, predmeti=None):
        self.predmeti = predmeti or []

    def __bool__(self):
        return len(self.predmeti) > 0

v = Vrec()
if v:
    print("Vreča ni prazna.")   # se ne izvede
```

### `__call__` — objekt kot funkcija

Objekt s `__call__` lahko **kličemo** kot funkcijo (`obj(x)`). To je uporabno za predmete s stanjem, npr. parametrizirane računske operacije.

```python
class Polinom:
    def __init__(self, koeficienti):
        self.k = koeficienti    # od najnižje stopnje navzgor

    def __call__(self, x):
        rez = 0
        for k in reversed(self.k):
            rez = rez * x + k    # Hornerjeva shema
        return rez

p = Polinom([1, 2, 3])    # 3x² + 2x + 1
p(2)                       # 17
p(0)                       # 1
```

### Dedovanje

Razred lahko **podeduje** atribute in metode drugega razreda. To omogoča ponovno uporabo in razširjanje obstoječe funkcionalnosti.

```python
class Zival:
    def __init__(self, ime):
        self.ime = ime

    def pozdravi(self):
        return f"Pozdravljen, jaz sem {self.ime}."

class Pes(Zival):    # Pes podeduje od Zival
    def __init__(self, ime, pasma):
        super().__init__(ime)    # kliče Zival.__init__
        self.pasma = pasma

    def pozdravi(self):
        # Razširimo metodo iz nadrazreda:
        osnovno = super().pozdravi()
        return osnovno + f" Sem {self.pasma}."

p = Pes("Reks", "ovčar")
p.pozdravi()           # 'Pozdravljen, jaz sem Reks. Sem ovčar.'
isinstance(p, Zival)   # True — Pes JE Žival
isinstance(p, Pes)     # True
```

`super()` vrne objekt z dostopom do nadrazreda, kar nam omogoča klic nadrazredove različice metode (npr. ko `__init__` razširjamo, namesto da bi ga povsem prepisali).

### Verižni klici (vračanje `self`)

Vzorec, pri katerem metoda vrne `self`, da lahko klice verižimo:

```python
class Zid:
    def __init__(self):
        self.deli = []

    def opeka(self, barva):
        self.deli.append(f"[{barva}]")
        return self      # ← omogoči verigo

    def izpis(self):
        return ''.join(self.deli)

Zid().opeka("rdeča").opeka("modra").opeka("rdeča").izpis()
# '[rdeča][modra][rdeča]'
```

### `@property` — atribut kot rezultat metode

Z dekoratorjem `@property` se izračunana vrednost obnaša kot atribut (brez oklepajev), čeprav je v ozadju metoda. Uporabno za izpeljane količine.

```python
class Krog:
    def __init__(self, polmer):
        self.polmer = polmer

    @property
    def ploscina(self):
        return 3.14159 * self.polmer ** 2

    @property
    def obseg(self):
        return 2 * 3.14159 * self.polmer

k = Krog(5)
k.ploscina     # 78.53975   ← brez oklepajev, izgleda kot atribut
k.obseg        # 31.4159
```

---

## 14. Iteratorji, generatorji in iterabilni objekti

### Iteratorji

Objekt z metodo `__next__`, ki vrača naslednji element. Ko ni več elementov, sproži `StopIteration`.

```python
class IteratorCezNiz:
    def __init__(self, niz):
        self.niz = niz
        self.indeks = 0

    def __next__(self):
        if self.indeks < len(self.niz):
            znak = self.niz[self.indeks]
            self.indeks += 1
            return znak
        else:
            raise StopIteration

it = IteratorCezNiz('abc')
next(it)   # 'a'
next(it)   # 'b'
next(it)   # 'c'
next(it)   # StopIteration
```

### Generatorji

Lažji način pisanja iteratorjev — z `yield` namesto `return`.

```python
def znaki_niza(niz):
    i = 0
    while i < len(niz):
        yield niz[i]    # "vrni in pavziraj"
        i += 1

gen = znaki_niza('abc')
next(gen)   # 'a'
next(gen)   # 'b'
```

```python
# Neskončni generator (Fibonaccijeva števila):
def fibonaccijeva_stevila(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b

f = fibonaccijeva_stevila()
[next(f) for _ in range(10)]   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Iterabilni objekti

Objekt, ki **ni** iterator, a iz njega **lahko** dobimo iterator (prek `__iter__`). Zanki `for` to naredi samodejno.

```python
class AritmeticnoZaporedje:
    def __init__(self, a, d):
        self.a = a
        self.d = d

    def __iter__(self):
        """Vrne generator — to naredi objekt iterabilen."""
        x = self.a
        while True:
            yield x
            x += self.d

zap = AritmeticnoZaporedje(2, 5)
for x in zap:
    print(x)
    if x > 20:
        break
# 2, 7, 12, 17, 22
```

**Razlika:**
- **Iterator**: ima `__next__`, pauzira in nadaljuje, "zapomni si" stanje.
- **Iterabilni objekt**: ima `__iter__`, ki vrne (svež) iterator.
- **Generator**: posebna vrsta iteratorja, narejen s funkcijo z `yield`.

### Generatorski izrazi

Kot izpeljani seznami, a z okroglimi oklepaji — **ne** ustvarijo celotnega seznama v pomnilniku, ampak vrednosti generirajo sproti:

```python
[x**2 for x in range(10)]    # SEZNAM — vseh 10 vrednosti je v pomnilniku
(x**2 for x in range(10))    # GENERATOR — vrednosti se računajo sproti

# Pri velikih (ali neskončnih) količinah podatkov:
sum(x**2 for x in range(10**8))    # učinkovito, brez seznama v pomnilniku

# Pri funkcijah, ki sprejmejo iterable, oklepajev sploh ne rabimo:
any(x > 100 for x in stevila)       # vrne True takoj, ko najde prvega
all(x > 0 for x in stevila)         # vrne False takoj, ko najde prvega <=0
max(len(b) for b in besede)
```

**Razlika v praksi:**

| | Izpeljani seznam `[...]` | Generatorski izraz `(...)` |
|---|---|---|
| Pomnilnik | shrani vse | drsi po enem elementu |
| Hitrost ustvarjanja | naredi vse takoj | lenobno |
| Lahko ga gledamo večkrat | ja | ne (po prvem prehodu prazen) |
| Podpira `len()`, indeksiranje | ja | ne |

`any` in `all` na generatorjih sta še posebej močna, ker se ustavita ob prvem zadetku (kratki stik):

```python
def vsebuje_negativno(sez):
    return any(x < 0 for x in sez)
```

---

## 15. Datoteke

### Branje datotek

```python
# Osnovno odpiranje (priporočeno z with):
with open('datoteka.txt', encoding='UTF-8') as dat:
    vsebina = dat.read()         # prebere VSE naenkrat
```

```python
with open('datoteka.txt', encoding='UTF-8') as dat:
    prva = dat.readline()        # prebere ENO vrstico
    vse = dat.readlines()        # seznam vseh preostalih vrstic
```

```python
# Sprehod po vrsticah (najprimernejše):
with open('datoteka.txt', encoding='UTF-8') as dat:
    for st, vrstica in enumerate(dat, 1):
        print(st, vrstica, end='')    # end='' ker vrstica že vsebuje \n
```

> ⚠️ Na **Windowsih** vedno dodaj `encoding='UTF-8'`, drugače bo privzeto `cp1250`.

### Pisanje datotek

```python
# 'w' — pisanje (povozi obstoječo vsebino):
with open('izhod.txt', 'w', encoding='UTF-8') as dat:
    dat.write('To je en stavek.\n')
    print('To gre v datoteko.', file=dat)

# 'a' — dodajanje (append, ne povozi):
with open('izhod.txt', 'a', encoding='UTF-8') as dat:
    dat.write('Ta vrstica se doda na konec.\n')
```

### Knjižnica os

```python
import os

os.getcwd()                    # trenutni imenik
os.chdir('pot/do/imenika')     # zamenjaj imenik
os.listdir()                   # seznam datotek v trenutnem imeniku
os.listdir('slike')            # seznam datotek v imeniku 'slike'

os.mkdir('nov_imenik')         # naredi imenik
os.makedirs('a/b/c', exist_ok=True)  # naredi gnezdene imenike
os.rename('staro.txt', 'novo.txt')   # preimenuj
os.remove('datoteka.txt')     # pobriši datoteko
os.rmdir('imenik')            # pobriši prazen imenik

# Delo s potmi:
os.path.join('mapa', 'podmapa', 'dat.txt')  # 'mapa/podmapa/dat.txt'
os.path.exists('pot')          # True, če pot obstaja
os.path.isdir('pot')           # True, če je imenik
os.path.split('/a/b/dat.txt')  # ('/a/b', 'dat.txt')
os.path.basename('/a/b/dat.txt') # 'dat.txt'
os.path.dirname('/a/b/dat.txt')  # '/a/b'
os.path.splitext('dat.txt')    # ('dat', '.txt')
os.path.abspath('.')           # absolutna pot
```

**Absolutna pot** (od korenskega imenika): `/home/user/uvp/datoteka.txt`
**Relativna pot** (glede na trenutni imenik): `../datoteke/vhodna.txt`
`..` = imenik višje, `.` = trenutni imenik

### JSON

```python
import json

# Python → JSON niz:
json.dumps([1, {'a': True, 'b': None}])
# '[1, {"a": true, "b": null}]'

# JSON niz → Python:
json.loads('[1, {"a": true, "b": null}]')
# [1, {'a': True, 'b': None}]

# Zapis v datoteko:
with open('podatki.json', 'w') as dat:
    json.dump({'ime': 'Janez', 'starost': 25}, dat, indent=4)

# Branje iz datoteke:
with open('podatki.json') as dat:
    podatki = json.load(dat)
```

**Mapping Python ↔ JSON:**

| Python | JSON |
|--------|------|
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| `dict` | objekt `{}` |
| `list` | matrika `[]` |
| `str` | niz `"..."` |
| `int` / `float` | število |

---

## 16. Regularni izrazi

```python
import re
```

### Vzorci za znake

| Vzorec | Ujema se z |
|--------|-----------|
| `.` | katerikoli znak (razen `\n`) |
| `\d` | števka `[0-9]` |
| `\D` | ni števka |
| `\w` | besedni znak `[a-zA-Z0-9_]` |
| `\W` | ni besedni znak |
| `\s` | beli znak (presledek, `\t`, `\n`) |
| `\S` | ni beli znak |
| `\b` | meja besede (ničelna širina) |
| `\B` | ni meja besede |
| `[abc]` | a, b ali c |
| `[a-z]` | katerakoli mala črka |
| `[^abc]` | karkoli razen a, b, c |
| `\\.` | dobesedna pika (ubežan posebni znak) |

> Regex pišemo v surovih nizih: `r'\d+'` (da se izognemo dvojnim poševnicam)

### Kvantifikatorji

| Vzorec | Pomen |
|--------|-------|
| `*` | 0 ali večkrat (požrešen) |
| `+` | 1 ali večkrat (požrešen) |
| `?` | 0 ali enkrat |
| `*?` | 0 ali večkrat (nepohlepen) |
| `+?` | 1 ali večkrat (nepohlepen) |
| `{m}` | točno m-krat |
| `{m,n}` | med m in n-krat |
| `{m,}` | vsaj m-krat |
| `{,n}` | največ n-krat |

```python
# Požrešen vs nepohlepen:
re.findall(r'd.*a',  'Oddal sem davčno napoved')   # ['dal sem da']  (dolg)
re.findall(r'd.*?a', 'Oddal sem davčno napoved')   # ['da', 'da']   (kratek)
```

### Funkcije knjižnice re

```python
re.search(r'\d+', 'abc 123 def')     # Match object za '123' (prva pojavitev)
re.match(r'\d+', '123 abc')          # Match object (le od začetka)
re.fullmatch(r'\d+', '123')          # Match object (celoten niz)
re.findall(r'\d+', 'a1 b22 c3')      # ['1', '22', '3']
re.finditer(r'\d+', 'a1 b22 c3')     # iterator Match objektov
re.split(r'[,;]', 'a,b;c')           # ['a', 'b', 'c']
re.sub(r'\d+', 'X', 'a1 b22')        # 'aX bX'  (zamenjaj)
```

### Match objekt

```python
m = re.search(r'(\d+) (\w+)', '500 g moke')
m.group(0)    # '500 g'  (celotna pojavitev)
m.group(1)    # '500'    (1. skupina)
m.group(2)    # 'g'      (2. skupina)
m.start()     # 0
m.end()       # 5
m.span()      # (0, 5)
```

### Poimenovane skupine

```python
vzorec = r'(?P<kolicina>\d+) (?P<enota>\w+)'
m = re.search(vzorec, '500 g moke')
m.group('kolicina')    # '500'
m.group('enota')       # 'g'
m.groupdict()          # {'kolicina': '500', 'enota': 'g'}
```

### Zastavice

```python
re.search(r'abc', 'ABC', flags=re.IGNORECASE)    # ne razlikuj velikih/malih
re.findall(r'X.*?Y', tekst, flags=re.DOTALL)     # . ujame tudi \n
re.search(r'...', tekst, flags=re.IGNORECASE | re.DOTALL)  # kombinacija
```

### Kompiliran vzorec (za večkratno uporabo)

```python
izraz = re.compile(r'(?P<kolicina>\d+) (?P<enota>\w+)', flags=re.IGNORECASE)
izraz.findall('500 g moke in 250 ml vode')
```

### Pogosti vzorci

```python
r'\d+'               # ena ali več števk
r'\w+'               # ena ali več besednih znakov (beseda)
r'\s+'               # ena ali več belih znakov
r'[A-Z][a-z]+'       # beseda z veliko začetnico
r'\b\w+\b'           # cela beseda
r'https?://\S+'      # URL
r'\d{1,2}\.\d{1,2}\.\d{4}'  # datum dd.mm.yyyy
r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # email
```

---

## 17. Koristne vgrajene funkcije — hiter pregled

```python
# Tipi in pretvorbe:
int(x)         # pretvori v celo število
float(x)       # pretvori v decimalno število
str(x)         # pretvori v niz
bool(x)        # pretvori v logično vrednost
list(x)        # pretvori v seznam
tuple(x)       # pretvori v nabor
set(x)         # pretvori v množico
dict(...)      # naredi slovar

# Matematika:
abs(x)         # absolutna vrednost
round(x, n)    # zaokroži na n decimalk
pow(x, y)      # x ** y
divmod(a, b)   # (a // b, a % b) hkrati

# Zaporedja:
len(x)         # dolžina
sum(x)         # vsota
min(x)         # minimum
max(x)         # maksimum
sorted(x)      # vrne nov urejen seznam
reversed(x)    # vrne iterator (obrnjen)
enumerate(x)   # vrne iterator (indeks, vrednost)
zip(x, y, ...) # vrne iterator naborov istoležnih elementov
range(n)       # 0, 1, ..., n-1
range(a, b)    # a, a+1, ..., b-1
range(a, b, k) # a, a+k, ..., do b-1

# I/O:
print(...)     # izpiše na konzolo
input(prompt)  # prebere vrstico s konzole

# Preverjanje tipov:
type(x)        # vrne tip objekta
isinstance(x, int)  # True, če je x tipa int

# Drugi:
help(f)        # izpiše dokumentacijo funkcije f
dir(obj)       # izpiše atribute/metode objekta
id(x)          # identifikator objekta (naslov v pomnilniku)
hash(x)        # hash vrednost (za nespremenljive objekte)
```

---

## 17½. Časovna zahtevnost — kratek pregled

Za pisni izpit je dobro vedeti, **katere operacije so hitre** in katere ne. Spodaj je tipičen Python s seznamom `n` elementov.

### Seznami `[]`

| Operacija | Zahtevnost | Opomba |
|-----------|:---:|---|
| `sez[i]` (dostop) | O(1) | hitro |
| `sez[i] = x` (zamenjava) | O(1) | hitro |
| `len(sez)` | O(1) | shranjeno posebej |
| `sez.append(x)` | O(1) | amortizirano |
| `sez.pop()` (zadnji) | O(1) | |
| `sez.pop(0)` ali `sez.insert(0, x)` | **O(n)** | premakniti je treba vse |
| `x in sez` | **O(n)** | |
| `sez.sort()` | O(n log n) | |

### Slovarji `{}` in množice `set`

| Operacija | Zahtevnost |
|-----------|:---:|
| `slovar[k]`, `slovar[k] = v`, `k in slovar` | **O(1)** |
| `k in mn`, `mn.add(x)`, `mn.remove(x)` | **O(1)** |

### Nizi

Nizi so **nespremenljivi** — vsako "spreminjanje" naredi nov niz:

```python
# SLABO — O(n²): vsak += naredi nov niz cele dolžine
rez = ''
for x in sez:
    rez += str(x)

# DOBRO — O(n): v seznam, nato join na koncu
deli = []
for x in sez:
    deli.append(str(x))
rez = ''.join(deli)
```

### Praktične implikacije

```python
# Iskanje v 1 000 000 elementov:
x in seznam       # do milijona primerjav
x in mnozica      # ena operacija!

# Če veliko preverjamo `x in nekaj`, raje pretvori v množico:
veliki = set(velik_seznam)
[x for x in y if x in veliki]    # zdaj hitro
```

---

## 18. Algoritemski vzorci

Pogosti vzorci, ki se pojavljajo pri reševanju nalog.

### Akumulator (vsota, produkt, štetje)

```python
# Vsota
vsota = 0
for x in sez:
    vsota += x

# Produkt
produkt = 1
for x in sez:
    produkt *= x

# Štetje elementov, ki ustrezajo pogoju
stevec = 0
for x in sez:
    if pogoj(x):
        stevec += 1
```

### Iskanje minimuma / maksimuma ročno

```python
naj = sez[0]
for x in sez[1:]:
    if x > naj:
        naj = x
# naj je sedaj maksimum

# Z vgrajeno funkcijo (krajše):
naj = max(sez)
```

### Filtriranje

```python
# Z zanko:
novi = []
for x in sez:
    if pogoj(x):
        novi.append(x)

# Z izpeljanim seznamom (krajše):
novi = [x for x in sez if pogoj(x)]
```

### Štetje pojavitev v slovar

```python
stevila = {}
for x in seznam:
    stevila[x] = stevila.get(x, 0) + 1
```

### Sklad (stack) — npr. preverjanje gnezdenja oklepajev

```python
def gnezdeni_oklepaji(niz):
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

Logika: uklepaje tlačimo na sklad (`append`), ob zaklepaju preverimo vrh (`pop`). Na koncu mora biti sklad prazen.

### Matrike (seznam seznamov)

```python
mat = [[1, 2, 3],
       [4, 5, 6]]

mat[i][j]           # element v vrstici i, stolpcu j
len(mat)            # število vrstic
len(mat[0])         # število stolpcev

# Iteracija po vseh elementih:
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j])

# Ustvarjanje matrike n×m z ničlami:
mat = [[0] * m for _ in range(n)]
# POZOR: ne piši [[0]*m]*n — vse vrstice bi bile isti objekt!
```

### Iteracija s koordinatami

Krajše in berljiveje kot `range(len(...))`:

```python
for i, vrstica in enumerate(mat):
    for j, vrednost in enumerate(vrstica):
        print(i, j, vrednost)
```

### Dostop do stolpcev in diagonal

```python
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# Stolpec j (z izpeljanim seznamom):
[vrstica[2] for vrstica in mat]   # [3, 6, 9]

# Glavna diagonala:
[mat[i][i] for i in range(len(mat))]              # [1, 5, 9]

# Protidiagonala:
[mat[i][-1-i] for i in range(len(mat))]           # [3, 5, 7]
```

### Transponiranje z `zip(*mat)`

Eleganten trik z razpakiranjem: `*mat` razdeli matriko na posamezne vrstice, `zip` pa potem iz njih sestavi stolpce.

```python
mat = [[1, 2, 3],
       [4, 5, 6]]

list(zip(*mat))
# [(1, 4), (2, 5), (3, 6)]

# Če bi raje seznam seznamov kot seznam naborov:
[list(v) for v in zip(*mat)]
# [[1, 4], [2, 5], [3, 6]]
```

### Sosedi v matriki (zelo pogost vzorec na izpitih!)

```python
# 4 sosedi (gor/dol/levo/desno):
def sosedi(mat, i, j):
    rez = []
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]):
            rez.append(mat[ni][nj])
    return rez

# 8 sosedov (z diagonalami):
smeri_8 = [(di, dj) for di in [-1, 0, 1]
                    for dj in [-1, 0, 1]
                    if (di, dj) != (0, 0)]
```

Ta vzorec se pojavi pri igri življenja, flood fill, iskanju poti, štetju mož v okolici ipd.

### Sploščenje in razgradnja v matriko

```python
# Matrika -> ravni seznam:
ravno = [x for vrstica in mat for x in vrstica]

# Ravni seznam dolžine n*m -> matrika n vrstic po m elementov:
mat = [ravno[i*m:(i+1)*m] for i in range(n)]
```

### Kopiranje matrik

Pri **gnezdenih** strukturah `mat[:]` ne zadošča (gl. tudi poglavje 11 o aliasih):

```python
mat = [[1, 2], [3, 4]]

# NAROBE — vrstice so še vedno deljene:
kopija = mat[:]
kopija[0][0] = 99
mat   # [[99, 2], [3, 4]]   ← spremenil se je!

# PRAVILNO — vsako vrstico posebej:
kopija = [vrstica[:] for vrstica in mat]
# ali: kopija = [list(v) for v in mat]
# ali: import copy; kopija = copy.deepcopy(mat)
```

### Klasične matrične operacije

```python
# Skalarno množenje:
def pomnozi_s_skalarjem(mat, k):
    return [[k * x for x in vrstica] for vrstica in mat]

# Seštevanje matrik iste velikosti:
def vsota_matrik(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

# Množenje matrik (A je n×k, B je k×m, rezultat n×m):
def pomnozi_matriki(A, B):
    n, k, m = len(A), len(B), len(B[0])
    rez = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for s in range(k):
                rez[i][j] += A[i][s] * B[s][j]
    return rez
```

### Rotacije in zrcaljenja

```python
# Rotacija za 90° v desno:
def zavrti_desno(mat):
    return [list(v) for v in zip(*mat[::-1])]

# Rotacija za 90° v levo:
def zavrti_levo(mat):
    return [list(v) for v in zip(*mat)][::-1]

# Zrcaljenje gor/dol:
[vrstica[:] for vrstica in mat[::-1]]

# Zrcaljenje levo/desno:
[vrstica[::-1] for vrstica in mat]
```

### Praktičen primer: en korak igre življenja

```python
def naslednji_korak(mat):
    n, m = len(mat), len(mat[0])
    nov = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # preštej žive sosede
            zivi = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di, dj) == (0, 0):
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        zivi += mat[ni][nj]
            # pravila Conwayja
            if mat[i][j] == 1 and zivi in (2, 3):
                nov[i][j] = 1
            elif mat[i][j] == 0 and zivi == 3:
                nov[i][j] = 1
    return nov
```

---

## 19. Pretvorbe baz (binarno, šestnajstiško, ...)

```python
# Iz desetiškega v druge baze:
bin(10)        # '0b1010'  (binarna)
oct(8)         # '0o10'    (osmiška)
hex(255)       # '0xff'    (šestnajstiška)

# Iz druge baze v desetiško:
int('1010', 2)   # 10   (iz binarne)
int('ff', 16)    # 255  (iz šestnajstiške)
int('17', 8)     # 15   (iz osmiške)
```

```python
# Splošna pretvorba iz niza v dani bazi v desetiško:
import string

def pretvori(niz, baza):
    """Pretvori niz v dani bazi v desetiško število."""
    znaki = '0123456789' + string.ascii_uppercase
    rezultat = 0
    for znak in niz.upper():
        rezultat = rezultat * baza + znaki.index(znak)
    return rezultat

pretvori('FF', 16)    # 255
pretvori('1010', 2)   # 10
```

Rekurzivna različica (en znak = zadnji, preostanek rekurzivno):
```python
def pretvori(niz, baza):
    znaki = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if niz == '':
        return 0
    return pretvori(niz[:-1], baza) * baza + znaki.index(niz[-1].upper())
```
