# PLONK — Uvod v programiranje

Tipi izpitnih nalog z vzorčno kodo, izpiti 2022–2025.
**Najdi tip → poglej vzorec → prilagodi.**

> Markdown različica datoteke `plonk_uvod_v_programiranje.html`.
> GitHub jo prikaže neposredno, brez posrednika.

## Kazalo

- [TIP 1: RAZREDI (Classes)](#tip-1-razredi-classes)
    - [RAZREDI — osnovna struktura](#razredi--osnovna-struktura)
- [TIP 2: DATOTEKE (File I/O)](#tip-2-datoteke-file-io)
    - [BRANJE IN PISANJE DATOTEK](#branje-in-pisanje-datotek)
    - [PISANJE DATOTEK — vzorci](#pisanje-datotek--vzorci)
- [TIP 3: REKURZIJA & SIMULACIJA](#tip-3-rekurzija--simulacija)
    - [REKURZIJA](#rekurzija)
    - [SIMULACIJA / IZŠTEVANKE](#simulacija--izštevanke)
    - [ISKANJE V MREŽI (grid)](#iskanje-v-mreži-grid)
- [TIP 4: NIZI, REGEX & SLOVARJI](#tip-4-nizi-regex--slovarji)
    - [NIZI — obdelava](#nizi--obdelava)
    - [REGEX — vzorci](#regex--vzorci)
    - [SLOVARJI — vzorci](#slovarji--vzorci)
- [TIP 5: DREVESA & GRAFOVSKE STRUKTURE](#tip-5-drevesa--grafovske-strukture)
    - [DREVESA (objekti, ki kažejo drug na drugega)](#drevesa-objekti-ki-kažejo-drug-na-drugega)
    - [GRAFI (dostopnost, povezave)](#grafi-dostopnost-povezave)
- [TIP 6: IGRE NA TABELI](#tip-6-igre-na-tabeli)
    - [ŠTIRI V VRSTO — vzorec igre na tabeli](#štiri-v-vrsto--vzorec-igre-na-tabeli)
    - [KORISTNI VZORCI](#koristni-vzorci)
- [QUICK REFERENCE — Python sintaksa za izpit](#quick-reference--python-sintaksa-za-izpit)
    - [VGRAJENE FUNKCIJE](#vgrajene-funkcije)
    - [COMPREHENSIONS & LAMBDA](#comprehensions--lambda)
    - [KAKO PREPOZNATI TIP NALOGE](#kako-prepoznati-tip-naloge)

---

## TIP 1: RAZREDI (Classes)

### RAZREDI — osnovna struktura
*Pojavilo se je na: Pesnik France (1.izpit 2023/24), Oseba (3.izpit 2023/24), Naseljenec (1.izpit 2024/25), Dvigalo (2.izpit 2024/25), Kristal (1.izpit 2022/23), Zabar (2.izpit 2022/23), StiriVVrsto (3.izpit 2022/23), Oseba/Imenik (3.izpit 2024/25)*
```python
class ImeRazreda:
    def __init__(self, arg1, arg2, opt=None):
        self.arg1 = arg1
        self.arg2 = arg2
        # pozor: mutable default!
        self.seznam = opt if opt is not None else []
        self.slovar = {}

    def __repr__(self):
        # simulira klic konstruktorja
        return f"ImeRazreda({self.arg1!r}, {self.arg2!r})"

    def __str__(self):
        # človeško berljiv opis
        return f"{self.arg1} {self.arg2}"

    def __lt__(self, other):
        # za primerjavo / sortiranje
        return self.arg1 < other.arg1

    def __getitem__(self, i):
        # za obj[i] dostop
        return self.seznam[i]
```
```python
# DEDOVANJE (podrazred razširi obstoječ)
class PodRazred(ImeRazreda):
    def nova_metoda(self, x):
        return x

# INSTANCE CHECK
isinstance(obj, ImeRazreda)  # → True/False

# SORTED z razredom kot ključem
sorted(seznam, key=ImeRazreda)

# MUTABLE DEFAULT — PAZI!
# NAPAČNO:
def __init__(self, lst=[]):  # ← bug!
# PRAVILNO:
def __init__(self, lst=None):
    self.lst = lst if lst is not None else []

# TIPIČNI ATRIBUTI:
self.ime = ime
self.otroci = []
self.stars = None
self.dobrine = {}
self.na_potezi = '*'
```
```python
# RAZRED Z LOGIKO — Dvigalo primer
class Dvigalo:
    def __init__(self, nd=0, post=None):
        self.nadstropje = nd
        self.postanki = post or []

    def razdalja(self, cilj):
        if not self.postanki:
            return abs(cilj - self.nadstropje)
        r = abs(self.nadstropje - self.postanki[0])
        for i in range(len(self.postanki)-1):
            r += abs(self.postanki[i]
                   - self.postanki[i+1])
        r += abs(self.postanki[-1] - cilj)
        return r

# RAZRED Z get/set na slovarju
def ropa(self, st, dobrina):
    curr = self.rop.get(st, [])
    curr.append(dobrina)
    self.rop[st] = curr

def usoda(self, st):
    d = self.rop.get(st, [])
    self.dobrine.extend(d)
    return d
```
> **Opozorilo.** **Stolpca si nasprotujeta.** Sredinski pravilno pravi `lst if lst is not None else []`, desni pa pri `Dvigalo` uporablja `post or []`. Nista enakovredna: `or` zamenja *vsako* lažno vrednost, torej tudi prazen seznam, ki ga klicatelj poda namenoma. Vedno piši `is not None`.
> **Namig.** KLJUČNE BESEDE v navodilu → razred: "definirajte razred", "konstruktor", "metoda", "atribut", "__str__", "__repr__"

---

## TIP 2: DATOTEKE (File I/O)

### BRANJE IN PISANJE DATOTEK
*Pojavilo se je na: Avtobusni prevozi (1.izpit 2023/24), Potapljanje ladjic (1.izpit 2024/25), Vročinski valovi (1.izpit 2022/23), Prijave (2.izpit 2022/23), Orientacijski tek (3.izpit 2024/25)*
```python
# BRANJE — osnova
with open(dat, encoding='utf-8') as f:
    for vrstica in f:
        vrstica = vrstica.strip()
        # ...obdelaj...

# PRESKOČI GLAVO
next(f)  # ali f.readline()

# RAZDELI PO VEJICI
deli = vrstica.split(',')
a, b, c = vrstica.strip().split(',')

# BRANJE CELE DATOTEKE
vsebina = f.read()
vrstice = f.readlines()

# PISANJE
with open(dat, 'w', encoding='utf-8') as f:
    f.write("tekst\n")
    print(tekst, file=f)  # samodejni \n
```
```python
# NAVODILO IZI: "začne s številko / s črko"
if vrstica[0].isdigit():   # → linija
if vrstica[0].isalpha():   # → postaja

# ZGRADBA SLOVAR iz datoteke (Avtobusi)
slovar = {}
trenutna = None
for v in f:
    v = v.strip()
    if v[0].isdigit():
        trenutna = v
        slovar[trenutna] = []
    else:
        slovar[trenutna].append(v)

# PISANJE S PUŠČICO
print(f"{ime}: {' -> '.join(sez)}", file=f)

# MANJKAJOČE VREDNOSTI (CSV)
val = -99.9 if len(s)==0 else float(s)
```
> **Namig.** NAVODILO → "preberi iz datoteke", "zapiši v datoteko", "vrstice", "CSV", "stolpci"

### PISANJE DATOTEK — vzorci
```python
# ROB (Potapljanje ladjic)
f.write('/' + '-'*n + '\\\n')
for v in plosca:
    f.write('|' + ''.join(v) + '|\n')
f.write('\\' + '-'*n + '/')

# RAZPOREJANJE V SKUPINE
if skupina:
    f.write("Skupina:\n")
    for x in sorted(skupina):
        f.write(f"- {x}\n")
    f.write("\n")  # prazna vrstica med skupinami

# PRESTEJ VRSTICE (ignorira # in prazne)
def prestej_vrstice(dat):
    u = 0
    with open(dat, encoding='utf-8') as f:
        for v in f:
            v = v.strip()
            if v and v[0] != '#': u += 1
    return u
```

---

## TIP 3: REKURZIJA & SIMULACIJA

### REKURZIJA
*Pojavilo se je na: Urejanje z zlivanjem (1.izpit 2023/24), Žabe/poti (1.izpit 2022/23), Gnezdenje (3.izpit 2023/24), Geslo v mapah (3.izpit 2022/23)*
```python
# OSNOVA REKURZIJE:
# 1. bazni primer (ko se ustavi)
# 2. rekurzivni klic (manjši problem)

# UREJANJE Z ZLIVANJEM
def uredi(s):
    if len(s) <= 1: return s  # baza!
    pol = len(s) // 2
    return zlij(uredi(s[:pol]), uredi(s[pol:]))

# ŠTETJE VARNIH POTI (grid, le ↓ in →)
def prestej_varne_poti(z, i, j):
    if not z[i][j]: return 0
    if i==0 and j==0: return 1
    poti = 0
    if i > 0: poti += prestej_varne_poti(z,i-1,j)
    if j > 0: poti += prestej_varne_poti(z,i,j-1)
    return poti

# ISKANJE V GNEZDENEM SLOVARJU
def najdi_geslo(r):
    if 'geslo.txt' in r: return 'geslo.txt'
    for m, vseb in r.items():
        if vseb is not None:
            p = najdi_geslo(vseb)
            if p: return f"{m}/{p}"
    return None
```
> **Namig.** NAMIG v navodilu: "rekurzivno", "namig: rekurzija", ali "razdeli na pol"

### SIMULACIJA / IZŠTEVANKE
*Pojavilo se je na: Izštevanke (2.izpit 2023/24), Katan (1.izpit 2024/25), Žive žabe (1.izpit 2022/23)*
```python
# IZŠTEVANKE — indeks v krogu
def izlocen(sez, ime, st):
    x = sez.index(ime)
    for _ in range(st - 1):
        x = (x + 1) % len(sez)
    return sez[x]

# ZMAGOVALEC + KOPIJA seznama
def pri_kom_zaceti(igr, fav, dol):
    for zac in igr:
        if zmagovalec(igr.copy(), zac, dol)==fav:
            return zac

# POPULACIJSKA DINAMIKA (Lotka-Volterra)
def cez_nekaj_let(alfe, z, p, leta):
    a1,a2,a3,a4 = alfe
    for _ in range(leta):
        zn = z + a1*z - a2*z*p
        pn = p + a3*p + a4*z*p
        z, p = max(zn,0), max(pn,0)
    return z, p

# GOSTIŠČE — štej porcije
while True:
    if g >= p: g-=p; porc+=1; lok+=1
    elif lok >= l: lok-=l; porc+=1; lok+=1
    else: break
```

### ISKANJE V MREŽI (grid)
*Pojavilo se je na: Osmerosmerke (1.izpit 2024/25)*
```python
# 8 SMERI
smeri = [(-1,-1),(-1,0),(-1,1),
         (0,-1),          (0,1),
         (1,-1), (1,0), (1,1)]

# PREVERI BESEDO v smeri
def preveri(mreza, beseda, zac, smer):
    i, j = zac; di, dj = smer
    for crka in beseda:
        if (i<0 or j<0 or
            i>=len(mreza) or j>=len(mreza[0])
            or crka!=mreza[i][j]):
            return False
        i+=di; j+=dj
    return True

# ISKANJE — preizkusi vse start+smer
for i in range(len(mreza)):
  for j in range(len(mreza[0])):
    for di in (-1,0,1):
      for dj in (-1,0,1):
        if di==0 and dj==0: continue
        if preveri(mreza,b,(i,j),(di,dj)):
            return (i,j),(di,dj)
```

---

## TIP 4: NIZI, REGEX & SLOVARJI

### NIZI — obdelava
*Pojavilo se je na: France (vsi izpiti), Kodiranje base64, DNA analiza, Premetanke*
```python
# OSNOVE
niz.strip()         # odstrani \n, presledke
niz.split(',')       # razdeli po ločilu
niz.startswith(x)   # začne z x
niz[0].isdigit()    # je številka?
niz[0].isalpha()    # je črka?
''.join(sez)         # seznam → niz
' -> '.join(sez)     # z ločilom

# REZINE
s[::k]   # vsak k-ti element
s[i:i+3] # 3 znaki od i

# ZAMENJAVA PRINT→RETURN (France)
v = v[:-1].replace("print(", "return ")

# SORTIRANJE LEKSIKOGRAFSKO s custom key
abeceda = {'a':1,'b':2,'č':4, ...}
def __lt__(self, other):
    for i in range(min(len(self.b),len(other.b))):
        if ab[self.b[i]] < ab[other.b[i]]:
            return True
        elif ab[self.b[i]] > ab[other.b[i]]:
            return False
    return len(self.b) < len(other.b)
```

### REGEX — vzorci
*Pojavilo se je na: France popravki (2.izpit 2023/24), Čustveni znaki, France zlogi*
```python
import re

# NAJDI VSE
re.findall(r'\d+', niz)       # vsa števila
re.findall(r':[a-z]+:', niz)  # :custvencek:
re.findall(r'\b\w{2,}\b', n)  # besede 2+ znakov

# ZAMENJAJ
re.sub(r'\d+', 'nekaj', niz)  # prim. recept

# POENOSTAVITEV (x = x + n  →  x += n)
# Vzorec: ime = ime op vrednost
deli = vrstica.split()
if len(deli)==5 and deli[1]=='=':
    ime = deli[0]
    if deli[2]==ime:  # ime je levo
        return zamik+ime+" "+deli[3]+"= "+deli[4]

# SAMOGLASNIKI + R ki ni ob soglasniku
sam = len(re.findall(r'[aeiou]', b, re.I))
rji = len(re.findall(
    r'([^aeiou]|^)r([^aeiou]|$)', b, re.I))

# MNOŽICA iz findall
mnozica.update(re.findall(vzorec, niz))
```

### SLOVARJI — vzorci
*Pojavilo se je na: Piknik (2.izpit 2024/25), Pogosti znaki (3.izpit 2023/24), Prijave na izpit (2.izpit 2022/23)*
```python
# ŠTETJE POJAVITEV
slovar = {}
for x in niz:
    slovar[x] = slovar.get(x, 0) + 1

# ZBIRANJE VREDNOSTI (piknik)
zbir = {}
for pod in prispevki.values():
    for hrana, kol in pod.items():
        zbir[hrana] = zbir.get(hrana,0) + kol

# SORTIRANJE SLOVARJA po vrednosti
pari = list(slovar.items())
pari.sort(key=lambda x: (-x[1], x[0]))

# OBRNJEN SLOVAR
inv = {v: k for k, v in slovar.items()}

# MNOŽICA ključev za iskanje
if key not in slovar.keys():
    # ali krajše:
if key not in slovar:

# GNEZDENJE (nested sorting)
gnezdo = (znaki[0],)
for z in znaki[1:]:
    gnezdo = (z, gnezdo)
```
> **Opozorilo.** Odsek »množica ključev« je le prikaz obeh zapisov, **ne veljavna koda** — `if` brez telesa je `IndentationError`. Na izpitu piši krajšo obliko `if key not in slovar:`; `.keys()` ni potreben in je počasnejši.

---

## TIP 5: DREVESA & GRAFOVSKE STRUKTURE

### DREVESA (objekti, ki kažejo drug na drugega)
*Pojavilo se je na: Žabarji (2.izpit 2022/23), Oseba (3.izpit 2023/24 - s stars/otroci)*
```python
# DREVO — osnovna struktura
class Zabar:
    def __init__(self, ime, spol):
        self.ime = ime
        self.spol = spol
        self.stars = None   # kazalec gor
        self.otroci = []    # seznam dol

    def rojstvo(self, ime, spol):
        o = Zabar(ime, spol)
        o.stars = self     # starš → otrok
        self.otroci.append(o)
        return o

# SORODSTVENO RAZMERJE
def sorodstveno_razmerje(z1, z2):
    if z2.stars is z1:   # z1 je starš z2
        return "oče" if z1.spol=="M" else "mati"
    if (z1.stars is not None and
        z1.stars is z2.stars):  # ista starša
        return "brat" if z1.spol=="M" else "sestra"
    return "drugo"
```
```python
# SKUPNI PREDNIK — hodi gor po drevesu
def zadnji_skupni_prednik(z1, z2):
    pr1, pr2 = [], []
    while z1: pr1.append(z1); z1=z1.stars
    while z2: pr2.append(z2); z2=z2.stars
    for p in pr1:
        if p in pr2: return p.ime

# GENERACIJA — štej korake do vrha
def katera_generacija(z):
    gen = 1
    while z.stars is not None:
        gen += 1; z = z.stars
    return gen

# REZERVACIJE (Kristal)
def dodaj_rezervacijo(self, traj, zac=0):
    kand = zac
    for oz, ok in self.rezervacije:
        if kand + traj <= oz: break
        if kand < ok: kand = ok
    nova = (kand, kand+traj)
    i = 0
    while i<len(self.rez) and self.rez[i][0]<nova[0]:
        i+=1
    self.rez.insert(i, nova)
    return nova
```
> **Namig.** NAVODILO → "starš", "otrok", "predniki", "generacija", atributa "stars" in "otroci" navajata na drevo

### GRAFI (dostopnost, povezave)
*Pojavilo se je na: Avtobusni prevozi 3.podnaloga, Orientacijski tek*
```python
# OBSTAJA POVEZAVA z 1 prestopom
def obstaja_povezava(slovar, zac, kon):
    vse = []
    for p in slovar.values(): vse += p
    if zac not in vse or kon not in vse:
        return None
    for p1 in slovar.values():
        if zac in p1:
          for prestop in p1:
            for p2 in slovar.values():
              if prestop in p2 and kon in p2:
                return True
    return False

# VELJAVNOST TEKA (proga = seznam točk)
def je_veljaven(tek, proga):
    if tek[0][0]!="START" or tek[-1][0]!="CILJ":
        return False
    i = 0
    t_na_progi = set(proga)
    for tocka, _ in tek:
        if tocka == proga[i]: i += 1
        elif tocka in t_na_progi: return False
    return i == len(proga)
```

---

## TIP 6: IGRE NA TABELI

### ŠTIRI V VRSTO — vzorec igre na tabeli
*Pojavilo se je na: Štiri v vrsto (3.izpit 2022/23)*
```python
# INICIALIZACIJA TABELE
polje = [['.' for _ in range(s)]
          for _ in range(v)]

# POTEZA — padanje žetona
def poteza(self, s):
    if (s < 0 or s >= self.sirina() or
        self.polje[0][s] != '.'):
        return False
    v = 0
    while v<self.visina() and self.polje[v][s]=='.':
        v += 1
    self.polje[v-1][s] = self.na_potezi
    # zamenjaj igralca
    self.na_potezi = ('o' if self.na_potezi=='*'
                      else '*')
    return True
```
```python
# PREVERI STIRICO v smeri (di, dj)
def preveri_stirico(self, v, s, dv, ds):
    if (self.polje[v][s] == '.' or
        v+3*dv >= self.visina() or
        s+3*ds >= self.sirina()): return None
    for i in (1,2,3):
        if self.polje[v+i*dv][s+i*ds] != self.polje[v][s]:
            return None
    return self.polje[v][s]

# ZMAGOVALEC — preizkusi vse 4 smeri
def zmagovalec(self):
    for i in range(self.visina()):
      for j in range(self.sirina()):
        for d in ((1,0),(0,1),(1,1),(-1,1)):
          p = self.preveri_stirico(i,j,*d)
          if p: return p
    return None
```

### KORISTNI VZORCI
```python
# MIN Z INDEKSOM (Dvigalo klic)
sez = [d.razdalja(nd) for d in dvigala]
return sez.index(min(sez))

# ENUMERATE + filter
for i, (tocka, cas) in enumerate(tek):
    cas_delta = cas - tek[i-1][1] if i>0 else 0

# ZLIJ dva urejena seznama
def zlij(a, b):
    r = []
    while a and b:
        if a[0] <= b[0]: r.append(a.pop(0))
        else: r.append(b.pop(0))
    return r + a + b

# CIKLIČNI INDEKS (krog)
x = (x + 1) % len(sez)

# GNEZDENA TABELA
mat = [[' ']*s for _ in range(v)]
mat[i][j] = '#'  # pazi: ne mat[i] = [...]!
```
> **Opozorilo.** `zlij` zgoraj uporablja `a.pop(0)`: ta je O(n) na klic, zato zlivanje pade na O(n²), poleg tega pa **izprazni vhodna seznama**. Z indeksoma je enako dolgo in brez obeh slabosti: `i = j = 0` → primerjaj `a[i]` in `b[j]` → vrni `r + a[i:] + b[j:]`.

---

## QUICK REFERENCE — Python sintaksa za izpit

### VGRAJENE FUNKCIJE
```python
sorted(sez, key=fn, reverse=True)
min/max(sez, key=fn)
enumerate(sez)       # (i, el)
zip(a, b)            # pari
isinstance(obj, Cls) # preveri tip
abs(x)
round(x, 1)
float(s) / int(s)
set(sez)             # množica
dict.get(k, default)
dict.items() / .keys() / .values()
list.pop(i)          # odstrani+vrni
list.insert(i, x)    # vstavi na mesto
list.index(x)        # prvi pojav
list.copy()          # plitka kopija!
list.extend(other)   # dodaj vse elemente
list.count(x)        # koliko x v listi
str.join(sez)
str.strip() / lstrip() / rstrip()
str.split(sep)
str.replace(a, b)
str.find(sub)        # -1 če ni
str.count(sub)
str.isdigit() / isalpha() / islower()
```

### COMPREHENSIONS & LAMBDA
```python
# LIST COMPREHENSION
[x**2 for x in sez if x > 0]

# DICT COMPREHENSION
{k: v for k, v in slovar.items() if v > 0}

# SET COMPREHENSION
{x for x in sez}

# LAMBDA za sortiranje
pari.sort(key=lambda x: (-x[1], x[0]))

# FILTER
[z for i, z in enumerate(s) if i%k == 0]

# VZOREC: pogostost znakov
from collections import Counter
Counter(niz)  # ali ročno z dict.get

# F-STRING triki
f"{obj!r}"    # repr(obj)
f"{x:.1f}"   # 1 decimalno mesto
f"{'—'*n}"   # ponavljanje
```

### KAKO PREPOZNATI TIP NALOGE
```python
KLJUČNE BESEDE → TIP

"razred"/"konstruktor"/"metoda"
  → Razred: __init__, __str__, __repr__

"datoteka"/"beri"/"zapiši"/"CSV"
  → File I/O: with open(...) as f

"rekurzivno"/"razpolovi"/"podproblem"
  → Rekurzija: bazni primer + klic

"simuliraj"/"krog"/"izštevanke"
  → Simulacija z while/for zanko

"mreža"/"smer"/"koordinate"/"polje"
  → Grid: 2D tabela + (di, dj) smeri

"starš"/"otrok"/"prednik"/"drevo"
  → Drevesna struktura s kazalci

"anagram"/"premetanka"/"niz"
  → sorted() primerjava

"slovar"/"pogostost"/"zberi"
  → dict.get(k, 0) + 1

"regex"/"vzorec"/"zamenjaj"
  → import re; re.findall/re.sub

"tabela"/"žeton"/"zmaga"/"4v vrsto"
  → Igra: 2D tabela + smerni vektorji
```
