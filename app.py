# Van de Flask bibliotheek importeer je de Flask class
# Van markupsafe importeren we de escape functie
# We importeren de random bibliotheek
from flask import Flask, abort
from markupsafe import escape
import random

# We maken een drie dimensionale reeks aan
# Hierin geven we voor iedere set, de winnende en de verliezende set
# Dit gebeurd op volgorde. Steen wint van schaar en verliest van papier
# Papier wint van steen en verliest van schaar en schaar wint van papier en verliest van steen
# In iedere reeks zie je: [winnende set, gelijke set, verliezende set]
sps_results = [['schaar', 'steen', 'papier'], ['steen', 'papier', 'schaar'], ['papier', 'schaar', 'steen']]

# Maak een instantie van de Flask class
# __name__ is een variabele die de naam van de Python module bevat
# De Flask class gebruikt deze om het juiste pad te vinden
# Als we dit bestand uitvoeren is de waarde hiervan __main__, dit veranderd als dit bestand geimporteerd wordt
app = Flask(__name__)

# Maak een route, dit is een URL die je kan bezoeken in de browser
# In dit geval is het de root van de website, de URL zonder iets erachter
@app.route('/')
def hello_world():
    # Deze functie wordt uitgevoerd als de route bezocht wordt
    # De return waarde wordt getoond in de browser / teruggeven aan de aanvrager
    return '<p>Hello, World!</p>'

# Maak een route, deze wordt gebruik voor het maken van een willekeurige set.
# Deze route wordt bereikt met localhost:5000/sps/
@app.route('/sps/')
def sps_move():
    # Geef een willekeurige set terug aan de applicatie.
    return random.choice(['steen', 'papier', 'schaar'])

# We maken een route voor het spelen van het spel
# We gebruiken hiervoor de link localhost:5000/sps/<move>
@app.route('/sps/<move>')
def sps_game(move):
    # Deze functie heeft één variabele, de set van de speler
    # Een try block wordt gebruikt om eventuele foutmeldingen op te vangen
    try:
        # Controleer of de input van de gebruik een valide optie is
        user_move = ['steen', 'papier', 'schaar'].index(move)

        # Laat de computer een waarde kiezen
        computer_move = sps_move()

        # Maak een variabele voor het resultaat
        result_index = (sps_results[user_move]).index(computer_move)
        result = ['Gewonnen!', 'Gelijk.', 'Verloren!'][result_index]
        
        
        # Geef het antwoord
        return f'{result}\nJouw {move} tegen mijn {computer_move}'

    # Tijdens het controleren is het mogelijk dat de interpreter een ValueError geeft
    # Dit gebeurd als de gebruiker iets invult dat geen geldige set is
    # Op deze manier kunnen we dit opvangen, in plaats van de applicatie laten vastlopen
    except ValueError:
        # We sturen error code 400 terug, dit staat voor bad request
        abort(400)
    