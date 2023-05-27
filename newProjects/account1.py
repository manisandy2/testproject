
import sys
import json

from googleapiclient import sample_tools
from googleapiclient.http import build_http
from openpyxl import Workbook

wb = Workbook()
ws = wb.active


def main(argv):
  
    
    MyBusinessAccount, flags = sample_tools.init(argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage")            # https://mybusinessaccountmanagement.googleapis.com/v1/accounts
    output = MyBusinessAccount.accounts().list().execute()


    firstAccount = output["accounts"][0]["name"]
    print(firstAccount)



            

if __name__ == "__main__":
  main(sys.argv)

