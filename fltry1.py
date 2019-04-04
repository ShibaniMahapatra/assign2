from flask import Flask
import ast
import urllib.request
import request
from flask import jsonify

from flask import render_template
# from flask import request
from token_name import *


listOfSymptomsIds=[]
listOfSymptoms=[]

dict_of_names={}
dict_of_ids={}


app = Flask(__name__)
@app.route("/search")
def home():
  return render_template('index.html')


@app.route("/api1", methods=['GET', 'POST'])
def api1():
    url_symptoms = urllib.request.urlopen("https://sandbox-healthservice.priaid.ch/symptoms?" + token)
    symptoms_read = (url_symptoms.read())
    string_symptoms = str(symptoms_read, 'utf-8')
    rawlist_sym = ast.literal_eval(string_symptoms)
    # print(rawlist_sym)
    for each in rawlist_sym:
        dict_of_names = {}
        dict_of_names[each["ID"]] = each["Name"]

        dict_of_ids[each["Name"]] = each["ID"]
        listOfSymptomsIds.append(dict_of_names)
        listOfSymptoms.append(each["Name"])
    print(listOfSymptomsIds)

    # return render_template('api1submit.html')
    return render_template('api1submit.html', message=listOfSymptomsIds)
    # return jsonify(listOfSymptomsIds)


@app.route("/api2", methods=['GET', 'POST'])
def api2():
    # id = input("Enter your id: ")
    # year = input("Enter your year: ")
    # gender = input("Enter your gender: ")
    id = request.form['ID value']
    year = request.form['Year value']
    gender = request.form['Gender value']
    url="https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[" + id + "]&gender=" + gender + "&year_of_birth=" + year + token
    rawlist_diag = ast.literal_eval(str((urllib.request.urlopen(url).read()), 'utf-8'))
    for symptoms in rawlist_diag:
        symptom = symptoms["Issue"]["Name"]
        print(symptom)


if __name__ == "__main__":
    app.run(debug=True)
