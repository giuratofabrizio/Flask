from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Gen():
  return render_template('Generale.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)