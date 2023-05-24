import requests

response = requests.get ( 'https://rajagroupuae.com/')

print (response.get_code)

print (response.json())