# Aufgaben vom 13.01.2025 als Bsp.: 

Aufgabe: Beantworte folgende Fragestellungen in eigenen Worten. Falls du die Antwort
nicht aus dem Kopf weißt, verwende die Folien von heute und Freitag, oder recherchiere
im Internet (nicht chatGPT die Antwort “ausspucken” lassen! Falls ihr A.I. benutzen
möchtet, lasst euch von ihr das Thema erklären und verfasst eure Antwort trotzdem in
eigenen Worten.)

-  1.1: Welche Protokolle sind bei einem “ping” Befehl involviert? Welche Aufgaben erfüllen sie dabei? Beschreibe den Prozess.
- 1.2: Was ist die Aufgabe eines Modems?
- 1.3: “Das Internet ist ein Netzwerk von Netzwerken” - Was ist mit dieser Aussage
gemeint?
- 1.4: Was ist der Unterschied zwischen einer MAC-Adresse und einer IP-Adresse?

## Welche Protokolle sind bei einem “ping” Befehl involviert? Welche Aufgaben erfüllen sie dabei? Beschreibe den Prozess. 

***ICMP (Internet Control Message Protocol):***

Aufgabe: ICMP ist das primäre Protokoll, das beim Ping-Befehl verwendet wird. Es dient dazu, Netzwerkgeräte über den Status ihrer Kommunikation zu informieren und Fehler zu melden.
Der Ping-Befehl sendet eine ICMP-Echoanforderung (Echo Request) an das Zielgerät. Das Zielgerät antwortet mit einer ICMP-Echo-Antwort (Echo Reply), wenn es erreichbar ist.
ICMP sorgt dafür, dass Informationen über Erreichbarkeit und Verzögerung zwischen den Geräten übermittelt werden, ohne dass die Kommunikation durch andere höhere Protokolle (wie TCP oder UDP) beeinflusst wird. 

***IP (Internet Protocol):***

Aufgabe: IP wird verwendet, um die ICMP-Nachrichten zu adressieren und zwischen den Geräten zu steuern.
Während ICMP für die Fehler- und Statusmeldung zuständig ist, sorgt IP dafür, dass die ICMP-Nachricht das richtige Ziel erreicht. Die IP-Adresse des sendenden und des empfangenden Geräts wird in den entsprechenden Feldern der ICMP-Nachricht codiert.
IP kümmert sich um das Routing der Daten durch das Netzwerk, insbesondere wenn die Geräte sich in verschiedenen Netzwerken befinden und die Nachricht über mehrere Router hinweg weitergeleitet werden muss. 

**ICMP:** Überträgt die Echoanforderung und -antwort, liefert Informationen über die Erreichbarkeit und Latenz.
**IP:** Adressiert und leitet die ICMP-Nachrichten zwischen den Geräten weiter. 

***Durch den Ping-Befehl kann man feststellen, ob ein Zielgerät erreichbar ist und wie lange die Antwort dauert.*** 


## Was ist die Aufgabe eines Modems? 

Der Begriff Modem setzt sich aus „Modulator“ und „Demodulator“ zusammen und bezeichnet ein Gerät, das Signale zwischen zwei Endgeräten über unterschiedliche Übertragungswege (Telefon, Kabel, Glasfaser usw.) austauschen kann. Ein Modem wird im Regelfall dazu verwendet, um die Kommunikation zwischen dem Router im Heimnetzwerk und der Gegenstelle beim Internetprovider zu ermöglichen. 


## “Das Internet ist ein Netzwerk von Netzwerken” - Was ist mit dieser Aussage gemeint? 

Hier ist gemeint, dass das Internet mehrere einzelne Netzwerke zu einem großen Netzwerk verbindet.  Das Internet ist nicht ein einzelnes, zentrales Netzwerk, sondern ein riesiges System von miteinander verbundenen Netzwerken. Diese können durch IP miteinander kommunizieren und somit Datenaustauschen bzw bereit stellen.  


## Was ist der Unterschied zwischen einer MAC-Adresse und einer IP-Adresse? 

Die MAC-Adresse bezeichnet den physischen Standort eines Geräts innerhalb eines lokalen Netzwerks (Hardware, zu finden in der Netzwerkkarte des Rechners), während die IP-Adresse die globale oder über das Internet zugängliche Identität des Geräts angibt. Die Ip ist temporär und kann sich ändern lassen. 


## Was genau ist eine Subnetzmaske? 

So wie jede Adresse durch einen Straßennamen und eine Hausnummer definiert ist, besteht eine IP-Adresse aus einer Netzwerkkomponente und einer Host-Komponente (hier findest du heraus, was deine IP-Adresse ist). Nehmen wir 192.168.123.132 als Beispiel. Die ersten drei Oktette (192.168.123.) stehen für das Netzwerk und das letzte Oktett identifiziert einen Rechner in deinem Netzwerk.Die Subnetzmaske spiegelt den Netzwerkanteil in einer IP-Adresse wider.

**Zweck der Subnetzmaske**

Die Subnetzmaske hilft dabei, Datenpakete im Netzwerk korrekt zu routen, indem sie es Routern und Computern ermöglicht, zu entscheiden, ob ein Zielgerät innerhalb des eigenen Netzwerks oder in einem anderen Netzwerk liegt. Wenn die Zieladresse im gleichen Netzwerk ist, wird das Paket direkt zugestellt, andernfalls wird es an den Router gesendet.


## Wie funktioniert das Routing, wenn ich eine Adresse außerhalb meines Subnetzes erreichen möchte? 

Wenn du eine Adresse außerhalb deines eigenen Subnetzes erreichen möchtest, muss das Routing über einen Router erfolgen. Das Routing funktioniert so, dass der Router dafür zuständig ist, Datenpakete von einem Netzwerk in ein anderes zu übertragen.

1. Überprüfung der Zieladresse

Wenn ein Gerät in deinem Netzwerk ein Paket an eine IP-Adresse senden möchte, prüft es zuerst, ob die Ziel-IP-Adresse innerhalb des gleichen Subnetzes liegt. Das passiert, indem die eigene IP-Adresse mit der Subnetzmaske und der Ziel-IP-Adresse verglichen wird.

Wenn die Ziel-IP-Adresse nicht im selben Subnetz liegt, muss das Paket an einen Router geschickt werden, der es weiterleitet.

2. Paket an den Router senden

Das Paket wird an den Standardgateway gesendet. Der Standardgateway ist in den Netzwerkeinstellungen deines Geräts definiert. Der Router ist dafür verantwortlich, das Paket weiterzuleiten.

3. Routenentscheidung des Routers

Der Router empfängt das Paket und prüft die Ziel-IP-Adresse, um zu entscheiden, wohin es weitergeleitet werden soll. Der Router verwendet dazu seine Routing-Tabelle, die Informationen darüber enthält, wie er Daten an verschiedene Netzwerke weiterleiten kann.

- Wenn der Router die Zieladresse direkt erreichen kann, wird das Paket an das entsprechende Zielnetzwerk weitergeleitet.
- Falls der Router die Zieladresse nicht direkt erreichen kann, wird das Paket an den nächsten Router weitergeleitet, der möglicherweise näher an dem Zielnetzwerk liegt. Dies wird als Weiterleitung (Forwarding) bezeichnet.

4. Route über mehrere Router

Falls die Zieladresse noch weiter entfernt ist, kann das Paket über mehrere Router weitergeleitet werden, bis es das Zielnetzwerk erreicht. Jeder Router entlang des Weges entscheidet anhand seiner Routing-Tabelle, wie er das Paket weiterleitet.

5. Erreichen des Zielnetzwerks

Schließlich wird das Paket von einem Router oder Gateway in das Zielnetzwerk weitergeleitet, und der Router, der direkt im Zielnetzwerk steckt, leitet das Paket dann an das entsprechende Zielgerät weiter.