#realizzare un server web che permetta di conoscere capoluoghi di regione.
#l'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo.
#caricare i capoluoghi di regione e le regioni in un'opportuna struttura dati

#modificare poi l'es precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button
from flask import Flask,render_template, request
app = Flask(__name__)

capoluoghiRegione = {'Abruzzo':'LAquila' , 'Basilicata':'Potenza' , 'Calabria':'Catanzaro' , 'Campania':'Napoli' ,
  'EmiliaRomagna':'Bologna' , 'Friuli':'Trieste' , 'Lazio':'Roma' , 'Liguria':'Genova' , 'Lombardia':'Milano' ,
  'Marche':'Ancona' , 'Molise':'Campobasso' , 'Piemonte':'Torino' , 'Puglia':'Bari' , 'Sardegna':'Cagliari' , 'Sicilia':'Palermo' , 
  'Toscana':'Firenze' , 'Trentino':'Trento' , 'Umbria':'Perugia' , 'ValleDAosta':'Aosta' , 'Veneto':'Venezia'}

Reg = list(capoluoghiRegione.keys())
Cap = list(capoluoghiRegione.values())

@app.route('/', methods=['GET'])
def RC():
    return render_template('RegioniCapoluoghi.html')


@app.route('/capreg', methods=['GET'])
def CR():
    CR = request.args['Tipo']
    if CR == 'Capoluogo':
        return render_template('Capoluogo.html')
    else: 
        return render_template('Regione.html')


@app.route("/reg", methods=["GET"])
def dataReg():
    regione = request.args["Regione"]
    for key, value in capoluoghiRegione.items():
        if regione == key:
            capoluogo = value
            return render_template("risultato.html", risposta = capoluogo)
    return "<h1>Errore</h1>"

@app.route("/cap", methods=["GET"])
def dataCap():
    capoluogo = request.args["Capoluogo"]
    for key, value in capoluoghiRegione.items():
        if capoluogo == value:
             regione = key
             return render_template("risultato.html", risposta = regione)
    return "<h1>Errore</h1>"





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)