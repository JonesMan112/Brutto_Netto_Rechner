ALLES MIT CHATGPT ERSTELLT

Allgemeine Anleitung zur Erstellung einer Einzel-.exe mit PyInstaller

(Optional) Virtuelle Umgebung anlegen und aktivieren
Empfohlen, um Abhängigkeiten sauber zu halten, klappt unter Windows wie folgt:

bat
Kopieren
Bearbeiten
cd <Dein_Projektordner>
python -m venv venv
venv\Scripts\activate
Benötigte Pakete installieren
Stelle sicher, dass Du im aktivierten Environment bist, und führe dann aus:

bat
Kopieren
Bearbeiten
python -m pip install pyinstaller setuptools
Einzel-.exe erstellen
Navigiere in Dein Projektverzeichnis (dort liegen main.py, lst2025.py und krankenkassen.db) und starte PyInstaller mit einer einzigen Zeile:

bat
Kopieren
Bearbeiten
python -m PyInstaller ^
  --name MeinRechner ^
  --onefile ^
  --windowed ^
  --add-data "lst2025.py;." ^
  --add-data "krankenkassen.db;." ^
  main.py
--name: Name der erzeugten EXE (ohne .exe)

--onefile: Alles in eine einzige ausführbare Datei packen

--windowed: GUI-Modus ohne Konsolenfenster

--add-data: Weitere Dateien (Quelle;Ziel) beilegen (unter Windows mit ;, unter macOS/Linux mit :)

Ergebnis finden und testen
Nach erfolgreichem Lauf liegt die EXE im Ordner

php-template
Kopieren
Bearbeiten
dist\<Name>\ <Name>.exe
Kopiere diese EXE auf einen beliebigen Rechner – sie läuft dort ohne Python-Installation.

Tipp:

Unter PowerShell kannst Du statt ^ auch einen Backtick ` verwenden.

Möchtest Du ein Icon hinzufügen, hängst Du --icon=mein_icon.ico an den PyInstaller-Aufruf an.
