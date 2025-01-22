# Aufgabenstellung für die Teilnehmer:

## 1. Beschreibe die Funktion der POST- und GET-Routen:
***- Was macht der Code bei einer Anfrage an /products mit POST?***
- Diese Route wird verwendet, um ein neues Produkt hinzuzufügen.
- Bei einer POST-Anfrage erwartet die API eine JSON-Nachricht, die mindestens die Felder "name" (Name des Produkts) und "price" (Preis des Produkts) enthält.
- Wenn die Anfrage diese Felder nicht enthält oder die JSON-Daten ungültig sind, wird eine Fehlermeldung mit Statuscode 400 zurückgegeben.
- Wenn die Eingabedaten korrekt sind, wird dem neuen Produkt eine ID zugewiesen. Die ID wird durch die maximale ID in der bestehenden Produktliste + 1 bestimmt, um sicherzustellen, dass jedes Produkt eine eindeutige ID hat.
- Das Produkt wird dann zur Liste der Produkte hinzugefügt, und das neu erstellte Produkt wird mit Statuscode 201 zurückgegeben.

***- Wie wird ein Produkt bei einer GET-Anfrage gefilter*** 
- Diese Route wird verwendet, um alle Produkte abzurufen.
Standardmäßig gibt die API alle Produkte in der Liste zurück (Statuscode 200).
- Es gibt jedoch einen optionalen Query-Parameter name. Wenn dieser Parameter vorhanden ist, wird die Liste gefiltert, sodass nur Produkte zurückgegeben werden, deren Name den angegebenen Suchbegriff (case-insensitive) enthält.


## 2. Führe die Anfragen in Postman aus:
- Teste die Erstellung eines Produkts mit POST /products.
- Rufe die Liste der Produkte mit GET /products ab.
- Nutze den Query-Parameter name in der GET-Anfrage.