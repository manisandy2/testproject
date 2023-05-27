from google.auth import exceptions
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up authentication credentials
credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/business.manage'],
)

# Set up the Google My Business API client
service = build('mybusinessbusinessinformation', 'v1', credentials=credentials)

# Set the location name or place ID of the business
location_name = 'accounts/115873825114492366496/locations/3374706989677147079'
fields_we_want = 'name'
fields = 'reviews(reviewId,reviewer(displayName),starRating,comment)'
try:
    # Retrieve the reviews for the location
    response = service.accounts().locations().reviews().list(
        parent=location_name,fields=fields
    ).execute()

    # Process the reviews
    reviews = response.get('reviews', [])
    for review in reviews:
        author_name = review.get('reviewer').get('displayName')
        rating = review.get('starRating')
        comment = review.get('comment')
        print(f'Author: {author_name}')
        print(f'Rating: {rating}')
        print(f'Comment: {comment}')
        print('---')

except exceptions.GoogleAuthError as auth_error:
    print(f'Authentication error: {auth_error}')
except Exception as e:
    print(f'Error occurred: {e}')