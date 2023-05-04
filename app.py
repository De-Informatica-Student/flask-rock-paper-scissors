# Importeer the Flask bibliotheek
# Van de Flask bibliotheek importeer je de Flask class
from flask import Flask, abort
from markupsafe import escape
import random

# Extra functie voor het bepalen van het resultaat
def check_move(move, win_condition, lose_condition):
    # Controleer of de gebruiker wint
    if (move == win_condition):
        return "Hoera! Jij wint!"
    
    # Controleer of de gebruiker verliest
    elif (move == lose_condition):
        return "Boe! Je verliest!"
    
    # De gebruiker wint niet, verliest niet, dus het is gelijk.
    else:
        return "Gelijkspel"

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

# We maken een route voor het spelen van het spel
# We gebruiken hiervoor de link localhost:5000/bke/<move>
@app.route('/bke/<move>')
def bke_move(move):
    # Deze functie heeft één variabele, de set van de speler
    # Een try block wordt gebruikt om eventuele foutmeldingen op te vangen
    try:
        # Controleer of de input van de gebruik een valide optie is
        (['steen', 'papier', 'schaar'].index(move))

        # Laat de computer een waarde kiezen
        computer = random.choice(['steen', 'papier', 'schaar'])

        # Maak een variabele voor het resultaat
        result = ''

        # We bepalen het resultaat
        if (computer == 'steen'):
            result = check_move(move, 'papier', 'schaar')
        elif (computer == 'papier'):
            result = check_move(move, 'schaar', 'steen')
        else:
            result = check_move(move, 'steen', 'papier')
        
        # Geef het antwoord
        return f'{result}\nJouw {move} tegen mijn {computer}'

    # Tijdens het controleren is het mogelijk dat de interpreter een ValueError geeft
    # Dit gebeurd als de gebruiker iets invult dat geen geldige set is
    # Op deze manier kunnen we dit opvangen, in plaats van de applicatie laten vastlopen
    except ValueError:
        # We sturen error code 400 terug, dit staat voor bad request.
        abort(400)
    