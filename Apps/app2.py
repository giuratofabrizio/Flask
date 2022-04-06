from flask import Flask,render_template
app = Flask(__name__)

import datetime

@app.route('/')
def hello_world():
  minuti= datetime.datetime.now().minute
  if minuti%2==0:
    col = 'green'
  else:
    col= 'red'
  return render_template('risposta.html', colore= col, min=minuti)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)