# -*- coding: utf-8 -*-
"""Lokalno preveri rešitve v datoteki Projekta Tomo — BREZ oddaje na strežnik.

Izpitna datoteka ob zagonu rešitve odda na strežnik in šele nato izpiše, katere
podnaloge so veljavne. Ta skripta naredi isto preverjanje, a brez oddaje:
izpitno mapo skopira v začasno mapo, iz kopije odstrani del za pošiljanje in
požene le teste. Izvirnih datotek se ne dotakne.

Uporaba:

    python preveri.py "Stari izpiti/2526_i1/01_znacke.py"   # ena datoteka
    python preveri.py "Stari izpiti/2526_i1"                # cela mapa
    python preveri.py "Stari izpiti"                        # vsi izpiti

Deluje samo za datoteke, ki imajo na dnu vgrajene Tomove teste.
"""
import os
import shutil
import subprocess
import sys
import tempfile

# Vrstica, s katero se v Tomovi datoteki začne pošiljanje na strežnik,
# in vrstica, s katero se nadaljuje izpis rezultatov.
ZACETEK_ODDAJE = '    print("Shranjujem rešitve na strežnik... ", end="")'
POVZETEK = "    Check.summarize()"


def brez_oddaje(izvorna_koda):
    """Iz vsebine datoteke odstrani del, ki rešitve pošlje na strežnik."""
    if ZACETEK_ODDAJE not in izvorna_koda or POVZETEK not in izvorna_koda:
        return None
    zacetek = izvorna_koda.index(ZACETEK_ODDAJE)
    konec = izvorna_koda.index(POVZETEK)
    return izvorna_koda[:zacetek] + izvorna_koda[konec:]


def preveri_datoteko(pot):
    """Požene teste ene izpitne datoteke in izpiše rezultat."""
    pot = os.path.abspath(pot)
    mapa = os.path.dirname(pot)
    ime = os.path.basename(pot)

    with open(pot, encoding="utf-8") as f:
        koda = f.read()

    okrnjena = brez_oddaje(koda)
    if okrnjena is None:
        print("{}: preskočeno (datoteka nima vgrajenih testov)".format(ime))
        return

    # Celo mapo skopiramo, ker naloge pogosto berejo podatkovne datoteke
    # iz iste mape (npr. potovanja_mala.csv, podatki.txt).
    with tempfile.TemporaryDirectory() as zacasna:
        delovna = os.path.join(zacasna, "izpit")
        shutil.copytree(mapa, delovna)

        with open(os.path.join(delovna, ime), "w", encoding="utf-8") as f:
            f.write(okrnjena)

        # PYTHONIOENCODING poskrbi, da šumniki v izpisu preživijo na Windowsu
        okolje = dict(os.environ, PYTHONIOENCODING="utf-8")
        rezultat = subprocess.run(
            [sys.executable, ime],
            cwd=delovna,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
            env=okolje,
        )

    print("=" * 60)
    print(ime)
    print("=" * 60)
    print(rezultat.stdout.strip())
    if rezultat.stderr.strip():
        print("--- napake med izvajanjem ---")
        print(rezultat.stderr.strip())
    print()


def poti_za_preverjanje(cilj):
    """Vrne seznam .py datotek: bodisi eno samo bodisi vse v (pod)mapah."""
    if os.path.isfile(cilj):
        return [cilj]

    najdene = []
    for koren, mape, datoteke in os.walk(cilj):
        for ime in sorted(datoteke):
            if ime.endswith(".py") and ime != os.path.basename(__file__):
                najdene.append(os.path.join(koren, ime))
    return najdene


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    cilj = sys.argv[1]
    if not os.path.exists(cilj):
        print("Ne najdem:", cilj)
        sys.exit(1)

    poti = poti_za_preverjanje(cilj)
    if not poti:
        print("V", cilj, "ni datotek .py")
        sys.exit(1)

    for pot in poti:
        preveri_datoteko(pot)


if __name__ == "__main__":
    main()
