def returnTicker(tabLinks):
    return tabLinks[0].text

def returnOwner(tabLinks):
    return tabLinks[1].text

def returnRelationship(whitespaceNoWraps):
    return whitespaceNoWraps[0].text 

def returnTransactionDate(whitespaceNoWraps):
    return whitespaceNoWraps[1].text 

def returnTransaction(whitespaceNoWraps):
    return whitespaceNoWraps[2].text 

def returnCost(textRights):
    return textRights[0].text 

def returnNumSharesTransacted(textRights):
    import locale
    locale.setlocale(locale.LC_ALL, '')

    return locale.atof(textRights[1].text) 

def returnValue(textRights):
    return textRights[2].text 

def returnTotalSharesOwned(textRights):
    import locale
    locale.setlocale(locale.LC_ALL, '')

    return locale.atof(textRights[3].text) 

def returnSECForm4URL(tabLinks):
    return tabLinks[2]['href']

def returnSECForm4FilingDate(tabLinks):
    return tabLinks[2].text

def returnPercentOfHoldingChanged(transaction, totalSharesOwned, numSharesTransacted):
    percentOfHoldingChanged = 0.0
    initial = totalSharesOwned - numSharesTransacted

    if initial == 0 and transaction == "Buy":
        percentOfHoldingChanged = 100
    elif initial == 0 and transaction == "Sale":
        percentOfHoldingChanged = -100
    elif transaction == "Buy":
        percentOfHoldingChanged = 100 * ((totalSharesOwned - initial) / initial) #(totalSharesOwned/numSharesTransacted)
    elif transaction == "Sale":
        percentOfHoldingChanged = -100 * (numSharesTransacted/(numSharesTransacted + totalSharesOwned))

    return percentOfHoldingChanged



def addAllValuesIntoDictionary(ticker, owner, relationship, transactionDate, transaction, cost, numSharesTransacted, value, totalSharesOwned, percentOfHoldingChanged, SECForm4URL, SECForm4FilingDate, timeBetweenTransactionAndToday, timeBetweenFilingAndToday, timeBetweenTransactionAndFiling):
    littleDic = {
        "ticker": ticker,
        "owner": owner,
        "Relationship": relationship,
        "transactionDate": transactionDate,
        "transaction": transaction,
        "cost": cost,
        "numShares": numSharesTransacted,
        "value": value,
        "totalSharesOwned": totalSharesOwned,
        "percentOfHoldingsChanged": str(percentOfHoldingChanged) + "%",
        "SECForm4URL": SECForm4URL,
        "SECForm4FilingDate": SECForm4FilingDate,
        "timeBetweenTransactionAndToday": timeBetweenTransactionAndToday,
        "timeBetweenFilingAndToday": timeBetweenFilingAndToday,
        "timeBetweenTransactionAndFiling": timeBetweenTransactionAndFiling
    }

    return {ticker: littleDic}
    








# ticker = tabLinks[0].text #singleLine.find('a', {"class" : "tab-link"}).text
# owner = tabLinks[1].text #singleLine.find('a', {"class" : "tab-link"}).text
# relationship = whitespaceNoWraps[0].text # singleLine.find('', {"class" : ""})
# transactionDate = whitespaceNoWraps[1].text # singleLine.find('', {"class" : ""})
# transaction = whitespaceNoWraps[2].text # singleLine.find('', {"class" : ""})
# cost = textRights[0].text # singleLine.find('', {"class" : ""})
# numSharesTransacted = locale.atof(textRights[1].text) # singleLine.find('', {"class" : ""})
# value = textRights[2].text # singleLine.find('', {"class" : ""})
# totalSharesOwned = locale.atof(textRights[3].text) # singleLine.find('', {"class" : ""})
# SECForm4URL = tabLinks[2]['href']
# SECForm4FilingDate = tabLinks[2].text #singleLine.find('', {"class" : ""})