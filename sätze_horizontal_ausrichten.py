"""
Diese Skript wandelt die im Corpus vertikal geschriebenen Sätze in horizontale Sätze um, entfernt alle <tags> und schreibt den so
generieten Text in eine Ausgabedatei.
"""
liste = list()
l1 = list()

n = 0
iterator = iter(l1)


def datei_oeffnen():
    with open("DEU.vert", "r") as f:
        for outerToken in f:
            #l1.append(outerToken.split()[0])
            yield outerToken.split()[0]
    

"""
Der Inhalt, der sich zwischen einem <p> und einem </p> Tag befindet wird an den aufrufenden zurück gegeben.
"""
def custom_for_loop(iterable):   
    l2 = list()
    satz_nr = 0
    for token in iterable():
        if token == "<p>":
            l2 = list()
            satz_nr += 1
        elif token == "</p>":
            l2.append("\n")
            yield l2
        else:
            l2.append(token)
            
"""
Diese Funktion entfernt alle anderen sich im Text befindelichen Tags. Und wandelt den Inhalt der Liste in einen String um.
"""
def entferne_tags(iterable: list):
    text = ""
    for i, token in enumerate(iterable):
        if token == "<g/>" or token == "<s>" or token == "</s>":
            continue
        text += str(token)
        if i < len(iterable) - 1 and iterable[i + 1] != "<g/>":
            text += " "
    return text

"""
Der übergebene Text wird in eine Ausgabedatei geschrieben.
"""
def schreibe_in_datei(text : str, satz_nr: int):
    with open("edd", "a") as f:
        f.write(f"{satz_nr}\t{text}")

print("Start:")
l1 = datei_oeffnen
print("Fertig mit Starten")

for satz_nr, satz in enumerate(custom_for_loop(l1)):
    satz = entferne_tags(satz)
    schreibe_in_datei(satz, satz_nr)
print("Fertig")
