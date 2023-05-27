# import requests

# # Set your API credentials
API_KEY = "AIzaSyAYI0RbWinikf9Si0eg6oEfknDVwnRhXzY"

# # Create a request object

# account_id = '115683479125390656399'

# headers = {
#     'Authorization': f'Bearer {API_KEY}',
#     'Content-Type': 'application/json'
# }

# request = requests.Request("GET", "https://mybusiness.googleapis.com/v4/accounts", headers={
#     "Authorization": "Bearer " + API_KEY
# })


# print(request.json)

# Check the response status code
# if response.status_code == 200:
#     # Get the location ID
#     location_id = response.json()["locations"][0]["id"]

#     print("Location ID:", location_id)
# else:
#     print("Error getting location ID:", response.status_code)


import googleapiclient.discovery

# Set your API credentials
# API_KEY = "YOUR_API_KEY"

# Create a service object
service = googleapiclient.discovery.build("mybusiness", "v4", credentials=API_KEY)

# Update the business hours
business_hours = {
    "dayOfWeek": "MONDAY",
    "open": {
        "time": "09:00"
    },
    "close": {
        "time": "17:00"
    }
}

response = service.locations().update(
    locationId="956808188434702278",
    body={"businessHours": business_hours}
).execute()

# Check the response status code
if response.status_code == 200:
    print("Business hours updated successfully")
else:
    print("Error updating business hours:", response.status_code)