def scrape():
    from urllib.request import urlopen, Request
    from bs4 import BeautifulSoup

    url = "https://finviz.com/insidertrading.ashx"
    req = Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urlopen(req)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return BeautifulSoup(html, "html.parser")

from datetime import datetime
import scraperFuncs as SF

scraped = scrape()
lines = scraped.find_all('tr', {"class" : "fv-insider-row"})
# singleLine = scraped.find('tr', {"class" : "fv-insider-row"})

print(len(lines))

for i in lines:
    tabLinks = i.find_all('a', {"class" : "tab-link"})

    whitespaceNoWraps = i.find_all('td', {"class" : "whitespace-nowrap"})
    whitespaceNoWraps.pop(0)
    whitespaceNoWraps.pop(3)

    textRights = i.find_all('td', {"class" : "text-right"})

    ticker = SF.returnTicker(tabLinks)
    owner = SF.returnOwner(tabLinks)
    relationship = SF.returnRelationship(whitespaceNoWraps)
    transactionDate = SF.returnTransactionDate(whitespaceNoWraps)
    transaction = SF.returnTransaction(whitespaceNoWraps)
    cost = SF.returnCost(textRights)
    numSharesTransacted = SF.returnNumSharesTransacted(textRights)
    value = SF.returnValue(textRights)
    totalSharesOwned = SF.returnTotalSharesOwned(textRights)
    SECForm4URL = SF.returnSECForm4URL(tabLinks)
    SECForm4FilingDate = SF.returnSECForm4FilingDate(tabLinks)
    percentOfHoldingChanged = SF.returnPercentOfHoldingChanged(transaction, totalSharesOwned, numSharesTransacted)

    today = datetime.now()
    formattedTransactionDate = datetime.strptime(transactionDate, "%b %d").replace(year=today.year)
    formattedSECForm4FilingDate = datetime.strptime(SECForm4FilingDate, "%b %d %I:%M %p").replace(year=today.year)

    timeBetweenTransactionAndToday = today - formattedTransactionDate

    timeBetweenFilingAndToday = today - formattedSECForm4FilingDate
    timeBetweenTransactionAndFiling = formattedSECForm4FilingDate - formattedTransactionDate
    bigDic = SF.addAllValuesIntoDictionary(ticker, owner, relationship, transactionDate, transaction, cost, numSharesTransacted, value, totalSharesOwned, percentOfHoldingChanged, SECForm4URL, SECForm4FilingDate, timeBetweenTransactionAndToday, timeBetweenFilingAndToday, timeBetweenTransactionAndFiling)

    print(bigDic)
    # print("Ticker: " + ticker)
    # print("Owner: " + owner)
    # print("relationship: " + relationship)
    # print("transactionDate: " + transactionDate)
    # print("transaction: " + transaction)
    # print("cost: " + cost)
    # print("numShares: " + str(numSharesTransacted))
    # print("value: " + value)
    # print("totalSharesOwned: " + str(totalSharesOwned))
    # print("percentOfHoldingsChanged: " + str(percentOfHoldingChanged) + "%")
    # print("SECForm4URL: " + SECForm4URL)
    # print("SECForm4FilingDate: " + SECForm4FilingDate)

    # print("timeBetweenTransactionAndToday: " + str(timeBetweenTransactionAndToday))
    # print("timeBetweenFilingAndToday: " + str(timeBetweenFilingAndToday))
    # print("timeBetweenTransactionAndFiling: " + str(timeBetweenTransactionAndFiling))

    # print("\n\n\n")