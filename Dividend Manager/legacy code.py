import csv

# filepath = "C:\\Users\\shado\Desktop\\Stonks\\Dividend Manager\\Sample Data\\simple_dividend_data.csv"
filepath = "C:\\Users\\shado\\Desktop\\Stonks\\Dividend Manager\\Sample Data\\dividend_data.csv"

with open(filepath, 'r') as file:
  csvreader = csv.reader(file)
  print(csvreader)
  for row in csvreader:
    csvreader
    if len(row) > 2 and "ï»¿" in row[0]: row[0] = row[0][-14:]
    print(row)