# https://www.alphavantage.co/
# https://www.alphavantage.co/documentation/#symbolsearch

# Ingest .csv file from fidelity
# Process data to form usable in python
# Format and print data to user

# Lookup how often dividends are paid out
# Display to user the upcoming date, yield
# Get upcoming ex-dates for dividends and alert user

import random, requests
from datetime import datetime, date, timedelta

import humanreadable as hr
import dataworkers as dw
import ingest

filepath = "C:\\Users\\shado\Desktop\\Stonks\\Dividend Manager\\Sample Data\\simple_dividend_data.csv"
filepath = "C:\\Users\\shado\\Desktop\\Stonks\\Dividend Manager\\Sample Data\\dividend_data.csv"

data = ingest.dividendCSV(filepath)

print(data.to_markdown())

print("\n\n\n")

# accounts = dw.getAccounts(data)
# print(accounts)

# positionsInAccount = dw.getPositionsByAccount(data, "Stocks")
# print(positionsInAccount)

# positionsByAccount = dw.listAllPositionsSeparatedByAccount(data, accounts)
# for i in positionsByAccount:
#     print(i + "\n")

# symbols = data['Symbol'].tolist()
# print(dw.listAllPositionsInAccount(data, "Stocks"))

# key = "L7Y8D16ELRTKBHYI"
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + 'LAC' + '&apikey=' + key
# r = requests.get(url) 
# stockInfo = r.json()
# print(stockInfo)

# print(data.loc[data['Account Name'] == "ROTH IRA", 'Ex-Date'])

# print(data.query('`Yield` != "--" & not `Yield`.isnull()'))
# print(dw.returnAllNonBlankByColumn(data, 'Ex-Date'))

# for i in dw.returnPositionsThatHaveExDatesSoon(data, 28):
#         print(data.query('`Ex-Date` == @i'))

allPositions = dw.getallpositions(data)
# print(allPositions)

# positionToCheck = "QQQ"
# print(dw.returnAllInstancesOfSymbol(data, "QQQ"))
# tallyUp = dw.tallyUp(data, positionToCheck)
# print(tallyUp)
# tallyUpAll = dw.tallyUpAll(data, allPositions)
# print(tallyUpAll)
# print(tallyUp, " and ", tallyUpAll[positionToCheck], " = ", tallyUpAll[positionToCheck] == tallyUp)

# monthToCheck = "08"
# augustExdates = dw.returnExdateBasedOnMonth(data, monthToCheck)
# print(augustExdates)
allExdatesByMonth = dw.returnAllExdatesBasedOnMonth(data)
# print(allExdatesByMonth)
# print(augustExdates, " and ", allExdatesByMonth[monthToCheck], " = ", allExdatesByMonth[monthToCheck] == augustExdates)

# for i in allExdatesByMonth:
#     print(i, allExdatesByMonth[i], "\n")
#     print(i, list(allExdatesByMonth[i].get("Ex-Date")), "\n\n\n")

octExdates = allExdatesByMonth["10"]

print(octExdates)