"""
Das Skript filtert alle gültigen Alignements aus der eingabedatei und schreibt diese in eine Ausgabedatei.
"""
liste_1 = list()
liste_2 = list()

"""
Diese Funktion öffnet die Eingabedatei und filtert alle Einträge raus, in denen eine -1 vorkommt.
-1 bedeutet, dass für diesen Satz in der anderen Sprache kein "Partnersatz" gibt.
Alle anderen Alignments werden in eine Liste geschrieben, welche an den Aufruf zurück gegeben wird.
"""
def datei_oeffnen():
    tmp_liste = list()
    with open("DEU_ENG.align", "r") as f:
        for paarung in f:
            deu = paarung.split()[0]
            eng = paarung.split()[1]
            if not deu.__contains__("-1") and not eng.__contains__("-1"):
                tmp_liste.append((deu,eng))
    return tmp_liste

"""
Die Funktion iteriert über die übergebene Liste und prüft jedes Alingmentpaar darauf, ob es ein Mehr- Zwei- oder Einzeiler ist.
DAnn wird dem Alignmenpaar die entsprechende Methode aufgerufen.
So müssen beide Teile des Päärchens das selbe Sonderzeichen beinhalten. bzw. beide keins.
"""
def pruefe_sonderzeichen(bereinigte_liste:list()):
    finale_liste = list()
    for deu,eng in bereinigte_liste:
        if deu.__contains__(":") and eng.__contains__(":"):
            if pruefe_doppelpunkte(deu, eng):
                finale_liste.append((deu, eng))
        if deu.__contains__(",") and eng.__contains__(","):
            if pruefe_groeßer_grenzwert(int(deu.split(",")[0])):
                finale_liste.append((deu, eng))
        if not deu.__contains__(":") and not deu.__contains__(",") and not eng.__contains__(":") and not eng.__contains__(","):
            if pruefe_groeßer_grenzwert(int(deu)):
                finale_liste.append((deu,eng))
        else:
            continue
    return finale_liste

"""
Die Funktion überprüft, ob das Alignmentpaar für beide Sprachen gleich viele Sätze beinhaltet.
Wenn nein, dann wird ein False zurück an den Aufruf gegeben.
"""
def pruefe_doppelpunkte(deu: str(), eng: str()):
    deu_1 = int(deu.split(":")[0])
    deu_2 = int(deu.split(":")[1])
    eng_1 = int(eng.split(":")[0])
    eng_2 = int(eng.split(":")[1])
    if pruefe_groeßer_grenzwert(deu_1):
        return deu_1 - deu_2 == eng_1 - eng_2
    else:
        return False


def pruefe_groeßer_grenzwert(zahl: int()):
    grenzwert = 10000000
    return zahl > grenzwert


"""
Die übergebne LIste mit gültigen Alignments wird in eine Ausgabedatei geschrieben.
"""
def schreibe_in_datei(finale_liste: list()):
    with open ("finale_paarungen", "a") as out_file:
        for token in finale_liste: 
            deu = token[0]
            eng = token[1]
            out_file.write(deu +"\t" + eng + "\n")
            
            
liste_1 = datei_oeffnen()
#print(liste_1)
list_2 = pruefe_sonderzeichen(liste_1)
schreibe_in_datei(list_2)
