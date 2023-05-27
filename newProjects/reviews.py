import sys
import json

from googleapiclient import sample_tools
from googleapiclient.http import build_http
from openpyxl import Workbook

wb = Workbook()
ws = wb.active



def reviews(argv):
    
    # service, flags = sample_tools.init(argv , "mybusiness", "v4", __doc__, path, scope="https://www.googleapis.com/auth/business.manage", discovery_filename=discovery_doc)
    MyBusinessAccount, flags = sample_tools.init(argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")
    
    
    reviewsApi = MyBusinessAccount.accounts().locations().reviews()
    request = reviewsApi.list(parent="accounts/115873825114492366496/locations/17696946108772609056")
    #reviewsList = request.execute()
    reviews = []

    # pagination
    # https://developers.google.com/api-client-library/python/guide/pagination
    while request is not None:
      response = request.execute()

      # Do something with the activities
      reviews += response["reviews"]

      request = reviewsApi.list_next(request, response) # all pages
      # request = None # first page only

    print(len(reviews))
    return reviews