#realizzare un sito web che permetta la registrazione degli utenti
# l'utente inserisce il nome, uno username, una password
# la conferma della password e il sesso. FATTO

# se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna(lista dizionari).FATTO
#prevedere la possibilità di fare il log-in inserendo username e password. FATTO
# se sono corrette, fornire un messaggio di benvenuto diverso a seconda del sesso. FATTO

from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def es():
    return render_template('es2.html')


@app.route('/dates', methods=['GET'])
def dates():
    Name = request.args['Name']
    Pass = request.args['Pass']
    Username = request.args['User']
    Confirm = request.args['Conf']
    Sex = request.args['Sex']

    lst= []

    if Pass==Confirm:
       lst.append({Username:Pass})
       if Sex=='M':
           return render_template('welcome.html', nome=Name)
       else:
           return render_template('welcomeW.html', nome=Name)
    else:
        return render_template('error.html')



@app.route('/login', methods=['GET'])
def login():
     return render_template('login.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)