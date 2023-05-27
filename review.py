# import requests

# # Set your API key and place_id
# API_KEY = 'AIzaSyBemnwfZmjiKegal9dnEBgAQVHHNOL3_j4'
# PLACE_ID = '13.040325,80.2287504,17'
# # SEARCH_KEYWORD = 'Poorvika Mobile World, North Usman Road, Postal Colony, T. Nagar, Chennai, Tamil Nadu'

# # Make API request to retrieve place details
# url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&key={API_KEY}'
# # url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={SEARCH_KEYWORD}&inputtype=textquery&fields=place_id&key={API_KEY}'

# response = requests.get(url)
# result = response.json()

# # Check if the request was successful
# if result['status'] == 'OK':
#     # Retrieve the reviews section from the response
#     reviews = result['result']['reviews']

#     # Print each review
#     for review in reviews:
#         author_name = review['author_name']
#         rating = review['rating']
#         review_text = review['text']
#         print(f'Author: {author_name}\nRating: {rating}\nReview: {review_text}\n---')
# else:
#     print(f'Error: {result["status"]}')


import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import googleapiclient.discovery

# Set your API credentials and business account details
API_CREDENTIALS_FILE = 'service_account.json'
BUSINESS_ACCOUNT_NAME = 'accounts/115683479125390656399'  # Replace with your business account ID

# Authenticate and authorize with the Google My Business API
credentials = service_account.Credentials.from_service_account_file(API_CREDENTIALS_FILE, scopes=['https://www.googleapis.com/auth/business.manage'])
credentials = credentials.with_subject(BUSINESS_ACCOUNT_NAME)
credentials.refresh(Request())

# Create a Google My Business API client
client = googleapiclient.discovery.build('mybusiness', 'v4', credentials=credentials)

# Retrieve reviews for the business account
reviews = client.accounts().locations().reviews().list(parent=BUSINESS_ACCOUNT_NAME).execute()

# Print each review
for review in reviews.get('reviews', []):
    reviewer_name = review.get('reviewer').get('displayName')
    rating = review.get('starRating')
    review_text = review.get('comment')
    review_time = review.get('createTime')
    print(f'Reviewer: {reviewer_name}\nRating: {rating}\nReview: {review_text}\nTime: {review_time}\n---')