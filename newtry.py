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



mainSymptomArray=[]
mainId=[]

def api4():
    listOfSymptoms.sort(key=len, reverse=True)
    print(listOfSymptoms)
    sentence = input("Enter your sentence:")
    for sym in listOfSymptoms:
        if sym in sentence:
            mainSymptomArray.append(sym)


    for mainsym in mainSymptomArray:
        for key in dict_of_ids.keys():
            if (key ==mainsym):
                # print(dict_of_ids[key])
                mainId.append((str(dict_of_ids[key])))
    stringId= ','.join(mainId)

    print(mainId)
    print(stringId)
    # IdArray=str(mainId).strip('[]')
    # IdArray = [str(x).replace(' ','') for x in mainId]
    # print(IdArray)
    # print(type(IdArray))
    year = input("Enter your year: ")
    gender = input("Enter your gender: ")
    url="https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[" + stringId + "]&gender=" + gender + "&year_of_birth=" + year + token
    print(url)
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
api4()
api5()