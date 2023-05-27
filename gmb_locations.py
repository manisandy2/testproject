# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build
#
# CLIENT_ID = str("280849678280-49a69fmkjs5lh4kh0tthidajg75pkc4p.apps.googleusercontent.com")
# CLIENT_SECRET = str(r"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")
# SCOPES = ["https://www.googleapis.com/auth/business.manage"]
#
# creds = Credentials.from_authorized_user_info(info=None, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scopes=SCOPES)
#
#
# service = build("mybusiness", "v4", credentials=creds)
#
# response = service.accounts().list().execute()
#
# for account in response.get("accounts", []):
#     print(f"Account name: {account['name']}")
#     for location in account.get("locations", []):
#         print(f"Location name: {location['locationName']}")

#
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


creds, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/business.manage'])
print(creds)
print(project_id)
# client = build('mybusinessbusinessinformation', 'v4', credentials=creds)
client = build('mybusinessbusinessinformation', 'v4', credentials=creds)
print(creds)
account_id = '115683479125390656399'
location_id = '02613928441639437097'
#
# location_name = 'accounts/{}/locations/{}'.format(account_id,location_id)
# # location = client.accounts().locations().get(name=location_name).execute()
# # location = client.accounts().locations().list().execute()
# # account_summaries = client.management().accountSummaries().list().execute()
# # print("Location :",location)
# # print(account_summaries)


response = client.accounts().locations().list(parent=f'accounts/{account_id}').execute()

if 'locations' in response:
    locations = response['locations']
    for location in locations:
        print(location['name'])
else:
    print('No locations found.')

