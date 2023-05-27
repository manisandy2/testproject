import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request


credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/plus.business.manage']
)


credentials.refresh(Request())
access_token = "AIzaSyAYI0RbWinikf9Si0eg6oEfknDVwnRhXzY"

# Replace with your access token and account ID
# access_token = google_service_account_get_access_token()
account_id = '115683479125390656399'

# Set up the request headers
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Make the API request
url = f'https://mybusiness.googleapis.com/v4/accounts/{account_id}'
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    account_info = response.json()
    # Process the account information as needed
    print(account_info)
else:
    print(f'Error: {response.status_code} - {response.text}')