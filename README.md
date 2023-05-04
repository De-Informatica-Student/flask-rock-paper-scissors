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
.venv\Scrips\activate               # Windows
. .venv/bin/activate                # Mac/Linux

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
Doormiddel van ```ctrl + c``` kun je applicatie stoppen.

## Input krijgen

Een antwoord geven op een verzoek is leuk,
maar het is ook fijn als de gebruiker van onze API input kan leveren.
Hiervoor gaan we 'Hello World' uitbreiden naar een persoonlijke begroeting.
We voegen een functie toe aan de applicatie. Deze ziet er als volgt uit.

```python
# Maak een route, deze gaat de gebruiker persoonlijk begroeten
# We veranderen de route door er een variabel in te zetten.
# We zetten de variabel tussen < en > en geven deze een naam.
@app.route('/<name>')
def hello_name(name):
    # Deze functie wordt uitgevoerd als de route bezocht wordt
    # Het verschil met de vorige functie is het bestaan van een parameter

    # Vervolgens begroeten we de gebruiker, let op de f voor de qoute
    # De f geeft aan dat we binnen de string variabele gaan plakken, tussen { en }
    return f'<p>Hello, {name}</p>'
```

De code moet vervolgens opnieuw worden opgestart.
Er is echter een andere manier om het programma te laten draaien.
Op deze manier hoeven we niet na elke wijziging het programma opnieuw op te starten.
We doen dit door Flask te starten in de zogehete 'debug' modus.

```ps
flask run --debug
```

Vervolgens kun je in je favoriete browser, de link uit de console openen.
In de navigatiebalk pas je het adres aan naar: ```http://127.0.0.1:5000/name```.
Vervang ```name``` door je eigen naam.
Er is echter een klein probleem met deze code, qua veiligheid is dit best slecht.
We moeten ervoor zorgen dat de input van de gebruiker wordt gefilterd.
De huidige zal ieder stuk tekst direct op het scherm tonen.
Als hier code in staat, dan zal dit worden uitgevoerd.
Je kan dit testen door als input in de browser ```<b>name``` in te vullen.
Je zal zien dat de tekst dan wordt geformateerd.
Dit lossen we op met de escape functie.

```python
# bovenin het document moeten we naast Flask, ook escape importeren
from markupsafe import escape

# Vervang de return in de functie met
return f'<p>Hello, {escape(name)}</p>'
```

De complete code ziet er nu uit als:

```python
# Importeer the Flask bibliotheek
# Van de Flask bibliotheek importeer je de Flask class
from flask import Flask
from markupsafe import escape

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

# Maak een route, deze gaat de gebruiker persoonlijk begroeten
# We veranderen de route door er een variabel in te zetten.
# We zetten de variabel tussen < en > en geven deze een naam.
@app.route('/<name>')
def hello_name(name):
    # Deze functie wordt uitgevoerd als de route bezocht wordt
    # Het verschil met de vorige functie is het bestaan van een parameter
    # Vervolgens begroeten we de gebruiker
    return f'<p>Hello, {escape(name)}</p>'
```
