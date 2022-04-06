#realizzare un sito web che permetta la registrazione degli utenti
# l'utente inserisce il nome, uno username, una password
# la conferma della password e il sesso. FATTO

# se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna(lista dizionari).FATTO
#prevedere la possibilità di fare il log-in inserendo username e password. FATTO
# se sono corrette, fornire un messaggio di benvenuto diverso a seconda del sesso. FATTO

from flask import Flask,render_template, request
app = Flask(__name__)

lst= []


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

    if Pass == Confirm:
        lst.append({'Name':Name,'User':Username,'Pass':Pass,'Sex':Sex})
        print(lst)
        return render_template('login.html')
    else:
        return render_template('errore.html')


@app.route('/login', methods=['GET'])
def login():

    User_log = request.args['User_log']
    Pass_log = request.args['Pass_log']

    for utente in lst:
        if utente['User'] == User_log and utente['Pass'] == Pass_log:
                if utente['Sex']=='M':
                     return render_template('welcome.html', name=utente['Name'])
                else:
                     return render_template('welcomeW.html', name=utente['Name'])

    return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)