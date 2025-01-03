# Aufgabe: Wörterbuch erstellen und Abfragen

## Hauptaufgabe:

#1.Erstelle ein Python-Programm, in dem die Teilnehmer ein Dictionary erstellen. Das Dictionary soll mindestens 10 deutsche Wörter mit ihren englischen Übersetzungen enthalten.
#2.Danach soll das Programm den Benutzer per Eingabe (input) fragen, welches deutsche Wort ins Englische übersetzt werden soll.Falls das Wort nicht im Dictionary ist, soll eine entsprechende Fehlermeldung angezeigt werden.

woerterbuch = {
"haus": "house",
"baum": "tree",
"auto": "car",
"buch": "book",
"tisch": "table",
"stuhl": "chair",
"hund": "dog",
"katze": "cat",
"apfel": "apple",
"wasser": "water"
}

deutsches_wort = input("Bitte geben Sie ein deutsches Wort ein: ").lower() 

if deutsches_wort in woerterbuch:
    print(f"Die englische Übersetzung von '{deutsches_wort}' ist '{woerterbuch[deutsches_wort]}'.")
else:
    print(f"Fehler: Das Wort '{deutsches_wort}' ist nicht im Wörterbuch enthalten.")