import requests
import json
import csv
username = 'e1be318dcfd57d0fc0a47a2432edb5ce'
password = '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'
shop = 'etc-demo.myshopify.com'
endpoint = 'admin/api/2020-07/customers.json'
url = f'https://{username}:{password}@{shop}/{endpoint}'
response = requests.get(url)
result = json.loads(response.text)['customers']
csv_headers = result[0].keys()
with open('customer_shopify.csv', 'w', newline='') as f:
    dict_writer = csv.DictWriter(f, csv_headers)
    dict_writer.writeheader()
    dict_writer.writerows(result)
