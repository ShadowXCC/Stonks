from decimal import Decimal


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

    soldPositionList = []

    for acc in oldAccountList:
        if acc not in newAccountList:
            soldPositionList.append(acc)

    return soldPositionList

def getAllPositions(data):
    r = sorted(list(set(list(data["Symbol"]))))
    if "Pending Activity" in r:
        r.remove("Pending Activity")
    if "SPAXX**" in r:
        r.remove("SPAXX**")
    if "FZFXX**" in r:
        r.remove("FZFXX**")
    if "FCASH**" in r:
        r.remove("FCASH**") 

    return r

def listEachValueOfPosition(snapshots, ticker):
    from decimal import Decimal
    r = []

    for snap in snapshots:
        temp = ""
        #lookup ticker in snap
        temp = (snapshots[snap].loc[snapshots[snap]['Symbol'] == ticker, 'Current Value']).to_string()
        temp = Decimal(temp[6:])
        r.append(temp)
    
    return r

def listPositionPerSnapshot(snapshots, ticker):
    r = []

    for snap in snapshots:
        temp = ""
        #lookup ticker in snap
        temp = snapshots[snap].query('`Symbol` == @ticker')
        r.append(temp)

    return r

def returnAllQuantitiesAcrossAllSnapshots(snapshots):
    r = {}
    allUniquePositionsAcrossAllSnapshots = {}

    for snap in snapshots:
        r[snap] = {}
        allPositions = getAllPositions(snapshots[snap])
        for symbol in allPositions:
            if symbol not in allUniquePositionsAcrossAllSnapshots:
                allUniquePositionsAcrossAllSnapshots[symbol] = 1
            else:
                allUniquePositionsAcrossAllSnapshots[symbol] = allUniquePositionsAcrossAllSnapshots[symbol] + 1

            temp = ""
            temp = (snapshots[snap].loc[snapshots[snap]['Symbol'] == symbol, 'Quantity']).to_string()
            temp = (temp[5:]).strip()
            if "--" not in temp:
                temp = Decimal(temp)
                r[snap][symbol] = temp
        

    return (r, allUniquePositionsAcrossAllSnapshots)

def checkForChangesInQuantityAcrossAllSnapshots(snapshots):
    data = returnAllQuantitiesAcrossAllSnapshots(snapshots)
    quantities = data[0]
    allPositions = data[1] #allUniquePositionsAcrossAllSnapshots

    differences = {}
    quantitiesKeys = list(quantities.keys())

    for i in range(0, len(quantities) - 1):
        q1 = quantities[quantitiesKeys[i]]
        q2 = quantities[quantitiesKeys[i + 1]]
        # print("q1", q1)
        # print("q2", q2)

        temp = {}
        for p in allPositions:
            if (p in q1) and (p in q2):
                # print("a", p, q2[p] - q1[p])
                temp[p] = q2[p] - q1[p] #q2 - q1
            # elif (p in q1) and (p not in q2):
                # print("b", p, q1[p])
            #     temp[p] = q1[p]
            elif (p not in q1) and (p in q2):
                # print("c", p, q2[p])
                temp[p] = q2[p]
            # elif (p not in q1) and (p not in q2):
            #   temp[p] = q2[p]
            elif (p in q1) and (p not in q2):
                # print("d", p)
                # This is almost the same as case B
                temp[p] = -1 * q1[p]
                
        differences[i] = temp

    return differences















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