from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests
import json

SCOPES = ['https://www.googleapis.com/auth/business.manage']
KEY_FILE_LOCATION = 'service_account.json'


creds = service_account.Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)

creds = creds.with_scopes(SCOPES)
creds.refresh(Request())
access_token = creds.token
print(access_token)
print(creds.refresh)

headers = {
    "Authorization": "Bearer " + creds.token,
    "Content-Type": "application/json",
}


endpoint = "https://mybusinessaccountmanagement.googleapis.com/v1/accounts"
params = {
    "pageSize": 50,
}

response = requests.get(endpoint, headers=headers, params=params)

print(response.text)

if response.status_code == 200:
    data = json.loads(response.text)
    for account in data["accounts"]:
        print("id",account["name"][9:])
        print(account["accountName"])
        print(account["type"])
        print(account["verificationState"])
        print(account["vettedState"])


else:
    print("Error:", response.status_code, response.text)

