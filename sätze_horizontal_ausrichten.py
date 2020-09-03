liste = list()
l1 = list()

n = 0
iterator = iter(l1)


def datei_oeffnen():
    with open("DEU.vert", "r") as f:
        for outerToken in f:
            #l1.append(outerToken.split()[0])
            yield outerToken.split()[0]
    


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
            

def entferne_tags(iterable: list):
    text = ""
    for i, token in enumerate(iterable):
        if token == "<g/>" or token == "<s>" or token == "</s>":
            continue
        text += str(token)
        if i < len(iterable) - 1 and iterable[i + 1] != "<g/>":
            text += " "
    return text


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
