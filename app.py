from flask import Flask, render_template, jsonify
from database import load_gba_dict_list_from_db, load_assessment_dict_from_db

app = Flask(__name__)

@app.route("/")
def hello_pharmabase():
  return render_template("home.html",
                          company="Pharmabase")
  
@app.route("/htainsights")
def hta_insights():
  gba_dict_list = load_gba_dict_list_from_db("SELECT * FROM gba")
  return render_template("htainsights.html",
                         table=gba_dict_list,
                         company="Pharmabase")

@app.route("/api/table")
def list_table():
  gba_dict_list = load_gba_dict_list_from_db("SELECT * FROM gba")
  return jsonify(gba_dict_list)



@app.route("/assessment/<id>")
def show_assessment(id):
  assessment_dict = load_assessment_dict_from_db(id)
  if not assessment_dict:
    return "Not Found", 404
  return render_template("assessmentpage.html",
                         assessment=assessment_dict)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)