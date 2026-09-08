# Izpitni priročnik — Uvod v programiranje

**Ena sama datoteka za izpit.** Del A — kako se naloge lotiš. Del B — vsa snov po tipih nalog.
Del C — koda za prepis. Del D — kaj se na izpitih ponavlja in tvoje ponavljajoče se napake.
Del E — načrt za zadnja dva dneva.

Poleg tega imej odprt le še svoj dnevnik napak — datoteko, v katero sproti zapisuješ vsako napako in kaj bi bilo prav.

**Kako se ta dokument povezuje z ostalimi v repozitoriju:**

| Dokument | Odgovarja na vprašanje |
|---|---|
| ta priročnik | *Kako se naloge lotim?* — postopek, tipi nalog, koda za prepis |
| [`uvod_v_programiranje_zapiski.md`](uvod_v_programiranje_zapiski.md) | *Kako deluje Python?* — jezik po temah |
| [`izpiti.md`](izpiti.md) | *Kako je bila rešena ta konkretna naloga?* — vseh 81 podnalog z razlago |
| [`vaje_in_naloge.md`](vaje_in_naloge.md) | *Kje dobim še naloge za vajo?* |

---

## Kazalo


**[Del A — Postopek reševanja](#del-a--postopek-reševanja)**

- [A0. Kaj vedno velja](#a0-kaj-vedno-velja)
- [A1. Prve tri minute — preden napišeš eno vrstico](#a1-prve-tri-minute--preden-napišeš-eno-vrstico)
- [A2. Postopek za eno podnalogo (7 korakov)](#a2-postopek-za-eno-podnalogo-7-korakov)
- [A3. Kako iz besedila prepoznaš tip naloge](#a3-kako-iz-besedila-prepoznaš-tip-naloge)
- [A4. Postopek po tipu](#a4-postopek-po-tipu)
    - [A4.1 Razred (na 8/9 izpitih, tvoja najdražja luknja)](#a41-razred-na-89-izpitih-tvoja-najdražja-luknja)
    - [A4.2 Datoteke (na 8/9 izpitih)](#a42-datoteke-na-89-izpitih)
    - [A4.3 Slovarji in štetje](#a43-slovarji-in-štetje)
    - [A4.4 argmax / argmin (najpogostejši prijem sploh, ~9 podnalog)](#a44-argmax--argmin-najpogostejši-prijem-sploh-9-podnalog)
    - [A4.5 Nizi](#a45-nizi)
    - [A4.6 Mreže in matrike](#a46-mreže-in-matrike)
    - [A4.7 Rekurzija](#a47-rekurzija)
    - [A4.8 Generatorji](#a48-generatorji)
- [A5. Ko je rdeče — postopek razhroščevanja](#a5-ko-je-rdeče--postopek-razhroščevanja)
- [A6. Zadnjih 10 minut](#a6-zadnjih-10-minut)
- [A7. Razporeditev časa (za 120-minutni izpit)](#a7-razporeditev-časa-za-120-minutni-izpit)

**[Del B — Snov po tipih nalog](#del-b--snov-po-tipih-nalog)**

- [Del 0 — Osnove, ki jih rabiš pri vsaki nalogi](#del-0--osnove-ki-jih-rabiš-pri-vsaki-nalogi)
    - [0.1 Kako je zgrajena naloga](#01-kako-je-zgrajena-naloga)
    - [0.2 Tipi in pretvorbe](#02-tipi-in-pretvorbe)
    - [0.3 Operatorji in števke števila](#03-operatorji-in-števke-števila)
    - [0.4 Pogoji in logika](#04-pogoji-in-logika)
    - [0.5 Zanke](#05-zanke)
    - [0.6 Funkcije in privzeti argumenti](#06-funkcije-in-privzeti-argumenti)
    - [0.7 Napake in kako jih brati](#07-napake-in-kako-jih-brati)
    - [0.8 Uvoz knjižnic](#08-uvoz-knjižnic)
- [Tip 1 — Naloge s števili in števkami](#tip-1--naloge-s-števili-in-števkami)
- [Tip 2 — Naloge z rekurzijo](#tip-2--naloge-z-rekurzijo)
    - [2a. Linearna rekurzija po številih](#2a-linearna-rekurzija-po-številih)
    - [2b. Rekurzija po nizih in rezinah](#2b-rekurzija-po-nizih-in-rezinah)
    - [2c. Dvojna rekurzija (dva klica)](#2c-dvojna-rekurzija-dva-klica)
    - [2d. Rekurzija po gnezdenih strukturah](#2d-rekurzija-po-gnezdenih-strukturah)
    - [2e. Rekurzija z zbiranjem VSEH rešitev (backtracking) ⚠️](#2e-rekurzija-z-zbiranjem-vseh-rešitev-backtracking-)
    - [2f. Urejanje z zlivanjem (merge sort)](#2f-urejanje-z-zlivanjem-merge-sort)
- [Tip 3 — Naloge z nizi](#tip-3--naloge-z-nizi)
    - [3a. Osnove](#3a-osnove)
    - [3b. Gradnja niza znak po znak](#3b-gradnja-niza-znak-po-znak)
    - [3c. Razrez na bloke in branje žetonov](#3c-razrez-na-bloke-in-branje-žetonov)
    - [3d. Formatiranje z f-nizi](#3d-formatiranje-z-f-nizi)
    - [3e. Šifre](#3e-šifre)
- [Tip 4 — Naloge s seznami in nabori](#tip-4--naloge-s-seznami-in-nabori)
    - [4a. Osnove in razlika seznam / nabor](#4a-osnove-in-razlika-seznam--nabor)
    - [4b. Iskanje maksimuma / minimuma (argmax, argmin)](#4b-iskanje-maksimuma--minimuma-argmax-argmin)
    - [4c. Urejanje s ključem](#4c-urejanje-s-ključem)
    - [4d. Sklad (stack)](#4d-sklad-stack)
    - [4e. Krožnost in simulacije](#4e-krožnost-in-simulacije)
    - [4f. Podzaporedja in primerjave](#4f-podzaporedja-in-primerjave)
    - [4g. Točke, razdalje, krogi](#4g-točke-razdalje-krogi)
- [Tip 5 — Naloge s slovarji in množicami](#tip-5--naloge-s-slovarji-in-množicami)
    - [5a. Slovar — osnove](#5a-slovar--osnove)
    - [5b. Štetje — vzorec, ki ga rabiš vsak izpit](#5b-štetje--vzorec-ki-ga-rabiš-vsak-izpit)
    - [5c. Gnezdene strukture](#5c-gnezdene-strukture)
    - [5d. Množice](#5d-množice)
    - [5e. Permutacije](#5e-permutacije)
- [Tip 6 — Naloge z matrikami in mrežami](#tip-6--naloge-z-matrikami-in-mrežami)
    - [6a. Ustvarjanje in dostop](#6a-ustvarjanje-in-dostop)
    - [6b. Sprehod, meje, smeri](#6b-sprehod-meje-smeri)
    - [6c. Izpis matrike kot niz](#6c-izpis-matrike-kot-niz)
    - [6d. Klasične matrične operacije](#6d-klasične-matrične-operacije)
- [Tip 7 — Naloge z razredi](#tip-7--naloge-z-razredi)
    - [7a. Skelet](#7a-skelet)
    - [7b. Posebne (dunder) metode](#7b-posebne-dunder-metode)
    - [7c. Metoda, ki vrne NOV objekt istega razreda](#7c-metoda-ki-vrne-nov-objekt-istega-razreda)
    - [7d. Objekt s stanjem, ki ga metode spreminjajo](#7d-objekt-s-stanjem-ki-ga-metode-spreminjajo)
    - [7e. Razred, ki hrani zbirko, in preverjanje vhoda](#7e-razred-ki-hrani-zbirko-in-preverjanje-vhoda)
    - [7f. Funkcije nad seznamom objektov](#7f-funkcije-nad-seznamom-objektov)
- [Tip 8 — Naloge z datotekami](#tip-8--naloge-z-datotekami)
    - [8a. Branje](#8a-branje)
    - [8b. Pisanje](#8b-pisanje)
    - [8c. CSV in strukturirane vrstice](#8c-csv-in-strukturirane-vrstice)
    - [8d. Mreža iz datoteke](#8d-mreža-iz-datoteke)
    - [8e. Preoblikovanje besedila](#8e-preoblikovanje-besedila)
    - [8f. Knjižnica `os` (redkeje, a se pojavi)](#8f-knjižnica-os-redkeje-a-se-pojavi)
- [Tip 9 — Naloge z generatorji](#tip-9--naloge-z-generatorji)
- [Dodatek A — klasične naloge z vaj](#dodatek-a--klasične-naloge-z-vaj)
- [Dodatek B — pasti, ki stanejo točke](#dodatek-b--pasti-ki-stanejo-točke)
- [Dodatek C — postopek reševanja naloge](#dodatek-c--postopek-reševanja-naloge)

**[Del C — Kuharica (samo koda za prepis)](#del-c--kuharica-samo-koda-za-prepis)**

- [1. Razred: skelet, ki pokrije 90 % nalog](#1-razred-skelet-ki-pokrije-90--nalog)
    - [1a. Razred s slovarjem v atributu; metoda vrne NOV objekt ✅](#1a-razred-s-slovarjem-v-atributu-metoda-vrne-nov-objekt-)
    - [1b. Objekt s stanjem, ki ga metoda spreminja korak za korakom ✅](#1b-objekt-s-stanjem-ki-ga-metoda-spreminja-korak-za-korakom-)
- [2. Datoteke](#2-datoteke)
    - [2a. Mreža iz datoteke → množica koordinat ✅](#2a-mreža-iz-datoteke--množica-koordinat-)
    - [2b. Tabela CSV z glavo vrstic in stolpcev → slovar s ključi-nabori ✅](#2b-tabela-csv-z-glavo-vrstic-in-stolpcev--slovar-s-ključi-nabori-)
    - [2c. Poročilo z natančnim formatom ✅](#2c-poročilo-z-natančnim-formatom-)
- [3. Štetje v slovar in frekvence](#3-štetje-v-slovar-in-frekvence)
- [4. argmax / argmin — najpogostejši vzorec na izpitu](#4-argmax--argmin--najpogostejši-vzorec-na-izpitu)
- [5. Nizi](#5-nizi)
- [6. Matrike in mreže (osmerosmerke, ladjice, QR)](#6-matrike-in-mreže-osmerosmerke-ladjice-qr)
- [7. Seznami, krožnost, podzaporedja](#7-seznami-krožnost-podzaporedja)
- [8. Množice](#8-množice)
- [9. Drobnarije, ki stanejo točke](#9-drobnarije-ki-stanejo-točke)
- [10. Rekurzija](#10-rekurzija)
    - [Ostali rekurzivni vzorci](#ostali-rekurzivni-vzorci)

**[Del D — Kaj se na izpitih ponavlja](#del-d--kaj-se-na-izpitih-ponavlja)**

- [D1. Zgradba je vsakič enaka](#d1-zgradba-je-vsakič-enaka)
- [D2. Prijemi po pogostosti](#d2-prijemi-po-pogostosti)
- [D3. Kaj so na izpitih dejansko dali](#d3-kaj-so-na-izpitih-dejansko-dali)
- [D4. Dve opozorili o testih](#d4-dve-opozorili-o-testih)
- [D5. Tvoje ponavljajoče se napake](#d5-tvoje-ponavljajoče-se-napake)

**[Del E — Zadnja dva dneva](#del-e--zadnja-dva-dneva)**

- [E1. Dan 1 — gradniki (5 h)](#e1-dan-1--gradniki-5-h)
- [E2. Dan 2 — simulacije (5 h)](#e2-dan-2--simulacije-5-h)
- [E3. Jutro izpita](#e3-jutro-izpita)
- [E4. Rezerva](#e4-rezerva)

---

# Del A — Postopek reševanja

## A0. Kaj vedno velja

- Izpit ima **3 naloge po 3 podnaloge**. Vrstni red je zadnji dve leti fiksen:
  **1 = strukture/rekurzija, 2 = razred, 3 = datoteke**.
- Podnaloge znotraj naloge so **odvisne**: 2. uporabi 1., 3. uporabi obe. Velja v 27/27 nalogah.
- Podnaloge se **ocenjujejo ločeno**. Delna rešitev je vredna točke. Nikoli ne pusti prazno.
- Testi na dnu datoteke **so** ocena. Ni skritih testov.

## A1. Prve tri minute — preden napišeš eno vrstico

1. Preleti **vseh 9 podnalog**, ne samo prve.
2. Ob vsako podnalogo si na papir napiši eno črko: `L` (lahka, vem takoj), `S` (srednja),
   `T` (ne vem, kako bi).
3. **Začni z vsemi `L`**, po vrsti čez vse tri naloge. Prve podnaloge so skoraj vedno lahke in
   skupaj vredne veliko. Šele nato `S`, `T` na koncu.
4. Če je naloga 2 razred, si takoj prepiši skelet razreda (Del C, §1) — imena metod boš dopolnil.

## A2. Postopek za eno podnalogo (7 korakov)

Ta postopek uporabi **vsakič**, tudi ko se ti zdi, da veš.

**1) Prepiši podpis DOSLOVNO iz besedila.**

```python
def najblizja_stranka(x, stranke):   # ime, vrstni red in število parametrov točno kot v besedilu
```

Ne dodajaj parametrov, ki jih besedilo ne omenja (stanje objekta je že v `self`), in ne
preimenuj metod. To te je lani stalo celo nalogo.

**2) Prepiši primer iz besedila kot komentar tik nad funkcijo.**

```python
# >>> najblizja_stranka((0, 0), [(3, 4), (1, 1)])
# (1, 1)
```

To je tvoja specifikacija. Ko boš mislil, da si končal, jo preberi še enkrat.

**3) Odgovori na tri vprašanja, preden pišeš telo:**

| Vprašanje | Zakaj |
|---|---|
| **Kaj vrnem?** vrednost / indeks / nov objekt / `None` | najpogostejša napaka je vrniti pravo stvar v napačni obliki |
| **Kakšnega tipa?** seznam / nabor / **množica** / slovar / `float` / niz | test primerja z `==`, in `[1,2]`, `(1,2)`, `{1,2}` niso enaki |
| **Kaj pri praznem/neveljavnem vhodu?** | ≥10 podnalog na starih izpitih zahteva `None` |

**4) Napiši najbolj neumno rešitev, ki dela.** Zanka in `if`. Brez elegance, brez enovrstičnic.
Elegantno pišeš, ko ostane čas — točke so iste.

**5) Vrni rezultat.** Preveri, da ima **vsaka veja** `return`. Funkcija brez `return` vrne `None`.

**6) Preveri v Tomu.** Šele zdaj.

**7) Preden greš na naslednjo podnalogo**, si odgovori: *ali bom to funkcijo klical v naslednji
podnalogi?* V 27/27 nalogah je bil odgovor da. Če je njena oblika neprimerna (vrne `True`/`False`,
ti pa boš rabil sam podatek), jo popravi zdaj, ne čez pol ure.

## A3. Kako iz besedila prepoznaš tip naloge

| Če v besedilu piše ... | Tip | Kam pogledaš |
|---|---|---|
| „Sestavite razred", „konstruktor", „metoda" | razred | Tip 7, §C1 |
| „ime datoteke", „preberite iz", „zapišite v" | datoteke | Tip 8, §C2 |
| „koliko", „kolikokrat", „najpogostejši", „frekvenca" | štetje v slovar | §5b, §C3 |
| „največji", „najmanjši", „najdaljši", „najbližji" | argmax/argmin | §4b, §C4 |
| „če jih je več, vrnite prvega" | argmax s **strogim** `>` | §4b |
| „če ni ..., vrnite `None`" | validacija vhoda | §A2, korak 3 |
| „vrnite **množico vseh**", „vse možne" | rekurzija z zbiranjem (backtracking) | §2e |
| „brez uporabe `sort`", „razpolovite" | rekurzija (merge sort) | §2f |
| „mreža", „tabela znakov", „plošča", „polje n×m" | matrike | Tip 6, §C6 |
| „sosednji", „v osmih smereh", „vodoravno, navpično, diagonalno" | smerni vektorji | §6b |
| „urejeno po ..., pri enakih po ..." | dvojni ključ `key=lambda x: (-x[1], x[0])` | §4c |
| „zaporedje se pojavi v", „podzaporedje" | dvojni indeks čez seznam | §4f |
| „ponavljajoče se v krogu", „izštevanka" | krožno `% len` | §4e |
| „vsakih 6 znakov", „po tri znake" | rezine fiksne dolžine `niz[i:i+3]` | §3c |
| „generator", „`yield`", „neskončno zaporedje" | generatorji | Tip 9 |
| natančen izpis s presledki/puščicami/robovi | f-nizi in format | §3d, §C2c |

## A4. Postopek po tipu

### A4.1 Razred (na 8/9 izpitih, tvoja najdražja luknja)

1. **Napiši skelet, preden bereš podrobnosti:**

   ```python
   class Ime:
       def __init__(self, a, b):
           self.a = a
           self.b = b
   ```

2. **Iz besedila prepiši imena vseh atributov** točno tako, kot so poimenovani. Test lahko
   preverja `i.x`, ne le vedenja.
3. **Konstruktor ne vrača ničesar.** Nikoli `return` v `__init__`.
4. **Vsaka metoda ima `self` kot prvi parameter**, tudi če ga ne uporabiš.
5. **Vse metode so zamaknjene v telo razreda.** Če je metoda na levem robu, ni metoda.
6. Za vsako metodo se vprašaj eno stvar: **spremeni objekt ali vrne novega?**
   - „doda", „premakne", „nastavi" → spremeni `self`, običajno vrne `None`
   - „unija", „presek", „vsota dveh" → **vrne nov objekt istega razreda**:

     ```python
     def unija(self, drugi):
         nov = Stevec()          # nov objekt
         ...                     # napolni ga
         return nov              # self ostane nespremenjen
     ```

7. Če besedilo kaže `>>> x` in izpis, rabiš `__repr__`; če kaže `print(x)`, rabiš `__str__`.
   **Nista isto:** `__repr__` naj izpiše **klic konstruktorja**:

   ```python
   def __repr__(self):
       return f'Oseba({self.ime!r}, {self.priimek!r}, vzdevek={self.vzdevek!r})'
   ```

8. Če besedilo primerja objekte (`==`, `in`, `sorted`), rabiš `__eq__` oz. `__lt__`.

### A4.2 Datoteke (na 8/9 izpitih)

Vzorec je vsakič isti: **preberi → zgradi strukturo → izpiši**. Ne poskušaj vsega naenkrat.

1. **Beri vedno tako:**

   ```python
   with open(ime, encoding='utf-8') as f:
       for vrstica in f:
           vrstica = vrstica.strip()
           if not vrstica:
               continue
   ```

   `strip()` **vedno** — nevidni `\n` na koncu je najpogostejši vzrok „pravilnega" rdečega testa.
2. **Najprej samo preberi in vrni strukturo.** Nič drugega. Preveri, da je struktura prava.
3. Pretvorbe takoj ob branju: `int(x)`, `float(x)`. Kar prebereš iz datoteke, je **niz**.
4. **Pisanje:**

   ```python
   with open(ime, 'w', encoding='utf-8') as f:
       print(vrstica, file=f)
   ```

5. **Format prepiši znak za znakom iz primera v besedilu.** Preštej presledke. Če je v primeru
   `(4, 5) ==3.61==> (1, 7)`, potem je `f'{a} =={d:.2f}==> {b}'` in nič drugega.
6. Zadnja vrstica: ali je na koncu prazna vrstica ali ne? `print` jo doda, `f.write` ne.

### A4.3 Slovarji in štetje

1. Štetje je vedno ta ena vrstica:

   ```python
   slovar[k] = slovar.get(k, 0) + 1
   ```

2. Zbiranje v seznam:

   ```python
   slovar.setdefault(k, []).append(v)
   ```

3. Če je ključ sestavljen (npr. par mest), je **nabor**: `slovar[(od, do)] = n`.
   Nato **vedno** `for (od, do), n in slovar.items()`, nikoli `.values()`.
4. Ključ mora biti nespremenljiv: niz, število, nabor. Seznam ne (`unhashable type: 'list'`).

### A4.4 argmax / argmin (najpogostejši prijem sploh, ~9 podnalog)

1. Vprašaj se: rabim **element**, **ključ** ali **indeks**? Vsak ima svojo obliko.
2. Ročna oblika, ki dela vedno (in ne ustvari novih seznamov, kar zna biti zahteva):

   ```python
   najboljsi = None
   najvec = None
   for x in seznam:
       v = kriterij(x)
       if najvec is None or v > najvec:   # strogi > vrne PRVEGA največjega
           najvec, najboljsi = v, x
   return najboljsi                       # pri praznem seznamu vrne None
   ```

3. Kratka oblika, ko prazen vhod ni problem: `max(slovar, key=slovar.get)`.
4. „Če jih je več, vrni prvega" → **strogi** `>` (ne `>=`). To je pogosta tiha izguba točk.

### A4.5 Nizi

1. Nizi so **nespremenljivi**: `s[0] = 'a'` ne obstaja. Gradi z `nov += znak` ali `''.join(seznam)`.
2. Pregled znak po znak: `for z in s`. Če rabiš indeks: `for i in range(len(s))`.
3. Večmestno število v nizu: zbiraj `while i < len(s) and s[i].isdigit()`, šele nato `int()`.
4. Rezine: `s[i:i+k]` za bloke fiksne dolžine, `s[::-1]` za obrat.
5. Iskanje žetonov (`#znacka`, `:custvencek:`): najprej `split()`, šele nato preverjaj obliko.

### A4.6 Mreže in matrike

1. **Ustvarjanje — samo tako:**

   ```python
   m = [[0 for _ in range(sirina)] for _ in range(visina)]
   ```

   `[[0] * sirina] * visina` naredi **isto vrstico večkrat** in nalogo podre.
2. Indeksiranje je `m[vrstica][stolpec]` = `m[y][x]`. Napiši si to na rob papirja; zamenjava
   `x` in `y` je najpogostejša napaka pri mrežah.
3. **Meje preveri, preden dostopaš:**

   ```python
   def znotraj(m, y, x):
       return 0 <= y < len(m) and 0 <= x < len(m[0])
   ```

4. Osem smeri: `SMERI = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]`.
5. Izpis: `'\n'.join(''.join(v) for v in m)`.

### A4.7 Rekurzija

1. **Najprej napiši bazni primer**, šele nato korak. Vprašaj: kdaj je odgovor takoj znan?
2. Rekurzivni klic mora dobiti **manjši** problem (krajši niz, manjše število, ostanek seznama).
3. Rezultat rekurzivnega klica **uporabi** (`return 1 + f(n-1)`), ne samo pokliči.
4. Če naloga hoče **vse rešitve**, je bazni primer množica z **eno prazno rešitvijo**, ne prazna
   množica:

   ```python
   def razbitja(n, s):
       if n == '':
           return {()}          # NE set() — sicer se vse zbriše in dobiš prazno
       vsa = set()
       for kos in se_zacne(n, s):
           for ostanek in razbitja(n[len(kos):], s):
               vsa.add((kos,) + ostanek)
       return vsa
   ```

5. Par „ali obstaja" + „vrni vse" je isti sprehod: prvi vrne `True` ob prvem uspehu, drugi zbira.

### A4.8 Generatorji

`yield` namesto `return`; funkcija se ustavi in nadaljuje ob naslednjem `next`. Neskončni
generator je `while True:` z `yield`. Prenos iz drugega generatorja: `yield from`.

## A5. Ko je rdeče — postopek razhroščevanja

**Najprej ugani, zakaj, šele nato poglej test.** Ugibanje je tisto, kar treniraš za izpit.

| Sporočilo | Kaj pomeni | Popravek |
|---|---|---|
| `NameError: name 'x' is not defined` | tipkarska napaka ali spremenljivka nastane šele v `if` | definiraj pred zanko |
| `TypeError: takes 2 positional arguments but 3 were given` | metoda brez `self` | dodaj `self` |
| `AttributeError: 'X' object has no attribute 'y'` | metoda zunaj razreda ali atribut ni nastavljen v `__init__` | zamakni metodo v razred |
| `IndexError: list index out of range` | ni preverjenih mej | `znotraj(...)` pred dostopom |
| `KeyError: k` | ključa še ni | `.get(k, 0)` ali `setdefault` |
| `TypeError: 'NoneType' object is not iterable` | funkcija je pozabila `return` | dodaj `return` v vsako vejo |
| `TypeError: unhashable type: 'list'` | seznam kot ključ ali v množici | pretvori v `tuple` |
| `ValueError: invalid literal for int()` | nisi odstranil `\n` ali vejice | `strip()`, preveri ločilo |
| `UnboundLocalError` | prirejaš spremenljivki, ki je definirana zunaj | definiraj jo znotraj funkcije |
| `IndentationError` | mešani presledki/tabulatorji | poravnaj |

**Rezultat je videti pravilen, test pa je rdeč** — po vrsti preveri:

1. **tip**: `[1, 2]` vs `(1, 2)` vs `{1, 2}` — test primerja z `==` in ti trije niso enaki;
2. **`None` vs `False`** pri neveljavnem vhodu;
3. **`round(x, 2)`** — če besedilo omenja dve decimalki, ga rabiš;
4. **presledki in prelomi vrstic** v izpisu — preštej jih v primeru iz besedila;
5. **vrstni red** rezultata — je zahtevan urejen?
6. **prazen vhod** — kaj vrne tvoja funkcija za `''`, `[]`, `{}`?

## A6. Zadnjih 10 minut

Pojdi čez vse tri naloge in preveri samo to:

- [ ] Ima **vsaka** funkcija `return` v vsaki veji?
- [ ] So vsi tipi rezultatov taki, kot zahteva besedilo?
- [ ] `round(...)` tam, kjer so decimalke?
- [ ] `None` pri praznem/neveljavnem vhodu?
- [ ] So vse metode **znotraj** razreda in imajo `self`?
- [ ] Je kje ostala vrednost iz primera zakodirana na trdo? (imena mest, števila iz besedila)
- [ ] Je vsaka podnaloga vsaj poskušena? Delna rešitev je vredna več kot prazna.

## A7. Razporeditev časa (za 120-minutni izpit)

| Čas | Kaj |
|---|---|
| 0:00–0:05 | preleti vseh 9 podnalog, označi `L`/`S`/`T` |
| 0:05–0:35 | vse podnaloge, označene z `L` (čez vse tri naloge) |
| 0:35–1:35 | `S`, po nalogah; pri vsaki najprej 1. podnaloga, ker jo 2. in 3. rabita |
| 1:35–1:50 | `T` — kar ostane; napiši vsaj delujoč osnovni primer |
| 1:50–2:00 | kontrolni seznam iz §A6 |

Če se pri eni podnalogi zatakneš za več kot 10 minut, **jo pusti in pojdi naprej**. Vrni se, ko
so ostale rešene. Podnaloge so ocenjene ločeno; ena zabita ne odnese ostalih.

---

# Del B — Snov po tipih nalog

Razlaga in primeri za vsak tip naloge. Kadar med izpitom ne veš, *kako* se lotiti,
je odgovor tu; kadar veš in rabiš samo kodo, je hitrejši Del C.

## Del 0 — Osnove, ki jih rabiš pri vsaki nalogi

### 0.1 Kako je zgrajena naloga

Vsaka naloga (na vajah, kolokviju, izpitu) zahteva **funkcijo z natančno določenim
imenom**, ki nekaj **sprejme** in nekaj **vrne**. Skoraj vedno je oblika taka:

```python
def ime_funkcije(argument1, argument2=privzeta_vrednost):
    """Kratek opis, kaj funkcija naredi."""
    rezultat = ...          # telo, zamaknjeno za 4 presledke
    return rezultat
```

Tri stvari, ki jih preveri vsak test:
1. **Ime funkcije je točno tako, kot piše v besedilu** (tudi imena metod in atributov).
2. **Vrne pravi tip**: `list` ni `tuple`, `set` ni `list`, `'3.5'` ni `3.5`.
3. **Vrne, ne izpiše.** `print(x)` ni `return x`. Funkcija brez `return` vrne `None`.

> Najpogostejša napaka na izpitu: funkcija pravilno izračuna rezultat, a ga ne vrne.
> Simptom: `TypeError: unsupported operand type(s) ... 'NoneType'`.

### 0.2 Tipi in pretvorbe

| Tip | Primer | Spremenljiv? | Opomba |
|---|---|---|---|
| `int` | `5`, `-3` | – | brez omejitve velikosti |
| `float` | `3.14` | – | približki! `math.sin(math.pi)` ni točno 0 |
| `bool` | `True`, `False` | – | podtip `int`: `True == 1` |
| `str` | `"abc"` | **ne** | `niz[0] = 'x'` je napaka |
| `list` | `[1, 2]` | **da** | urejen, dovoljuje ponovitve |
| `tuple` | `(1, 2)` | ne | fiksna dolžina, lahko ključ slovarja |
| `dict` | `{"a": 1}` | da | ključ → vrednost |
| `set` | `{1, 2}` | da | brez ponovitev, neurejen, hiter `in` |
| `None` | `None` | – | "ni vrednosti"; preverjaj z `is None` |

```python
int("42")        # 42          str -> int
float("3.14")    # 3.14        str -> float   (KLJUČNO pri branju datotek!)
str(42)          # '42'
list("abc")      # ['a','b','c']
tuple([1, 2])    # (1, 2)
set([1, 1, 2])   # {1, 2}
"".join(['a','b'])   # 'ab'    seznam znakov -> niz
```

`int("3.5")` **je napaka** — najprej `float`, šele nato po potrebi `int`.

### 0.3 Operatorji in števke števila

```python
+  -  *          # osnovno
/                # deljenje, VEDNO float:  7 / 2 == 3.5
//               # celoštevilsko:          7 // 2 == 3
%                # ostanek:                7 % 2 == 1
**               # potenca:                2 ** 10 == 1024
abs(x)  round(x, n)  divmod(a, b)          # divmod vrne (a//b, a%b)
```

Prioriteta: `**` → `*  /  //  %` → `+  -`. Oklepaji vse povozijo.
Klasična napaka: `x ** 1/2` je `(x ** 1) / 2`, ne koren — piši `x ** (1/2)` ali `x ** 0.5`.

Skrajšano posodabljanje: `x += 2`, `x -= 2`, `x *= 2`, `x //= 2`, `x %= 2`.

**Razstavljanje števila na števke** — zapomni si ta par:

```python
n % 10       # zadnja števka (enice)
n // 10      # število brez zadnje števke
```

```python
def vsota_stevk(n):
    vsota = 0
    while n != 0:
        vsota += n % 10
        n //= 10
    return vsota
```

Za tromestno število: `enice = n % 10`, `desetice = (n // 10) % 10`, `stotice = n // 100`.

### 0.4 Pogoji in logika

```python
if pogoj1:
    ...
elif pogoj2:
    ...
else:
    ...

x = a if pogoj else b        # pogojni izraz (ternary)
```

Primerjave: `==  !=  <  <=  >  >=`. Verižno: `0 < x < 10` deluje in pomeni `0 < x and x < 10`.

| Operacija | V Pythonu |
|---|---|
| in (konjunkcija) | `a and b` |
| ali (disjunkcija) | `a or b` |
| ne (negacija) | `not a` |
| implikacija a→b | `not a or b` |
| ekvivalenca a↔b | `a == b` oz. `(not a or b) and (not b or a)` |
| XOR | `a != b` oz. `(a and not b) or (not a and b)` |
| NAND | `not (a and b)` |

NAND je univerzalen: `not a ≡ nand(a,a)`, `a and b ≡ nand(nand(a,b), nand(a,b))`,
`a or b ≡ nand(nand(a,a), nand(b,b))`.

**Kratki stik**: `or` neha vrednotiti pri prvem `True`, `and` pri prvem `False`.
To izkoristi za varne preverbe:

```python
if sez and sez[0] > 5:        # sez[0] se ne vrednoti, če je sez prazen
if x != 0 and y / x > 2:      # ne deli z nič
```

Kaj je `False` samo po sebi: `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`.
Zato `if not sez:` pomeni "če je seznam prazen".

### 0.5 Zanke

```python
for x in zbirka:              # niz, seznam, nabor, slovar, datoteka, range
    ...

for i in range(n):            # 0, 1, ..., n-1
for i in range(a, b):         # a, ..., b-1
for i in range(a, b, k):      # a, a+k, ...
for i in range(10, 0, -1):    # 10, 9, ..., 1

for i, x in enumerate(sez):        # (indeks, element)
for a, b in zip(sez1, sez2):       # istoležni pari; ustavi se pri krajšem
for k, v in slovar.items():        # (ključ, vrednost)

while pogoj:                  # kadar ne vemo, kolikokrat
    ...
```

`break` prekine zanko, `continue` preskoči preostanek te iteracije, `pass` ne naredi nič.

Poseben, a koristen `for ... else`: blok `else` se izvede, **če ni bilo `break`**.

```python
for d in prastevila:
    if s % d == 0:
        break
else:
    prastevila.append(s)      # ni bilo delitelja -> praštevilo
```

### 0.6 Funkcije in privzeti argumenti

```python
def koren(x, n=2):            # n je neobvezen; brez presledkov okoli =
    return x ** (1 / n)

koren(64)         # 8.0
koren(64, n=3)    # ~4.0
```

Privzeti argumenti stojijo **za** obveznimi. Klic po imenu (`f(b=2, a=1)`) je dovoljen
v poljubnem vrstnem redu.

> ⚠️ **Privzeti argument nikoli ne sme biti spremenljiv objekt** (seznam, slovar, množica).
> Python ga ustvari **enkrat, ob definiciji**, ne ob vsakem klicu:
> ```python
> def slabo(x, sez=[]):        # sez si zapomni vsebino prejšnjega klica!
>     sez.append(x); return sez
> slabo(1)  # [1]
> slabo(2)  # [1, 2]  ← ni [2]
>
> def dobro(x, sez=None):
>     if sez is None:
>         sez = []
>     sez.append(x); return sez
> ```

Neobvezni argument, ki spremeni obnašanje (pogosto na izpitih):

```python
def roka_usode(vsota=None):
    if vsota is not None:      # če je podan, kar določi rezultat
        return vsota
    return randint(1, 6) + randint(1, 6)
```

**Lokalne spremenljivke** znotraj funkcije ne obstajajo zunaj nje in ne povozijo globalnih.

**Lambda** je anonimna funkcija za enkratno uporabo, skoraj vedno kot `key=`:

```python
sez.sort(key=lambda par: par[1])
```

### 0.7 Napake in kako jih brati

| Vrsta | Kdaj | Primeri |
|---|---|---|
| **SyntaxError** | pred izvajanjem, program sploh ne steče | manjkajoč `:`, neujemajoč `)` |
| **Napaka ob izvajanju** | med izvajanjem | `ZeroDivisionError`, `NameError`, `ValueError`, `KeyError`, `IndexError`, `TypeError`, `AttributeError` |
| **Vsebinska (logična)** | nikoli ne javi — samo napačen rezultat | `x ** 1/2` namesto `x ** (1/2)` |

**Ključna informacija je v zadnji vrstici sporočila o napaki.** Pogosti prevodi:

- `AttributeError: 'X' object has no attribute 'y'` → metoda ni v razredu ali je narobe poimenovana
- `TypeError: ... 'NoneType'` → nekje manjka `return`
- `KeyError: 'x'` → ključa ni v slovarju; uporabi `.get(kljuc, privzeto)`
- `IndexError` → indeks čez rob; preveri meje
- `IndentationError` → mešani zamiki; uporabljaj **4 presledke**

### 0.8 Uvoz knjižnic

```python
import math
math.sqrt(2)   math.pi   math.floor(3.7)   math.ceil(3.2)
math.factorial(5)   math.sin(x)   math.radians(stopinje)   math.gcd(a, b)

from math import sqrt, pi          # uvozi samo, kar rabiš

import random
random.randint(1, 6)       # celo število, OBE meji vključeni
random.uniform(0, 1)       # float
random.choice(seznam)
random.shuffle(seznam)     # premeša NA MESTU, ne vrne ničesar
random.seed(42)            # ponovljivo naključje
```

---

## Tip 1 — Naloge s števili in števkami

**Kako jih prepoznaš:** vhod je celo število, rešitve ne smeš iskati prek `str(n)`,
ker gre za vajo iz `%` in `//`.

**Osnovni vzorec (zanka):**

```python
while n != 0:
    stevka = n % 10
    ...              # obdelaj števko
    n //= 10
```

**Osnovni vzorec (rekurzija):** glej [Tip 2](#tip-2--naloge-z-rekurzijo).

#### Primeri

```python
def vsota_stevk(n):
    vsota = 0
    while n != 0:
        vsota += n % 10
        n //= 10
    return vsota

def vsota_lihih_stevk(n):
    vsota = 0
    while n > 0:
        s = n % 10
        if s % 2 == 1:
            vsota += s
        n //= 10
    return vsota

def obrat(n):                       # obrat tromestnega
    return (n % 10) * 100 + ((n // 10) % 10) * 10 + (n // 100)

def obratno(n, acc=0):              # obrat poljubnega, z akumulatorjem
    if n == 0:
        return acc
    return obratno(n // 10, acc * 10 + n % 10)

def je_palindromsko(n):
    return n == obratno(n)

def st_stevk(n):
    if n < 10:
        return 1
    return 1 + st_stevk(n // 10)
```

**Kontrolna števka (SI12)** — postopek: števke od desne pomnoži z 2, 3, 4, …,
seštej, vzemi `% 11`, kontrolna števka je `11 - ostanek`; če je 10 ali 11, je 0.

```python
def dodaj_kontrolno_stevko(n):
    vsota = 0
    sklic = n
    mnozitelj = 2
    while sklic > 0:
        vsota += (sklic % 10) * mnozitelj
        sklic //= 10
        mnozitelj += 1
    ks = 11 - vsota % 11
    if ks > 9:
        ks = 0
    return n * 10 + ks
```

**Datumi:**

```python
def je_prestopno(leto):
    return (leto % 4 == 0 and leto % 100 != 0) or leto % 400 == 0

def stevilo_dni(mesec, leto):
    if mesec in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if mesec in (4, 6, 9, 11):
        return 30
    return 29 if je_prestopno(leto) else 28

def je_veljaven_datum(dan, mesec, leto):
    return 1 <= mesec <= 12 and 1 <= dan <= stevilo_dni(mesec, leto)
```

**Obresti:** enostavno `A₀·(1 + m·n)`, obrestno obrestno `A₀·(1 + m)ⁿ`;
mesečna → letna mera: `((1 + m) ** 12 - 1) * 100`.

**Praštevila:**

```python
def je_prastevilo(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):   # dovolj je do korena
        if n % d == 0:
            return False
    return True

def prastevila_do(n):
    return [k for k in range(2, n + 1) if je_prastevilo(k)]
```

**Numerični približki** — vzorec "izboljšuj, dokler ni dovolj dobro":

```python
def koren_newton(n, eps=1e-10):     # x_{k+1} = (x_k + n/x_k) / 2
    x = n / 2
    while abs(x * x - n) >= eps:
        x = (x + n / x) / 2
    return x

def zlati_rez(eps=1e-10):           # φ = 1 + 1/φ
    x = 1
    while True:
        nov = 1 + 1 / x
        if abs(nov - x) < eps:
            return nov
        x = nov
```

**Bisekcija** (razpolavljanje intervala) — logaritemsko hitro iskanje:

```python
def bisekcija(f, a, b, eps=1e-10):
    while b - a > eps:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2
```

**Pretvorbe baz:**

```python
bin(10)          # '0b1010'
hex(255)         # '0xff'
int('1010', 2)   # 10
int('ff', 16)    # 255

import string
def pretvori(niz, baza):
    znaki = '0123456789' + string.ascii_uppercase
    rezultat = 0
    for znak in niz.upper():
        rezultat = rezultat * baza + znaki.index(znak)
    return rezultat
```

---

## Tip 2 — Naloge z rekurzijo

**Kako jih prepoznaš:** besedilo pravi "rekurzivno", ali pa je problem naravno
definiran prek manjše različice samega sebe (zaporedja, razbitja, drevesa,
gnezdene strukture).

**Vsaka rekurzivna funkcija ima dva dela:**
1. **bazni primer** — kdaj se ustavi (najprej ga napiši!),
2. **rekurzivni korak** — klic na **manjšem** primeru.

```python
def f(n):
    if n == 0:              # BAZA
        return ...
    return ... f(n - 1) ... # KORAK: manjši primer
```

> Python ima omejitev globine ~1000 klicev. Za zelo globoke rekurzije uporabi zanko.

### 2a. Linearna rekurzija po številih

```python
def fakulteta(n):
    if n == 0:
        return 1
    return n * fakulteta(n - 1)

def vsota_prvih(n):
    if n == 0:
        return 0
    return n + vsota_prvih(n - 1)

def vsota_prvih_potenc(n, k=1):
    if n == 0:
        return 0
    return n ** k + vsota_prvih_potenc(n - 1, k)

def vsota_stevk(n):
    if n == 0:
        return 0
    return n % 10 + vsota_stevk(n // 10)

def produkt_stevk(n):
    if n < 10:
        return n
    return (n % 10) * produkt_stevk(n // 10)

def najvecja_stevka(n):
    if n < 10:
        return n
    return max(n % 10, najvecja_stevka(n // 10))
```

**Collatz** (če je sodo `n//2`, sicer `3n+1`, dokler ne prideš do 1):

```python
def naslednji_clen(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def dolzina_zaporedja(n):
    if n == 1:
        return 1
    return 1 + dolzina_zaporedja(naslednji_clen(n))

def najvecji_clen(n):
    if n == 1:
        return 1
    return max(n, najvecji_clen(naslednji_clen(n)))
```

**Evklidov algoritem** (največji skupni delitelj):

```python
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)
```

**Fibonacci z akumulatorjema** (učinkovito, brez podvajanja klicev):

```python
def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci(n - 1, b, a + b)
```

### 2b. Rekurzija po nizih in rezinah

Vzorec: odlušči prvi ali zadnji znak, ostalo prepusti rekurziji. Baza je prazen niz.

```python
def prezrcali(niz):
    if niz == "":
        return ""
    return niz[-1] + prezrcali(niz[:-1])

def zlij(a, b):                      # izmenično po en znak
    if a and b:
        return a[0] + b[0] + zlij(a[1:], b[1:])
    return a + b

def filtriraj(geslo, crke):          # vislice: neuganjene črke -> '_'
    if geslo == "":
        return ""
    prvi = geslo[0] if geslo[0].lower() in crke.lower() else "_"
    return prvi + filtriraj(geslo[1:], crke)

def vsak_k_ti(niz, k):
    if k <= 0 or niz == "":
        return ""
    return niz[0] + vsak_k_ti(niz[k:], k)
```

### 2c. Dvojna rekurzija (dva klica)

```python
def binomski_rekurzija(n, k):        # Pascalov trikotnik
    if k == 0 or k == n:
        return 1
    return binomski_rekurzija(n-1, k) + binomski_rekurzija(n-1, k-1)

def binomski_ucinkovit(n, k):        # brez podvajanja; deli šele po množenju
    if k == 0:
        return 1
    return (n - k + 1) * binomski_ucinkovit(n, k - 1) // k

def stirling(n, k):                  # razdelitve n-množice na k nepraznih delov
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * stirling(n-1, k) + stirling(n-1, k-1)
```

### 2d. Rekurzija po gnezdenih strukturah

Naloga "Pogosti znaki" (izpit 23/24 i3): gnezdo `("A", ("P", ("O", ("X", ("Z",)))))`.

```python
def indeks(gnezdo, znak):
    if gnezdo[0] == znak:
        return (0,)
    if len(gnezdo) == 1:             # ni več globlje
        return None
    naprej = indeks(gnezdo[1], znak)
    return None if naprej is None else (1,) + naprej
```

### 2e. Rekurzija z zbiranjem VSEH rešitev (backtracking) ⚠️

**To je najtežji tip in se je pojavil na izpitu 25/26 i2 (`Razbitje`).**
Vedno pride v paru: najprej "ali sploh gre" (`True`/`False`), nato "vrni vse".

```python
def se_zacne(n, s):                  # vsi kosi iz s, ki so predpona n
    return [kos for kos in s if n.startswith(kos)]

def se_razbije(n, s):                # ali je razbitje mogoče
    if n == '':
        return True                  # BAZA: prazen niz je razbit
    for kos in se_zacne(n, s):
        if se_razbije(n[len(kos):], s):
            return True              # dovolj je ena uspešna pot
    return False

def razbitja(n, s):                  # VSA razbitja kot množica naborov
    if n == '':
        return {()}                  # BAZA: ena rešitev — prazen nabor
    vsa = set()
    for kos in se_zacne(n, s):
        for ostanek in razbitja(n[len(kos):], s):
            vsa.add((kos,) + ostanek)
    return vsa
```

**Ključ:** razlika je samo v baznem primeru. Pri `True/False` je `True`,
pri zbiranju rešitev je `{()}` — množica z **enim praznim naborom**.
Če vrneš `set()`, se nič ne sestavi in rezultat je vedno prazen.

### 2f. Urejanje z zlivanjem (merge sort)

Izpit 23/24 i1. "Razdeli, rekurzivno uredi polovici, zlij."

```python
def zlij(a, b):
    rezultat = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            rezultat.append(a[i]); i += 1
        else:
            rezultat.append(b[j]); j += 1
    return rezultat + a[i:] + b[j:]      # priloži, kar je ostalo

def uredi(seznam):
    if len(seznam) <= 1:                 # 0 ali 1 element je vedno urejen
        return seznam
    s = len(seznam) // 2
    return zlij(uredi(seznam[:s]), uredi(seznam[s:]))
```

---

## Tip 3 — Naloge z nizi

### 3a. Osnove

Niz je **nespremenljivo** zaporedje znakov. Vsaka metoda vrne **nov** niz.

```python
niz = 'REKURZIJA'
#      0 1 2 3 4 5 6 7 8
#     -9-8-7-6-5-4-3-2-1

niz[0]       # 'R'      prvi
niz[-1]      # 'A'      zadnji
niz[2:6]     # 'KURZ'   od 2 do 5 (6 ni vključen)
niz[:6]      # 'REKURZ'
niz[2:]      # 'KURZIJA'
niz[1:8:2]   # 'EUZJ'   vsak drugi
niz[::-1]    # obrnjen niz
```

Rezina nikoli ne javi `IndexError` — `niz[5:100]` je preprosto krajša.

```python
'zala' + 'gasper'       # stikanje
3 * 'ab'                # 'ababab'
len(niz)
'gram' in 'programiranje'    # True — podniz
'abak' <= 'abeceda'          # leksikografska primerjava
```

**Metode, ki jih res rabiš:**

```python
niz.upper()  niz.lower()  niz.title()  niz.capitalize()
niz.strip()  niz.lstrip()  niz.rstrip()      # odstrani bele znake z robov
niz.strip('.,')                              # ali dane znake
niz.split()          # razdeli po belih znakih, odvrže prazne
niz.split(',')       # razdeli po vejicah
'-'.join(seznam)     # obratno od split
niz.replace('a', 'b')        niz.replace('a', 'b', 2)   # samo prvi 2
niz.count('a')
niz.find('ab')       # indeks ali -1 če ni
niz.index('ab')      # indeks, NAPAKA če ni
niz.startswith('ab')  niz.endswith('c')
niz.isdigit()  niz.isalpha()  niz.isalnum()  niz.islower()  niz.isupper()
```

Ubežni znaki: `'\n'` nova vrstica, `'\t'` tabulator, `'\\'` poševnica,
`'\''` narekovaj. Surovi niz `r'\n'` ne pretvarja ničesar.

`ord('A')` da kodo znaka (65), `chr(65)` da znak nazaj — rabiš ju pri Cezarjevi šifri.

### 3b. Gradnja niza znak po znak

Nizi so nespremenljivi, zato `vrstica + '.'` **samo po sebi ne naredi nič** —
rezultat moraš prirediti nazaj.

```python
rezultat = ''
for znak in niz:
    rezultat += preslikaj(znak)     # += , ne samo +
```

Enakovredno in hitrejše pri dolgih nizih:

```python
kosi = []
for znak in niz:
    kosi.append(preslikaj(znak))
rezultat = ''.join(kosi)
```

**Vzorec "stikalo"** — ko se obnašanje preklaplja med dvema načinoma:

```python
def poudari_besede(naslov):         # *tako* -> TAKO
    rezultat = ''
    poudarjeno = False
    for z in naslov:
        if z == '*':
            poudarjeno = not poudarjeno
        elif poudarjeno:
            rezultat += z.upper()
        else:
            rezultat += z
    return rezultat
```

Isti vzorec reši odstranjevanje HTML značk (`v_znacki = True/False`).

### 3c. Razrez na bloke in branje žetonov

**Bloki fiksne dolžine** (DNA-kodoni po 3, base64 po 6):

```python
kodoni = [dna[i:i+3] for i in range(0, len(dna) - 2, 3)]   # samo POLNI bloki
```

`len(dna) - 2` poskrbi, da zadnji, nepopolni blok odpade. Preveri na `''` in na
nizu dolžine 1–2: rezultat mora biti `[]`.

**Skupine zaporednih enakih znakov** (stiskanje niza):

```python
def stisni(niz):
    rezultat = ''
    i = 0
    while i < len(niz):
        j = i
        while j < len(niz) and niz[j] == niz[i]:
            j += 1
        st = j - i
        rezultat += niz[i] if st == 1 else niz[i] + str(st)
        i = j
    return rezultat
```

**Večmestno število sredi niza** (`'-12d'`):

```python
i = 0
while i < len(opis):
    if opis[i].isdigit():
        j = i
        while j < len(opis) and opis[j].isdigit():
            j += 1
        stevilo = int(opis[i:j])
        znak = opis[j] if j < len(opis) else ''
        i = j + 1
    else:
        stevilo, znak = 1, opis[i]
        i += 1
    ...   # obdelaj (stevilo, znak)
```

**Žeton med ločili** (`#znacka`, `:custvencek:`):

```python
def znacke(vsebina):
    najdene = set()
    i = 0
    while i < len(vsebina):
        if vsebina[i] == '#':
            j = i + 1
            while j < len(vsebina) and vsebina[j].isalnum():
                j += 1
            if j > i + 1:            # za '#' mora biti vsaj en znak
                najdene.add(vsebina[i:j])
            i = j
        else:
            i += 1
    return najdene
```

Za `:beseda:` je krajša pot prek `split(':')` — lihi kosi so med dvopičjema:

```python
def custvencki(besedilo):
    najdeni = set()
    kosi = besedilo.split(':')
    for k in range(1, len(kosi), 2):
        if kosi[k] and all('a' <= z <= 'z' for z in kosi[k]):
            najdeni.add(f':{kosi[k]}:')
    return najdeni
```

**Ročni razrez na besede** (če `split` ni dovoljen):

```python
def razrez(niz):
    besede = []
    b = ''
    for z in niz:
        if z in ' \t\n':
            if b:
                besede.append(b); b = ''
        else:
            b += z
    if b:
        besede.append(b)
    return besede
```

### 3d. Formatiranje z f-nizi

```python
f'{ime} je star {starost} let.'
f'{a/b:.2f}'          # '3.14'    2 decimalki
f'{a/b:.5}'           # '3.1429'  5 značilnih mest
f'{1/3:.2%}'          # '33.33%'
f'{n:07d}'            # '0000042' celo število, 7 mest, ničle spredaj
f'{ime:<10}'          # levo poravnano na 10 znakov
f'{cena:>8.2f}'       # desno poravnano
f'{"NASLOV":*^30}'    # sredinsko, polnilo '*'
f'{vrednost!r}'       # repr (nizi dobijo narekovaje) — za __repr__
```

Ponovljeni znak: `'=' * 12`, `'-' * n`.

### 3e. Šifre

```python
def sifriraj(sifra, beseda):                 # substitucijska šifra: slovar znak->znak
    return ''.join(sifra[c] for c in beseda)

def ali_je_sifra(sifra):                     # je bijekcija?
    return set(sifra.values()) == set(sifra.keys())

def inverz(sifra):
    if not ali_je_sifra(sifra):
        return None
    return {v: k for k, v in sifra.items()}

def cezar(niz, k):                           # zamik po abecedi
    rezultat = ''
    for c in niz:
        if 'A' <= c <= 'Z':
            rezultat += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            rezultat += c
    return rezultat
```

Urejanje po **lastni abecedi** (slovenska, izpit 23/24 i1):

```python
ABECEDA = 'abcčdefghijklmnoprsštuvzž'
def kljuc(beseda):
    return [ABECEDA.index(znak) for znak in beseda]

sorted(besede, key=kljuc)
```

---

## Tip 4 — Naloge s seznami in nabori

### 4a. Osnove in razlika seznam / nabor

| | seznam `[...]` | nabor `(...)` |
|---|---|---|
| spremenljiv | da | **ne** |
| namen | homogena zbirka, poljubna dolžina | heterogena, fiksna dolžina (točka, datum, zapis) |
| ključ slovarja | ne | **da** |

```python
t = (1,)              # nabor z enim elementom — vejica je obvezna!
t = ()                # prazen nabor
x, y = (3, 4)         # razpakiranje
a, *ostalo = [1,2,3]  # a=1, ostalo=[2,3]
a, b = b, a           # zamenjava (v resnici nabor)
```

Rezine, `in`, `len`, `+`, `*` delujejo kot pri nizih.

**Metode seznamov:**

```python
sez.append(x)          # doda na konec
sez.extend(drug)       # doda vse elemente drugega
sez.insert(i, x)       # vstavi pred indeks i
sez.remove(x)          # odstrani PRVO pojavitev x
sez.pop()   sez.pop(i) # odstrani in VRNE
del sez[i]  del sez[2:4]
sez.index(x)  sez.count(x)
sez.sort()             # uredi NA MESTU, vrne None!
sorted(sez)            # vrne NOV urejen seznam
sez.reverse()          # obrne na mestu
sez[::-1]              # nova obrnjena kopija
```

> ⚠️ **Aliasi.** `b = a` ne naredi kopije — obe imeni kažeta na isti seznam.
> Kopijo naredi z `a[:]` ali `list(a)`. Če naloga pravi "ne spreminjaj vhodnega
> seznama", je to obvezno.

**Izpeljani seznami:**

```python
[2 * n for n in range(1, 10)]
[n**2 for n in range(10) if n % 2 == 0]
[int(c) for c in str(3141592)]
[(i, j) for i in range(3) for j in range(i, 3)]      # dve zanki
{x: x**2 for x in sez}                               # izpeljan slovar
{x for x in sez if x > 0}                            # izpeljana množica
```

### 4b. Iskanje maksimuma / minimuma (argmax, argmin)

**Najpogostejši vzorec na izpitih.** Vaje pogosto prepovejo `min`/`max`.

```python
# največji element (ročno)
naj = sez[0]
for x in sez[1:]:
    if x > naj:
        naj = x

# največji z varovalko za prazen seznam
def najvecji(sez):
    if not sez:
        return None
    naj = sez[0]
    for x in sez[1:]:
        if x > naj:
            naj = x
    return naj
```

**Argmin brez ustvarjanja novih seznamov** (izpit 25/26 i1 to izrecno zahteva):

```python
def najblizja_stranka(centrala, stranke):
    najblizja = None
    for stranka in stranke:
        if najblizja is None or razdalja(centrala, stranka) < razdalja(centrala, najblizja):
            najblizja = stranka
    return najblizja        # None, če je seznam prazen — točno kot zahtevajo
```

**Argmin/argmax, ki vrne INDEKS** (izpit 24/25 i2, `klic`):

```python
def klic(nadstropje, dvigala):
    najboljsi = 0
    for i in range(1, len(dvigala)):
        if dvigala[i].razdalja(nadstropje) < dvigala[najboljsi].razdalja(nadstropje):
            najboljsi = i
    return najboljsi        # < in ne <= -> prvi najmanjši
```

Z vgrajenimi funkcijami:

```python
max(slovar, key=slovar.get)        # ključ z največjo vrednostjo
max(seznam, key=len)               # najdaljši element
min(range(len(sez)), key=lambda i: f(sez[i]))    # indeks najmanjšega
```

`min`/`max` vrneta **prvi** najmanjši/največji, kar je običajno točno tisto,
kar zahteva besedilo ("če jih je več, vrni prvega").

### 4c. Urejanje s ključem

```python
sorted(sez)                                  # nov urejen seznam
sorted(sez, reverse=True)                    # padajoče
sorted(sez, key=len)                         # po dolžini
sorted(pari, key=lambda p: p[1])             # po drugem elementu para
```

**Dvojni ključ** — padajoče po številu, pri enakem naraščajoče po abecedi
(pojavi se skoraj vsako leto):

```python
urejeno = sorted(pogostost.items(), key=lambda p: (-p[1], p[0]))
prvi_trije = [ime for ime, n in urejeno[:3]]
```

Nabori se primerjajo leksikografsko, zato deluje tudi trik brez `key`:

```python
pari = [(-strani, avtor) for avtor, strani in skupaj.items()]
pari.sort()
```

### 4d. Sklad (stack)

Sklad je navaden seznam, kjer dodajaš z `append` in jemlješ z `pop`.
Klasika: preverjanje gnezdenja oklepajev.

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
    return not sklad        # na koncu mora biti prazen
```

Če je vrsta oklepaja samo ena, zadošča števec: +1 za `(`, −1 za `)`,
nikoli ne sme pasti pod 0, na koncu mora biti 0.

### 4e. Krožnost in simulacije

```python
i = (i + korak) % len(seznam)          # krožno naprej
izlocen = seznam.pop(i)                # odstrani in nadaljuj
```

Izštevanke (izpit 23/24 i2): ponavljaj, dokler ne ostane en igralec.

```python
def zmagovalec(igralci, zacetni, izstevanke):
    igralci = list(igralci)            # kopija — ne kvari vhoda
    i = igralci.index(zacetni)
    k = 0
    while len(igralci) > 1:
        i = (i + izstevanke[k % len(izstevanke)] - 1) % len(igralci)
        igralci.pop(i)
        i %= len(igralci)              # po brisanju je isti indeks že naslednji
        k += 1
    return igralci[0]
```

### 4f. Podzaporedja in primerjave

```python
def je_podzaporedje(proga, obiskane):
    """Ali se vse točke proge pojavijo v obiskanih v pravem vrstnem redu."""
    k = 0
    for tocka in obiskane:
        if k < len(proga) and tocka == proga[k]:
            k += 1
    return k == len(proga)
```

```python
all(pogoj(x) for x in sez)     # velja za vse
any(pogoj(x) for x in sez)     # velja za vsaj enega
all(c in drugi for c in prvi)  # so vsi znaki prvega v drugem
```

### 4g. Točke, razdalje, krogi

```python
def razdalja(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def v_uniji(x0, y0, krogi):
    for x, y, r in krogi:                       # razpakiranje v zanki!
        if (x - x0)**2 + (y - y0)**2 <= r**2:
            return True
    return False

def v_preseku(x0, y0, krogi):
    for x, y, r in krogi:
        if (x - x0)**2 + (y - y0)**2 > r**2:
            return False
    return True
```

---

## Tip 5 — Naloge s slovarji in množicami

### 5a. Slovar — osnove

```python
s = {'a': 1, 'b': 5}
s['a']              # 1
s['x']              # KeyError!
s.get('x')          # None
s.get('x', 0)       # 0        ← uporabljaj tega
s['c'] = 10         # dodaj ali posodobi
del s['a']
s.pop('b')          # odstrani in vrne
'a' in s            # preverja KLJUČE

for k in s: ...                 # po ključih
for v in s.values(): ...        # po vrednostih
for k, v in s.items(): ...      # po parih

s.update(drug)      # vrine drugega (drugi povozi)
{**a, **b}          # nov slovar, b povozi a
```

Ključ mora biti **nespremenljiv**: niz, število, nabor — nikoli seznam.
Vrstni red je vrstni red vstavljanja (Python 3.7+).

### 5b. Štetje — vzorec, ki ga rabiš vsak izpit

```python
def pogostost(zbirka):
    stevilo = {}
    for x in zbirka:
        stevilo[x] = stevilo.get(x, 0) + 1
    return stevilo
```

Deluje enako za znake v nizu, besede v seznamu, imena v datoteki.

### 5c. Gnezdene strukture

**Slovar seznamov** — več vrednosti pod istim ključem:

```python
slovar.setdefault(kljuc, []).append(vrednost)

# ali eksplicitno:
if kljuc not in slovar:
    slovar[kljuc] = []
slovar[kljuc].append(vrednost)
```

**Slovar slovarjev** (štetje obiskov, prispevki za piknik):

```python
def obiski(zapisi):
    rez = {}
    for uporabnik, stran in zapisi:
        if uporabnik not in rez:
            rez[uporabnik] = {}
        rez[uporabnik][stran] = rez[uporabnik].get(stran, 0) + 1
    return rez
```

Seštevanje čez gnezden slovar:

```python
def zbrano(prispevki):
    skupaj = {}
    for oseba, stvari in prispevki.items():
        for stvar, kolicina in stvari.items():
            skupaj[stvar] = skupaj.get(stvar, 0) + kolicina
    return skupaj
```

**Slovar s ključi-nabori** (izpit 25/26 i2, Air Triglav): `{(od, do): stevilo}`.

```python
for (od, do), stevilo in podatki.items():
    if od == kraj:
        odhodi += stevilo
    if do == kraj:
        prihodi += stevilo
```

> ⚠️ Ključ je nabor, ne slovar — `kljuc.values()` ne obstaja. Do vrednosti prideš
> z `podatki[kljuc]` ali z razpakiranjem v `.items()`, kot zgoraj.

**Filtriranje rezultata** (npr. "slovar naj ne vsebuje tistih z 0"):

```python
return {k: v for k, v in rezultat.items() if v > 0}
```

### 5d. Množice

```python
m = {1, 2, 3}
prazna = set()        # {} je prazen SLOVAR!

m.add(x)      m.update([a, b])
m.remove(x)   # napaka, če ni
m.discard(x)  # brez napake

A | B    # unija
A & B    # presek         ← "imata kaj skupnega"
A - B    # razlika
A ^ B    # simetrična razlika
A <= B   # podmnožica
```

Množice uporabi, kadar: rezultat ne sme imeti ponovitev, vrstni red ni pomemben,
ali potrebuješ hitro preverjanje `in`.

```python
def skupne_besede(a, b):
    return sorted(set(a.lower().split()) & set(b.lower().split()))
```

**Presek za "obstaja povezava"** (izpit 23/24 i1, avtobusni prevozi):

```python
if set(linija_a) & set(linija_b):
    ...      # liniji imata skupno postajo -> prestop je mogoč
```

**Vzorec "ponavljaj, dokler se množica spreminja"** (tranzitivno zaprtje):

```python
def ustrezljivi(oseba, zaljubljeni):
    rezultat = {kdo for kdo in zaljubljeni if oseba in zaljubljeni[kdo]}
    spremenjeno = True
    while spremenjeno:
        spremenjeno = False
        for kdo in zaljubljeni:
            if kdo in rezultat:
                continue
            if any(t in rezultat for t in zaljubljeni[kdo]):
                rezultat.add(kdo)
                spremenjeno = True
    return rezultat
```

### 5e. Permutacije

Permutacijo predstavimo kot slovar `x → π(x)` ali kot seznam slik ali kot cikle.

```python
def cikel(p, x):
    sez = [x]
    naslednji = p[x]
    while naslednji != x:
        sez.append(naslednji)
        naslednji = p[naslednji]
    return sez

def cikli(p):
    obiskani = set()
    rezultat = []
    for x in sorted(p):
        if x in obiskani:
            continue
        c = cikel(p, x)
        obiskani.update(c)
        rezultat.append(c)
    return rezultat

def je_permutacija(p):
    return set(p.keys()) == set(p.values())

def inverz_perm(p):                  # seznamski zapis, 1-indeksiran
    n = len(p)
    inv = [0] * n
    for i in range(n):
        inv[p[i] - 1] = i + 1
    return inv
```

**Red permutacije** = najmanjši skupni večkratnik dolžin ciklov.
**Inverz v cikličnem zapisu** = vsak cikel obrni (`c[::-1]`).

---

## Tip 6 — Naloge z matrikami in mrežami

Zadnji dve leti se ta tip pojavlja skoraj vedno (osmerosmerke, ladjice, koda QR,
Dostavljalec Miran).

### 6a. Ustvarjanje in dostop

```python
mat = [[1, 2, 3],
       [4, 5, 6]]

mat[i][j]              # vrstica i, stolpec j
n = len(mat)           # število vrstic
m = len(mat[0])        # število stolpcev

# nova n×m matrika
matrika = [[None for _ in range(m)] for _ in range(n)]
matrika = [[0] * m for _ in range(n)]
```

> ⚠️ **Nikoli `[[0] * m] * n`** — vse vrstice bi bile isti objekt in sprememba
> ene bi spremenila vse.

### 6b. Sprehod, meje, smeri

```python
for i in range(len(mat)):
    for j in range(len(mat[0])):
        ...

def znotraj(mreza, i, j):
    return 0 <= i < len(mreza) and 0 <= j < len(mreza[0])

SMERI = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
SOSEDI4 = [(-1,0), (1,0), (0,-1), (0,1)]
```

**Hoja v dani smeri** (osmerosmerke):

```python
def preveri_besedo(mreza, beseda, zacetek, smer):
    i, j = zacetek
    di, dj = smer
    for znak in beseda:
        if not znotraj(mreza, i, j) or mreza[i][j] != znak:
            return False
        i, j = i + di, j + dj
    return True

def poisci_besedo(mreza, beseda):
    for i in range(len(mreza)):
        for j in range(len(mreza[0])):
            for smer in SMERI:
                if preveri_besedo(mreza, beseda, (i, j), smer):
                    return (i, j), smer
    return None
```

**Sosedi z mejami** (igra življenja):

```python
def zivi_sosedi(svet, i, j):
    n, m = len(svet), len(svet[0])
    st = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and svet[ni][nj]:
                st += 1
    return st

def igra(svet):
    n, m = len(svet), len(svet[0])
    novo = [[False] * m for _ in range(n)]      # novo stanje računaj iz STAREGA
    for i in range(n):
        for j in range(m):
            ss = zivi_sosedi(svet, i, j)
            novo[i][j] = (ss in (2, 3)) if svet[i][j] else (ss == 3)
    return novo
```

### 6c. Izpis matrike kot niz

```python
def __str__(self):
    return '\n'.join(''.join(pretvori(x) for x in vrstica) for vrstica in self.matrika)
```

Kjer je npr. `pretvori`: `None → '.'`, `0 → ' '`, `1 → '#'`.

Okvir okoli plošče (potapljanje ladjic):

```python
n = len(plosca[0])
print('/' + '-' * n + '\\', file=f)
for vrstica in plosca:
    print('|' + ''.join(vrstica) + '|', file=f)
print('\\' + '-' * n + '/', file=f)
```

### 6d. Klasične matrične operacije

```python
def identiteta(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def sled(M):
    return sum(M[i][i] for i in range(min(len(M), len(M[0]))))

def transponiraj(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def sestej(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def uporabi(M, v):                     # M · v
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def pomnozi(A, B):
    n, m, p = len(A), len(A[0]), len(B[0])
    rez = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                rez[i][j] += A[i][k] * B[k][j]
    return rez
```

---

## Tip 7 — Naloge z razredi

**Razred je na izpitu v 8 od 9 primerov.** To je najbolj donosen sklop za učenje.

### 7a. Skelet

```python
class ImeRazreda:
    def __init__(self, a, b=0):        # konstruktor
        self.a = a                      # atributi objekta
        self.b = b
        self.stanje = []                # dodatno stanje, ki ga naloga rabi

    def metoda(self, x):                # PRVI parameter je vedno self
        return self.a + x

objekt = ImeRazreda(10)     # __init__ se pokliče samodejno
objekt.a                    # 10
objekt.metoda(5)            # 15
```

Tri pravila, ki jih testi neizprosno preverijo:

1. **Konstruktor ne vrača ničesar.** Vrednosti shrani v `self.<ime>`.
   `return matrika` v `__init__` je napaka.
2. **Vsaka metoda ima `self`** kot prvi parameter, tudi `__str__`.
3. **Metode so v telesu razreda** (zamaknjene) in se imenujejo **točno** tako kot
   v besedilu. `premik`, ne `__premik__`; in nikoli kot samostojna funkcija pod razredom.

Privzete vrednosti v konstruktorju (izpit 24/25 i2, mirujoče dvigalo v pritličju):

```python
def __init__(self, nadstropje=0, postanki=None):
    self.nadstropje = nadstropje
    self.postanki = [] if postanki is None else list(postanki)
```

### 7b. Posebne (dunder) metode

| Metoda | Kdaj se pokliče |
|---|---|
| `__init__(self, ...)` | `Razred(...)` |
| `__repr__(self)` | izpis v konzoli, `repr(o)` — naj izgleda kot klic konstruktorja |
| `__str__(self)` | `print(o)`, `str(o)` — človeku prijazno |
| `__eq__(self, o)` | `o1 == o2` |
| `__lt__(self, o)` | `o1 < o2` → omogoči `sort`, `min`, `max` |
| `__add__` `__sub__` `__mul__` `__truediv__` | `+ - * /` |
| `__len__(self)` | `len(o)` |
| `__getitem__(self, i)` | `o[i]` in `o[1:5]` |
| `__contains__(self, x)` | `x in o` |
| `__call__(self, x)` | `o(x)` |
| `__iter__(self)` | `for x in o` |

```python
def __repr__(self):
    return f'Dvigalo({self.nadstropje!r}, {self.postanki!r})'   # !r doda narekovaje

def __str__(self):
    return f'dvigalo v {self.nadstropje}. nadstropju'

def __eq__(self, other):
    return (self.a, self.b) == (other.a, other.b)      # naborni trik

def __lt__(self, other):
    return (self.leto, self.mesec, self.dan) < (other.leto, other.mesec, other.dan)
```

`__lt__` z naborom je najlažji način za "primerjaj po prvem, pri enakem po drugem".

### 7c. Metoda, ki vrne NOV objekt istega razreda

Aritmetika (`Ulomek`, `Polinom`) in množične operacije (`Stevec`, izpit 25/26 i1)
delujejo enako: zgradi nov objekt in ga **vrni**, originalov ne spreminjaj.

```python
class Stevec:
    def __init__(self, elementi):
        self.stevilo = {}
        for element in elementi:
            self.stevilo[element] = self.stevilo.get(element, 0) + 1

    def koliko(self, element):
        return self.stevilo.get(element, 0)

    def __eq__(self, other):
        return self.stevilo == other.stevilo

    def dodaj(self, element):
        self.stevilo[element] = self.stevilo.get(element, 0) + 1

    def unija(self, other):
        nov = Stevec([])                                  # prazen nov objekt
        for element in set(self.stevilo) | set(other.stevilo):
            nov.stevilo[element] = self.koliko(element) + other.koliko(element)
        return nov

    def presek(self, other):
        nov = Stevec([])
        for element in set(self.stevilo) & set(other.stevilo):
            nov.stevilo[element] = min(self.koliko(element), other.koliko(element))
        return nov
```

```python
class Ulomek:
    def __init__(self, st, im):
        if im < 0:
            st, im = -st, -im                 # predznak vedno v števcu
        d = abs(gcd(st, im))
        self.st = st // d                     # vedno okrajšan
        self.im = im // d

    def __str__(self):  return f'{self.st}/{self.im}'
    def __repr__(self): return f'Ulomek({self.st}, {self.im})'
    def __eq__(self, o):  return self.st == o.st and self.im == o.im
    def __add__(self, o): return Ulomek(self.st*o.im + self.im*o.st, self.im*o.im)
    def __sub__(self, o): return Ulomek(self.st*o.im - self.im*o.st, self.im*o.im)
    def __mul__(self, o): return Ulomek(self.st*o.st, self.im*o.im)
    def __truediv__(self, o): return Ulomek(self.st*o.im, self.im*o.st)
```

```python
class Polinom:
    def __init__(self, koef):
        zadnji = len(koef)
        while zadnji > 0 and koef[zadnji - 1] == 0:
            zadnji -= 1
        self.koef = koef[:zadnji]           # rezina = kopija, odreže ničle

    def stopnja(self):
        return len(self.koef) - 1 if self.koef else float('-inf')

    def __call__(self, x):                  # Hornerjev algoritem
        rezultat = 0
        for a in reversed(self.koef):
            rezultat = rezultat * x + a
        return rezultat

    def __add__(self, o):
        d = max(len(self.koef), len(o.koef))
        a = self.koef + [0] * (d - len(self.koef))
        b = o.koef + [0] * (d - len(o.koef))
        return Polinom([a[i] + b[i] for i in range(d)])

    def __mul__(self, o):
        if not self.koef or not o.koef:
            return Polinom([])
        k = [0] * (len(self.koef) + len(o.koef) - 1)
        for i, a in enumerate(self.koef):
            for j, b in enumerate(o.koef):
                k[i + j] += a * b
        return Polinom(k)
```

### 7d. Objekt s stanjem, ki ga metode spreminjajo

Metoda **ne vrne** novega objekta, ampak spremeni `self` (izpit 25/26 i2, `Izvidnica`;
24/25 i1, `Naseljenec`).

```python
class Izvidnica:
    def __init__(self, x, y, smer, st_korakov):
        self.x = x
        self.y = y
        self.smer = smer
        self.st_korakov = st_korakov
        self.najdbe = set()

    def premik(self):
        if self.x <= 0:              # pot je zaključena — ne naredi nič
            return
        if self.st_korakov > 0:
            self.st_korakov -= 1
            if self.smer == 'S':
                self.y += 1
            elif self.smer == 'J':
                self.y -= 1
            elif self.smer == 'V':
                self.x += 1
        else:
            self.x -= 1              # po porabljenih korakih vedno na zahod

    def preisci(self):
        if ima_zanimivost(self.x, self.y):
            self.najdbe.add((self.x, self.y))

    def do_sedaj(self):
        return self.najdbe
```

Simulacijo vodi funkcija **zunaj** razreda:

```python
def preiskovanje(zacetki):
    izvidnice = []
    for x, y, smer, st_korakov in zacetki:
        izvidnica = Izvidnica(x, y, smer, st_korakov)
        while izvidnica.x > 0:
            izvidnica.preisci()
            izvidnica.premik()
        izvidnice.append(izvidnica)
    return izvidnice
```

Podoben vzorec — `BitniCekin` (metoda vrne `True`/`False` o uspehu):

```python
class BitniCekin:
    def __init__(self, stanje=0):
        self.stanje = stanje

    def dvig(self, koliko):
        if self.stanje >= koliko:
            self.stanje -= koliko
            return True
        return False

    def polog(self, koliko):
        self.stanje += koliko
        return self.stanje

def prenesi(rac1, rac2, koliko):
    if rac1.dvig(koliko):
        rac2.polog(koliko)
        return True
    return False
```

### 7e. Razred, ki hrani zbirko, in preverjanje vhoda

```python
class Oseba:
    def __init__(self, ime, priimek, vzdevek=None):
        self.ime = ime
        self.priimek = priimek
        self.vzdevek = vzdevek

    def __str__(self):                                # Ime "Vzdevek" Priimek
        if self.vzdevek is None:
            return f'{self.ime} {self.priimek}'
        return f'{self.ime} "{self.vzdevek}" {self.priimek}'

    def __repr__(self):                               # KLIC KONSTRUKTORJA, ne isto kot __str__
        return f'Oseba({self.ime!r}, {self.priimek!r}, vzdevek={self.vzdevek!r})'


class Imenik:
    def __init__(self):
        self.imenik = {}

    def dodaj(self, stevilka, oseba):
        if not isinstance(oseba, Oseba):
            return                                    # tiho ne naredi nič
        preostanek = stevilka[1:] if stevilka[:1] == '+' else stevilka
        if not preostanek.isdigit():                  # same števke, razen vodilnega '+'
            return
        self.imenik[stevilka] = oseba

    def klice(self, stevilka):
        if stevilka in self.imenik:
            return f'Kliče: {self.imenik[stevilka]}'   # uporabi __str__ Osebe
        return 'Kliče: neznana številka'
```

Dvoje, kar se tu izgubi največ točk:
- **`__repr__` ni `__str__`.** `__repr__` mora izgledati kot klic konstruktorja
  (`Oseba('Janez', 'Kranjski', vzdevek=None)`), `__str__` pa kot lep opis.
  Če enega definiraš prek drugega, pade test.
- Opis objekta v drugem razredu vedno dobi prek `str(objekt)` ali f-niza — ne
  podvajaj logike.

### 7f. Funkcije nad seznamom objektov

```python
def uredi(teze, starosti):
    zajci = [Zajec(t, s) for t, s in zip(teze, starosti)]
    zajci.sort()                     # deluje, ker ima Zajec __lt__
    return zajci

def urnik(termini):
    urejeni = sorted(termini)
    for i in range(len(urejeni) - 1):
        if urejeni[i].prekriva(urejeni[i + 1]):
            return False
    return True
```

Prekrivanje intervalov `[a,b)` in `[c,d)`: **`a < d and c < b`**. Zapomni si.

---

## Tip 8 — Naloge z datotekami

**Datoteke so na izpitu v 8 od 9 primerov**, praktično vedno kot tretja naloga.

### 8a. Branje

```python
# najpogosteje: vrstico po vrstico
with open('vhod.txt', encoding='utf-8') as d:
    for vrstica in d:
        vrstica = vrstica.strip()      # odstrani '\n'
        if not vrstica:
            continue                   # preskoči prazne
        ...

# vse naenkrat
with open('vhod.txt', encoding='utf-8') as d:
    vsebina = d.read()                 # en niz
    vrstice = d.readlines()            # seznam vrstic (z '\n')
```

`with` poskrbi, da se datoteka zapre tudi ob napaki.
**`encoding='utf-8'` na Windowsu ni izbira** — brez njega dobiš `cp1250` in šumniki
se pokvarijo.

Če rabiš številke vrstic: `for i, vrstica in enumerate(d):` (od 0) ali
`enumerate(d, 1)` (od 1).

### 8b. Pisanje

```python
with open('izhod.txt', 'w', encoding='utf-8') as d:      # 'w' povozi vsebino
    d.write('besedilo\n')                                # write NE doda \n
    print('besedilo', file=d)                            # print ga doda

with open('izhod.txt', 'a', encoding='utf-8') as d:      # 'a' doda na konec
    ...
```

Branje in pisanje hkrati:

```python
with open('vhod.txt', encoding='utf-8') as v, \
     open('izhod.txt', 'w', encoding='utf-8') as i:
    for vrstica in v:
        print(preoblikuj(vrstica.rstrip('\n')), file=i)
```

**Natančen format izpisa je vedno predpisan** — preberi besedilo dobesedno:

```python
print(f'{kljuc}: ' + ' -> '.join(postaje), file=f)      # 1: Sodisce -> Trg
print('    '.join([tocka, str(cas), str(razlika)]), file=f)   # 4 presledki
print(f'{centrala} =={d:.2f}==> {stranka}', file=f)     # (4, 5) ==3.61==> (1, 7)
print('=' * 12, file=f)                                  # točno 12 znakov
```

### 8c. CSV in strukturirane vrstice

**Vrstica → nabor z pretvorbo tipov.** Najpogostejša napaka: pozabiti `int`/`float`.

```python
def preberi(ime):
    podatki = []
    with open(ime, encoding='utf-8') as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue
            podatki.append(tuple(float(x) for x in vrstica.split(',')))
    return podatki

def nabor(niz):                       # prvi stolpec je ime, ostali števila
    deli = niz.split(',')
    deli[1:] = [int(x) for x in deli[1:]]
    return tuple(deli)
```

**Tabela z glavo vrstic in stolpcev → slovar s ključi-nabori** (Air Triglav).
Imen **nikoli ne zapiši na trdo** — preberi jih iz prve vrstice.

```python
def preberi_podatke(ime_datoteke):
    podatki = {}
    with open(ime_datoteke, encoding='utf-8') as f:
        vrstice = [v.rstrip('\n').split(',') for v in f if v.strip()]
    kraji = [k for k in vrstice[0][1:] if k]          # glava brez vodilnega '-'
    for vrstica in vrstice[1:]:
        izhodisce = vrstica[0]
        for cilj, vrednost in zip(kraji, vrstica[1:]):   # zip preživi odvečno vejico
            if vrednost.strip() != '':                   # prazna celica = ni podatka
                podatki[(izhodisce, cilj)] = int(vrednost)
    return podatki
```

**Datoteka → slovar seznamov** (avtobusne linije, 23/24 i1): ime linije se začne
s številko, ime postaje s črko.

```python
def linije(ime):
    rezultat = {}
    trenutna = None
    with open(ime, encoding='utf-8') as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue
            if vrstica[0].isdigit():
                trenutna = vrstica
                rezultat[trenutna] = []
            else:
                rezultat[trenutna].append(vrstica)
    return rezultat
```

### 8d. Mreža iz datoteke

```python
def poisci_stranke(vhodna):
    stranke = set()
    with open(vhodna, encoding='utf-8') as f:
        for i, vrstica in enumerate(f):
            for j, znak in enumerate(vrstica.strip()):
                if znak == '#':
                    stranke.add((i, j))
    return stranke

def preberi_mrezo(ime):
    with open(ime, encoding='utf-8') as f:
        return [vrstica.strip() for vrstica in f if vrstica.strip()]
```

### 8e. Preoblikovanje besedila

**Preskoči prazne vrstice in komentarje:**

```python
if not vrstica.strip() or vrstica.strip().startswith('#'):
    continue
```

**Odstrani HTML značke** (vzorec "stikalo"):

```python
def html2txt(vhod, izhod):
    with open(vhod, encoding='utf-8') as v, open(izhod, 'w', encoding='utf-8') as i:
        v_znacki = False
        for vrstica in v:
            rezultat = ''
            for z in vrstica:
                if z == '<':
                    v_znacki = True
                elif z == '>':
                    v_znacki = False
                elif not v_znacki:
                    rezultat += z
            if rezultat.strip():
                i.write(rezultat)
```

**Najpogostejše besede:**

```python
def najpogostejse_besede(vhod, n, izhod):
    besede = {}
    with open(vhod, encoding='utf-8') as d:
        for vrstica in d:
            for b in vrstica.lower().replace(',', ' ').replace('.', ' ').split():
                besede[b] = besede.get(b, 0) + 1
    naj = sorted(besede.items(), key=lambda p: (-p[1], p[0]))[:n]
    with open(izhod, 'w', encoding='utf-8') as f:
        for b, st in naj:
            print(f'{b} {st}', file=f)
```

**Poročilo z okrasjem** (Air Triglav, 3. podnaloga):

```python
def porocilo(potovanja, kraj):
    prihodi = odhodi = 0
    for (od, do), stevilo in potovanja.items():
        if od == kraj:
            odhodi += stevilo
        if do == kraj:
            prihodi += stevilo
    with open(f'{kraj}.txt', 'w', encoding='utf-8') as f:
        print(kraj, file=f)
        print('=' * 12, file=f)
        print(f'Prihodi: {prihodi}', file=f)
        print(f'Odhodi: {odhodi}', file=f)
        print('-' * 12, file=f)
        print(f'Saldo: {prihodi - odhodi}', file=f)
```

### 8f. Knjižnica `os` (redkeje, a se pojavi)

```python
import os
os.getcwd()                      os.listdir()
os.path.join('mapa', 'dat.txt')  os.path.exists(pot)
os.path.splitext('dat.txt')      # ('dat', '.txt')
os.rename(staro, novo)           os.remove(pot)
```

---

## Tip 9 — Naloge z generatorji

Generator je funkcija z **`yield` namesto `return`**. Ob klicu ne izračuna ničesar —
vrne iterator, ki vrednosti proizvaja **na zahtevo**. Zato lahko predstavlja
neskončna zaporedja.

```python
def stevke(n):
    while n > 0:
        yield n % 10          # "vrni in počakaj"
        n //= 10

g = stevke(1337)
next(g)              # 7
list(stevke(1337))   # [7, 3, 3, 1]
for s in stevke(1337): ...
```

**Neskončni generatorji** — vzame se le toliko, kolikor je treba:

```python
def potence_naravnih(k):
    n = 1
    while True:
        yield n ** k
        n += 1

def fibonaccijeva_stevila(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b

f = fibonaccijeva_stevila()
[next(f) for _ in range(10)]     # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

`list(...)` na neskončnem generatorju se **nikoli ne konča** — uporabi `next` v zanki.

```python
def collatz(n):
    yield n
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        yield n

def delitelji(n):                # yield from: prepusti vse vrednosti naprej
    mali, veliki = [], []
    d = 1
    while d * d <= n:
        if n % d == 0:
            mali.append(d)
            if d != n // d:
                veliki.append(n // d)
        d += 1
    yield from mali
    yield from reversed(veliki)
```

**Iterator ročno** (razred z `__next__`, ki na koncu sproži `StopIteration`) in
**iterabilni objekt** (razred z `__iter__`, ki vrne generator):

```python
class AritmeticnoZaporedje:
    def __init__(self, a, d):
        self.a, self.d = a, d

    def __iter__(self):
        x = self.a
        while True:
            yield x
            x += self.d
```

Razlika: **iterator** ima `__next__` in si zapomni stanje; **iterabilni objekt**
ima `__iter__`, ki vrne svež iterator; **generator** je iterator, narejen z `yield`.

---

## Dodatek A — klasične naloge z vaj

Kratek pregled, katera vaja pokriva kateri tip. Če katere ne znaš rešiti na pamet,
je to tvoja luknja.

| Vaja | Tip | Bistvo |
|---|---|---|
| Kontrolne števke, Datumi, Obresti | 1 | `%`, `//`, pogoji, `round` |
| Vsote potenc, Vsote števk, Enkratne števke | 2 | linearna rekurzija |
| Collatzovo zaporedje | 1, 2 | isto z zanko in z rekurzijo |
| Binomski simbol, Stirlingova števila | 2 | dvojna rekurzija |
| Nizi: ogrevanje, vgrajene metode | 3 | metode na nizih |
| Rezine in rekurzija | 2b, 3 | `niz[1:]`, baza = prazen niz |
| Sestavljanje | 3d | f-nizi, poravnave |
| Pravilni del gesla (vislice) | 3 | gradnja niza znak po znak |
| Kvadratni koren, Zlati rez | 1 | iterativni približki |
| Sprehod | 3c, 4 | akumulacija koordinat, števke v nizu |
| Gnezdenje oklepajev, Sklad oklepajev | 4d | sklad |
| Primerjanje, Delo s seznami | 4a, 4b | min/max ročno |
| Matrike (seznami) | 6 | identiteta, sled, transponiranje |
| Praštevila | 1 | deljenje do √n, `for/else` |
| Preverimo urejanje | 4 | sprehod po sosednjih parih |
| Ali sva za skupaj | 3, 4 | štetje črk, sosednje vsote |
| Krogi | 4g | razpakiranje `for x, y, r in krogi` |
| Permutacije (seznam in slovar) | 5e | cikli, inverz, red |
| Družinski piknik, Kuhamo in pečemo | 5 | slovarji, `get`, primerjava zalog |
| Šifriranje | 3e, 5 | slovar znak→znak, inverz |
| Ljubezen nam je vsem v pogubo | 5d | množice, tranzitivno zaprtje |
| Razdalje med točkami, Poudarjanje znakov | 3, 4g | evklidska razdalja, stikalo |
| Disemvoweling, Lepšanje in šifriranje | 3 | razrez besedila, ovijanje vrstic |
| Igra življenja | 6 | sosedi, novo stanje iz starega |
| Poker | 4, 5 | modeliranje z nabori, `random.shuffle`, kombinacije |
| Bitni cekini, Zajec | 7d | objekt s stanjem, `__lt__` |
| Ulomki, Polinomi, Matrike (razred) | 7c | metode, ki vrnejo nov objekt |
| Enostavne naloge z generatorji, Vse se začne z ena | 9 | `yield` |
| Datoteke: ogrevanje, Imena, Kolokviji | 8a–8c | branje, štetje, CSV |
| Pogoste besede | 8e, 5b | štetje + urejanje po pogostosti |
| HTML datoteke | 8e | stikalo `<` … `>` |

Nekaj rešitev, ki jih ni drugje v teh zapiskih:

```python
# Olepšano besedilo — ovijanje na dano širino
def olepsano(s, sirina):
    vrstice = []
    trenutna = ''
    for b in s.split():
        if not trenutna:
            trenutna = b
        elif len(trenutna) + 1 + len(b) <= sirina:
            trenutna += ' ' + b
        else:
            vrstice.append(trenutna)
            trenutna = b
    if trenutna:
        vrstice.append(trenutna)
    return '\n'.join(vrstice)

# Disemvoweling — samoglasniki na konec
def disemvowel(s):
    samoglasniki = ''.join(z for z in s if z in 'aeiouAEIOU')
    ostalo = ''.join(z for z in s if z not in 'aeiouAEIOU')
    return ostalo + samoglasniki

# Poudari — presledek med črkami
def poudari(naslov):
    return ' '.join(naslov.upper())

# Palindrom
def je_palindrom(niz):
    return niz == niz[::-1]

# Poker: lestvica
def tvorijo_lestvico(karte):
    visine = sorted(k[0] for k in karte)
    return all(visine[i] == visine[0] + i for i in range(len(visine)))
```

---

## Dodatek B — pasti, ki stanejo točke

| Past | Kaj se zgodi | Rešitev |
|---|---|---|
| `sez.sort()` prirediš | `None` | `sorted(sez)` ali sortiraj v ločeni vrstici |
| `[[0]*3]*3` | vse vrstice isti objekt | `[[0]*3 for _ in range(3)]` |
| `{}` za prazno množico | dobiš slovar | `set()` |
| `niz[0] = 'x'` | `TypeError` | `niz = niz[:0] + 'x' + niz[1:]` |
| `vrstica + '.'` brez prireditve | nič se ne zgodi | `vrstica += '.'` |
| `def f(x, sez=[])` | seznam se deli med klici | `sez=None` + `if sez is None` |
| `b = a` pri seznamu | alias, ne kopija | `b = a[:]` ali `list(a)` |
| pozabljen `return` | `None` | preveri vsako vejo funkcije |
| manjkajoč `self` | `TypeError` / `AttributeError` | vsaka metoda se začne s `self` |
| metoda zunaj razreda | `AttributeError: no attribute 'x'` | zamakni jo v telo razreda |
| ime metode po svoje | `AttributeError` | prepiši ime iz besedila |
| `/` namesto `//` | `float` namesto `int` | `//` za celoštevilsko |
| pozabljen `float()` pri branju | primerja nize | `float(x)` / `int(x)` |
| pozabljen `round(x, 2)` | napačen rezultat | preberi, ali naloga to zahteva |
| vrneš `False` namesto `None` | test pade | beri besedilo dobesedno |
| vrneš seznam namesto nabora/množice | test pade | `tuple(...)`, `set(...)` |
| deljenje z 0 pri deležu | `ZeroDivisionError` | najprej `if vseh == 0: return None` |
| `n[0] == kos[0]` za predpono | primerja le prvo črko | `n.startswith(kos)` |
| imena iz primera zakodirana na trdo | pade na drugem vhodu | zanka čez prebrane podatke |
| `x ** 1/2` | `(x**1)/2` | `x ** 0.5` ali `x ** (1/2)` |
| mešani zamiki | `IndentationError` | povsod 4 presledki |
| brez `encoding='utf-8'` | pokvarjeni šumniki | vedno ga dodaj |
| bazni primer `set()` pri zbiranju rešitev | vedno prazen rezultat | `{()}` |

---

## Dodatek C — postopek reševanja naloge

1. **Preberi celo nalogo, vse tri podnaloge, preden začneš pisati.**
   Podnaloga 1 je skoraj vedno pomožna funkcija za 2 in 3 — napiši jo v obliki,
   ki jo boš rabil naprej.
2. **Iz besedila prepiši:** ime funkcije/metode, imena atributov, tip rezultata.
3. **Poglej primere `>>>`.** V njih je vse: robni primeri, tip rezultata, format izpisa.
   Če se primer v besedilu in testi ne ujemata, **veljajo testi**.
4. **Najprej robni primer**, da glavni del ostane čist:
   ```python
   def f(seznam):
       if not seznam:
           return None
       ...
   ```
5. **Napiši ogrodje**: `def ime(args):` … `return rezultat`. Nato ga zapolni.
6. **Preveri na roko** s prvim primerom iz besedila.
7. **Preglej seznam pasti** (Dodatek B) za tisto, kar si pravkar napisal:
   `return`? tip? `round`? `None`? `self`?
8. **Če se zatakne pri 3. podnalogi**, oddaj vsaj različico, ki reši osnovni primer —
   podnaloge se ocenjujejo ločeno.

---

# Del C — Kuharica (samo koda za prepis)

Brez razlage, za hitrost. Sklici oblike **§C4** v Delu A pomenijo razdelek 4 tega dela.
Odseki z ✅ so bili pognani skozi prave teste Projekta Tomo in sprejeti.

## 1. Razred: skelet, ki pokrije 90 % nalog

`__str__`/`__repr__` so zahtevali v 6 od 8 nalog z razredom — a v obeh izpitih
2025/26 **ne**, tam sta bila `__eq__` in vsebinske metode. Znaj oboje.

```python
class Dvigalo:
    def __init__(self, nadstropje=0, postanki=None):   # privzete vrednosti!
        self.nadstropje = nadstropje
        # POZOR: nikoli `postanki=[]` v glavi funkcije (skupen seznam med objekti)
        self.postanki = [] if postanki is None else list(postanki)

    def __repr__(self):
        # repr naj izgleda kot klic konstruktorja
        return f'Dvigalo({self.nadstropje!r}, {self.postanki!r})'

    def __str__(self):
        return f'dvigalo v {self.nadstropje}. nadstropju'

    def __eq__(self, other):
        return (self.nadstropje, self.postanki) == (other.nadstropje, other.postanki)

    def __lt__(self, other):          # omogoči <, sorted(), min(), max()
        return self.nadstropje < other.nadstropje

    def __len__(self):
        return len(self.postanki)

    def __getitem__(self, i):         # omogoči objekt[i] IN objekt[1:5]
        return self.postanki[i]
```

Pasti, ki so te že stale točk:
- konstruktor **ne vrača** ničesar — vrednosti shrani v `self.<ime>`;
- vsaka metoda ima kot prvi parameter `self`;
- metode pišeš **znotraj telesa razreda** (z zamikom) in **z imenom iz besedila**
  — `premik`, ne `__premik__`, in ne kot samostojno funkcijo pod razredom;
- `!r` v f-nizu da `repr` (nizi dobijo narekovaje) — točno to rabiš v `__repr__`.

Preverjanje tipa (24/25 i3):
```python
if not isinstance(oseba, Oseba):
    return
```

### 1a. Razred s slovarjem v atributu; metoda vrne NOV objekt ✅
Vzorec iz `Stevec` (25/26 i1) — najnovejši tip razredne naloge.

```python
class Stevec:
    def __init__(self, elementi):
        self.stevilo = {}
        for element in elementi:
            self.stevilo[element] = self.stevilo.get(element, 0) + 1

    def koliko(self, element):
        return self.stevilo.get(element, 0)      # 0, če ga ni

    def __eq__(self, other):
        return self.stevilo == other.stevilo     # slovarja primerjaj kar z ==

    def dodaj(self, element):
        self.stevilo[element] = self.stevilo.get(element, 0) + 1

    def unija(self, other):
        nov = Stevec([])                         # nov, prazen objekt istega razreda
        for element in set(self.stevilo) | set(other.stevilo):
            nov.stevilo[element] = self.koliko(element) + other.koliko(element)
        return nov                               # ... in ga vrni

    def presek(self, other):
        nov = Stevec([])
        for element in set(self.stevilo) & set(other.stevilo):
            nov.stevilo[element] = min(self.koliko(element), other.koliko(element))
        return nov
```

### 1b. Objekt s stanjem, ki ga metoda spreminja korak za korakom ✅
Vzorec iz `Izvidnica` (25/26 i2). Vse, kar metoda potrebuje, je že v `self` —
metoda naj **ne** dobiva istih podatkov še enkrat kot parametre.

```python
class Izvidnica:
    def __init__(self, x, y, smer, st_korakov):
        self.x = x
        self.y = y
        self.smer = smer
        self.st_korakov = st_korakov
        self.najdbe = set()          # dodatno stanje, ki ga naloga rabi kasneje

    def premik(self):
        if self.x <= 0:              # pot je zaključena — ne naredi nič
            return
        if self.st_korakov > 0:
            self.st_korakov -= 1
            if self.smer == 'S':
                self.y += 1
            elif self.smer == 'J':
                self.y -= 1
            elif self.smer == 'V':
                self.x += 1
        else:
            self.x -= 1              # po porabljenih korakih vedno na zahod

    def preisci(self):
        if ima_zanimivost(self.x, self.y):
            self.najdbe.add((self.x, self.y))

    def do_sedaj(self):
        return self.najdbe
```

Simulacijo do konca potem vodi funkcija zunaj razreda:
```python
def preiskovanje(zacetki):
    izvidnice = []
    for x, y, smer, st_korakov in zacetki:
        izvidnica = Izvidnica(x, y, smer, st_korakov)
        while izvidnica.x > 0:
            izvidnica.preisci()
            izvidnica.premik()
        izvidnice.append(izvidnica)
    return izvidnice
```

---

## 2. Datoteke

```python
# --- branje vrstic ---
def preberi(ime):
    vrstice = []
    with open(ime, encoding='utf-8') as f:
        for vrstica in f:
            vrstice.append(vrstica.strip())     # strip() odstrani '\n'
    return vrstice

# --- branje CSV v nabore števil (GPS!) ---
def preberi_stevila(ime):
    podatki = []
    with open(ime, encoding='utf-8') as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if not vrstica:
                continue
            podatki.append(tuple(float(x) for x in vrstica.split(',')))
    return podatki                              # NE nizi — pretvori v float/int!

# --- pisanje ---
def zapisi(slovar, ime):
    with open(ime, 'w', encoding='utf-8') as f:
        for kljuc, seznam in slovar.items():
            print(f'{kljuc}: ' + ' -> '.join(seznam), file=f)

# --- preslikava datoteke vrstico po vrstico ---
def popravi(vhodna, izhodna):
    with open(vhodna, encoding='utf-8') as vhod, open(izhodna, 'w', encoding='utf-8') as izhod:
        for vrstica in vhod:
            print(preoblikuj(vrstica.rstrip('\n')), file=izhod)
```

Formatiran izpis, kot ga radi zahtevajo:
```python
print('    '.join([tocka, str(cas), str(razlika)]), file=f)   # 4 presledki
print(f'{ime:<10}{cena:>8.2f}', file=f)                        # poravnava
```

Preskoči prazne vrstice in komentarje (23/24 i2):
```python
if not vrstica.strip() or vrstica.strip().startswith('#'):
    continue
```

### 2a. Mreža iz datoteke → množica koordinat ✅
Vzorec iz `poisci_stranke` (25/26 i1). `enumerate` na datoteki in na vrstici
naenkrat je najkrajša pot do koordinat.

```python
def poisci_stranke(vhodna):
    stranke = set()
    with open(vhodna, encoding='utf-8') as f:
        for i, vrstica in enumerate(f):
            for j, znak in enumerate(vrstica.strip()):
                if znak == '#':
                    stranke.add((i, j))
    return stranke
```

### 2b. Tabela CSV z glavo vrstic in stolpcev → slovar s ključi-nabori ✅
Vzorec iz Air Triglav (25/26 i2). **Nikoli ne zakodiraj imen iz primera** —
preberi jih iz prve vrstice. `zip` sam poskrbi za odvečno vejico na koncu vrstice.

```python
def preberi_podatke(ime_datoteke):
    podatki = {}
    with open(ime_datoteke, encoding='utf-8') as f:
        vrstice = [v.rstrip('\n').split(',') for v in f if v.strip()]
    kraji = [k for k in vrstice[0][1:] if k]        # glava brez vodilnega '-'
    for vrstica in vrstice[1:]:
        izhodisce = vrstica[0]
        for cilj, vrednost in zip(kraji, vrstica[1:]):
            if vrednost.strip() != '':              # prazna celica = ni podatka
                podatki[(izhodisce, cilj)] = int(vrednost)
    return podatki
```

Branje takega slovarja nazaj (past: `a.values()` na ključu ne obstaja):
```python
for (od, do), stevilo in podatki.items():
    if od == kraj:
        odhodi += stevilo
    if do == kraj:
        prihodi += stevilo
```

### 2c. Poročilo z natančnim formatom ✅
```python
with open(f'{kraj}.txt', 'w', encoding='utf-8') as f:
    print(kraj, file=f)
    print('=' * 12, file=f)          # "vrstici imata po 12 znakov"
    print(f'Prihodi: {prihodi}', file=f)
    print(f'Odhodi: {odhodi}', file=f)
    print('-' * 12, file=f)
    print(f'Saldo: {prihodi - odhodi}', file=f)

# vrstica oblike:  (4, 5) ==3.61==> (1, 7)
print(f'{centrala} =={d:.2f}==> {stranka}', file=f)
```

---

## 3. Štetje v slovar in frekvence

```python
def pogostost(niz):
    slovar = {}
    for znak in niz:
        slovar[znak] = slovar.get(znak, 0) + 1
    return slovar

# seštevanje gnezdenih slovarjev (piknik)
def zbrano(prispevki):
    skupaj = {}
    for oseba, stvari in prispevki.items():
        for stvar, kolicina in stvari.items():
            skupaj[stvar] = skupaj.get(stvar, 0) + kolicina
    return skupaj

# slovar seznamov (linije, rop)
slovar.setdefault(kljuc, []).append(vrednost)
```

---

## 4. argmax / argmin — najpogostejši vzorec na izpitu

```python
# največji po vrednosti v slovarju -> ključ
najboljsi = max(slovar, key=slovar.get)

# ročni argmin, ki NE ustvari novega seznama in ne spremeni vhodnega ✅
# (25/26 i1 to izrecno zahteva)
def najblizja_stranka(centrala, stranke):
    najblizja = None
    for stranka in stranke:
        if najblizja is None or razdalja(centrala, stranka) < razdalja(centrala, najblizja):
            najblizja = stranka
    return najblizja          # None, če je seznam prazen — točno kot zahtevajo

# najmanjši objekt v seznamu -> INDEKS (dvigala, orientacijski tek)
def klic(nadstropje, dvigala):
    najboljsi = 0
    for i in range(1, len(dvigala)):
        if dvigala[i].razdalja(nadstropje) < dvigala[najboljsi].razdalja(nadstropje):
            najboljsi = i
    return najboljsi

# ali krajše (min vrne PRVI najmanjši, kar je običajno ravno zahtevano)
najboljsi = min(range(len(dvigala)), key=lambda i: dvigala[i].razdalja(nadstropje))

# najdaljši element seznama
najdaljsi = max(seznam, key=len)
```

Urejanje z dvojnim ključem — padajoče po številu, naraščajoče po abecedi
(23/24 i3, `najpogostejsa_imena`):
```python
urejeno = sorted(pogostost.items(), key=lambda par: (-par[1], par[0]))
prvi_trije = [ime for ime, n in urejeno[:3]]
```

Urejanje po lastni abecedi (23/24 i1, slovenska abeceda):
```python
ABECEDA = 'abcčdefghijklmnoprsštuvzž'
def kljuc(beseda):
    return [ABECEDA.index(znak) for znak in beseda]
sorted(besede, key=kljuc)
```

---

## 5. Nizi

```python
niz.strip() .lstrip() .rstrip()      niz.split(',')      ' -> '.join(seznam)
niz.replace('a', 'b')                niz.startswith('#') niz.endswith('=')
niz.isdigit() .isalpha() .isalnum()  niz.lower() .upper() niz.count('a')
niz.find('x')   # -1 če ni          niz.index('x')  # napaka če ni
```

Gradnja niza (nizi so **nespremenljivi** — `vrstica + '.'` samo po sebi ne naredi nič):
```python
vrstica = ''
for znak in mreza_vrstica:
    vrstica += '.'          # ali: kosi.append('.') ... ''.join(kosi)
```

Rezanje na bloke fiksne dolžine (DNA, base64):
```python
kodoni = [dna[i:i+3] for i in range(0, len(dna) - 2, 3)]   # samo POLNI bloki
```

Branje večmestnega števila iz niza (sprehodi):
```python
i = 0
while i < len(opis):
    if opis[i].isdigit():
        j = i
        while j < len(opis) and opis[j].isdigit():
            j += 1
        stevilo = int(opis[i:j])
        znak = opis[j] if j < len(opis) else ''
        i = j + 1
    else:
        stevilo, znak = 1, opis[i]
        i += 1
    # ... obdelaj (stevilo, znak)
```

Preverjanje predpone — in vsi kosi, ki so predpona niza ✅ (25/26 i2):
```python
def se_zacne(n, s):
    return [kos for kos in s if n.startswith(kos)]
```
⚠️ `n[0] == kos[0]` **ni** isto — primerja le prvo črko.

Branje "žetonov" iz niza — vzorec, ki reši značke, čustvenčke in števila ✅
(25/26 i1, `znacke`):
```python
def znacke(vsebina):
    najdene = set()
    i = 0
    while i < len(vsebina):
        if vsebina[i] == '#':
            j = i + 1
            while j < len(vsebina) and vsebina[j].isalnum():
                j += 1
            if j > i + 1:                 # za '#' mora biti vsaj en znak
                najdene.add(vsebina[i:j])
            i = j
        else:
            i += 1
    return najdene
```

Delež z varovalko pred deljenjem z 0 ✅:
```python
def delez_objav_z_znackami(objave, oseba):
    vseh = z_znacko = 0
    for kdo, vsebina in objave:
        if kdo == oseba:
            vseh += 1
            if znacke(vsebina):
                z_znacko += 1
    if vseh == 0:
        return None            # naloga skoraj vedno zahteva None, ne 0
    return z_znacko / vseh
```

Iskanje vzorca `:beseda:` brez regexa (klepet):
```python
def custvencki_v_besedilu(besedilo):
    najdeni = set()
    kosi = besedilo.split(':')
    for k in range(1, len(kosi), 2):          # lihi kosi so med dvopičjema
        if kosi[k] and all('a' <= z <= 'z' for z in kosi[k]):
            najdeni.add(f':{kosi[k]}:')
    return najdeni
```

Validacija znakov:
```python
if not all(z in 'ATGC' for z in dna):
    return None
```

---

## 6. Matrike in mreže (osmerosmerke, ladjice, QR)

```python
# ustvarjanje n x m matrike — NIKOLI [[None] * m] * n (skupne vrstice!)
matrika = [[None for _ in range(m)] for _ in range(n)]

# izpis matrike kot niz
def __str__(self):
    return '\n'.join(''.join(pretvori(x) for x in vrstica) for vrstica in self.matrika)

# osem smeri
SMERI = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# preverjanje meja — vedno, preden dostopaš!
def znotraj(mreza, i, j):
    return 0 <= i < len(mreza) and 0 <= j < len(mreza[0])

# hoja v smeri
def preveri_besedo(mreza, beseda, zacetek, smer):
    i, j = zacetek
    di, dj = smer
    for znak in beseda:
        if not znotraj(mreza, i, j) or mreza[i][j] != znak:
            return False
        i, j = i + di, j + dj
    return True

# iskanje po vseh začetkih in smereh
for i in range(len(mreza)):
    for j in range(len(mreza[0])):
        for smer in SMERI:
            if preveri_besedo(mreza, beseda, (i, j), smer):
                return (i, j), smer
```

Okvir okoli plošče (ladjice):
```python
n = len(plosca[0])
print('/' + '-' * n + '\\', file=f)
for vrstica in plosca:
    print('|' + ''.join(vrstica) + '|', file=f)
print('\\' + '-' * n + '/', file=f)
```

---

## 7. Seznami, krožnost, podzaporedja

```python
# krožno gibanje (izštevanke)
i = (i + korak - 1) % len(igralci)
izlocen = igralci.pop(i)

# ali je `proga` podzaporedje `tek`-a (orientacijski tek)
def je_podzaporedje(proga, obiskane):
    it = iter(obiskane)
    return all(tocka in it for tocka in proga)

# ročno, brez trikov:
def je_podzaporedje(proga, obiskane):
    k = 0
    for tocka in obiskane:
        if k < len(proga) and tocka == proga[k]:
            k += 1
    return k == len(proga)
```

---

## 8. Množice

```python
a & b   # presek        a | b   # unija       a - b   # razlika
if mnozica_a & mnozica_b:   # imata kaj skupnega -> obstaja prestop
```

---

## 9. Drobnarije, ki stanejo točke

```python
round(x, 2)                       # kadar naloga reče "zaokroži na dve mesti"
return None                       # kadar vhod ni veljaven (NE False, če piše None)
tuple(seznam)                     # kadar test pričakuje nabor, ne seznam
list(seznam)                      # kopija, da ne pokvariš vhodnega argumenta
from random import randint        # randint(1, 6) vključuje obe meji
abs(a - b)                        # razdalja
(dx ** 2 + dy ** 2) ** 0.5        # evklidska razdalja
sum(seznam) / len(seznam)         # povprečje
```

Privzeti argument, ki lahko določi rezultat (Katan, `roka_usode`):
```python
def roka_usode(vsota=None):
    if vsota is not None:
        return vsota
    return randint(1, 6) + randint(1, 6)
```

Neobvezni interval (Osebe, `najpogostejsa_imena`):
```python
def najpogostejsa_imena(osebe, spol, obdobje=None):
    for oseba in osebe:
        if oseba.spol != spol:
            continue
        if obdobje is not None and not (obdobje[0] <= oseba.letnica <= obdobje[1]):
            continue
        ...
```

---

## 10. Rekurzija

Vrnila se je v 25/26 i2 (`Razbitje`), in sicer v obeh oblikah: "ali sploh gre"
in "vrni **vse** rešitve". Ta dvojica je skoraj recept — nauči se je kot par. ✅

```python
# a) ali je razbitje mogoče -> True/False
def se_razbije(n, s):
    if n == '':                       # bazni primer: prazen niz je razbit
        return True
    for kos in se_zacne(n, s):        # vsi možni prvi kosi
        if se_razbije(n[len(kos):], s):
            return True               # dovolj je ena uspešna pot
    return False

# b) VSA razbitja -> množica naborov
def razbitja(n, s):
    if n == '':
        return {()}                   # ena rešitev: prazen nabor (NE set()!)
    vsa = set()
    for kos in se_zacne(n, s):
        for ostanek in razbitja(n[len(kos):], s):
            vsa.add((kos,) + ostanek)  # kos prilepi pred vsako rešitev ostanka
    return vsa
```

Ključna razlika med (a) in (b): bazni primer. Pri `True/False` je `True`,
pri zbiranju rešitev je `{()}` — množica z **enim praznim naborom**. Če vrneš
`set()`, dobiš vedno prazen rezultat.

### Ostali rekurzivni vzorci

```python
def uredi(seznam):
    if len(seznam) <= 1:              # bazni primer: 0 ali 1 element je urejen
        return seznam
    sredina = len(seznam) // 2
    return zlij(uredi(seznam[:sredina]), uredi(seznam[sredina:]))

def zlij(a, b):
    rezultat = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            rezultat.append(a[i]); i += 1
        else:
            rezultat.append(b[j]); j += 1
    return rezultat + a[i:] + b[j:]

# rekurzija po gnezdenih naborih (pogosti znaki)
def indeks(gnezdo, znak):
    if gnezdo[0] == znak:
        return (0,)
    if len(gnezdo) == 1:
        return None
    naprej = indeks(gnezdo[1], znak)
    return None if naprej is None else (1,) + naprej
```

---

# Del D — Kaj se na izpitih ponavlja

Iz analize 9 starih izpitov: 27 nalog, 81 podnalog (23/24 i1–i3, 24/25 i1–i3, 25/26 poskusni + i1 + i2).

> Rešitve vseh teh podnalog, z razlago in preverjene s Tomovimi testi, so v
> [`izpiti.md`](izpiti.md). Tam je tudi tabela vzorcev po nalogah; spodnja
> tabela §D2 jih razvršča po **pogostosti**, kar je uporabnejše pri
> načrtovanju učenja.

## D1. Zgradba je vsakič enaka

- **3 naloge po 3 podnaloge.**
- Podnaloge znotraj naloge so **stopnjevane in odvisne**: 1. je pomožna funkcija ali konstruktor,
  2. jo uporabi, 3. uporabi obe. Velja v **27/27 nalogah**.
- Tri stalne domene: **podatkovne strukture** (9/9 izpitov), **razred** (8/9), **datoteke** (8/9).
- **Vrstni red je zadnji dve leti fiksen:** naloga 1 = strukture/rekurzija, 2 = razred, 3 = datoteke.

## D2. Prijemi po pogostosti

| # | Prijem | Kje |
|---|---|---|
| 1 | **argmax / argmin** — element, ključ ali indeks z največ/najmanj nečesa (~9 podnalog) | §A4.4, §4b |
| 2 | **`None` pri neveljavnem ali praznem vhodu** (≥10 podnalog) | §A2 |
| 3 | **Razred** (8 nalog): `__str__`/`__repr__` v 6 od 8; v 25/26 namesto tega `__eq__`, metoda, ki vrne **nov objekt**, in objekt s **stanjem** | §A4.1, Tip 7, §C1 |
| 4 | **Štetje v slovar** `d[k] = d.get(k, 0) + 1` (5 podnalog) | §5b, §C3 |
| 5 | **Datoteka → struktura → natančno formatiran izpis** (8 podnalog) | §A4.2, Tip 8 |
| 6 | **Mreža s koordinatami** (4 naloge, vse v zadnjih dveh letih — trend navzgor) | §A4.6, Tip 6 |
| 7 | **Rekurzija** — po premoru se je vrnila v 25/26 i2, in sicer kot backtracking (vrni *vse* rešitve) | §A4.7, §2e |
| 8 | **`sorted(..., key=...)`**, pogosto dvojni ključ `key=lambda x: (-x[1], x[0])` | §4c |
| 9 | **Množice** kot rezultat ali za presek (6 podnalog) | §5d, §C8 |
| 10 | **Rezine fiksne dolžine** `niz[i:i+3]` (DNA, base64) | §3c |
| 11 | **`round(x, 2)`** na koncu — poceni izgubljene točke | §C9 |
| 12 | **Slovar s ključi-nabori** `{(od, do): n}` | §A4.3, §C2b |

Naloge se **nikoli ne ponovijo dobesedno**. Ponavljajo se ti prijemi, in teh je malo.

## D3. Kaj so na izpitih dejansko dali

| Izpit | 1. naloga | 2. naloga | 3. naloga |
|---|---|---|---|
| 23/24 i1 | Urejanje z zlivanjem (rekurzija) | Pesnik France (razred) | Avtobusni prevozi (datoteke) |
| 23/24 i2 | Izštevanke (seznami, krožnost) | Pesnik France (datoteke) | Baza 64 (nizi + slovarji) |
| 23/24 i3 | Pesnik France (nizi) | Pogosti znaki (slovarji + rekurzija) | Osebe (razred) |
| 24/25 i1 | Klepet (slovarji + množice) | Katan (razred + `random`) | Osmerosmerke (datoteke + mreža) |
| 24/25 i2 | Piknik (gnezdeni slovarji) | Dvigala (razred) | Ladjice (datoteke + mreža) |
| 24/25 i3 | Analiza DNA (nizi) | Telefonski imenik (razred) | Orientacijski tek (datoteke) |
| 25/26 posk. | Sprehodi (nizi) | GPS (datoteke) | Koda QR (razred + mreža) |
| 25/26 i1 | Značke (nizi + množice) | Štetje (razred `Stevec`) | Miran (datoteke + mreža) |
| 25/26 i2 | — | Vrhskala (razred s stanjem) | Razbitje (rekurzija), Air Triglav (datoteke) |

→ Za naslednji rok računaj: **ena naloga z razredom, ena z datotekami, ena s strukturami ali rekurzijo.**

## D4. Dve opozorili o testih

⚠️ **Zeleno ≠ pravilno.** Na 25/26 i2 je `se_zacne` primerjal samo prvi znak (`n[0] == a[0]`) in vseh
7 testov je slučajno prestal, ker se v njih noben napačen niz ni začel z isto črko. Prav je
`n.startswith(kos)`. Ker so podnaloge odvisne, taka „zelena" 1. podnaloga podre 2. in 3.

⚠️ **Primer v besedilu je lahko napačen, testi ne.** V nalogi Vrhskala besedilo trdi, da se
izvidnica `(1, 3, 'S', 18)` ustavi v `(0, 20)`; Tomo sprejme `(0, 21)`. Ob neujemanju veljajo testi.

## D5. Tvoje ponavljajoče se napake

Iz tvojih poskusov na `2526_poskusni`, `2526_i2` in `2324_i1`:

| Tema | Kaj se je zgodilo | Kaj velja |
|---|---|---|
| **Razredi** | metode napisane zunaj razreda (`__preisci__`), odvečni parametri, konstruktor z `return` | metode **v telesu** razreda, s `self`, z **imenom iz besedila**; konstruktor ne vrača ničesar |
| **Rekurzija** | `zlij` in `uredi` brez baznega primera → `RecursionError` | **najprej bazni primer**, šele nato korak |
| **Posploševanje** | imena mest zakodirana na trdo (Air Triglav) | zanka čez podatke iz datoteke, nikoli čez primer iz besedila |
| **Tipi** | niz namesto `float`, `()` namesto `set()`, element namesto seznama | preberi, kakšen tip naloga zahteva, in ga vrni točno takega |
| **Nizi** | `vrstica + '.'` brez prireditve, `"/n"` namesto `"\n"` | nizi so nespremenljivi → `vrstica += '.'` |

To so **sistemske** napake, ne naključne. Prvi dve sta te stali celo nalogo.

---

# Del E — Zadnja dva dneva

Vaje rešuj v Tomu (isto okolje kot na izpitu). Zapiski in Google da, UI ne — tudi pri vaji ne,
sicer meriš napačno stvar. Vsako napako sproti zapiši v svoj dnevnik napak.

⚠️ **Tvoje lokalne izpitne datoteke že vsebujejo rešitve.** Za vajo na prazno si
nalogo prenesi s [projekt-tomo.si](https://www.projekt-tomo.si/) ali pa v
urejevalniku pobriši telo funkcije, preden začneš. V rešitev v
[`izpiti.md`](izpiti.md) poglej **šele po poskusu** — sicer meriš prepoznavanje
namesto reševanja.

## E1. Dan 1 — gradniki (5 h)

| Čas | Kaj |
|---|---|
| 0:00–0:15 | Tomo odprt, priročnik odprt, dnevnik napak odprt |
| 0:15–1:30 | **Razredi.** `Stevec` (25/26 i1, naloga 2) **na prazno, brez gledanja**. Če pade, napiši še enkrat na prazno. Nato *Osebe* (23/24 i3, n. 3) in *Dvigala* (24/25 i2, n. 2) |
| 1:30–1:45 | odmor |
| 1:45–2:45 | **Datoteke.** *Potapljanje ladjic* (24/25 i2, n. 3): branje → mreža → izpis. Izpis primerjaj z besedilom znak za znakom |
| 2:45–3:30 | **Strukture in argmax.** *Prispevki za piknik* (24/25 i2, n. 1). Nato na roko napiši vse tri oblike argmaxa (§A4.4) |
| 3:30–3:45 | odmor |
| 3:45–4:40 | **Rekurzija.** *Urejanje z zlivanjem* (23/24 i1, n. 1) in *Razbitje* (25/26 i2, n. 3) — bazni primer je `{()}`, ne `set()` |
| 4:40–5:00 | dopolni dnevnik napak, naredi si kazalo na eno stran |

## E2. Dan 2 — simulacije (5 h)

| Čas | Kaj |
|---|---|
| 0:00–0:10 | preberi samo svoj dnevnik napak |
| 0:10–2:10 | **Simulacija 1: 25/26 i1** (Značke / Štetje / Miran). Isti letnik, nerešeno, pokrije vse tri stebre po vrsti. Časovnik, brez gledanja testov |
| 2:10–2:50 | pregled: za vsako rdečo **najprej ugani, zakaj**, šele nato poglej test. Vsako napako zapiši |
| 2:50–3:05 | odmor |
| 3:05–4:35 | **Simulacija 2: 24/25 i1** (Klepet / Katan / Osmerosmerke), 90 min — namenoma pod pritiskom. Doda `random`, privzete argumente in mrežo z 8 smermi |
| 4:35–5:00 | pregled, dopolni dnevnik napak, preberi §A6 in §A7 |

**Zvečer pred izpitom ne rešuj ničesar novega.** Spanje ti tu prinese več kot še ena naloga.

## E3. Jutro izpita

Preberi samo svoj dnevnik napak in §A6 (kontrolni seznam). Nič drugega.

## E4. Rezerva

Če kje ostane čas (ne na račun spanja): 24/25 i3 (DNA / imenik / tek), 23/24 i3, 23/24 i2,
25/26 poskusni.
