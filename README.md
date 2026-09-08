# UVP — Uvod v programiranje

Zapiski, rešeni izpiti in vaje za predmet **Uvod v programiranje** (Python).

## Vsebina repozitorija

| Datoteka | Kaj vsebuje |
|---|---|
| [`uvod_v_programiranje_zapiski.md`](uvod_v_programiranje_zapiski.md) | Zapiski celotne snovi — od osnovnih tipov do razredov, generatorjev, datotek in regularnih izrazov. Uporabi kot priročnik. |
| [`izpiti.md`](izpiti.md) | Vseh devet izpitnih rokov (2023/24, 2024/25, 2025/26), rešenih in razloženih: 27 nalog × 3 podnaloge. Vseh 81 rešitev je **preverjenih** z vgrajenimi testi Projekta Tomo. |
| [`vaje_in_naloge.md`](vaje_in_naloge.md) | Vaje po temah in vzorčne naloge za utrjevanje (rešitve pregledane, a brez uradnih testov). |
| [`izpiti/`](izpiti/) | Izvorne izpitne datoteke Projekta Tomo z vpisanimi rešitvami — 27 datotek `.py`, urejenih po rokih, skupaj s podatkovnimi datotekami, ki jih naloge berejo. |

Če se učiš za izpit, je smiseln vrstni red: **zapiski → vaje → izpiti**.

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

## Opombe

- **Datoteke v `izpiti/` ne morejo oddajati rešitev.** Iz njih sta odstranjena
  osebna žetona Projekta Tomo (žeton računa in žetoni posameznih podnalog), ker
  je repozitorij javen in bi ju lahko kdorkoli uporabil za oddajo v tvojem imenu.
  Na njihovem mestu sta oznaki `TVOJ_ZETON` in `ZETON_PODNALOGE`.
- **Kako vseeno oddati.** Datoteko si na novo prenesi s
  [projekt-tomo.si](https://www.projekt-tomo.si/) (takrat vsebuje tvoje žetone) in
  vanjo prepiši rešitve iz tega repozitorija. Rešitve so v datotekah med vrsticami
  z oznakami podnalog `# ====@številka=`.
- **Vse rešitve so preverjene lokalno**, z vgrajenimi testi iz teh istih datotek,
  a **še niso bile oddane** na Projekt Tomo.
- Prejšnje datoteke `vaje.md`, `izpitne_naloge_resene.md` in `Resene_naloge.md` so združene v [`vaje_in_naloge.md`](vaje_in_naloge.md) (brez podvojene naloge o gnezdenih oklepajih). Njihove izvirne različice ostajajo dosegljive v zgodovini repozitorija.
