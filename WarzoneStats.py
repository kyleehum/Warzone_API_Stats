import requests
import pandas as pd

#Kyle's Warzone Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/kai_uhl/psn"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)

print(results.text)

#Kyle's Weekly Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/weekly-stats/kai_uhl/psn"

headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers)

print(response.text)

#Kevin's Weekly Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/weekly-stats/kevynk/psn"

headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers)

print(response.text)

#Kevin's Warzone Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/kevynk/psn"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)

print(results.text)

