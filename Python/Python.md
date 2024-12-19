# Python

## Was ist Python?
Python ist eine Programmiersprache 

## Installation
- Powershell öffnen
- Ubunto auswählen
- Prüfen ob Python installiert ist bzw. welche Version vorhanden ist. 
 Befehl: python 3 --version

 Wir können die Befehle von Python auch über Vision Studio Pro eingeben.
 Hierzu:
 - Readme- Datei erstellen
 - script.py erstellen
 - Toggle Panel öffnen
 - "Auswahl" neben dem Plus auf WSL
 - Befehl: sudo apt install python3 python3-pip Python installieren

 ## Python Benutzeroberfläche öffnen
 - Befehl python3 script.py 
 - <<< an den Krokodil-Klammern erkennt man, dass man auf der P-Oberfläche ist.
 - mit exit () verlässt man diese wieder



 ## Python-Datentypen
 Folgende Datentypen gibt es: 
 - Numbers - Int, Float, Complex
 - Bool - True, False
 - Sequence - String, List, Tuple
 - Mapping - Dict
 - Sets - Set, Frozenset 
 

## print f

 ### Beispiel für Abfrage Namen und Anzeige des Namens

 person1 = input("Wie ist dein Vorname?")
person2 = input("Wie ist dein Nachnahme?")

print(f"Dein Name ist: {person1} {person2}") 


### Beipiel für Zahleneingabe und Addition (bzw Rechenoperation) 

zahl1 = input("Nenne bitte eine Zahl?")
zahl2 = input("Nenne bitte eine weitere Zahl?")

zahl1_int = int(zahl1)
zahl2_int = int(zahl2)
print(f"Die Summe ergibt: {zahl1_int + zahl2_int}")



## Bsp für Zahlen positiv bzw negativ. IF Aufgabe

zahl = float(input("Gib eine Zahl ein:"))

if zahl > 0:
    print("Die Zahl ist positiv")

elif zahl == 0:
    print("Die Zahl ist null")

else : 
    print("Die Zahl ist negativ")

istgerade = (zahl == 2 and zahl != -1) or (zahl % 2 == 0)

if istgerade: 
    print("Die Zahl ist gerade.")

else: 
    print("Die Zahl ist ungerade.")


## Schnellsuche für das kleine Hirn

^ = and
v = oder -> Voder

    - if = Bedingung
    - elif = Folgebedingung 
    - else = Endebedingung

float = Zahl

Print = Ausgabe im Terminal 
Pring f = fast mehrere Bedingungen zusammen

cd = Ordner öffnen
cd .. = zurück 
 
Input = Eingabe durch User

Import = Import von Paketen

Bsp. Ordnerfolge: datetime.datetime.now
    - datetime.datetime -> Hauptordner
    - datetime -> Unterordner 
    - now -> Datei 

