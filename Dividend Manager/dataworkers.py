def getAccounts(data):
    r = list(set(list(data["Account Name"])))
    
    return r

def getPositionsByAccount(data, account):
    r = data.query('`Account Name` == @account')

    return r

def listAllPositionsSeparatedByAccount(data, accounts):
    r = ["", ""]

    for account in accounts:
        r.append(str(getPositionsByAccount(data, account)))

    return r