import google.auth
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import datetime

# Set up authentication
SCOPES = ['https://www.googleapis.com/auth/business.manage']
KEY_FILE_LOCATION = 'service_account.json'

ser_creds = service_account.Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)
print(ser_creds)

info_creds = service_account.Credentials.from_service_account_info(KEY_FILE_LOCATION,scopes=SCOPES)
print(info_creds)

# Create a client object
# client = build('mybusiness', 'v4', credentials=creds)
# print(client)

# # Set the location ID for your business
# location_id = '02613928441639437097'
data = requests.get('https://business.google.com/posts/l/02613928441639437097')
print(data.json())
#
#
# # Set the text for your post
# post_text = 'New post on Google My Business!'
#
# # Set the call-to-action button for your post
# call_to_action = {
#     'actionType': 'LEARN_MORE',
#     'url': 'https://www.example.com'
# }
#
# # Set the start and end date/time for your post
# start_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
# end_time = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
#
# # Create the post
# post = {
#     'languageCode': 'en-US',
#     'summary': post_text,
#     'callToAction': call_to_action,
#     'event': {
#         'title': post_text,
#         'startDate': start_time,
#         'endDate': end_time
#     }
# }
#
# try:
#     # Call the API to create the post
#     response = client.accounts().locations().localPosts().create(parent=f'accounts/{project_id}/locations/{location_id}', body=post).execute()
#     print(f"Post created! ID: {response['name']}")
# except HttpError as error:
#     print(f"An error occurred: {error}")