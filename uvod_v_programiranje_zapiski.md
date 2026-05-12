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
17. [Koristne vgrajene funkcije — hiter pregled](#18-koristne-vgrajene-funkcije--hiter-pregled)

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

*Zapiski sledijo učbeniku Matije Pretnarja — Uvod v programiranje (2022).*
*Dodano: vgrajene funkcije, iskanje z bisekcijo.*
