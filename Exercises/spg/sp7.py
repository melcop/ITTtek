# importerer Flask klassen og render_template funktionen fra flask modulet
from flask import Flask, render_template
# laver en instans af Flask klassen med dunder parametret __name__ som,
# gør at applikationen ved hvor resourcer kan findes
app = Flask(__name__)
# Decorater metode som gør at hello funktionen kaldes når man tilgår root URL /
@app.route('/')
def hello():
    """View funktion der returnerer og viser templaten home.html"""
    return render_template('home.html')

# if statement der tjekker om filen er hovedfilen som blev startet af python
if __name__ == '__main__':
    # starter applikationen i debug mode
    app.run(debug=True)