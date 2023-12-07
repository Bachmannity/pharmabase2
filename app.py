from flask import Flask, render_template, jsonify, request
from database import load_gba_dict_list_from_db, load_assessment_dict_from_db, load_gba_dict_list_from_query

app = Flask(__name__)

@app.route("/")
def hello_pharmabase():
  return render_template("home.html",
                          company="Pharmabase")

@app.route("/htainsights")
def search_hta_insights():
  return render_template("htainsightssearch.html")

@app.route("/htainsights/results", methods=['post'])
def hta_insights():
  search_results = request.form
  assessment_dicts = load_gba_dict_list_from_query(search_results)
  if not assessment_dicts:
    return "Not Found", 404
  return render_template("htainsightsresults.html",
                         search_results=search_results,
                         assessment_dicts=assessment_dicts)

@app.route("/htainsights/results/assessment/<id>")
def show_assessment(id):
  assessment_dict = load_assessment_dict_from_db(id)
  if not assessment_dict:
    return "Not Found", 404
  return render_template("assessmentpage.html",
                         assessment=assessment_dict)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)