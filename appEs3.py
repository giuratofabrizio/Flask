#realizzare un server web che permetta di conoscere capoluoghi di regione.
#l'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo.
#caricare i capoluoghi di regione e le regioni in un'opportuna struttura dati

#modificare poi l'es precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button






from flask import Flask,render_template, request
app = Flask(__name__)













if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)