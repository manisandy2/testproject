
import sys
import json

from googleapiclient import sample_tools
from googleapiclient.http import build_http
from openpyxl import Workbook

wb = Workbook()
ws = wb.active


def main(argv):
  
    
    MyBusinessAccount, flags = sample_tools.init(argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")                                                                                                                      # https://mybusinessaccountmanagement.googleapis.com/v1/accounts
    MyBusinessInformation, flags = sample_tools.init(argv, "mybusinessbusinessinformation", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")
    service, flags = sample_tools.init(argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")

    output = MyBusinessAccount.accounts().list().execute()


    firstAccount = output["accounts"][0]["name"]

    print(firstAccount)
    fields_we_want = 'name'



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
            

if __name__ == "__main__":
  main(sys.argv)

