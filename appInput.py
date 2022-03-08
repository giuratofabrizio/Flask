from flask import Flask,render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('form.html')

@app.route('/date', methods=['GET'])
def data():
    Name = request.args['Name']
    return render_template('welcome.html', nome=Name)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)