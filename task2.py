#!/usr/bin/env python3
"""Script uses the Survey Monkey service to create a survey"""

import http.client
import sys
import json
import argparse


def get_data_from_input_file():
    """Returns survey data in Python object format"""
#   input_file = 'qa_task2.json'
    input_file = ''
    while input_file == '':
        input_file = input("Enter a JSON file:\n")
    try:
        file = open(input_file, encoding="utf-8")
    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(1)
    else:
        with file:
            try:
                survey_data = json.load(file)
            except:
                print("Enter a correct JSON file")
                print('Example:\n{"Survey_Name":{"Page_Name":{"Question1":{"Description":"Description of question 1","Answers":["Answer1","Answer2","Answer3"]},"Question2":{"Description":"Description of question 2","Answers":["Answer1","Answer2","Answer3"]},"Question3":{"Description":"Description of question 3","Answers":["Answer1","Answer2","Answer3"]}}}}')
                sys.exit(1)
            else:
                return survey_data

def create_survey_json():
    """Converts the data into the appropriate json format"""
    survey_data = get_data_from_input_file()
    survey = {
        "title": list(survey_data.keys())[0],
        "pages": []
    }
    for page_name, page_data in survey_data[list(survey_data.keys())[0]].items():
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
    return json.dumps(survey)

def get_access_token():
    """Gets access_token from input"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--access_token", help="access token")
    args = parser.parse_args()
    return args.access_token

def execute_request(method, url, payload):
    """Connection to the surveymonkey"""
    access_token = get_access_token()
    conn = http.client.HTTPSConnection("api.surveymonkey.com")
    headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {access_token}"
    }

    conn.request(method, url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return json.loads(data)

def create_survey_preview(survey_data):
    """Creates survey preview"""
    result = execute_request("POST", "/v3/surveys", survey_data)
    return result['id']

def create_survey_collector(survey_data):
    """Creates survey collector"""
    survey_id = create_survey_preview(survey_data)
    payload = {
      "type": "weblink"
    }
    result = execute_request("POST", f"/v3/surveys/{survey_id}/collectors", json.dumps(payload))
    return result['id']
"""
def create_message(collector_id):
    payload = {
      "type": "invite",
      "subject": "Share your opinion with us",
      "body_text (for email invitations)": "We want your opinion!"
    }

    result = execute_request("POST", f"/v3/collectors/{collector_id}/messages", json.dumps(payload))
    return result['id']

def upload_recipients(collector_id, message_id):
     
    payload = {
      "type": "invite",
      "recipient_status": "",
      "subject": "Share your opinion with us",
      "body_text (for email invitations)": "We want your opinion!"
    }

    result = execute_request("POST", f"/v3/collectors/{collector_id}/messages/{message_id}/recipients/bulk", json.dumps(payload))
    return result['id']
"""

if __name__ == "__main__":

    json_survey_data = create_survey_json()

    collector_id = create_survey_collector(json_survey_data)

    """
    print('+++++++++++++++++++create_message')
    message_id = create_message(collector_id)
    print(message_id)
    """
