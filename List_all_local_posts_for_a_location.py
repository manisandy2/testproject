# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build
#
# from google.oauth2 import service_account
# from google.oauth2 import credentials
# from google.auth.transport.requests import Request
# import requests
# import json
#
# SCOPES = ['https://www.googleapis.com/auth/business.manage']
# KEY_FILE_LOCATION = 'service_account.json'
#
#
# creds = service_account.Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)
#
# creds = creds.with_scopes(SCOPES)
# creds.refresh(Request())
# access_token = creds.token
# print(access_token)
#
# # Replace the placeholders with your own values
# location_name = 'locations/LOCATION_ID'
# api_version = 'v4'
#
# # Create a credentials object with the access token and refresh token
# creds = credentials.Credentials. .Credentials.from_authorized_user_info(info={}, token=access_token)
#
# # Build the API client object
# api_client = build('mybusiness', api_version, credentials=creds)
#
# # Call the accounts.locations.localPosts.list method to retrieve all local posts for the location
# posts = api_client.accounts().locations().localPosts().list(parent=location_name).execute()
#
# # Print the list of local posts
# print(posts)