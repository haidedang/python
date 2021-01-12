import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
sys.path.append('/Users/Hai/github/python/utils')
import usersDB
import pickle
from time import sleep

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tutorial").sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

print(data)
revenue = usersDB.loadState('revenue.pickle')
print(revenue)

orderIDList = list(revenue.keys())

i = 3

for order in orderIDList:
    try:
        insertRow = [order, revenue[order]["price"], revenue[order]["costs"]]
    except:
        insertRow = [order, revenue[order]["price"] , 0]
    sheet.insert_row(insertRow, i)
    i += 1
    sleep(2)
