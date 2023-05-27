import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up authentication
creds, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/business.manage'])
# creds, project_id = google.auth.default()
creds = Credentials.from_authorized_user_info(creds)

account_id = '115683479125390656399'
location_id = '02613928441639437097'

# Build the API client
service = build('mybusinessbusinessinformation', 'v1', credentials=creds)

# Set the location ID for the location you want to retrieve information about
# location_id = '1234567890'

# Call the v1.locations method to retrieve information about the location
location = service.locations().get(name=f'locations/{location_id}').execute()

# Print the name and address of the location
print(f"Location name: {location['locationName']}")
print(f"Location address: {location['address']['addressLines'][0]}, {location['address']['locality']}, {location['address']['regionCode']} {location['address']['postalCode']}")


from google.oauth2.credentials import Credentials

# Set up authorized user information
scope = "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid",
info = {
    "access_token": "ya29.a0AWY7CkkYP_ulChtStdAAvtAUlg2SAeNzzPbJ8wXc3KPIbb_M4yevv0vi8BRBkIa3Wm70u5eFUbRlX6rEnDEgc334T_4p6UCkxiVCvKrb5NpPZfgt-0VAwVJnYF_MThTugjlkmzSdB34g1u7FROkti5VMgZPMaCgYKAZ0SARESFQG1tDrp3wgefDDGuZ-lAFlp81HZvQ0163",
    "refresh_token": "1//043h0Zu1esNTvCgYIARAAGAQSNwF-L9IronGfuCJEVy6u4YZB3Li3vqeGvrwwFiqtRFN77wDjEw_bb2CDvyhdVvbzo3baty4di54",
    "token_uri": "https://oauth2.googleapis.com/token",
    "client_id": "407408718192.apps.googleusercontent.com",
    "client_secret": "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",
}

# Create Credentials object from authorized user info
creds = Credentials.from_authorized_user_info(info)
print(creds)
location_id = '02613928441639437097'
service = build('mybusinessbusinessinformation', 'v1', credentials=creds)

location = service.locations().get(name=f'locations/{location_id}').execute()
print(location)

# import google.auth
# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build

# # Set up authentication
# # creds, project_id = google.auth.default()
# creds, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/business.manage'])
# creds = Credentials.from_authorized_user_info(creds)

# # Build the API client
# service = build('mybusinessbusinessinformation', 'v1', credentials=creds)

# # Set the location ID for the location you want to retrieve call settings for
# # location_id = '1234567890'

# # Set the language code for the settings you want to retrieve
# language_code = 'en-US'

# # Call the locations.getBusinesscallssettings method to retrieve the call settings
# settings = service.locations().getBusinesscallssettings(name=f'locations/{location_id}', languageCode=language_code).execute()

# # Print the call settings
# print(f"Call settings for location {location_id}:")
# print(f"  Business hours: {settings['businessHours']}")
# print(f"  Phone number: {settings['phoneNumber']}")
# print(f"  Call tracking enabled: {settings['callTrackingEnabled']}")