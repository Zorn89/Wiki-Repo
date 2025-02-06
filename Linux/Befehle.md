## Was ist der absolute Pfad in Linux
Ein absoluter Pfad ist der vollständige Pfad zu einer Datei oder einem Verzeichnis, beginnend vom Wurzelverzeichnis (/). Es zeigt den exakten Speicherort auf dem Dateisystem an, unabhängig davon, in welchem Verzeichnis du dich gerade befindest.

## Was ist der relative Pfad in Linux
Ein relativer Pfad ist der Pfad zu einer Datei oder einem Verzeichnis im Verhältnis zum aktuellen Verzeichnis. Er gibt den Speicherort relativ zu deinem jetzigen Arbeitsverzeichnis an.

## Was macht der Befehl rm -rf / (!!!NICHT AUSFÜHREN!!!)
Der Befehl rm -rf / ist äußerst gefährlich. Hier eine Erklärung:
·rm: Der Befehl zum Löschen von Dateien.
·-r: Steht für rekursiv, was bedeutet, dass der Befehl auch Unterverzeichnisse und deren Inhalte löscht.
·-f: Steht für "force", was bedeutet, dass der Befehl ohne Bestätigung ausgeführt wird, auch wenn Dateien schreibgeschützt sind.
·/: Der Schrägstrich ist das Wurzelverzeichnis, was bedeutet, dass alles auf dem System gelöscht wird, wenn dieser Befehl ausgeführt wird.

***Achtung:*** Dieser Befehl löscht alles auf deinem System, was zu einem vollständigen Datenverlust und dem Ausfall des Systems führen würde. 

## Wo befindet sich das Benutzerverzeichnis in Linux
Das Benutzerverzeichnis befindet sich in der Regel im Verzeichnis /home. Jeder Benutzer hat dort ein eigenes Verzeichnis mit seinem Benutzernamen als Namen des Verzeichnisses.
Beispiel:
·Das Benutzerverzeichnis für einen Benutzer username befindet sich unter /home/username.


## Wie navigiere ich mich von egal wo in das Benutzerverzeichnis 
Das Benutzerverzeichnis schnell erreichen, indem man den absoluten Pfad verwendest. Zum Beispiel:

cd /home/username

Alternativ kannst der Befehl ~ (Tilde) verwenden, um schnell in ein eigenes Benutzerverzeichnis zu wechseln:
cd ~
Die Tilde (~) ist eine Abkürzung für das Benutzerverzeichnis des aktuell angemeldeten Benutzers.


