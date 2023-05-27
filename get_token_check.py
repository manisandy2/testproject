# import requests
# from google.oauth2 import service_account

# # Set up OAuth 2.0 credentials
# credentials = service_account.Credentials.from_service_account_file(
#     'Service.json',
#     scopes=['https://www.googleapis.com/auth/business.manage'])

# print(credentials.)

# # Obtain access token
# access_token = credentials.token

# # Make an API request using the access token
# url = 'https://mybusinessaccountmanagement.googleapis.com/v1/accounts'
# headers = {'Authorization': f'Bearer {access_token}'}
# response = requests.get(url, headers=headers)

# # Print the API response
# print(response.json())



# import google.auth
# from google.auth.transport.requests import Request
# from google.oauth2 import service_account
# import requests

# # Authenticate with service account credentials
# credentials = service_account.Credentials.from_service_account_file(
#     'service_account.json',
#     scopes=['https://www.googleapis.com/auth/business.manage'])

# # Obtain access token
# if credentials.expired and credentials.refresh_token:
#     credentials.refresh(Request())
# access_token = credentials.token

# # Make an API request using the access token
# url = 'https://mybusinessaccountmanagement.googleapis.com/v1/accounts'
# headers = {'Authorization': f'Bearer {access_token}'}
# response = requests.get(url, headers=headers)

# # Print the API response
# print(response.json())

# from google.oauth2.service_account import Credentials
# import requests

# # Load the service account credentials from the JSON file
# creds = Credentials.from_service_account_file('service_account.json')

# # Use the credentials to obtain an access token
# print(creds._subject)
# access_token = creds.token

# Include the access token in the Authorization header of your API requests
# headers = {'Authorization': 'Bearer ' + access_token}

# Make your API request using the appropriate library function
# response = requests.get('https://mybusiness.googleapis.com/v4/accounts', headers=headers)


from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2.credentials import UserAccessTokenCredentials
import requests
import json

# Define the necessary variables
SCOPES = ['https://www.googleapis.com/auth/business.manage']
KEY_FILE_LOCATION = 'service_account.json'

# Load the service account credentials from the JSON file
creds = service_account.Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)

# Authenticate and retrieve an access token

creds = creds.with_scopes(SCOPES)
creds.refresh(Request())
# print(creds.token)
# Use the access token in your API requests
# headers = {'Authorization': f'Bearer {creds.token}'}
# print(headers)


# response = requests.get('https://mybusiness.googleapis.com/v4/accounts', headers=headers)
# print(response.headers)


headers = {
    "Authorization": "Bearer " + creds.token,
    "Content-Type": "application/json",
}

# Define API endpoint and request parameters
endpoint = "https://mybusinessaccountmanagement.googleapis.com/v1/accounts"
params = {
    "pageSize": 50,
}

# Make API request
response = requests.get(endpoint, headers=headers, params=params)

# Handle response
if response.status_code == 200:
    data = json.loads(response.text)
    for account in data["accounts"]:
        print("id",account["name"][9:])
        print(account["accountName"])
        print(account["type"])
        print(account["verificationState"])
        print(account["vettedState"])
        data = 'https://mybusiness.googleapis.com/v4/accounts/'+ str(account["name"][9:]) + "/" + str(14437095772377273965)
        print(data)
        data1 = requests.get(data)
        print(data1.text)
else:
    print("Error:", response.status_code, response.text)


# https://mybusiness.googleapis.com/v4/accounts/{accountId}/locations
# https://business.google.com/posts/l/14437095772377273965
