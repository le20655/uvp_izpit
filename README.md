# UVP — Uvod v programiranje

Zapiski, rešeni izpiti in vaje za predmet **Uvod v programiranje** (Python).

## Vsebina repozitorija

| Datoteka | Odgovarja na vprašanje |
|---|---|
| [`izpitni_prirocnik.md`](izpitni_prirocnik.md) | **Kako se naloge lotim?** Postopek reševanja podnaloge v sedmih korakih, snov razvrščena po *tipih nalog*, kuharica s kodo za prepis, pregled kaj se na izpitih ponavlja in načrt za zadnja dva dneva. |
| [`uvod_v_programiranje_zapiski.md`](uvod_v_programiranje_zapiski.md) | **Kako deluje Python?** Zapiski celotne snovi — od osnovnih tipov do razredov, generatorjev, datotek in regularnih izrazov. |
| [`izpiti.md`](izpiti.md) | Vseh devet izpitnih rokov (2023/24, 2024/25, 2025/26), rešenih in razloženih: 27 nalog × 3 podnaloge. Vseh 81 rešitev je **preverjenih** z vgrajenimi testi Projekta Tomo. |
| [`vaje_in_naloge.md`](vaje_in_naloge.md) | Vaje po temah in vzorčne naloge za utrjevanje (rešitve pregledane, a brez uradnih testov). |
| [`preveri.py`](preveri.py) | Orodje, ki požene teste iz izpitne datoteke **brez oddaje** na strežnik. Poženeš ga nad svojimi datotekami Projekta Tomo, ki niso del tega repozitorija. |
| [`dnevnik_napak.md`](dnevnik_napak.md) | Predloga za sprotno beleženje lastnih napak — edina datoteka, ki jo pogledaš zjutraj pred izpitom. |

Če se učiš za izpit: **priročnik (Del A) → vaje → izpiti → priročnik (Del E)**.
Zapiski so referenca, v katero pogledaš, ko česa ne veš, ne pa branje od začetka
do konca.

### Preverjanje rešitve brez oddaje

```
python preveri.py "Stari izpiti/2526_i1/01_znacke.py"   # ena datoteka
python preveri.py "Stari izpiti/2526_i1"                # cel izpitni rok
python preveri.py "Stari izpiti"                        # vsi izpiti
```

Pot je pot do tvojih datotek Projekta Tomo na disku.

Skripta izpitno mapo skopira v začasno mapo, iz kopije odstrani del za
pošiljanje na strežnik in požene le teste. Izvirnih datotek se ne dotakne.

## Povezave za učenje Pythona

**Osnove**

- [W3Schools — Python](https://www.w3schools.com/python/default.asp) — kratke, praktične strani z zgledi; dobro za hitro preverjanje sintakse.
- [Matija Pretnar — Uvod v programiranje](https://matija.pretnar.info/uvod-v-programiranje/00-uvod.html) — gradivo predmeta, v slovenščini in po istem vrstnem redu kot predavanja.
- [Uradni Pythonov vodič](https://docs.python.org/3/tutorial/) — natančnejši od obeh zgornjih; vzemi ga, ko te zanima, *zakaj* nekaj deluje tako, kot deluje.
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — brezplačna knjiga, ki snov razlaga skozi uporabne programčke (datoteke, preglednice, splet).

**Za vajo**

- [Projekt Tomo](https://www.projekt-tomo.si/) — sistem, prek katerega oddajaš naloge; vsebuje tudi vaje iz prejšnjih let.
- [Exercism — Python](https://exercism.org/tracks/python) — naloge z avtomatskim preverjanjem in mentorskimi komentarji.

**Orodja, ki pridejo prav**

- [Python Tutor](https://pythontutor.com/) — izvajanje programa korak za korakom, z vidnimi spremenljivkami in klici. Neprecenljivo pri razumevanju rekurzije.
- [regex101](https://regex101.com/) — sestavljanje in razlaga regularnih izrazov (izberi različico *Python*).
- [Dokumentacija standardne knjižnice](https://docs.python.org/3/library/index.html) — kaj vse zna `str`, `list`, `dict`, `re`, `collections`.
