import requests
import pandas as pd
import re
import io


#Kyle's Overall Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/kai_uhl/psn"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
cleanresults = results.text.replace('"', "")
cleanedresults = cleanresults.replace(',', " ")

print(cleanedresults)

data = io.StringIO(cleanedresults)
df = pd.read_csv(data, sep=" ")


#Kyle's Weekly Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/weekly-stats/kai_uhl/psn"

headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
cleanresults = results.text.replace('"', "")
cleanedresults = cleanresults.replace(',', " ")

print(cleanedresults)

#converts string to dataframe
data = io.StringIO(cleanedresults)
df = pd.read_csv(data, header = None, sep=" ")
df.to_csv('kyleweeklystats224.csv')


#Kevin's Weekly Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/weekly-stats/kevynk/psn"

headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
cleanresults = results.text.replace('"', "")
cleanedresults = cleanresults.replace(',', " ")

print(cleanedresults)

#converts string to dataframe
data = io.StringIO(cleanedresults)
df1 = pd.read_csv(data, header = None, sep=" ")
df1.to_csv('kevinweeklystats224.csv')


#Kevin's Overall Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/kevynk/psn"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
print(results.text)

#Dande's Warzone Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/TomatoCultivator%234902131/acti"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
print(results.text)

#Dande's Warzone Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/heal%1694/battle"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
print(results.text)

#Johnson's Overall Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/appledoglol/psn"
headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
results = requests.request("GET", url, headers=headers)
print(results.text)


#Johnson's Weekly Stats
url = "https://call-of-duty-modern-warfare.p.rapidapi.com/weekly-stats/appledoglol/psn"

headers = {
    'x-rapidapi-key': "dc34a85caemshe2f48db1fbb3572p15fd8bjsn3a20a35d4f3c",
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)