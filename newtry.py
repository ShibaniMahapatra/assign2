import ast
import urllib.request
import yaml
from token_name import *

listOfSymptomsIds=[]
listOfSymptoms=[]

dict_of_names={}
dict_of_ids={}




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


def api4():
    listOfSymptoms.sort(key=len, reverse=True)
    print(listOfSymptoms)
    sentence = input("Enter your sentence:")
    for sym in listOfSymptoms:
        if sym in sentence:
            mainSymptom = sym
            break

    for key in dict_of_ids.keys():
        if (key == mainSymptom):
            mainid = dict_of_ids[key]

    print(mainid)
    year = input("Enter your year: ")
    gender = input("Enter your gender: ")
    url="https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[" + str(mainid) + "]&gender=" + gender + "&year_of_birth=" + year + "&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNoaWJhbmkubmV3OTdAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI0ODE1IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDE5LTAzLTIwIiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1NTQxODgxMjMsIm5iZiI6MTU1NDE4MDkyM30.cc8cpsYULGcjnesa4mJrQoFHY8nVpJlf0qqLSM7w1_s&format=json&language=en-gb"
    rawlist_diag = ast.literal_eval(str((urllib.request.urlopen(url).read()), 'utf-8'))
    for symptoms in rawlist_diag:
        symptom = symptoms["Issue"]["Name"]
        print(symptom)

def api2():
    id = input("Enter your id: ")
    year = input("Enter your year: ")
    gender = input("Enter your gender: ")
    url="https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[" + id + "]&gender=" + gender + "&year_of_birth=" + year + token
    rawlist_diag = ast.literal_eval(str((urllib.request.urlopen(url).read()), 'utf-8'))
    for symptoms in rawlist_diag:
        symptom = symptoms["Issue"]["Name"]
        print(symptom)

def api5():
    latitude = input("Enter latitude")
    longitude = input("Enter longitude")
    url_for_search = "https://api.betterdoctor.com/2016-03-01/doctors?location=" + latitude + "%2C" + longitude + "%2C100&user_location=" + latitude + "%2C" + longitude + "&skip=0&limit=10&user_key=027ea541c429554b2af7a1c11d089b00"
    string_doctor = str(urllib.request.urlopen(url_for_search).read(), 'utf-8')
    total_data = yaml.load(string_doctor, Loader=yaml.FullLoader)
    doctorData = total_data["data"]
    for docProfile in doctorData:
        profile = docProfile['profile']
        firstname = profile['first_name']
        lastname = profile['last_name']
        # print(lastname)
        name = firstname + " " + lastname
        print(name)

api1()
api2()
# api4()
api5()