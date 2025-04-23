Virtuelle Umgebung aktivieren (falls noch nicht geschehen):


cd "C:\Users\lewec\Documents\Coding Experimente\first"
.\venv\Scripts\activate
PyInstaller (und setuptools) sicher installieren:


python -m pip install pyinstaller setuptools
PyInstaller per Modul aufrufen (ohne Mehrfach-Zeilen-Prompt):


python -m PyInstaller --name BruttoNettoRechner --onefile --windowed --add-data "lst2025.py;." --add-data "krankenkassen.db;." main.py
– Wichtig:

Kein Backtick (\``) oder Caret (^`) nötig, wenn Du alles in einer Zeile schreibst.

Achte auf genau dieses Semikolon-Format ("lst2025.py;.") unter Windows.


.\dist\BruttoNettoRechner\BruttoNettoRechner.exe
Deine einzelne, lauffähige EXE, die die eingebettete krankenkassen.db und lst2025.py korrekt lädt.

Test
Kopiere die .exe in einen anderen Ordner (oder auf einen anderen PC) – sie startet ohne Python-Installation.
