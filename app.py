from flask import Flask, render_template

app = Flask(__name__)

DATABASE = [
  {
    'id': 890,
    'therapy': 'Uplinza',
    'disease': 'NMOSD',
    'benefit': 'Unquantifiable'
  },
  {
    'id': 670,
    'therapy': 'Dupixent',
    'disease': 'Asthma',
    'benefit': 'None'
  },
  {
    'id': 750,
    'therapy': 'Rinvoq',
    'disease': 'AD',
    'benefit': 'Minor'
  },
  {
    'id': 520,
    'therapy': 'Vyvgart',
    'disease': 'MG',
    'benefit': 'Considerable'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', database=DATABASE, company="Pharmabase")

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)