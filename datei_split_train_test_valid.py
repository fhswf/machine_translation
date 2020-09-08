"""
Dieses Skript öffnet eine Eingabedatei und teilt den Text in drei kleinere Dateien auf.
Das Verhältnis der länge der Dateien kann frei gewählt werden. (Beispiel: train = 70% test = 20% valid = 10%)
"""
from tqdm import tqdm # Wird importiert, um Fortschrittsbalken anzuzeigen.

def datei_oeffnen(name_eingabe_datei: str()):
    l1 = list()
    with open (name_eingabe_datei, "r") as eingabe_datei:
        for satz in eingabe_datei:
             l1.append(satz)
    return l1


def schreibe_in_ausgabedatei(name_ausgabe_datei: str(),satz: str()):
    with open(name_ausgabe_datei, "a") as ausgabe_datei:
        ausgabe_datei.write(satz)
    
liste_1 = datei_oeffnen("lange_sätze_en")
for nummer, satz in enumerate(tqdm(liste_1)):
    if nummer < round(len(liste_1) * 0.1):
        schreibe_in_ausgabedatei("valid.en",satz)
    if nummer <= round(len(liste_1) * 0.2) and nummer >= round(len(liste_1) * 0.1):
        schreibe_in_ausgabedatei("test.en", satz)
    if nummer > (len(liste_1) * 0.2):
        schreibe_in_ausgabedatei("train.en",satz)

