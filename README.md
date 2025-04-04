# SchnitzelGraph
A program to generate different paths through a graph
---
Sidenote:

Um Konflikte durch unterschiedliche Versionen von Modulen zu vermeiden, sollten wir *venv* und eine *requirements.txt* nutzen.

Man kann einfach im Arbeitsverzeichnis eine virtuelle Umgebung aufsetzen:

1. Einrichten: `python -m venv .venv`
2. Aktivieren: `source .venv/bin/activate`

Wenn man erfolgreich in die virtuelle Umgebung gewechselt ist, sieht man normalerweise im Terminal am Anfang einer Zeile: `(.venv)`

Die meisten IDEs erkennen venv und gehen automatisch in die Umgebung, wenn sie eine entdecken - in VSCode muss man dafür vielleicht die Python Extension installieren.

Dann gibt es noch die 'requirements.txt'-Datei. Da sind alle installierten Python-Module in der Umgebung aufgelistet. 

Man kann die einfach mit `pip install -r requirements.txt` installieren.
Werden neue Module installiert, macht man `pip freeze > requirements.txt` und die Datei wird geupdatet.
So sind wir hoffentlich alle auf einem Stand.


