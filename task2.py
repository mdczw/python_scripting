#!/usr/bin/env python3

import http.client
import sys
import json


def get_json_file():
    input_file = ''
    while input_file == '':
        input_file = input("Enter a JSON file:\n")
    try:
        file = open(input_file)
    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(1)
    else:
        with file:
            json_file = json.load(file)
    return json_file


def create_survey_api(json_file):
    try:
        survey = {
            "title": list(json_file.keys())[0],
            "pages": []
        }
        for page_name, page_data in json_file[list(json_file.keys())[0]].items():
            page = {
                "title": page_name,
                "questions": []
                }
            for question_name, question_data in page_data.items():
                question = {
                    "headings": [{"heading": question_data['Description']}],
                    "family": "single_choice",
                    "subtype": "vertical",
                    "answers": {"choices": []}
                }
                for answer_name in question_data['Answers']:
                    answer = {
                        "text": answer_name
                    }
                    question["answers"]["choices"].append(answer)
                page["questions"].append(question)
            survey["pages"].append(page)
    except:
        print("Enter a correct JSON file")
        print('Example:\n{ "Survey_Name": { "Page_Name": { "Question1": { "Description" : "Description of question 1", "Answers" : [ "Answer1", "Answer2", "Answer3" ] }, "Question2": { "Description" : "Description of question 2", "Answers" : [ "Answer1", "Answer2", "Answer3" ] }, "Question3": { "Description" : "Description of question 3", "Answers" : [ "Answer1", "Answer2", "Answer3" ] } } } }')
        sys.exit(1)
    else:
        return json.dumps(survey)


def surveymonkey_connaction(access_token, payload):
    conn = http.client.HTTPSConnection("api.surveymonkey.com")
    headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {access_token}"
    }

    conn.request("POST", "/v3/surveys", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

access_token = "EiwSAO2.L6DsGStNzQCccy9q7tCB4x22swJmYJQprzRghUnUGTVFX5CUCpv45Kvh1olFm08ZEMMpmrdfTqpDaAEUxfVs78YDOJfORSY-pS7TKpsE2npQU7tzhVACF.5Z"
json_file = get_json_file()
payload = create_survey_api(json_file)
surveymonkey_connaction(access_token, payload)
