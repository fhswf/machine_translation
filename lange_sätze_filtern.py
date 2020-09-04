"""
1. Datei öffnen
    benötige: Dateinamen, eine Liste
    1.1 Alle Sätze in der Datei in eine Liste schreiben.

2. Duch diese Liste iterieren
    benötige: Liste mit Sätzen, Liste in die ich die gelöschten Nummern schreiben kann.
    2.1 Dabei überprüfen, ob der Satz min. 5 Leerzeichen enthält.
    Wenn nein:
        Stelle in der Liste in zweite Liste schreiben
        Eintrag löschen
    Wenn ja:
        continue
    2.2 Neue Sätze in Datei speichern.

3. Für das Gegenstück:
    1. ausführen
    2. Lösche alle Einträge in der Liste, die mit einträgen aus der in 2. erstellten Liste korrelieren.
"""

from tqdm import tqdm

def datei_oeffnen(input_datei: str()):
    liste_mit_sätzen = list()
    with open(input_datei, "r") as input_datei:
        for satz in input_datei:
            liste_mit_sätzen.append(satz)
    return liste_mit_sätzen


def pruefe_laenge(liste_mit_sätzen: list()):
    liste_mit_indexen_von_kurzen_sätzen = list()
    liste_mit_langen_sätzen = list()
    for index, satz in enumerate(tqdm(liste_mit_sätzen)):
        if satz.count(" ") < 5:
            liste_mit_indexen_von_kurzen_sätzen.append(index)
        else:
           liste_mit_langen_sätzen.append(satz)
    return liste_mit_indexen_von_kurzen_sätzen, liste_mit_langen_sätzen
    


def filter_zur_kurze_saetze(liste_mit_sätzen: list(), liste_mit_indexen: list()):
    _indexe = set(liste_mit_indexen)
    lange_saetze = [satz for index, satz in enumerate(tqdm(liste_mit_sätzen)) if index not in _indexe]
    return lange_saetze

def schreibe_lange_sätze_in_datei(liste_mit_sätzen: str(), output_datei: str()):
    with open(output_datei, "w") as output_datei:
        for satz in liste_mit_sätzen:
            output_datei.write(satz)


liste_de= list()
liste_en = list()
liste_mit_langen_sätzen = list()
liste_mit_indexen_von_kurzen_sätzen = list()
liste_de = datei_oeffnen("aligned_sentences_deu")
liste_en = datei_oeffnen("aligned_sentences_en")
print("Sätze auf länge prüfen")
liste_mit_indexen_von_kurzen_sätzen, liste_mit_langen_sätzen = pruefe_laenge(liste_de)

# Hier werden die langen Sätze aus der 1. Datei in eine outputdatei geschrieben.
print("in datei schreiben.")
schreibe_lange_sätze_in_datei(liste_mit_langen_sätzen,"lange_sätze_deu")

print("aus der partner-datei löschen")
liste_mit_langen_sätzen = filter_zur_kurze_saetze(liste_en, liste_mit_indexen_von_kurzen_sätzen)

schreibe_lange_sätze_in_datei(liste_mit_langen_sätzen, "lange_sätze_en")
print("Fertig")



