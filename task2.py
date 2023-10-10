#!/usr/bin/env python3

import http.client

conn = http.client.HTTPSConnection("api.surveymonkey.com")

#with open('qa_task2.json') as f:
#    payload = f.read()

payload = "{\"title\":\"New Survey\",\"nickname\":\"My Survey\",\"language\":\"en\",\"buttons_text\":{\"next_button\":\"string\",\"prev_button\":\"string\",\"exit_button\":\"string\",\"done_button\":\"string\"},\"custom_variables\":{},\"footer\":true}"

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "Bearer EiwSAO2.L6DsGStNzQCccy9q7tCB4x22swJmYJQprzRghUnUGTVFX5CUCpv45Kvh1olFm08ZEMMpmrdfTqpDaAEUxfVs78YDOJfORSY-pS7TKpsE2npQU7tzhVACF.5Z"
    }

conn.request("POST", "/v3/surveys", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

