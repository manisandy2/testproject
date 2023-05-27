from google.oauth2 import service_account
from google.auth.transport.requests import Request

def google_service_account_get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        'service_account.json',
        scopes=['https://www.googleapis.com/auth/plus.business.manage']
    )

    # print("Refresh :",credentials.refresh(Request()))
    credentials.refresh(Request())
# Check if the token has expired and refresh if necessary
# if credentials.expired:
#     try:
#         credentials.refresh(Request())
#     except Exception as e:
#         print(f'Error refreshing access token: {e}')

# Extract the access token
    access_token = credentials.token
    print(credentials.signer_email)
    print(credentials.expired)
    print(credentials.quota_project_id)
    print(credentials.has_scopes)
    print(credentials.from_service_account_file)
    print(credentials.from_service_account_info)
    print(credentials.project_id)
    print(credentials.refresh)
    print(credentials.service_account_email)
    print(credentials.with_always_use_jwt_access)
    print(credentials.)
    print(credentials.has_scopes)
    print(credentials.has_scopes)
    print(credentials.has_scopes)
    return access_token
    # print("Access Token",access_token)

print(google_service_account_get_access_token())