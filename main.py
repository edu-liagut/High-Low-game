"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal.
Highscore sparas i JSON-format.
"""

import random
import json

# === FILHANTERING ===

def ladda_highscore(filnamn="highscore.json"):
    try:
        fil = open(filnamn, "r", encoding="utf-8")
        data= json.load(fil)
        fil.close()
        return data
    except FileNotFoundError:
        return[]
    """
    Laddar highscore-listan från en JSON-fil.

    Parametrar:
        filnamn (str): Namnet på filen att läsa från

    Returnerar:
        list: En lista med dictionaries, varje dictionary har nycklarna "namn" och "gissningar"
              Returnerar tom lista om filen inte finns.
    """
    # TODO: Implementera funktionen
    # Tips: Använd try/except för FileNotFoundError
    # Tips: json.load() för att läsa
    pass


def spara_highscore(highscore_lista, filnamn="highscore.json"):
    fil = open(filnamn, "w", encoding="utf-8")
    json.dump(highscore_lista, fil, indent=4, ensure_ascii=False)
    fil.close()
    """
    Sparar highscore-listan till en JSON-fil.

    Parametrar:
        highscore_lista (list): Listan som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    # TODO: Implementera funktionen
    # Tips: Använd json.dump() med indent=4 och ensure_ascii=False
    pass


# === SPELMECKANIK ===

def spela_omgang():
    hemligt_tal = random.randint(1,100)
    antal_gissningar = 0
    while True:
        gissa = int(input("Gissa ett nummer->"))
        antal_gissningar += 1
        if gissa > hemligt_tal:
            print(f"{gissa} är för högt, försök igen!")
        elif gissa < hemligt_tal:
            print(f"{gissa} är för lågt, försök igen!")
        else:
            print(f"Right on the money!, du gissade totalt {antal_gissningar} gånger!")
            return antal_gissningar
spela_omgang()
"""
    Spelar en omgång av Högt/lågt.

    Returnerar:
        int: Antalet gissningar som behövdes för att gissa rätt
    """
    # TODO: Implementera funktionen
    # 1. Välj ett slumpmässigt tal mellan 1 och 100 med random.randint()
    # 2. Skapa en variabel för antal gissningar (börja på 0)
    # 3. Skapa en while-loop som fortsätter tills spelaren gissar rätt
    # 4. Inuti loopen: fråga efter gissning, öka räknaren, ge feedback (högt/lågt/rätt)
    # 5. När spelaren gissar rätt: returnera antalet gissningar
pass


# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):
    if not highscore_lista:
        print("Inget highscore sparat ännu")
        return
    sorterad = sorted(highscore_lista, key=lambda x: x["gissningar"])
    print("\n===HIGHSCORE===")
    for index,spelare in enumerate(sorterad, start=1):
        """
    Visar highscore-listan sorterad med bästa spelaren först.

    Parametrar:
        highscore_lista (list): Listan som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Kontrollera om listan är tom först
    # Tips: Sortera med sorted() och key=lambda x: x["gissningar"]
    # Tips: Använd enumerate() för att numrera spelarna från 1
    pass


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda highscore med ladda_highscore()
    # 2. Skapa en while-loop som visar menyn
    # 3. Menyn ska ha alternativen:
    #    1. Spela ny omgång
    #    2. Visa highscore
    #    3. Avsluta
    # 4. Vid val 1:
    #    - Anropa spela_omgang() för att få antalet gissningar
    #    - Fråga efter spelarens namn
    #    - Skapa en dictionary {"namn": namn, "gissningar": antal}
    #    - Lägg till i highscore-listan
    #    - Spara med spara_highscore()
    # 5. Vid val 2: anropa visa_highscore()
    # 6. Vid val 3: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()