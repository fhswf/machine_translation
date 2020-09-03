liste_deutsche_alignments = list()
liste_englische_alignments = list()
liste_zum_schreiben = list()


def datei_oeffnen():
    deu_liste = list()
    eng_liste = list()
    with open("finale_paarungen", "r") as f:
        for paarung in f:
            deu_liste.append(paarung.split()[0])
            eng_liste.append(paarung.split()[1])         
    return deu_liste,eng_liste


def verteiler_funktion(liste_mit_alignments:list(), input_datei:str()):
    satzliste = list()
    satzteilliste = list()
    print(input_datei)
    with open(input_datei, "r") as input:
        for x in input:
            satzteilliste.append((x.split("\t")[1]))
    for token in liste_mit_alignments:
        if token.__contains__(":"):
            satzliste.append(hole_sätze_doppelpunkt(token, satzteilliste))
        
        if  token.__contains__(","):
            satzliste.append(hole_sätze_komma(token, satzteilliste))

        if not token.__contains__(":") and not token.__contains__(","):
            satzliste.append(hole_einzeiler(token,satzteilliste))
        continue
    return satzliste


def hole_sätze_doppelpunkt(token: str(), satzteilliste:list()):
    startzeile = int(token.split(":")[0])
    endzeile = int(token.split(":")[1])
    fertiger_text = ""
    while startzeile <=  endzeile:
        fertiger_text +=satzteilliste[startzeile]
        startzeile += 1
    return  fertiger_text 


def hole_sätze_komma(token:str(), satzteilliste:list()):
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


def schreibe_in_datei(output_datei:str(), liste_zum_schreiben:list()):
    with open(output_datei, "w") as output_datei:
        for satz in liste_zum_schreiben:
            output_datei.write(satz)
        

liste_deutsche_alignments,liste_englische_alignments = datei_oeffnen()
#print(f"Deutsche liste: {liste_deutsche_alignments} \nenglische LIste: {liste_englische_alignments}")
liste_zum_schreiben = verteiler_funktion(liste_deutsche_alignments,"deutsch_vorbereitet")
schreibe_in_datei("alignte_sätze_deu",liste_zum_schreiben)
