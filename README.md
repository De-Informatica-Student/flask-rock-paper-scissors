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
# Van de Flask bibliotheek importeer je de Flask class
# Van markupsafe importeren we de escape functie
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

## Een willekeurige set

Laten we beginnen met het maken van het spel.
We zullen nog niet kijken naar het spelen van het spel,
maar we gaan de computer een willekeurige set laten doen.
We gaan hiervoor de ```hello_name``` functie (de onderste functie) vervangen.
Voordat we echter kunnen beginnen met schrijven van de functie,
moeten we de random bibliotheek importeren.
Deze voegen we toe aan het rijtje met van importeer opdrachten bovenin het document.

```python
# Van de Flask bibliotheek importeer je de Flask class
# Van markupsafe importeren we de escape functie
# We importeren de random bibliotheek
from flask import Flask, abort
from markupsafe import escape
import random
```

We willen dat de computer een keuze nmaakt tussen steen, papier en schaar.
De ```random``` bibliotheek biedt hier een goede functie voor: ```choice```.
Deze functie kiest een willekeurig item uit een reeks.
Door deze functie een reeks te geven met alle optie waaruit gekozen kan worden,
krijgen we een willekeurige keuze terug.
*Onthoud dat we de ```hello_name``` functie **vervangen** met deze.

```python
# Maak een route, deze wordt gebruik voor het maken van een willekeurige set.
# Deze route wordt bereikt met localhost:5000/sps/
@app.route('/sps/')
def sps_move():
    # Geef een willekeurige set terug aan de applicatie.
    return random.choice(['steen', 'papier', 'schaar'])
```

## Het Spel

Laten we beginnen met het implementeren van het spel.
We zouden het kunnen aanpakken door een groot mijnenveld aan voorwaardes te schrijven.
Echter lijkt het me interresant om te kiezen voor een iets kortere oplossing.
Hiervoor hebben we een verzameling nodig die voor iedere zet,
de winnende en de verliezende set bevat.
Hiervoor kunnen we een ```drie dimensionale reeks``` gebruiken,
in het Engels is dit een ```three dimensional array```.
Dit is een reeks, die reeksen bevat.
Deze array zetten we direct onder de import opdrachten neer.

```python
# We maken een drie dimensionale reeks aan
# Hierin geven we voor iedere set, de winnende en de verliezende set
# Dit gebeurd op volgorde. Steen wint van schaar en verliest van papier
# Papier wint van steen en verliest van schaar en schaar wint van papier en verliest van steen
# In iedere reeks zie je: [winnende set, gelijke set, verliezende set]
sps_results = [['schaar', 'steen', 'papier'], ['steen', 'papier', 'schaar'], ['papier', 'schaar', 'steen']]
```

