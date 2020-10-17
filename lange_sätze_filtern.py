"""
Dieses Skript filtert Sätze aus einem Textcorpus heraus, die länger als 6 Wörter sind.
Diese Sätze werden in eine Ausgabedatei geschrieben.
Dies ist notwendig, um z.B Artikelüberschriften die nur aus "Artikel 37" bestehen, oder Tabellen die in Schrift umgewandelt wurden zu entfernen.

1. Die Dateien, aus denen zu kurze Sätze gefiltert werden sollen werden geöffnet.
2. Mit einer der beiden daraus entstehenden Liste wird die pruefe_laenge-Funktion aufgerufen. (In diesem Fall mit den deutschen Sätzen.)
3. Die daraus enstandene Liste mit den Indexen der zu kuren Sätze zusammen mit der anderen aus Schritt 1 entstanden Liste (englische Sätze) werden
    in filter_zu_kurze_saete gegeben. Dort werden aus der Englischen Liste nur Sätze genommen, die nicht in der Liste mit den Indexen der zu kruzen Sätze vorkommen.
4. Die Listen mit den langen Sätzen werden in die entsprechenden Output-Dateien geschrieben.
"""

from tqdm import tqdm # Wird importiert, um Fortschrittsbalken anzuzeigen.


"""
Die übergebene Datei wird geöffnet und ihr Inhalt in eine Liste geschrieben.
"""
def datei_oeffnen(input_datei: str()):
    liste_mit_saetzen = list()
    with open(input_datei, "r") as input_datei:
        for satz in input_datei:
            liste_mit_saetzen.append(satz)
    return liste_mit_saetzen

"""
Für alle Sätze in der liste_mit_saetzen wird überprüft, ob sie mindestens so lang sind, wie in satzlaenge_woerter angegeben.
Wenn nein, wird ihr Index in eine neue liste gespeichert. Wenn ja, werden sie in eine entsprechende liste gespeichert.
Der Fortschrit wird mit hilfe des tqdm-moduls als Ladebalken angezeigt.
Am Ende werden beide Listen, die mit den Indexen der zu kuren Sätze und die Liste mit langen Sätzen zurück an den Aufrufer gegeben.
"""
def pruefe_laenge(liste_mit_saetzen: list(), satzlaenge_woerter: int()):
    liste_mit_indexen_von_kurzen_saetzen = list()
    liste_mit_langen_saetzen = list()
    for index, satz in enumerate(tqdm(liste_mit_saetzen)):
        if satz.count(" ") < satzlaenge_woerter -1 :
            liste_mit_indexen_von_kurzen_saetzen.append(index)
        else:
           liste_mit_langen_saetzen.append(satz)
    return liste_mit_indexen_von_kurzen_saetzen, liste_mit_langen_saetzen
    

"""
Die Funktion bekommt zwei Listen übergeben, in der liste_mit_saetzen stehen alle Sätze, die aus der zweiten Textdatei geladen wurden. In der liste_mit_indexen
stehen die Indexe der Sätze, die in der ersten Liste zu kurz waren.
Die indexe werden danach in sein Set umgewandelt, damit die Zugriffszeit konstant bleibt.
Danach wird mit einer Listecomprehension eine Liste erzeugt, in der nur Sätze stehen, deren in Index nicht in dem set _indexe stehen.(Das ist die Liste aus pruefe_laenge)
Am Ende wird die Liste mit den langen sätzen zurück an den Aufrufer gegeben.
"""
def filter_zur_kurze_saetze(liste_mit_saetzen: list(), liste_mit_indexen: list()):
    _indexe = set(liste_mit_indexen)
    lange_saetze = [satz for index, satz in enumerate(tqdm(liste_mit_saetzen)) if index not in _indexe]
    return lange_saetze

"""
Der Inhalt der liste_mit_sätzen wir in die output_datei geschrieben.
"""
def schreibe_lange_saetze_in_datei(liste_mit_saetzen: str(), output_datei: str()):
    with open(output_datei, "w") as output_datei:
        for satz in liste_mit_saetzen:
            output_datei.write(satz)


liste_de= list()
liste_en = list()
liste_mit_langen_saetzen = list()
liste_mit_indexen_von_kurzen_saetzen = list()
liste_de = datei_oeffnen("Beispiel")
liste_en = datei_oeffnen("aligned_sentences_en")
liste_mit_indexen_von_kurzen_saetzen, liste_mit_langen_saetzen = pruefe_laenge(liste_de, 11)

# Hier werden die langen Sätze aus der 1. Datei in eine outputdatei geschrieben.
schreibe_lange_saetze_in_datei(liste_mit_langen_saetzen,"Beispiel")


liste_mit_langen_saetzen = filter_zur_kurze_saetze(liste_en, liste_mit_indexen_von_kurzen_saetzen)

schreibe_lange_saetze_in_datei(liste_mit_langen_saetzen, "lange_sätze_en")




