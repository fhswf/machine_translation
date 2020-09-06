"""
Dieses Skript überprüft alle Alignments in der Inputdatei darauf, ob sie gültig sind oder nicht. Wenn sie gültig sind, werden sie in eine
neue Datei geschrieben. Sind sie nicht gültig so werden sie ignoriert.

1. Datei mit den Alignment wird geöffnet und der Inhalt in zwei Listen aufgeteilt.
2. Mit jeder dieser Listen wird die verteiler_funktion aufgerufen. Sie dient dazu die verschiedenen Fälle, die auftreten können zu verwalten und entsprechende Funktionen
    aufzurufen.
3. Die aus Schritt 2 resultierende Liste mit Sätzen wird in eine Outputdatei geschrieben.
"""
liste_deutsche_alignments = list()
liste_englische_alignments = list()
liste_zum_schreiben = list()

"""
Die Paarungen werden geöffnet und am Leerzeichen aufgeteilt.
Die aufgeteilten Paarungen werden in zwei Listen geschrieben.
Diese werden an den Aufrufer zurück gegeben.
"""
def datei_oeffnen():
    deu_liste = list()
    eng_liste = list()
    with open("finale_paarungen", "r") as f:
        for paarung in f:
            deu_liste.append(paarung.split()[0])
            eng_liste.append(paarung.split()[1])         
    return deu_liste , eng_liste

"""
Diese Funktion bekommt eine LIste mit alignments und eine input-datei übergeben.
In der Input-Datei stehen Sätze, welche geordnet werden sollen.
1. Die inputdatei wird geöffnet.
2. Der Inhalt dieser Datei wird in eine liste geschrieben.
3. Es wird über die Liste mit den Alignements iteriert. Wenn es zweizeier (","), ein Einzeiler ("")oder mehrzeiler (":") sind werden spezielle Funktionen aufgerufen.
4. Die so erstelle Liste mit sortieren Sätzen wird zurück an den Aufrufer geben.
"""
def verteiler_funktion(liste_mit_alignments:list(), input_datei:str()):
    satzliste = list()
    satzteilliste = list()
    print(input_datei)
    with open(input_datei, "r") as input:
        for x in input:
            satzteilliste.append((x.split("\t")[1]))
    for token in liste_mit_alignments:
        if token.__contains__(":"):
            satzliste.append(hole_saetze_doppelpunkt(token, satzteilliste))
        
        if  token.__contains__(","):
            satzliste.append(hole_saetze_komma(token, satzteilliste))

        if not token.__contains__(":") and not token.__contains__(","):
            satzliste.append(hole_einzeiler(token,satzteilliste))
        continue
    return satzliste

"""
Diese Funktion teilt das übergebene Alignment am : auf.
Solange die startzeile kleiner ist als die Endzeile, wird der fertige_text um den nächsten Satz aus der übergebenen Liste erweitet.
Dieser wird dann zurück an die verteiler_funktion gegeben.
"""
def hole_saetze_doppelpunkt(token: str(), satzteilliste:list()):
    startzeile = int(token.split(":")[0])
    endzeile = int(token.split(":")[1])
    fertiger_text = ""
    while startzeile <=  endzeile:
        fertiger_text +=satzteilliste[startzeile]
        startzeile += 1
    return  fertiger_text 

"""
Die Funktion teilt das übergebne Alignement am , auf.
Dann wird der finale Text um die beiden Sätze, die sich an den indexen an Liste befinden erweitert und am Ende zurück an 
die verteiler_funktion gegeben.
"""
def hole_saetze_komma(token:str(), satzteilliste:list()):
    finaler_text = ""
    erster_satz = int(token.split(",")[0])
    letzter_satz = int(token.split(",")[1])      
    finaler_text += satzteilliste[erster_satz]
    finaler_text += satzteilliste[letzter_satz]

    return finaler_text


def hole_einzeiler(token:str(), satzteilliste:list()):
    finaler_text = ""
    satz = token.split("\t")[0]
    finaler_text += satzteilliste[int(satz)]
    return finaler_text

"""
Die Liste mit den fertig sortierten Sätzen wird in die übergebene Output-datei geschrieben.
"""
def schreibe_in_datei(output_datei:str(), liste_zum_schreiben:list()):
    with open(output_datei, "w") as output_datei:
        for satz in liste_zum_schreiben:
            output_datei.write(satz)
        

liste_deutsche_alignments,liste_englische_alignments = datei_oeffnen()
#print(f"Deutsche liste: {liste_deutsche_alignments} \nenglische LIste: {liste_englische_alignments}")
liste_zum_schreiben = verteiler_funktion(liste_deutsche_alignments,"deutsch_vorbereitet")
schreibe_in_datei("aligned_sentences_deu",liste_zum_schreiben)
