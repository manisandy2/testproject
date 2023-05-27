import sys
import json

from googleapiclient import sample_tools
from googleapiclient.http import build_http
from openpyxl import Workbook

wb = Workbook()
ws = wb.active


def main(argv):
    # driver.get()
    
    MyBusinessAccount, flags = sample_tools.init(argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")
    MyBusinessInformation, flags = sample_tools.init(argv, "mybusinessbusinessinformation", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")
    service, flags = sample_tools.init(argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")

    output = MyBusinessAccount.accounts().list().execute()
    print("List of Accounts:\n")
    print("sdfsd",json.dumps(output, indent=2) + "\n")

    firstAccount = output["accounts"][0]["name"]

    print(firstAccount)
    fields_we_want = 'name'

    # locationsList = MyBusinessInformation.accounts().locations().list(parent=firstAccount,readMask=fields_we_want).execute()
    # firstLocation = locationsList["locations"][0]["name"]
    # print(firstLocation)
    # print(locationsList)

   
    # locations = locationsList.get('locations', [])
    # nextPageToken =  locationsList.get("nextPageToken",[])

    # print(nextPageToken)

    # for location in locations:
    #   print(location["name"])

    
    
    response = MyBusinessInformation.accounts().locations().list(parent=firstAccount,readMask=fields_we_want).execute()

  
    locations = response.get('locations', [])
    for location in locations:
      print(location)
    
  
    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = MyBusinessInformation.accounts().locations().list(parent=firstAccount,readMask=fields_we_want ,pageToken=page_token).execute()
      locations = response.get('locations', [])
      for location in locations:
        
        print(location)
            

  



    # reviewsApi = service.accounts().locations().reviews()

    # request = reviewsApi.list(parent=firstLocation)

    # reviews = []

    # # for location in locationsList:
    # #    print(location)
    # # return firstLocation

    # while request is not None:
    #   response = request.execute()

    #   # Do something with the activities
    #   reviews += response["reviews"]

    #   request = reviewsApi.list_next(request, response) # all pages
    #   # request = None # first page only

    # print(len(reviews))
    # return reviews
       

if __name__ == "__main__":
  main(sys.argv)

