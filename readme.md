# Lotto-Generator (6 aus 49)

Ein plattformunabhängiger Lotto-Tip-Generator mit einer modernen grafischen Benutzeroberfläche auf Basis von Python 3 und Tkinter. 

Dieses Projekt modernisiert eine bewährte Logik und bringt sie in ein sauberes, zentriertes Grid-Layout, das unter Windows sowie Linux (z. B. Debian/Linux Mint) gleichermaßen perfekt ausgerichtet ist.

## Features

* **Dynamisches Grid-Layout:** Jede Zahl steht sauber zentriert in ihrer eigenen Spalte – unabhängig von der System-Schriftart.
* **Plattformübergreifend:** Automatische Anpassung von Icons (`.png` / `.ico`) und Pfaden für Linux und Windows.
* **Tastatur-Shortcuts:** Schnelle Bedienung über Hotkeys (z. B. `Strg+E` für neuen Tipp, `Strg+T` für Datei-Ansicht).
* **Editor-Anbindung:** Öffnet die generierte `lotto.txt` direkt im Standard-Texteditor des Betriebssystems.
* **Zentrierte GUI:** Dank eines maßgeschneiderten `center`-Moduls startet das Fenster immer perfekt in der Bildschirmmitte.

## Voraussetzungen

* Python 3.x
* Tkinter (unter Linux ggf. über `sudo apt install python3-tk` zu installieren)

## Starten des Programms

```bash
python3 main.pyw
