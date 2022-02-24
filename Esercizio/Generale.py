from flask import Flask, render_template
app = Flask(__name__)
import random

@app.route('/')
def Gen():
  return render_template('Generale.html')


@app.route('/meteo')
def meteo():
    nRandom = random.randint(0,8)
    if nRandom <= 2:
        immagine = "static/Pioggia.jpg"
    elif nRandom <= 5:
        immagine = "static/nuvole.jpg"
    else:
        immagine = "static/sole.jpg"
    return render_template("meteo.html", meteo=immagine)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)