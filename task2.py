#!/usr/bin/env python3

import http.client
import sys
import json

access_token = "cOmUpOXfevWx560egh1njpwsRLrkeBsT9ORXgYpvDYdo0u9okmRUiuCPnDSy6BUf3FzzwlfkY3cufVlOBKY-CmPcVt-3JINsJOZrAfHaNYtP1Hyg3gGuyR-.EEsYROJu"

def get_json_file():
    input_file = 'qa_task2.json'
    while input_file == '':
        input_file = input("Enter a JSON file:\n")
    try:
        file = open(input_file)
    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(1)
    else:
        with file:
            try:
                json_file = json.load(file)
            except:
                print("Enter a correct JSON file")
                print('Example:\n{"Survey_Name":{"Page_Name":{"Question1":{"Description":"Description of question 1","Answers":["Answer1","Answer2","Answer3"]},"Question2":{"Description":"Description of question 2","Answers":["Answer1","Answer2","Answer3"]},"Question3":{"Description":"Description of question 3","Answers":["Answer1","Answer2","Answer3"]}}}}')
                sys.exit(1)
            else:
                return json_file


def create_survey_api(json_file):

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
    return json.dumps(survey)


def execute_request(method, url, payload):
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

def create_survey():
    json_file = get_json_file()
    result = execute_request("POST", "/v3/surveys", create_survey_api(json_file))
    return result['id']

def create_collector(survey_id):
    payload = {
      "type": "weblink"
    }
    result = execute_request("POST", f"/v3/surveys/{survey_id}/collectors", json.dumps(payload))
    return result['id']
'''
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
'''
survey_id = create_survey() 

collector_id = create_collector(survey_id)

'''
print('+++++++++++++++++++create_message')
message_id = create_message(collector_id)
print(message_id)
'''
