# Steen, Papier, Schaar API in Flask

Dit project is een voorbeeld van hoe Flask gebruikt kan worden om een API op te zetten.
Om dit voor elkaar te krijgen gaan we een API maken voor steen, papier schaar.
De API geeft een gebruiker de mogelijkheid om een simpel spelletje te spelen.
De twee versies van het spel worden geïmplementeerd om zo verschillende routes te proberen.

[Voor het installeren van Python, kun je naar deze instructie kijken.](https://www.informaticastudent.net/1304512_python-installeren-op-windows)

## Installatie

We beginnen het project met het maken van een virtuele Python omgeving.
Het voordeel van een virtuele Python omgeving is dat alles wat het project nodig heeft op één plek staat.
Maak via de console een nieuwe map aan voor het project.
Vervolgens maak je een virtuele omgeving aan met Python.
De omgeving moet vervolgens worden geactiveerd.
En als laatste moet Flask geïnstalleerd worden met pip.

```ps
# Maak een map aan, vervang 'myproject' door de naam die jij wilt.
mkdir myproject

# Maak een virtuele Python omgeving. Het commando zegt:
#   py      (python3 op Mac/Linux)  Python
#   -3      (onnodig op Mac/Linux)  Gebruik Python versie 3
#   -m                              Draai module als een script
#   venv                            Maak een virtuele omgeving (de module)
#                                   Staat voor Virtual ENVironment
#   .venv                           Waar de omgeving moet worden opgeslagen
py -3 -m venv .venv

# Activeer de omgeving zodat we hem in de console kunnen gebruiken
.venv\Scrips\activate           # Windows
. .venv/bin/activate            # Mac/Linux

# Installeer Flask met pip
pip install Flask
```

## Hello World

De volgende stap is het testen van de installatie.
Ook voor een bibliotheek zoals deze maken we gebruik van 'Hello World'.
In de map van ons project maken we een bestand aan genaamd 'app.py'.
De naamgeving is belangrijk, het is de standaard naar voor een Flask applicatie.
Door dit te gebruiken hebben we later een korter commando om het programma te starten.
De inhoud van het bestand is als volgt:

```python
# Importeer the Flask bibliotheek
# Van de Flask bibliotheek importeer je de Flask class
from flask import Flask

# Maak een instantie van de Flask class
# __name__ is een variabele die de naam van de Python module bevat
# De Flask class gebruikt deze om het juiste pad te vinden
# Als we dit bestand uitvoeren is de waarde hiervan __main__, dit veranderd als dit bestand geimporteerd wordt.
app = Flask(__name__)

# Maak een route, dit is een URL die je kan bezoeken in de browser
# In dit geval is het de root van de website, de URL zonder iets erachter
@app.route('/')
def hello_world():
    # Deze functie wordt uitgevoerd als de route bezocht wordt
    # De return waarde wordt getoond in de browser / teruggeven aan de aanvrager
    return '<p>Hello, World!</p>'
```

Vervolgens moet de applicatie worden uitgevoerd.
Door het gebruik van de naamconventie kunnen we een kort commando gebruiken.
Het commando ```flask run``` is voldoende.
Op de link die verschijnt in de console in je favoriete browser,
de tekst 'Hello, World!' zou moeten verschijnen.