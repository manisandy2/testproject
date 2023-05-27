
# import argparse
# import sys

# # from google.ads.googleads.client import GoogleAdsClient
# # from google.ads.googleads.errors import GoogleAdsException
# customer_id = "4282180022"
# print(type(customer_id))
# credentials = {
#         "developer_token":"gropIHZzhgnM4qXkoQbfPw",
#         "refresh_token":"1//0gdMYixwLy_03CgYIARAAGBASNwF-L9Irnv-cp3sFDYcYbq9bI637WhEd8kW5ecDlTWzsvHBnsO-DvwR1TZI0IuuP3Eo-ikffh3E",
#         "client_id":"361934167021-2g260lromqoqaoocttbknlssmjgo4p24.apps.googleusercontent.com",
#         "client_secret":"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",
#         "login_customer_id":'4282180022',
#         "use_proto_plus":True
#     }
# client = GoogleAdsClient.load_from_dict(credentials,version="v13")

# def main(client, customer_id):
#     ga_service = client.get_service("GoogleAdsService")
#     query = """
#         SELECT
#             customer.id,
#             customer.descriptive_name,
#             customer.currency_code,
#             customer.time_zone,
#             customer.tracking_url_template,
#             customer.auto_tagging_enabled
#         FROM customer
#         LIMIT 1"""

#     request = client.get_type("SearchGoogleAdsRequest")
#     request.customer_id = customer_id
#     request.query = query
#     response = ga_service.search(request=request)
#     customer = list(response)[0].customer

#     print(f"Customer ID: {customer.id}")
#     print(f"\tDescriptive name: {customer.descriptive_name}")
#     print(f"\tCurrency code: {customer.currency_code}")
#     print(f"\tTime zone: {customer.time_zone}")
#     print(f"\tTracking URL template: {customer.tracking_url_template}")
#     print(f"\tAuto tagging enabled: {customer.auto_tagging_enabled}")


# main(client=client,customer_id=customer_id)
