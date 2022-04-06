#realizzare un server web che permetta di effettuare il log-in, l'utente inserisce lo username e la password: se lo username è admin e la password xxx123#, #altrimenti ci dà un messaggio d'errore

from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def es():
    return render_template('es.html')


@app.route('/date', methods=['GET'])
def date():
    Name = request.args['Name']
    
    Pass = request.args['Pass']

    if Name==('admin') and Pass==('xxx123#'):
       return render_template('welcome.html', nome=Name)
    else:
        return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)