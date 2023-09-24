# https://www.alphavantage.co/

# Ingest .csv file from fidelity
# Process data to form usable in python
# Format and print data to user

# Lookup how often dividends are paid out
# Display to user the upcoming date, yield
# Get upcoming ex-dates for dividends and alert user

import ingest
import dataworkers as dw

filepath = "C:\\Users\\shado\Desktop\\Stonks\\Dividend Manager\\Sample Data\\simple_dividend_data.csv"
# filepath = "C:\\Users\\shado\\Desktop\\Stonks\\Dividend Manager\\Sample Data\\dividend_data.csv"

data = ingest.dividendCSV(filepath)

print(data.to_markdown())

print("\n\n\n")

accounts = dw.getAccounts(data)
# print(accounts)

positionsInAccount = dw.getPositionsByAccount(data, "Stocks")
# print(positionsInAccount)

positionsByAccount = dw.listAllPositionsSeparatedByAccount(data, accounts)
# print(type(positionsByAccount))
for i in positionsByAccount:
    print(type(i))