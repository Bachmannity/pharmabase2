from flask import Flask, render_template, jsonify
from database import load_table_from_db

app = Flask(__name__)

@app.route('/')
def hello_pharmabase():
  table = load_table_from_db("select * from gba")
  return render_template('home.html',
                         table=table,
                         company="Pharmabase")

@app.route('/api/table')
def list_table():
  table = load_table_from_db("select * from gba")
  return jsonify(table)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)