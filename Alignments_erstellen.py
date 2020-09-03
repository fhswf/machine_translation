liste_1 = list()
liste_2 = list()


def datei_oeffnen():
    tmp_liste = list()
    with open("DEU_ENG.align", "r") as f:
        for paarung in f:
            deu = paarung.split()[0]
            eng = paarung.split()[1]
            if not deu.__contains__("-1") and not eng.__contains__("-1"):
                tmp_liste.append((deu,eng))
    return tmp_liste


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
