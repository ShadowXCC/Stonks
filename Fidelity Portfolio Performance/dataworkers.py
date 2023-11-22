def getNewlyPurchasedPositions(oldData, newData):
    # Get list of positions from both accounts
    # compare lists, IF IN NEW AND NOT IN OLD
    oldAccountList = getAllPositions(oldData)
    newAccountList = getAllPositions(newData)

    # print(oldAccountList)
    # print()
    # print(newAccountList)

    newPositionList = []

    for acc in newAccountList:
        if acc not in oldAccountList:
            newPositionList.append(acc)

    return newPositionList

def getFullySoldPositions(oldData, newData):
    # Get list of positions from both accounts
    # compare lists, IF IN OLD AND NOT IN NEW
    oldAccountList = getAllPositions(oldData)
    newAccountList = getAllPositions(newData)

    newPositionList = []

    for acc in oldAccountList:
        if acc not in newAccountList:
            newPositionList.append(acc)

    return newPositionList

def getAllPositions(data):
    r = sorted(list(set(list(data["Symbol"]))))

    return r

def listEachValueOfPosition(snapshots, ticker):
    from decimal import Decimal
    r = []

    for snap in snapshots:
        temp = ""
        #lookup ticker in snap
        # data.loc[data['Account Name'] == account, 'Symbol']
        temp = (snapshots[snap].loc[snapshots[snap]['Symbol'] == ticker, 'Current Value']).to_string()
        temp = Decimal(temp[6:])
        # r.append(snapshots[snap].loc[snapshots[snap]['Symbol'] == ticker, 'Current Value'])
        # print(snapshots[snap].query('`Symbol` == @ticker'))
        r.append(temp)

    
    return r

def listPositionPerSnap(snapshots, ticker):
    return







def getAccounts(data):
    r = list(set(list(data["Account Name"])))
    
    return r

def getPositionsByAccount(data, account):
    r = data.query('`Account Name` == @account')

    return r

def listAllPositionsSeparatedByAccount(data, accounts):
    r = []

    for account in accounts:
        r.append(str(getPositionsByAccount(data, account)))

    return r

def listAllPositionsInAccount(data, account):
    return data.loc[data['Account Name'] == account, 'Symbol']

def returnAllNonBlankByColumn(data, column):
    # subframe = fooframe.query("`{0}` == 'Large'".format(myvar))

    return data.query('`{0}` != "--" & not `{0}`.isnull()'.format(column))